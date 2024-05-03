"""
The UserInput class is initialised at the start of the program.
It is used to ask the user for specific instructions regarding the program's execution.
It then returns a dictionary of keys, which other classes can use.

For V1.0, the UserInput class will only ask the user for the start and end index of the PDF files to be processed.
"""

import sys
from logging import info
import re
class UserInput():
    def __init__(self):
        """
        Initializes the UserInput object.
        """
        
        self.user_input = {}
        info("UserInput initialized successfully \n\n")
    def init(self):
        """
        Asks the user for the start and end index of the PDF files to be processed.
        Returns:
            dict: A dictionary containing the start and end index provided by the user.
        """
        info("Getting user input")
        self.user_input["start_index"] = input(self._get_input_message("start index"))
        while not self._validate_digit(self.user_input["start_index"]):
            self.user_input["start_index"] = input(self._get_input_message("start index"))

        self.user_input["end_index"] = input(self._get_input_message("end index"))
        while not self._validate_digit(self.user_input["end_index"]):
            self.user_input["end_index"] = input(self._get_input_message("end index"))
        if int(self.user_input["end_index"]) < int(self.user_input["start_index"]):
            raise ValueError("End index cannot be less than start index")
        
        self.user_input["remove_indices"] = input("Enter the pdf numbers to be removed, separated by a comma: ")
        while not self._validate_remove_indices(self.user_input["remove_indices"]):
            self.user_input["remove_indices"] = input("Enter the pdf numbers to be removed, separated by a comma: ")
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

    def _validate_remove_indices(self, remove_indices:str):
        """
        Validates the user input for removed PDFs.
        Args:
            remove_indices (str): The user input for removed PDFs.
        Returns:
            bool: True if the input is valid, False otherwise.
        """
        if remove_indices == "":
            return True
        pdf_numbers = remove_indices.split(",")
        for pdf_number in pdf_numbers:
            if re.match(r'^\d+-\d+$', pdf_number):
                return True
            if pdf_number.isdigit() and int(pdf_number) >= 0:
                return True
            
        return False
    def _get_input_message(self, digit_name):
        """
        Generates the input message for the user.
        Args:
            digit_name (str): The name of the digit being asked for.
        Returns:
            str: The input message.
        """
        return f"Enter the {digit_name}. It should be a value greater than 0. Enter -1 to Terminate: "
    def get(self,key:str):
        """
        Returns the user input.
        Returns:
            dict: A dictionary containing the user input.
        """
        if key not in self.user_input:
            raise KeyError(f"Key {key} not found in user input")
        return self.user_input.get(key)