"""
This file contains useful functions to cut down copying and pasting similar code.
"""

import pickle

from Nucleus.nucleus import Nucleus


# A function to write an object as a pickle file
def write_pickle(file_name, item):
    pickle_out = open(file_name, "wb")
    pickle.dump(item, pickle_out)
    pickle_out.close()


# A function to read in a pickle file
def read_pickle(file_name):
    pickle_in = open(file_name, "rb")
    item = pickle.load(pickle_in)
    pickle_in.close()
    return item


# A function to generate a nucleus.pickle file
def build_nucleus():
    pickle_file = "nucleus.pickle"
    py_file = "build.py"
    directory = "Autama-Backend"

    nucleus = Nucleus()
    write_pickle(pickle_file, nucleus)

    sentence1 = 'A file called "' + pickle_file + '" should have been generated. '
    sentence2 = 'Make sure it is in the same directory "' + py_file + '" is in. '
    sentence3 = 'Both "' + pickle_file + '" and "' + py_file + '" should be in the "' + directory + '" directory. '
    sentence4 = "Give it a few seconds if you don't see it right away."
    print(sentence1 + sentence2 + sentence3 + sentence4)
