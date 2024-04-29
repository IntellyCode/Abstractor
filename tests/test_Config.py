import unittest
import logging
import os
from src.abstractor.Config import Config

class ConfigTests(unittest.TestCase):
    def setUp(self):
        self.config = Config("./src/abstractor/config.json")

    def test_get_log_level(self):
        log_level = self.config.get("log_level")
        self.assertIsNotNone(log_level)
        self.assertIn(log_level, ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"])

    def test_get_openai_api_key(self):
        openai_api_key = self.config.get("openai_api_key")
        self.assertIsNotNone(openai_api_key)

    def test_get_input_dir(self):
        input_dir = self.config.get("input_dir")
        self.assertIsNotNone(input_dir)
        self.assertTrue(os.path.isdir(input_dir))

    def test_get_output_dir(self):
        output_dir = self.config.get("output_dir")
        self.assertIsNotNone(output_dir)
        self.assertTrue(os.path.isdir(output_dir))

    def test_get_display_mode(self):
        display_mode = self.config.get("display_mode")
        self.assertIsNotNone(display_mode)
        self.assertIn(display_mode, ["L", "S"])

    def test_get_pages_per_pdf(self):
        pages_per_pdf = self.config.get("pages_per_pdf")
        self.assertIsNotNone(pages_per_pdf)

    def test_get_start_index(self):
        start_index = self.config.get("start_index")
        self.assertIsNotNone(start_index)
        self.assertTrue(start_index.isdigit())
        self.assertGreaterEqual(int(start_index), 0)

    def test_get_end_index(self):
        end_index = self.config.get("end_index")
        self.assertIsNotNone(end_index)
        self.assertTrue(end_index.isdigit())
        self.assertGreaterEqual(int(end_index), 0)

    def test_get_instruction(self):
        instruction = self.config.get("instruction")
        self.assertIsNotNone(instruction)

    def test_get_full(self):
        full_config = self.config.get_full()
        self.assertIsNotNone(full_config)

if __name__ == "__main__":
    unittest.main()