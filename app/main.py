# from pdf_processing.extractor import PDFExtractor
# from pdf_processing.pdf2html import PDF2HTML
from pdf_processing.extractor import PDFExtractor
from pdf_processing.store_information import StoreInformation
# from rdf_generation.generator import RDFGenerator
# from chatgpt_integration.chatgpt_client import ChatGPTClient
import os 

def main():
    input_dir = 'input'
    xml_output_dir = 'output/xml'
    html_output_dir = 'output/html'
    json_output_dir = 'output/json'
    rdf_output_dir = 'output/rdf'
    analysis_output_dir = 'output/analysis'  # Directory for saving analysis results
    optimize_text=1
    no_frames=True
    font_format="woff"
    # extractor = PDFExtractor()
    # pdf2html = PDF2HTML()
    extractor = PDFExtractor()
    store_info= StoreInformation('output/json/')
    # rdf_generator = RDFGenerator()
    # chatgpt_client = ChatGPTClient()

    # Ensure output directories exist
    os.makedirs(rdf_output_dir, exist_ok=True)
    os.makedirs(analysis_output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_dir, filename)
            print(f"Processing {filename}...")


            # Extract text and images from PDF
            text_blocks = extractor.extract_text(pdf_path)
            images = extractor.extract_images(pdf_path)

            # Save the text blocks as paragraphs
            pdf_content_dict = store_info.clean_text_and_keep_headers(text_blocks)
            store_info.save_dict(pdf_content_dict, filename)

            # for i in range(len(text_blocks)):
            # for i in range(3,4):
            #     print(f"text block {i}:",text_blocks[i])


            # # Converting pdf to html
            # html = pdf2html.convert_pdf_to_html(
            #     pdf_path,
            #     html_output_dir,
            #     filename,
            #     optimize_text,
            #     no_frames,
            #     font_format)
        
            # Extract text and images from PDF
            # text_blocks = extractor.extract_text(pdf_path)
            # images = extractor.extract_images(pdf_path)
            # xml_blocks = extractor.convert_pdf_to_xml(pdf_path)
            
            # print("text:",text_blocks)
            # print("images:",images)
            # # Generate RDF for text blocks and images
            # rdf_filename = filename.replace('.pdf', '.rdf')
            # rdf_path = os.path.join(rdf_output_dir, rdf_filename)
            # rdf_generator.generate_rdf(text_blocks, images, rdf_path)

            # # Analyze content for importance using ChatGPT
            # analysis_results = []
            # for text in text_blocks:
            #     importance = chatgpt_client.analyze_content(text)  
            #     analysis_results.append((text, importance))


            # # Save analysis results
            # analysis_filename = filename.replace('.pdf', '_analysis.txt')
            # analysis_path = os.path.join(analysis_output_dir, analysis_filename)
            # with open(analysis_path, 'w') as analysis_file:
            #     for text, importance in analysis_results:
            #         analysis_file.write(f"Text: {text}\nImportance: {importance}\n\n")

            # print(f"Finished processing {filename}.")

if __name__ == '__main__':
    main()