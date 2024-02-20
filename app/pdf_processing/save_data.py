import os
import json

class SaveData:

    def save_dict(self, data_dict,directory,filename):
        """
        Save the provided text blocks to a file within the specified directory, 
        with each text block separated by two newline characters, resembling paragraphs.

        :param text_blocks: A list of strings, each representing a text block to be saved.
        :param filename: The name of the file to save the text blocks in. This allows for dynamic file naming.
        """

        # Define filename 
        json_filename = filename.replace(".pdf", ".json")

        # Define the full path for the file
        file_path = os.path.join(directory, json_filename)

        # Write the dictionary to a JSON file
        with open(file_path, 'w') as json_file:
            json.dump(data_dict, json_file)
    
    def save_figures(self, figures, output_folder):
        """
        Saves each figure extracted from a PDF into its own file.
        :param figures: List of tuples containing (image_bytes, image_format).
        :param output_folder: The folder where the figures will be saved.
        """
        os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
        for i, (image_bytes, image_format) in enumerate(figures, start=1):
            image_filename = f"figure_{i}.{image_format}"
            image_path = os.path.join(output_folder, image_filename)
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
    
    def save_text_to_file(self, text, output_txt_path,filename):
        """
        Saves the extracted text blocks to a text file.

        :param text: A list of text blocks to save.
        :param output_txt_path: The path where the extracted text will be saved as a text file.
        """
        txt_filename = filename.replace(".pdf", ".txt")
        file_path = os.path.join(output_txt_path, txt_filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            for block in text:
                f.write(block + '\n\n')  # Separate text blocks by an empty line for readability