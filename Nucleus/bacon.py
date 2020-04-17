"""
BACON = Building Autama's Core Overall Nature

This file contains a class to handle generating an Autama's personality.
"""

from itertools import chain
from random import choice
from Nucleus.utils import get_dataset
from Nucleus.tools import read_pickle


class Bacon:
    def __init__(self):
        self.__nucleus = read_pickle("nucleus.pickle")
        self.__args = self.__nucleus.get_args()
        self.__tokenizer = self.__nucleus.get_tokenizer()

    # A method to generate a random personality. It returns a list of personality trait strings.
    def generate_personality(self):
        encoded_personality = self.__generate_encoded_personality()
        return self.__decode_personality(encoded_personality)

    # A method for generating one encoded personality
    def __generate_encoded_personality(self):
        dataset = get_dataset(self.__tokenizer, self.__args.dataset_path, self.__args.dataset_cache)
        personalities = [dialog["personality"] for dataset in dataset.values() for dialog in dataset]
        personality = choice(personalities)
        return personality

    # A method for decoding an encoded personality
    def __decode_personality(self, encoded_personality: list):
        encoded_personality_string = self.__tokenizer.decode(chain(*encoded_personality))
        decoded_personality_list = [i + "." for i in encoded_personality_string.split(".")]
        decoded_personality_list.pop()
        return decoded_personality_list
