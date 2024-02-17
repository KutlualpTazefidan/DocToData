import os
import re

class StoreInformation:

    def __init__(self, directory):
        """
        Initialize the StoreInformation with a directory.

        :param directory: The directory where the text blocks file will be saved.
        """
        self.directory = directory

    def save_as_paragraphs(self, text_blocks,filename):
        """
        Save the provided text blocks to a file within the specified directory, 
        with each text block separated by two newline characters, resembling paragraphs.

        :param text_blocks: A list of strings, each representing a text block to be saved.
        :param filename: The name of the file to save the text blocks in. This allows for dynamic file naming.
        """
        # Ensure the directory exists
        os.makedirs(self.directory, exist_ok=True)

        # Define the full path for the file
        file_path = os.path.join(self.directory, filename)

        # Open the file in write mode and write each text block, separated by two newlines
        with open(file_path, 'w') as file:
            for block in text_blocks:
                file.write(block + '\n\n')  # Two newline characters to separate text blocks


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

    def clean_text_and_keep_headers(self, input_text):
        cleaned_text = []
        header_pattern = re.compile(r'^[A-ZÄÖÜ0-9\s-]+$')
        sentence_pattern = re.compile(r'.*[a-zA-Z].*[.!?]')
        
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

        # Join the paragraphs with two newlines to separate them
        return '\n\n'.join(cleaned_text)