import os
import subprocess

class PDF2HTML:
    
    @staticmethod
    def convert_pdf_to_html(
            path:str,
            html_output_dir:str, 
            filename:str,
            optimize_text: int = 1,  # Added parameter for text optimization
            no_frames: bool = True,  # Added parameter to control frames usage
            font_format: str = 'woff'  # Added parameter to specify font format
            ):
        
        """
        Converts a PDF file to an HTML file after sanitizing text elements.
        
        Parameters:
            path (str): The path to the PDF file to be converted.
            html_output_dir (str): The directory where the HTML file will be saved.
            filename (str): The name of the output HTML file.
            optimize_text (int): Option to optimize text layer quality. Default is 1 (enabled).
            no_frames (bool): Whether to output a single HTML file without using frames. Default is True (no frames).
            font_format (str): Specifies the font format (e.g., 'woff', 'ttf'). Default is 'woff'.
            
        Returns:
            None. The result is the creation of an HTML file at the specified output directory.
        """

        # Ensure output directories exist
        if not os.path.exists(html_output_dir):
            os.makedirs(html_output_dir)
            print(f"Created directory: {html_output_dir}")

        html_output_path = os.path.join(html_output_dir, filename.replace('.pdf', '.html'))

        # Building the command with the new options
        command = [
            "pdf2htmlEX",
            "--zoom", "1.3",
            f"--optimize-text={optimize_text}",
            f"--font-format={font_format}"
        ]

        # Adding the no-frames option if specified
        # if no_frames:
        #     command.append("--no-frames")

        # Adding the input and output paths at the end of the command
        command.extend([path, html_output_path])

        try:
            # Execute the command
            subprocess.run(command, check=True)
            print(f"Conversion successful. HTML file saved as: {html_output_path}")
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during conversion: {e}")
