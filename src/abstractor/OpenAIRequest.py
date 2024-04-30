"""
This module contains the OpenAIRequest class, which uses the OpenAI API to make requests to the OpenAI GPT-3 model.
"""

from openai import OpenAI
import json
from logging import info
from src.abstractor.Config import Config

class OpenAIRequest():
    """
    This class represents an object that interacts with the OpenAI API to make requests to the OpenAI GPT-3 model.

    Attributes:
        client (OpenAI): The OpenAI client object used to make API requests.
        model (str): The name of the OpenAI model to use.
        instruction (str): The instruction to provide to the model.
    """

    def __init__(self, config: Config):
        """
        Initializes an OpenAIRequest object.

        Args:
            config (Config): The configuration object containing the OpenAI API key, model name, and instruction.
        """
        info("Initializing OpenAIRequest Object")
        
        self.client = OpenAI(api_key=config.get("openai_api_key"))
        self.model = config.get("openai_model")
        self.instruction = config.get("instruction")

    def get_response(self, content):
        """
        Sends a request to the OpenAI GPT-3 model and returns the response.

        Args:
            content (str): The content of the user's input.

        Returns:
            dict: The response from the OpenAI GPT-3 model, parsed as a dictionary.
        """
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": self.instruction    
                },
                {
                    "role": "user",
                    "content": content
                }
            ]
        )
        val_string = completion.choices[0].message.content
        info("Response: " + val_string)
        try:
            data = json.loads(val_string)
        except:
            data = {"VALUE": val_string}
        return data