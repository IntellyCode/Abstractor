"""
This class is responsible for taking a ready abstract and writing it to the appropriate output file.
1. The output directory is defined in the configuration file
2. The output file path is defined as the function input
3. This class has only 1 method

Usage:
    writer = AbstractWriter(conf)
    writer.set_output_file("output.txt")
    writer.write("This is the abstract content")

Attributes:
    output_dir (str): The output directory path defined in the configuration file.
    output_file (str): The name of the output file.
    output_file_path (str): The full path of the output file.

Methods:
    __init__(self, conf: Config.Config): Initializes the AbstractWriter object.
    write(self, abstract: str): Writes the abstract to the output file.
    set_output_file(self, output_file: str): Sets the output file path.
"""

from logging import debug, info, critical
import os.path as path
from src.abstractor.Config import Config

class AbstractWriter():
    def __init__(self, conf: Config):
        """
        Initializes the AbstractWriter object.

        Args:
            conf (Config.Config): The configuration object.

        Returns:
            None
        """
        debug("Initializing AbstractWriter")
        self.output_dir = conf.get("output_dir")
        self.output_file = None
        self.output_file_path = None
        debug("Output directory: %s", self.output_dir)
        info("AbstractWriter initialized successfully \n\n")

    def write_str(self, abstract: str):
        """
        Writes the abstract to the output file.

        Args:
            abstract (str): The abstract content.

        Returns:
            None
        """
        info("Writing abstract to output file")
        debug("Writing abstract to file: %s", self.output_file_path)
        if not path.exists(self.output_dir):
            critical("Output directory does not exist")
        if not self.output_file:
            critical("Output file not set")
        try:
            with open(self.output_file_path, "a") as f:
                f.write(abstract)
                info("Abstract written successfully \n\n")
        except Exception as e:
            critical("Error writing abstract to file: %s", e)

    def write_dict(self, abstract: dict):
        """
        Writes the abstract to the output file.

        Args:
            abstract (dict): The abstract content.

        Returns:
            None
        """
        info("Writing abstract to output file")
        debug("Writing abstract to file: %s", self.output_file_path)
        if not path.exists(self.output_dir):
            critical("Output directory does not exist")
        if not self.output_file:
            critical("Output file not set")
        try:
            with open(self.output_file_path, "a") as f:
                for key, value in abstract.items():
                    # Write value as a string
                    try:
                        for k,v in value.items():
                            f.write(str(k).upper() + " \n" + str(v) + "\n")
                    except:
                        f.write(str(value) + "\n")
                    
                info("Abstract written successfully \n\n")
        except Exception as e:
            critical("Error writing abstract to file: %s", e)
    def set_output_file(self, output_file: str):
        """
        Sets the output file path.

        Args:
            output_file (str): The name of the output file.

        Returns:
            None
        """
        if self.output_file == output_file:
            return
        self.output_file = output_file
        self.output_file_path = path.join(self.output_dir, self.output_file)
        debug("Output file set to: %s", self.output_file_path)
