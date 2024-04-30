"""
The UserInput class is initialised at the start of the program.
It is used to ask the user for specific instructions regarding the program's execution.
It then returns a dictionary of keys, which other classes can use.

For V1.0, the UserInput class will only ask the user for the start and end index of the PDF files to be processed.
"""

import sys
from logging import info
class UserInput():
    def __init__(self):
        """
        Initializes the UserInput object.
        """
        
        self.user_input = {}
        info("UserInput initialized successfully \n\n")
    def get_user_input(self):
        """
        Asks the user for the start and end index of the PDF files to be processed.
        Returns:
            dict: A dictionary containing the start and end index provided by the user.
        """
        info("Getting user input")
        self.user_input["start_index"] = input(self._get_input_message("start index"))
        while not self._alidate_digit(self.user_input["start_index"]):
            self.user_input["start_index"] = input(self._get_input_message("start index"))

        self.user_input["end_index"] = input(self._get_input_message("end index"))
        while not self._validate_digit(self.user_input["end_index"]):
            self.user_input["end_index"] = input(self._get_input_message("end index"))

        return self.user_input

    def _validate_digit(self, digit:str):
        """
        Validates the user input.
        Args:
            digit (str): The user input to be validated.
        Returns:
            bool: True if the input is valid, False otherwise.
        """
        if digit == "-1":
            sys.exit("Terminated by user")
        if (not digit.isdigit() or int(digit) < 0):
            return False
        return True

    def _get_input_message(self, digit_name):
        """
        Generates the input message for the user.
        Args:
            digit_name (str): The name of the digit being asked for.
        Returns:
            str: The input message.
        """
        return f"Enter the {digit_name}. It should be a value greater than 0. Enter -1 to Terminate: "