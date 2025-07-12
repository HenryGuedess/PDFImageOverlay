from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
from io import BytesIO
from PIL import Image

input_pdf = "Your PDF path"
new_image = "theimage.png"
output_pdf = "newpdf.pdf"

def create_image_page(image_path, page_size):
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=page_size)
    
    page_width = page_size[0]
    page_height = page_size[1]
    
    with Image.open(image_path) as img:
        original_width, original_height = img.size
    
    aspect_ratio = original_height / original_width
    
    
    margin_sides = 0  
    new_width = page_width - (2 * margin_sides) 
    new_height = new_width * aspect_ratio
    
    x_position = margin_sides  
    y_position = 41  
    
    
    c.drawImage(image_path, x_position, y_position, width=new_width, height=new_height)
    c.showPage()
    c.save()
    packet.seek(0)
    return PdfReader(packet).pages[0]

reader = PdfReader(input_pdf)
writer = PdfWriter()

first_page = reader.pages[0]
page_size = (float(first_page.mediabox.width), float(first_page.mediabox.height))

image_page = create_image_page(new_image, page_size)

for page in reader.pages:
    page.merge_page(image_page)
    writer.add_page(page)

with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print(f"New PDF saved as {output_pdf}")
