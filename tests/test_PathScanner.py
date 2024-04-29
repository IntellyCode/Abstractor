import unittest
from src.abstractor.PathScanner import PathScanner
from logging import *
from src.abstractor.Config import Config
class PathScannerTests(unittest.TestCase):
    def setUp(self):
        self.config = Config("./src/abstractor/config.json")
        self.path_scanner = PathScanner(config=self.config)

    def test_display_pdfs(self):
        debug("Testing Displaying pdfs")
        self.path_scanner.scan()
        self.path_scanner.display_pdfs()
if __name__ == "__main__":
    unittest.main()