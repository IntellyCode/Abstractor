"""
This class is responsible for reading the configuration file and providing the configuration to the other classes
1. The configuration file is a json file
2. The configuration file is read in the constructor and is passed as a file path
3. The configuration file is read only once
4. Program will exit if the configuration file is not found or wrong
"""

import json
from logging import basicConfig
import os

class Config:
    def __init__(self, config_path:str = "config.json"):
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.validate()

    def validate(self):
        conf = self.config
        log_level = conf.get("log_level")
        if not log_level or log_level not in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            raise ValueError("log_level not found in configuration file or invalid value")
        if not conf.get("openai_api_key"):
            raise ValueError("openai_api_key not found in configuration file")
        input_dir = conf.get("input_dir")
        if not input_dir or not os.path.isdir(input_dir):
            raise ValueError("input_dir not found or not a valid directory in configuration file")
        output_dir = conf.get("output_dir")
        if not output_dir or not os.path.isdir(output_dir):
            raise ValueError("output_dir not found or not a valid directory in configuration file")
        display_mode = conf.get("display_mode")
        if not display_mode or display_mode not in ["L", "S"]:
            raise ValueError("display_mode not found in configuration file or invalid value")
        if not conf.get("pages_per_pdf"):
            raise ValueError("pages_per_pdf not found in configuration file")
        start_index = conf.get("start_index")
        if not start_index or not start_index.isdigit() or int(start_index) < 0:
            raise ValueError("start_index not found in configuration file or invalid value")
        end_index = conf.get("end_index")
        if not end_index or not end_index.isdigit() or int(end_index) < 0:
            raise ValueError("end_index not found in configuration file or invalid value")
        if not conf.get("instruction"):
            raise ValueError("instruction not found in configuration file")
        basicConfig(level=log_level)
    def get(self, key):
        return self.config.get(key)
    def get_full(self):
        return self.config