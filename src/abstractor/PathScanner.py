"""
This class is responsible for scanning the input directory, defined in the configuration file, 
and returning a list of all the pdf files in the directory and its subdirectories.

The class provides the following functionalities:
1. Scanning the directory and returning a list of pdf files.
2. Displaying the list of pdf files in the console.
3. Getting the list of pdf files.

The pdf files are returned in a sorted order. The criteria for sorting is alphabetical.

The list of pdf files is shown in the console as a dictionary. The key is the index of the file in the list and the value is the file name (as defined in the configuration).

The User has the option to select from which index to start and from which file to start.

The User has the option to select up to which index to run the program.

The start and end point can also be defined in the configuration file.
"""

import json
from os import walk, path
from re import search
from logging import *
from src.abstractor.Config import Config
from src.abstractor.UserInput import UserInput

class PathScanner():
    def __init__(self, config:Config, user_input:UserInput):
        """
        Initializes the PathScanner object.

        Args:
            config (Config.Config): The configuration object.

        Attributes:
            scanning_dir (str): The input directory to be scanned.
            display_mode (str): The display mode for showing the list of pdf files.
            pdf_files (list): The list of pdf files.
            start_index (int): The index to start from.
            end_index (int): The index to end at.
        """
        self.scanning_dir = config.get("input_dir")
        self.display_mode = config.get("display_mode")
        self.pdf_files = []
        self.user_input = user_input    
        debug("Scanning directory: %s", self.scanning_dir)
        debug("Display mode: %s", self.display_mode)
        debug("Pdf files: %s", self.pdf_files)
        info("PathScanner initialized successfully \n\n")
    
    def scan(self):
        """
        Scans the directory and returns a list of pdf files in the directory.
        """
        info("Scanning directory")
        pdf_files = []
        debug("\n ***Scanning directory: %s ***\n", self.scanning_dir)
        for root, dirs, files in walk(self.scanning_dir):
            debug("Scanning directory: %s", root)
            debug("Files in directory: %s", files)
            debug("Directories in directory: %s", dirs)
            for file in files:
                if file.endswith(".pdf"):
                    pdf_files.append(path.join(root, file))
                    
        pdf_files.sort(key=lambda x: (int(''.join(filter(str.isdigit, x))), x.lower()))
        info("Files scanned \n\n")
        self.pdf_files = pdf_files
    
    def display_pdfs(self):
        """
        Displays the list of pdf files in the console.
        """
        for i in range(len(self.pdf_files)):
            if self.display_mode == "L":
                print(f"{i}: {self.pdf_files[i]}\n")
            elif self.display_mode == "S":
                pdf_name = self.pdf_files[i].split("/")[-1]
                print(f"{i}: {pdf_name}\n")
                        
    def get_pdf_files(self):
        """
        Returns the list of pdf files.

        Returns:
            list: The list of pdf files.
        """
        return self.pdf_files
    def get_pdf_files_range(self):
        """
        Selects the range of pdf files to be processed, including the start and end index.
        """ 
        start_index = int(self.user_input.get("start_index"))
        end_index = int(self.user_input.get("end_index"))
        self.pdf_files = self.pdf_files[start_index:end_index+1]
        info("Pdf files selected \n\n")
        return self.pdf_files