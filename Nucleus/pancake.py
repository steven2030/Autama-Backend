"""
PANCAKE = Preparing Autama's Name Carefully And Kinda Equally

This file contains a class to handle generating random name.
"""

from random import choice, seed


class Pancake:
    def __init__(self):
        self.__female_names_file = "female_names.txt"
        self.__male_names_file = "male_names.txt"
        self.__female_names_list = open(self.__female_names_file).read().splitlines()
        self.__male_names_list = open(self.__male_names_file).read().splitlines()

    # A method to generate a random female name
    def generate_female_name(self):
        seed()
        return choice(self.__female_names_list)

    # A method to generate a random male name
    def generate_male_name(self):
        seed()
        return choice(self.__male_names_list)

    """Methods for testing."""

    # A method to print female names list
    def print_female_names(self):
        print(self.__female_names_list)

    # A method to print male names list
    def print_male_names(self):
        print(self.__male_names_list)