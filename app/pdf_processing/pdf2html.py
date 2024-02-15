import os
import subprocess

class PDF2HTML:
    
    @staticmethod
    def convert_pdf_to_html(
            path:str,
            html_output_dir:str, 
            filename:str):
        
        """
        Converts a PDF file to an XML file after sanitizing text elements.
        
        Parameters:
            path (str): The path to the PDF file to be converted.
            html_output_dir (str): The directory where the HTML file will be saved.
            filename (str): The name of the output XML file.
            
        Returns:
            The pdfquery.PDFQuery object after loading the PDF and converting it to XML.
        """
        # Ensure output directories exist
        if not os.path.exists(html_output_dir):
            os.makedirs(html_output_dir)
            print(f"Created directory: {html_output_dir}")

        html_output_path = os.path.join(html_output_dir, filename.replace('.pdf', '.html'))


        try:
            # The command to execute pdf2htmlEX
            command = ["pdf2htmlEX", "--zoom", "1.3", path, html_output_path]

            # Execute the command
            subprocess.run(command, check=True)
            print(f"Conversion successful. HTML file saved as: {html_output_path}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during conversion: {e}")
