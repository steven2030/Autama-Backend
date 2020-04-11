"""
HAM = Human Autama Messaging

This file contains a class to handle conversing with an Autama.
"""

from Nucleus.tools import read_pickle


class Ham:
    def __init__(self, name: str, personality: list):
        self.__nucleus = read_pickle("nucleus.pickle")
        self.__name = name
        self.__personality = personality

    # A method to display the Autama's personality
    def display_personality(self):
        self.__nucleus.display_personality(self.__personality)

    # A method returns Autama's output by taking in user's input
    def converse(self, user_input: str):
        return self.__nucleus.converse_with(self.__personality, user_input)

    # Method checks for name and then converse
    def name_check_converse(self, user_input: str):
        if "what is your name" in user_input or "name" in user_input:
            return "my name is " + self.__name
        elif "who are you" in user_input or "who dis" in user_input:
            return "i'm " + self.__name
        else:
            return self.converse(user_input)
