import sys

import openpyxl
import pandas as pd
import pymupdf as fitz

# Dictionary mapping annotation type names to their numerical values
ANNOT_TYPES = {
    "PDF_ANNOT_TEXT": 0,
    "PDF_ANNOT_LINK": 1,
    "PDF_ANNOT_FREE_TEXT": 2,
    "PDF_ANNOT_LINE": 3,
    "PDF_ANNOT_SQUARE": 4,
    "PDF_ANNOT_CIRCLE": 5,
    "PDF_ANNOT_POLYGON": 6,
    "PDF_ANNOT_POLY_LINE": 7,
    "PDF_ANNOT_HIGHLIGHT": 8,
    "PDF_ANNOT_UNDERLINE": 9,
    "PDF_ANNOT_SQUIGGLY": 10,
    "PDF_ANNOT_STRIKE_OUT": 11,
    "PDF_ANNOT_REDACT": 12,
    "PDF_ANNOT_STAMP": 13,
    "PDF_ANNOT_CARET": 14,
    "PDF_ANNOT_INK": 15
}

def extract_annotations_to_excel(pdf_path, excel_path, desired_annot_types):
    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Error opening PDF file: {e}")
        return

    annotation_data = []
    total_annots = 0
    annotation_type_counts = {}

    for page_num in range(doc.page_count):
        page = doc[page_num]
        annots = page.annots()

        for annot in annots:
            total_annots += 1
            annot_type = annot.type

            # Handle the case where annot.type is a tuple
            if isinstance(annot_type, tuple):
                annot_type_num, annot_type_name = annot_type
            else:
                annot_type_num = annot_type
                annot_type_name = [k for k, v in ANNOT_TYPES.items() if v == annot_type_num][0]

            if annot_type_name not in annotation_type_counts:
                annotation_type_counts[annot_type_name] = 0
            annotation_type_counts[annot_type_name] += 1

            if annot_type_num in desired_annot_types:
                annot_info = {
                    "Page": page_num + 1,
                    "Type": annot_type_name,
                    "Content": annot.info.get("content", ""),
                    "Rect": annot.rect,
                    "Author": annot.info.get("title", ""),
                }
                annotation_data.append(annot_info)

    print(f"Total annotations found: {total_annots}")
    print("Annotation types found:")
    for annot_type, count in annotation_type_counts.items():
        print(f"  {annot_type}: {count}")

    print(f"\nAnnotations of desired types found: {len(annotation_data)}")

    if not annotation_data:
        print("No annotations of the desired types were found.")
        return

    df = pd.DataFrame(annotation_data)
    try:
        df.to_excel(excel_path, index=False)
        print(f"Annotations successfully written to {excel_path}")
    except Exception as e:
        print(f"Error writing to Excel file: {e}")

    doc.close()

# Modify the main part of the script to use annotation names instead of numbers
if __name__ == "__main__":
    pdf_file = "/Users/harrisonweiss/Downloads/report.pdf"
    excel_output = "/Users/harrisonweiss/Downloads/annotation_log.xlsx"

    desired_types = []
    for item in ANNOT_TYPES:
        desired_types.append(ANNOT_TYPES[item])

    extract_annotations_to_excel(pdf_file, excel_output, desired_types)
