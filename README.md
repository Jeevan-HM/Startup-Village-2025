# 🏡 Property Inspection Report Generator

A high-performance Flask web application that generates professional, TREC-compliant PDF property inspection reports from JSON data. Built with async processing, modern UI, and optimized for speed.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ✨ Features

### 🚀 Performance
- **Lightning Fast**: Async image downloading with aiohttp and concurrent processing
- **Thread Pool Optimization**: CPU-intensive LaTeX generation runs in parallel
- **Smart Caching**: Images are cached to avoid redundant downloads
- **Batch Processing**: Handles multiple images and sections efficiently

### 📄 PDF Generation
- **TREC-Compliant**: Follows Texas Real Estate Commission standards
- **Professional Layout**: Clean, organized sections with proper formatting
- **Rich Content**: Includes title page, inspection details, and comprehensive sections
- **Image Support**: Auto-converts WEBP, PNG, JPG formats and embeds in PDF
- **Dynamic Tables**: Uses LaTeX longtable for multi-page content

### 🎨 User Interface
- **Modern Design**: Gradient color scheme with smooth animations
- **Drag & Drop**: Easy file upload with visual feedback
- **Loading Animation**: Beautiful progress indicators with step tracking
- **Responsive**: Works seamlessly on desktop and mobile devices
- **Form Reset**: Automatically resets for multiple uploads

### 🖼️ Image Processing
- **Format Detection**: Uses Pillow to identify true image formats
- **Auto-Conversion**: Converts WEBP and unsupported formats to PNG
- **Optimization**: Resizes images to fit within report constraints
- **Error Handling**: Gracefully handles failed downloads

## 🛠️ Technology Stack

**Backend**
- Flask 3.0.0 - Web framework
- asyncio - Asynchronous processing
- aiohttp 3.9.1 - Async HTTP client for image downloads

**PDF Generation**
- LaTeX (pdflatex) - Professional typesetting
- Custom template system - Dynamic content insertion

**Image Processing**
- Pillow 10.1.0 - Image manipulation and format conversion

**Frontend**
- HTML5, CSS3 - Modern web standards
- Vanilla JavaScript - No framework dependencies
- Google Fonts (Inter) - Clean typography

## 📋 Prerequisites

- Python 3.8 or higher
- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🐳 Quick Start with Docker

The easiest way to run the application:

```bash
# Build the Docker image
docker build -t property-inspector .

# Run the container
docker run -p 8080:8080 property-inspector

# Access the application at http://localhost:8080
```

## 💻 Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Jeevan-HM/Startup-Village-2025.git
cd Startup-Village-2025
```

### 2. Install LaTeX

**macOS:**
```bash
brew install --cask mactex
# Or use BasicTeX for a smaller install:
brew install --cask basictex
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install texlive-latex-base texlive-latex-extra texlive-fonts-recommended
```

**Windows:**
- Download and install [MiKTeX](https://miktex.org/download)
- Or use [TeX Live](https://www.tug.org/texlive/)

**Verify Installation:**
```bash
pdflatex --version
```

### 3. Set Up Python Environment

**Using pip:**
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Using uv (faster):**
```bash
# Install uv if you haven't
pip install uv

# Create environment and install dependencies
uv sync
```

### 4. Run the Application

```bash
# Using Flask directly
python app.py

# Or using the start script
chmod +x start.sh
./start.sh
```

The application will be available at `http://localhost:8080`

## 📁 Project Structure

```
Startup-Village-2025/
├── app.py                  # Flask application entry point
├── create_form.py          # PDF generation logic
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── start.sh               # Startup script
│
├── templates/
│   └── index.html         # Main web interface
│
├── static/
│   └── css/
│       └── style.css      # Application styles
│
├── latex/
│   └── report.tex         # LaTeX template
│
├── uploads/               # Temporary JSON uploads
└── outputs/               # Generated PDFs and temp files
```

## 🎯 Usage

### 1. Prepare Your JSON Data

Your JSON file should follow this structure:

```json
{
  "inspection": {
    "clientInfo": {
      "name": "John Doe"
    },
    "address": {
      "fullAddress": "123 Main St, City, State 12345"
    },
    "inspector": {
      "name": "Inspector Name",
      "email": "inspector@example.com"
    },
    "schedule": {
      "date": 1699123200000
    },
    "sections": [
      {
        "name": "SECTION NAME",
        "lineItems": [
          {
            "title": "Item Title",
            "inspectionStatus": "I",
            "isDeficient": false,
            "comments": [
              {
                "label": "Comment label",
                "value": "Comment text",
                "photos": [
                  {
                    "url": "https://example.com/image.jpg"
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

### 2. Upload and Generate

1. Open the application in your browser
2. Click "Choose JSON file" or drag and drop your file
3. Click "Generate Report"
4. Wait for the progress animation to complete
5. Your PDF will automatically download

### 3. Upload Another File

After generation completes:
- The form automatically resets
- Simply select another JSON file
- Generate as many reports as needed

## 🔧 Configuration

### Environment Variables

Create a `.env` file (optional):

```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
MAX_CONTENT_LENGTH=52428800  # 50MB in bytes
```

### Customization

**Change Port:**
Edit `app.py`:
```python
app.run(debug=True, host="0.0.0.0", port=YOUR_PORT)
```

**Modify LaTeX Template:**
Edit `latex/report.tex` to customize PDF appearance.

**Adjust Image Sizes:**
Edit `create_form.py` in the `generate_latex_body()` function.

## 🐛 Troubleshooting

### PDF Generation Fails

**Issue**: "PDFLaTeX compilation failed"

**Solutions:**
1. Verify LaTeX is installed: `pdflatex --version`
2. Check LaTeX packages are installed
3. Review error logs in `outputs/[timestamp]/latex/` folder
4. Ensure images URLs are accessible

### Images Not Appearing

**Issue**: Images don't show in PDF

**Solutions:**
1. Verify image URLs are publicly accessible
2. Check internet connection
3. Look for download errors in console output
4. Supported formats: JPG, PNG, WEBP (auto-converted)

### Loading Animation Stuck

**Issue**: Animation doesn't disappear after generation

**Solutions:**
1. Refresh the page (F5)
2. Check browser console for JavaScript errors
3. Ensure Flask is running without errors
4. Verify PDF was generated in `outputs/` folder

### Port Already in Use

**Issue**: "Address already in use"

**Solution:**
```bash
# Find and kill process using port 8080
lsof -ti:8080 | xargs kill -9

# Or change port in app.py
```

## 🚀 Deployment

### Docker Deployment

```bash
# Build production image
docker build -t property-inspector:latest .

# Run with volume mounting for persistence
docker run -d \
  -p 8080:8080 \
  -v $(pwd)/outputs:/app/outputs \
  --name property-inspector \
  property-inspector:latest
```

### Traditional Deployment

Use a production WSGI server:

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:8080 app:app
```

### Environment Configuration

For production, set these environment variables:
```bash
export FLASK_ENV=production
export FLASK_DEBUG=False
export SECRET_KEY="generate-a-secure-random-key"
```

## 📊 Performance

- **Average Generation Time**: 3-8 seconds (depends on image count)
- **Concurrent Image Downloads**: Up to 10 parallel connections
- **Maximum File Size**: 50MB JSON files
- **PDF Size**: Typically 2-15MB depending on images

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Jeevan-HM**
- GitHub: [@Jeevan-HM](https://github.com/Jeevan-HM)

## 🙏 Acknowledgments

- Texas Real Estate Commission (TREC) for inspection standards
- Flask community for excellent documentation
- LaTeX community for powerful typesetting tools

## 📧 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: [Your email or contact method]

---

<div align="center">
Made with ❤️ for property inspectors
</div>
