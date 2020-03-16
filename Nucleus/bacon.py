"""
BACON = Building Autama's Core Overall Nature

This file contains a class to handle generating and saving an Autama's personality.
"""

from Nucleus.nucleus import Nucleus
from Nucleus.tools import write_json


class Bacon:
    def __init__(self):
        self.__extension = ".json"
        self.__nucleus = Nucleus()

    def generate_identity(self, autama_id: str):
        personality = self.__nucleus.generate_personality()
        self.__nucleus.display_personality(personality)
        file = autama_id + self.__extension
        write_json(file, personality)
