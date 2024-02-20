import os
import re
import json
import fitz

class ProcessExtractedText:

    def __init__(self):
        """
        Initialize the StoreInformation with a directory.

        :param directory: The directory where the text blocks file will be saved.
        """

    def preprocess_text(self, lines):
        processed_lines = []
        current_line = ""

        for line in lines:
            stripped_line = line.strip()
            if not stripped_line:  # Skip empty lines
                continue
            current_line += " " + stripped_line
            if re.match(r'.*[.!?]$', stripped_line):  # If line ends with sentence-ending punctuation
                processed_lines.append(current_line.strip())
                current_line = ""

        # Add the last line if it's not empty
        if current_line:
            processed_lines.append(current_line.strip())

        return processed_lines

    def extract_chapters(self,text, start_number, end_number):
        # Define the regular expression pattern dynamically
        extracted_texts = []

        # print("text:",text)
        # Extracting the abstract
        for i in range(start_number,end_number):
            chapter_pattern = re.compile(rf' {i}\.(.*?) {i+1}\.')
            # Extract the abstract
            match = chapter_pattern.search(text)
            if match:
                chapter = match.group(1).strip()
                extracted_texts.append(chapter)

        return extracted_texts

    def process_text(self, input_text):
        cleaned_text = []
        header_pattern = re.compile(r'^[A-ZÄÖÜ0-9\s-]+$')
        sentence_pattern = re.compile(r'.*[a-zA-Z].*[.!?]')
        page_pattern = re.compile(r'Page \d{1,2}')

        for item in input_text:
            lines = self.preprocess_text(item.split('\n'))
            cleaned_paragraph = []
            for line in lines:
                if header_pattern.match(line) or sentence_pattern.match(line):
                    cleaned_paragraph.append(line)

            # Join the lines within a paragraph into a single string
            paragraph_text = ' '.join(cleaned_paragraph)
            if paragraph_text:  # Only add non-empty paragraphs
                cleaned_text.append(paragraph_text)

        # Remove the Page and it's number from the string 
        cleaned_text_wo_page = [page_pattern.sub('',paragraph) for paragraph in cleaned_text]
        cleaned_text_wo_page = " ".join(cleaned_text_wo_page)

        # print("test inpt",cleaned_text_wo_page)
        
        # Extracting the title
        title_pattern = re.compile(r'(.+?)(?=\bABSTRACT\b)')
        # Extracting the title
        match = title_pattern.search(cleaned_text_wo_page)
        if match:
            title = match.group(1).strip()
            # cleaned_text_wo_page = cleaned_text_wo_page.replace(match.group(0), '').strip()  # Remove the extracted part from the source text

        # Extracting the abstract
        abstract_pattern = re.compile(r'ABSTRACT(.*?) 1\.')
        # Extract the abstract
        match = abstract_pattern.search(cleaned_text_wo_page)
        if match:
            abstract = match.group(1).strip()
            # cleaned_text_wo_page = cleaned_text_wo_page.replace(match.group(0), '').strip()  # Remove the extracted part from the source text

        # Define start and end numbers
        start_number = 1
        end_number = 10  # Change this to your desired end number

        # Extract text between consecutive numbers
        extracted_texts = self.extract_chapters(cleaned_text_wo_page, start_number, end_number)

        # Creating a dictionary
        data_dict = {'title': title, 'abstract': abstract}

        for i in range(1,len(extracted_texts)+1):
            data_dict[str(i)] = extracted_texts[i-1]

        print('data_dict',data_dict)
        return data_dict
    
    def extract_figures(self, pdf_path):
        figures = []
        with fitz.open(pdf_path) as doc:
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                images = page.get_images(full=True)
                for img_index, img_info in enumerate(images):
                    xref = img_info[0]
                    base_image = doc.extract_image(xref)
                    image_bytes = base_image["image"]
                    image_format = base_image["ext"]
                    figures.append((image_bytes, image_format))
        return figures