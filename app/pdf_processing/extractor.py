import fitz  # PyMuPDF
from PIL import Image
import io
import os 
class PDFExtractor:
    def extract_text(self, pdf_path):
        """
        Extracts all text from a given PDF file using PyMuPDF.

        :param pdf_path: The path to the PDF file.
        :return: A list of text blocks, one per page.
        """
        text_blocks = []
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text = page.get_text()
                if text:
                    text_blocks.append(text)
        return text_blocks
    
    def convert_pdf_to_xml(self, pdf_path):
        """
        Converts a given PDF file to XML format, allowing access to text and equations using tags.

        :param pdf_path: The path to the PDF file.
        :return: A list of XML content strings, one per page.
        """
        xml_pages = []
        with fitz.open(pdf_path) as doc:
            for page in doc:
                # Use get_text("xml") to get the page content in XML format
                xml = page.get_text("xml")
                if xml:
                    xml_pages.append(xml)
        return xml_pages


    def extract_images(self, pdf_path):
        """
        Converts all pages of a given PDF file to images using PyMuPDF.

        :param pdf_path: The path to the PDF file.
        :return: A list of image objects (as PIL images).
        """
        images = []
        with fitz.open(pdf_path) as doc:
            for page_num, page in enumerate(doc):
                pix = page.get_pixmap()
                img_data = pix.tobytes("ppm")  # Convert the pixmap to bytes in PPM format
                img = Image.open(io.BytesIO(img_data))  # Create a PIL image from the byte data
                images.append(img)
        return images
    
