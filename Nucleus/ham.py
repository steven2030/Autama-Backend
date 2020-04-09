"""
HAM = Human Autama Messaging

This file contains a class to handle conversing with an Autama.
"""

from Nucleus.nucleus import Nucleus
from Nucleus.tools import read_json


class Ham:
    def __init__(self, name: str, personality: list):
        self.__nucleus = Nucleus()
        self.__name = name
        #self.__file_name = autama_id + ".json"
        #self.__personality = read_json(self.__file_name)
        self.__personality = personality

    # A method to display the Autama's personality
    def display_personality(self):
        self.__nucleus.display_personality(self.__personality)

    # A method returns Autama's output by taking in user's input
    def converse(self, user_input: str):
        # Returning placeholder for testing purpose
        placeholder = "A response from Ham. This is a placeholder. User's input: " + user_input
        return placeholder
        #return self.__nucleus.converse_with(self.__personality, user_input)

    # Method checks for name and then converse
    def name_check_converse(self, user_input: str):
        if "what is your name" in user_input or "name" in user_input:
            return "my name is " + self.__name
        elif "who are you" in user_input or "who dis" in user_input:
            return "i'm " + self.__name
        else:
            return self.converse(user_input)
