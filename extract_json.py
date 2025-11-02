import json


def create_markdown_from_json(json_file_path, output_md_file):
    """
    Parses an inspection JSON and creates a hierarchical
    Markdown file based on sections, lineItems, and comments.
    """

    try:
        # --- 1. Read the JSON file ---
        with open(json_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # --- 2. Access the core data ---
        # Use .get() for safe access in case keys are missing
        inspection_data = data.get("inspection")
        if not inspection_data:
            print(f"Error: No 'inspection' key found in {json_file_path}")
            return

        sections = inspection_data.get("sections")
        if not sections:
            print(f"Error: No 'sections' key found under 'inspection'")
            return

        md_lines = []
        md_lines.append("# Inspection Report")

        # --- 3. Loop through the structure ---

        # Level 1: Sections
        for i, section in enumerate(sections, start=1):
            section_name = section.get("name")
            if section_name:
                # Add a blank line before new sections for readability
                md_lines.append("")
                md_lines.append(f"{i}. {section_name}\n")

            # Level 2: LineItems
            line_items = section.get("lineItems", [])
            for j, line_item in enumerate(line_items, start=1):
                item_title = line_item.get("title")
                if item_title:
                    # Note the indentation (two spaces)
                    md_lines.append(f"  {i}.{j}. {item_title}\n")

                # Level 3: Comments
                comments = line_item.get("comments", [])
                for k, comment in enumerate(comments, start=1):
                    comment_label = comment.get("label")
                    if comment_label:
                        # Note the indentation (four spaces)
                        md_lines.append(f"    {i}.{j}.{k}. {comment_label}\n")

        # --- 4. Write the Markdown file ---
        output_content = "\n".join(md_lines)
        with open(output_md_file, "w", encoding="utf-8") as f:
            f.write(output_content)

        print(f"Successfully created Markdown file: {output_md_file}")

    except FileNotFoundError:
        print(f"Error: The file '{json_file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{json_file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


json_filename = "inspection.json"
markdown_filename = "inspection_report.md"

create_markdown_from_json(json_filename, markdown_filename)
