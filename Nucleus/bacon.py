"""
BACON = Building Autama's Core Overall Nature

This file contains a class to handle generating an Autama's personality.
"""

from Nucleus.nucleus import Nucleus


class Bacon:
    def __init__(self):
        self.__extension = ".json"
        self.__nucleus = Nucleus()

    """def generate_identity(self, autama_id: str):
        personality = self.__nucleus.generate_personality()
        self.__nucleus.display_personality(personality)
        file = autama_id + self.__extension
        return personality"""
