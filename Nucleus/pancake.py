"""
PANCAKE = Preparing Autama's Name Carefully And Kinda Equally

This file contains a class to handle generating random name. The class
reads in names from two files, and then randomly picks one to
generate as the name. One of the files is called female_names.txt,
and it contains the top 1000 female names from 2018. The other file
is called male_names.txt, and it contains the top 1000 male names
from 2018. The names are from the Social Security' site which could
be found here: https://www.ssa.gov/cgi-bin/popularnames.cgi
"""

from random import choice, seed, shuffle


class Pancake:
    def __init__(self):
        self.__female_names_file = "Nucleus/female_names.txt"
        self.__male_names_file = "Nucleus/male_names.txt"
        self.__female_names_list = open(self.__female_names_file).read().splitlines()
        self.__male_names_list = open(self.__male_names_file).read().splitlines()
        self.__first_names_list = self.__female_names_list + self.__male_names_list

    # A method to generate a random female name
    def generate_female_name(self):
        seed()
        return choice(self.__female_names_list)

    # A method to generate a random male name
    def generate_male_name(self):
        seed()
        return choice(self.__male_names_list)

    # A method to generate a random first name
    def generate_first_name(self):
        seed()
        shuffle(self.__first_names_list)
        return choice(self.__first_names_list)

    """Methods for testing."""

    # A method to print female names list
    def print_female_names(self):
        print(self.__female_names_list)

    # A method to print male names list
    def print_male_names(self):
        print(self.__male_names_list)

    # A method to print first names list
    def print_first_names(self):
        print(self.__first_names_list)