"""
This class is responsible for scanning the input directory, defined in the configuration file, 
and returning a list of all the pdf files in the directory and its subdirectories.
1. The pdf files are returned in a sorted order. The criteria for sorting is alphabetical
2. This list is shown in the console as a dictionary. The key is the index of the file in the list and the value is the file name (as defined in the configuration)
3. The User has the option to select from which index to start and from which file to start
4. The User has the option to select up to which index to run the program
5. The start and end point can also be defined in the configuration file
"""
import json
from os import walk, path
from re import search
from logging import *
class PathScanner():
    def __init__(self,config_path:str = "config.json"):
        with open(config_path,"r") as f:
            config = json.load(f)
            basicConfig(level=config["log_level"])
            debug("Initializing PathScanner")
            self.scanning_dir = config["input_dir"]
            self.display_mode = config["display_mode"]
            self.pdf_files = []
            try:
                self.start_index = int(config["start_index"])
            except:
                self.start_index = None
            try:
                self.end_index = int(config["end_index"])
            except:
                self.end_index = None
        
        debug("Scanning directory: %s",self.scanning_dir)
        debug("Display mode: %s",self.display_mode)
        debug("Start index: %s",self.start_index)
        debug("End index: %s",self.end_index)
        debug("Pdf files: %s",self.pdf_files)
        info("PathScanner initialized successfully \n\n")
    def scan(self):
        """
        Scans the directory and returns a list of pdf files in the directory
        """
        info("Scanning directory")
        pdf_files = []
        debug("\n ***Scanning directory: %s ***\n",self.scanning_dir)
        for root, dirs, files in walk(self.scanning_dir):
            debug("Scanning directory: %s",root)
            debug("Files in directory: %s",files)
            debug("Directories in directory: %s",dirs)
            for file in files:
                if file.endswith(".pdf"):
                    pdf_files.append(path.join(root, file))
                    
        pdf_files.sort(key=lambda x: (int(''.join(filter(str.isdigit, x))), x.lower()))
        info("Files scanned \n\n")
        self.pdf_files = pdf_files
    def display_pdfs(self):
        for i in range(len(self.pdf_files)):
            if self.display_mode == "L":
                    print(f"{i}: {self.pdf_files[i]}\n")
            elif self.display_mode == "S":
                pdf_name = self.pdf_files[i].split("/")[-1]
                print(f"{i}: {pdf_name}\n")
                        
            