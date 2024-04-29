import unittest
from src.abstractor.AbstractWriter import AbstractWriter
from src.abstractor.Config import Config
from logging import *
from os import path
class AbstractWriterTests(unittest.TestCase):
    def setUp(self):
        self.config = Config("./src/abstractor/config.json")
        self.abstract_writer = AbstractWriter(self.config)

    def test_write_abstract(self):
        debug("Testing writing abstract to output file")
        abstract = "This is a sample abstract."
        self.abstract_writer.set_output_file("output.txt")
        self.abstract_writer.write(abstract)
        # Assert that the output file exists
        self.assertTrue(path.exists(self.abstract_writer.output_file_path))
        # Assert that the content of the output file matches the abstract
        with open(self.abstract_writer.output_file_path, "r") as f:
            content = f.read()
            self.assertEqual(content, abstract)

if __name__ == "__main__":
    unittest.main()