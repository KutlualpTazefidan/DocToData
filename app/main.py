# from pdf_processing.extractor import PDFExtractor
# from pdf_processing.pdf2html import PDF2HTML
from pdf_processing.extractor import TextExtractor
from pdf_processing.save_data import SaveData
from pdf_processing.process_extracted_text import ProcessExtractedText
# from rdf_generation.generator import RDFGenerator
# from chatgpt_integration.chatgpt_client import ChatGPTClient
import os 

def main():
    input_dir = 'input'
    xml_output_dir = 'output/xml'
    txt_output_dir = 'output/txt'
    html_output_dir = 'output/html'
    json_output_dir = 'output/json'
    rdf_output_dir = 'output/rdf'
    fig_output_dir = 'output/fig'
    analysis_output_dir = 'output/analysis'  # Directory for saving analysis results
    optimize_text=1
    no_frames=True
    font_format="woff"
    # extractor = PDFExtractor()
    # pdf2html = PDF2HTML()
    extractor = TextExtractor()
    save_data = SaveData()
    process_text= ProcessExtractedText()
    # rdf_generator = RDFGenerator()
    # chatgpt_client = ChatGPTClient()

    # Ensure output directories exist
    os.makedirs(rdf_output_dir, exist_ok=True)
    os.makedirs(analysis_output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            print(f"Processing {filename}...")


            # Extract text PDF
            pdf_text = extractor.extract_text(pdf_path)
            save_data.save_text_to_file(pdf_text, txt_output_dir,filename)

            # Save the text blocks as paragraphs
            pdf_content_dict = process_text.process_text(pdf_text)
            save_data.save_dict(pdf_content_dict, json_output_dir, filename)
        
            # Extract text and images from PDF
            figures = process_text.extract_figures(pdf_path)
            save_data.save_figures(figures,fig_output_dir)
            
            # # Analyze content for importance using ChatGPT
            # analysis_results = []
            # for text in text_blocks:
            #     importance = chatgpt_client.analyze_content(text)  
            #     analysis_results.append((text, importance))
            
            # Extract mathematical formula
            # formula = extractor.math_formula(pdf_path)



            # # Save analysis results
            # analysis_filename = filename.replace('.pdf', '_analysis.txt')
            # analysis_path = os.path.join(analysis_output_dir, analysis_filename)
            # with open(analysis_path, 'w') as analysis_file:
            #     for text, importance in analysis_results:
            #         analysis_file.write(f"Text: {text}\nImportance: {importance}\n\n")

            # print(f"Finished processing {filename}.")

if __name__ == '__main__':
    main()