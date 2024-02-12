from pdf_processing.extractor import PDFExtractor
from rdf_generation.generator import RDFGenerator
from chatgpt_integration.chatgpt_client import ChatGPTClient

import os 
def main():
    input_dir = 'input'
    rdf_output_dir = 'output/rdf'
    analysis_output_dir = 'output/analysis'  # Directory for saving analysis results

    extractor = PDFExtractor()
    rdf_generator = RDFGenerator()
    chatgpt_client = ChatGPTClient()

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
            
            print("text:",text_blocks)
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