import unittest
from unittest.mock import MagicMock
from src.abstractor.OpenAIRequest import OpenAIRequest
from src.abstractor.Config import Config

class OpenAIRequestTests(unittest.TestCase):
    def setUp(self):
        self.config = Config("./src/abstractor/config.json")
        self.openai_request = OpenAIRequest(self.config)

    def test_get_response(self):
        response = self.openai_request.get_response("Hella, I am a tast messge.")
        print(response)
        self.assertIsInstance(response, dict)

if __name__ == "__main__":
    unittest.main()