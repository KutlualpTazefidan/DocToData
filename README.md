# PDF to RDF Converter with ChatGPT Analysis

This Python script is designed to read PDF files, extract text and images, convert them into RDF (Resource Description Framework) format, and perform analysis using ChatGPT to determine the importance of the content.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/pdf-to-rdf-converter.git
    ```

2. Install the required dependencies:

    ```bash
    pip install PyPDF2 pdfminer.six Pillow rdflib
    ```

## Usage

1. Place your PDF files in the `input_pdfs/` directory.

2. Run the script `main.py`:

    ```bash
    python main.py
    ```

3. The script will process the PDF files, extract text and images, convert them into RDF format, and save the output RDF files in the `output_rdf/` directory.

4. You can now analyze the RDF files to extract information or perform further processing.

## Configuration

- Modify the script `main.py` to customize any specific configurations, such as file paths, RDF namespaces, or ChatGPT analysis settings.

## File Structure

- `pdf_reader/`: Module for reading PDF files and extracting text and images.
- `rdf_converter/`: Module for converting extracted content into RDF format.
- `main.py`: Main script to run the PDF to RDF conversion process.

## Dependencies

- PyPDF2: For reading PDF files.
- pdfminer.six: For extracting text from PDF files.
- Pillow: For dealing with images.
- rdflib: For working with RDF data.

## License

This project is licensed under the [MIT License](LICENSE).