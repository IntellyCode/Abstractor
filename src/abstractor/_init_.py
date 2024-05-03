"""
Init of the module. Contains the logic to combine all predefined classes, to create the abstractor module.
The purpose of this module is:
1. The PathScanner class is used to scan the input directory for PDF files.
2. For PDFs where the text is not selectable, the PdfEditor class is used to convert the PDF into images.
3. The Images are then cropped to focus around the text (manual)
4. The cropped images are passed to the MacOS OcrScanner, via the OcrScanner class, to extract the text.
5. The text is sent to ChatGPT following the instruction defined in the configuration file
6. The output is written using the AbstractWriter class to the respective txt file in the specified output directory.
"""

from src.abstractor.PathScanner import PathScanner
from src.abstractor.PdfEditor import PdfEditor
from src.abstractor.OcrScanner import OcrScanner
from src.abstractor.OpenAIRequest import OpenAIRequest
from src.abstractor.AbstractWriter import AbstractWriter
from src.abstractor.Config import Config
from src.abstractor.UserInput import UserInput
from logging import info, debug

# Initialize configuration, user input, path scanner, OCR scanner, OpenAI request, and abstract writer
config = Config("./src/abstractor/config.json")
user_input = UserInput()
path_scanner = PathScanner(config, user_input)
ocr_scanner = OcrScanner(config)
openai_request = OpenAIRequest(config)
abstract_writer = AbstractWriter(config)

# Scan the input directory for PDF files
path_scanner.scan()

# Display the PDF files found
path_scanner.display_pdfs()

# Initialize user input
user_input.init()

#Select the PDFs to be removes
pdfs_to_remove = path_scanner.select_pdfs_to_remove()
debug("PDFs to remove: " + str(pdfs_to_remove))

# Get the range of PDF files
path_scanner.select_pdf_range()

# Remove some PDF files
path_scanner.remove_pdfs(pdfs_to_remove)

# Get the list of PDF files
pdf_files = path_scanner.get_pdf_files()
info("Final list of pdf_file: %s",pdf_files)
# Process each PDF file
for file in pdf_files:
    info("Processing file: " + file)
    
    # Initialize PDF editor with the file and configuration
    pdf_editor = PdfEditor(file, config)
    
    # Convert the PDF into images
    pdf_editor.convert()
    
    # Crop the images to focus around the text (manual)
    pdf_editor.crop_images()
    
    # Get the output file name
    file_array = file.split("/")
    output_file = file_array[-2] + ".txt"
    
    # Set the output file for abstract writer
    abstract_writer.set_output_file(output_file)
    
    # Get the images from PDF editor
    images = pdf_editor.get_images()
    debug("Images: " + str(images))
    
    # Write the PDF file name as a header
    abstract_writer.write_str(file_array[-1] + ":\n")
    
    # Process each image
    for image in images:
        # Scan the image using OCR scanner
        text = ocr_scanner.scan(image)
        
        # Get the edited text from OpenAI request
        edited_text = openai_request.get_response(text)
        debug("Edited text: " + str(edited_text))
        
        # Write the edited text to abstract writer
        abstract_writer.write_dict(edited_text)
    
    # Add new lines after each PDF file
    abstract_writer.write_str("\n\n")
        


