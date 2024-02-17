import fitz  # PyMuPDF
from PIL import Image
import io

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