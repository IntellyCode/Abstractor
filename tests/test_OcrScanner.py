import unittest
from unittest.mock import MagicMock
from PIL import Image
from src.abstractor.OcrScanner import OcrScanner
from src.abstractor.Config import Config

class OcrScannerTests(unittest.TestCase):
    def setUp(self):
        self.config = Config("./src/abstractor/config.json")
        self.scanner = OcrScanner(self.config)

    def test_scan_returns_text(self):
        # Arrange
        image = Image.open("./tests/images/test_image.png")

        # Act
        result = self.scanner.scan(image)

        # Assert
        self.assertIsInstance(result, str)
        self.assertNotEqual(result, "")
if __name__ == "__main__":
    unittest.main()