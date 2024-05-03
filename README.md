# Abstractor

## Description

This project is called "Abstractor" and it aims to provide a solution for abstracting text content.

## Features

- Text abstraction
- Configurable abstraction parameters
- Works with OpenAI API

## Installation

To install the project, follow these steps:

1. Clone the repository: `git clone https://github.com/username/repository.git`
2. Navigate to the project directory: `cd Abstractor`
3. In src/abstractor create a [config.json](#configuration) file. Add the configuration there.

## Usage

To use the project, follow these steps:

1. The project requires an API key from OpenAI. You can get one by signing up at OpenAI. Add it to the config file.
2. This is not a complete module yet, hence you can use any of the defined classes directly
3. An example of the algorithm is in the _init_.py file. 
4. Output and Input are defined in the config file. You can change them as needed.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## License

This project is licensed under the [MIT License](LICENSE).


## Configuration
 - log_level : The level of logging to be used, as in the python logging module
 - opeanai_api_key: The API key for OpenAI
 - opeanai_model: The model to be used for abstraction
 - input_dir: The directory where the input files are stored
 - output_dir: The directory where the output files will be stored
 - display_mode: "S" or "L" representing the short and long format
 - pages_per_pdf: Number of pages in each pdf to scan and abstract
 - pdf_image_crop: a dictionary regarding image cropping
    - threshold: The threshold for cropping the image (as defined in the PLI module)
    - margin: The margin to be left around the image
    - dpi: The dpi of the image
- instruction: The instruction to send to ChatGPT. Example: "The following text comes after an OCR scan. Fix and complete any missing letters, wrong words but do not add your own sentences or text. Output everything as a long line of text by removing all new-line characters and adding instead only 1 whitespace in their place"


## Potential Features
- [] File selection should be starting from the file directories, instead of all the pdf files in 1 array
- [] An easier way to select and avoid certain files for scanning
- [] Modify the OpenAI API prompt, to ensure better responses
- [] Avoid running OCR, when the PDF already has selectable text
- [] Use a different OCR model to make the app compatible on windows
- [] Name of output file is currently based on the parent directory of the file being red. Not always representative of the topic / date
- [] Add a UI showing the input directory, to easily select what pdf files to scan
