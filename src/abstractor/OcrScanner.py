"""
The OcrScanner class is used to run OCR scans on specified images. 
It uses the MacOS built-in OCR tool to extract text from images, hence the programm is only compatible with MacOS.
"""

from ocrmac.ocrmac import OCR
from logging import info
from src.abstractor.Config import Config
from PIL import Image

class OcrScanner():
    def __init__(self,config:Config):
        """
        Initializes the OcrScanner object.
        """
        info("OcrScanner initialized successfully \n\n")
        self.recognition_level = config.get("recognition_level")
        self.lang = config.get("language_preference")
    def scan(self, image: Image):
        """
        Scans the image and returns the text extracted from the image.
        
        Args:
            image_path (str): The path to the image file.
        
        Returns:
            str: The text extracted from the image.
        """
        info("Scanning image")
        self.OCR = OCR(image,recognition_level=self.recognition_level,language_preference=self.lang)
        text = self.OCR.recognize()
        return_string = ""
        for element in text:
                return_string += str(element[0]) + ' '
        return_string += '\n'
        info("Image scanned successfully \n\n")
        return return_string