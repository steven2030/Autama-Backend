"""
HAM = Human Autama Messaging

This file contains a class to handle conversing with an Autama.
"""

from Nucleus.nucleus import Nucleus
from Nucleus.tools import read_json


class Ham:
    def __init__(self, autama_id: str):
        self.__nucleus = Nucleus()
        self.__file_name = autama_id + ".json"
        self.__personality = read_json(self.__file_name)

    # A method to display the Autama's personality
    def display_personality(self):
        self.__nucleus.display_personality(self.__personality)

    # Method returns Autama's output by taking in user's input
    def converse(self, user_input: str):
        return self.__nucleus.converse_with(self.__personality, user_input)
