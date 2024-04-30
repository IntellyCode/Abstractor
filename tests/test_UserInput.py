import unittest
from unittest.mock import patch
from src.abstractor.UserInput import UserInput

class UserInputTests(unittest.TestCase):
    def setUp(self):
        self.user_input = UserInput()

    @patch('builtins.input', side_effect=['1', '5'])
    def test_get_user_input(self, mock_input):
        expected_output = {'start_index': '1', 'end_index': '5'}
        result = self.user_input.get_user_input()
        self.assertEqual(result, expected_output)

    def test_get_input_message(self):
        digit_name = 'start index'
        expected_output = "Enter the start index. It should be a value greater than 0. Enter -1 to Terminate: "
        result = self.user_input._get_input_message(digit_name)
        self.assertEqual(result, expected_output)

if __name__ == "__main__":
    unittest.main()