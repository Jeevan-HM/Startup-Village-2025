import asyncio
import json
import os
import secrets
from datetime import datetime
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, send_file, url_for
from werkzeug.utils import secure_filename

from create_form import generate_pdf_from_json

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024  # 50MB max file size
app.config["UPLOAD_FOLDER"] = "uploads"
app.config["OUTPUT_FOLDER"] = "outputs"

# Ensure directories exist
Path(app.config["UPLOAD_FOLDER"]).mkdir(exist_ok=True)
Path(app.config["OUTPUT_FOLDER"]).mkdir(exist_ok=True)


def allowed_file(filename):
    """Check if file is a JSON file."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() == "json"


@app.route("/")
def index():
    """Main page with upload form."""
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    """Handle JSON file upload and generate PDF."""
    if "file" not in request.files:
        flash("No file selected", "error")
        return redirect(url_for("index"))

    file = request.files["file"]

    if file.filename == "":
        flash("No file selected", "error")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash("Only JSON files are allowed", "error")
        return redirect(url_for("index"))

    try:
        # Read and parse JSON
        json_data = json.load(file.stream)

        # Generate unique output directory for this request
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = os.path.join(app.config["OUTPUT_FOLDER"], timestamp)
        os.makedirs(output_dir, exist_ok=True)

        # Copy template directory structure
        import shutil

        latex_output = os.path.join(output_dir, "latex")
        os.makedirs(latex_output, exist_ok=True)

        # Copy report.tex if it exists
        if os.path.exists("latex/report.tex"):
            shutil.copy("latex/report.tex", os.path.join(latex_output, "report.tex"))

        # Generate PDF asynchronously
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        pdf_path = loop.run_until_complete(
            generate_pdf_from_json(json_data, latex_output)
        )
        loop.close()

        if not os.path.exists(pdf_path):
            flash("Failed to generate PDF", "error")
            return redirect(url_for("index"))

        flash("Report generated successfully!", "success")
        return send_file(
            pdf_path,
            as_attachment=True,
            download_name=f"inspection_report_{timestamp}.pdf",
            mimetype="application/pdf",
        )

    except json.JSONDecodeError:
        flash("Invalid JSON file format", "error")
        return redirect(url_for("index"))
    except Exception as e:
        flash(f"Error generating report: {str(e)}", "error")
        return redirect(url_for("index"))


@app.route("/health")
def health():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
