import unittest
from src.abstractor.PathScanner import PathScanner
from logging import *

class PathScannerTests(unittest.TestCase):
    def setUp(self):
        self.path_scanner = PathScanner("./src/abstractor/config.json")

    def test_display_pdfs(self):
        debug("Testing Displaying pdfs")
        self.path_scanner.scan()
        self.path_scanner.display_pdfs()
if __name__ == "__main__":
    unittest.main()