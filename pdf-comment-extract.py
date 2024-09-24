import fitz  # PyMuPDF
from openpyxl import Workbook

def extract_annotations(pdf_path):
    print(f"Opening PDF: {pdf_path}")
    doc = fitz.open(pdf_path)

    annotations = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        print(f"Checking page {page_num + 1}")

        page_annotations = list(page.annots())

        for annot in page_annotations:
            annotation_type = annot.type[1]  # Get the string representation of the type
            print(f"Found annotation of type: {annotation_type}")

            annotation = {
                'page_number': page_num + 1,
                'type': annotation_type,
                'content': annot.info.get('content', ''),
                'author': annot.info.get('title', ''),  # 'title' often contains the author name
                'created': annot.info.get('creationDate', ''),
                'modified': annot.info.get('modDate', ''),
                'referenced_text': get_referenced_text(page, annot)
            }

            # Add specific properties based on annotation type
            if annotation_type in ['FreeText', 'Text']:
                annotation['text'] = annot.info.get('content', '')
            elif annotation_type in ['Highlight', 'Underline', 'StrikeOut', 'Squiggly']:
                annotation['highlighted_text'] = get_highlighted_text(page, annot)
            elif annotation_type in ['Square', 'Circle', 'Line', 'Polygon', 'PolyLine']:
                annotation['vertices'] = str(annot.vertices)  # Convert to string for Excel

            annotations.append(annotation)

        print(f"Found {len(page_annotations)} annotations on page {page_num + 1}")

    doc.close()
    return annotations

def get_referenced_text(page, annot):
    rect = annot.rect
    expanded_rect = fitz.Rect(rect.x0 - 10, rect.y0 - 10, rect.x1 + 10, rect.y1 + 10)
    return page.get_text("text", clip=expanded_rect).strip()

def get_highlighted_text(page, annot):
    try:
        highlighted_text = page.get_textbox(annot.rect)
        return highlighted_text.strip()
    except Exception as e:
        print(f"Error extracting highlighted text: {e}")
        return ""

def save_to_excel(annotations, excel_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "PDF Annotations"

    headers = ["Page Number", "Type", "Content", "Author", "Created", "Modified", "Referenced Text",
               "Text", "Highlighted Text", "Vertices"]
    ws.append(headers)

    for annot in annotations:
        row = [
            annot['page_number'],
            annot['type'],
            annot['content'],
            annot['author'],
            annot['created'],
            annot['modified'],
            annot['referenced_text'],
            annot.get('text', ''),
            annot.get('highlighted_text', ''),
            annot.get('vertices', '')
        ]
        ws.append(row)

    # Adjust column widths
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = min((max_length + 2) * 1.2, 100)  # Cap width at 100
        ws.column_dimensions[column_letter].width = adjusted_width

    wb.save(excel_path)
    print(f"Excel file saved: {excel_path}")

# Example usage
pdf_path = '../report.pdf'
excel_path = '../annotations.xlsx'

extracted_annotations = extract_annotations(pdf_path)
print(f"Total annotations extracted: {len(extracted_annotations)}")

if extracted_annotations:
    save_to_excel(extracted_annotations, excel_path)
    print(f"Annotations have been extracted and saved to {excel_path}")
else:
    print("No annotations were extracted from the PDF.")
