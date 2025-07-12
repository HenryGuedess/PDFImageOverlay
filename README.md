# PDFImageOverlay

This Python script overlays an image onto every page of an existing PDF file, maintaining the original PDF's page size and adding the image with specified margins.

## Features

* Overlays a specified image onto all pages of an input PDF.
* Preserves the original PDF's page dimensions.
* Scales the image to fit the page width with a configurable side margin.
* Uses PyPDF2 for PDF manipulation and ReportLab for image insertion.

## Prerequisites

* Python 3.x
* Required libraries:
   * PyPDF2
   * ReportLab
   * Pillow (PIL)

Install the dependencies using:

```bash
pip install PyPDF2 reportlab Pillow
```

## Usage

1. Update the following variables in the script:
   * input_pdf: Path to the input PDF file.
   * new_image: Path to the image file (e.g., PNG, JPG).
   * output_pdf: Path for the output PDF file.

2. Run the script:

```bash
python script.py
```

The script will:
- Read the input PDF.
- Create a new PDF page with the image scaled to fit the page width (with margins).
- Merge the image onto each page of the original PDF.
- Save the result as a new PDF file.

## Code Overview

**Input Handling**: Reads the input PDF using PyPDF2.PdfReader.

**Image Page Creation**: Uses reportlab.pdfgen.canvas to create a temporary PDF page with the image, scaled to fit the page width while maintaining the aspect ratio.

**Merging**: Merges the image page onto each page of the input PDF using merge_page.

**Output**: Saves the modified PDF using PyPDF2.PdfWriter.

## Configuration

**Margins**: Adjust margin_sides (default: 0) and y_position (default: 41) in the create_image_page function to control the image's placement.

**Image Scaling**: The image is scaled to fit the page width minus the side margins. Modify new_width calculation for different scaling behavior.

## Example

```python
input_pdf = "input.pdf"
new_image = "logo.png"
output_pdf = "output_with_logo.pdf"
```

This will overlay logo.png onto every page of input.pdf and save the result as output_with_logo.pdf.

## Notes

* Ensure the image file format is supported by Pillow (e.g., PNG, JPG).
* The script assumes the input PDF and image files exist in the specified paths.
* Adjust y_position and margin_sides to avoid overlapping important content in the PDF.
