"""
This class is responsible for reading the configuration file and providing the configuration to the other classes.

Attributes:
    config (dict): The configuration dictionary loaded from the configuration file.

Methods:
    __init__(self, config_path:str = "config.json"): Initializes the Config object by reading the configuration file.
    validate(self): Validates the configuration loaded from the file.
    get(self, key): Retrieves the value of a specific configuration key.
    get_full(self): Retrieves the full configuration dictionary.

"""

import json
from logging import basicConfig, info
import os

class Config:
    # TODO: Remove API key from config.json before making repository public
    def __init__(self, config_path:str = "config.json"):
        """
        Initializes the Config object by reading the configuration file.

        Args:
            config_path (str): The path to the configuration file. Defaults to "config.json".
        """
        print("Initializing Config")
        with open(config_path, "r") as f:
            self.config = json.load(f)
        self.validate()

    def validate(self):
        """
        Validates the configuration loaded from the file.

        Raises:
            ValueError: If any required configuration key is missing or has an invalid value.
        """
        print("Validating configuration \n\n")
        conf = self.config
        for key, value in conf.items():
            if isinstance(value, int):
                raise ValueError(f"Integer value found for key {key}. Only non-integer values are allowed.")
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
        if not conf.get("pages_per_pdf") or not conf.get("pages_per_pdf").isdigit() or int(conf.get("pages_per_pdf")) < 1:
            raise ValueError("pages_per_pdf not found in configuration file or invalid value")
        start_index = conf.get("start_index")
        if not start_index or not start_index.isdigit() or int(start_index) < 0:
            raise ValueError("start_index not found in configuration file or invalid value")
        end_index = conf.get("end_index")
        if not end_index or not end_index.isdigit() or int(end_index) < 0:
            raise ValueError("end_index not found in configuration file or invalid value")
        if not conf.get("instruction"):
            raise ValueError("instruction not found in configuration file")
        if not conf.get("recognition_level"):
            conf["recognition_level"] = "accurate"
        if not conf.get("language_preference"):
            conf["language_preference"] = None
        if not conf.get('openai_model'):
            conf['openai_model'] = 'gpt-3.5-turbo-1106'
        if not conf.get("pdf_image_crop") or not conf.get("pdf_image_crop").get("threshold") or not conf.get("pdf_image_crop").get("margin") or not conf.get("pdf_image_crop").get("threshold").isdigit() or not conf.get("pdf_image_crop").get("margin").isdigit() or int(conf.get("pdf_image_crop").get("threshold")) < 0 or int(conf.get("pdf_image_crop").get("margin")) < 0:
            raise ValueError("pdf_image_crop not found in configuration file or missing required keys")
        if not conf.get("pdf_image_crop").get("dpi") or not conf.get("pdf_image_crop").get("dpi").isdigit() or int(conf.get("pdf_image_crop").get("dpi")) < 1:
            conf["pdf_image_crop"]["dpi"] = 700
        basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

    def get(self, key):
        """
        Retrieves the value of a specific configuration key.

        Args:
            key (str): The configuration key to retrieve.

        Returns:
            The value of the configuration key, or None if the key is not found.
        """
        return self.config.get(key)

    def get_full(self):
        """
        Retrieves the full configuration dictionary.

        Returns:
            The full configuration dictionary.
        """
        return self.config