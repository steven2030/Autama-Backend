"""
This file contains useful functions to cut down copying and pasting similar code.
"""

import pickle
import json


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


# A function to write an object as a json file
def write_json(file_name: str, item):
    json_out = open(file_name, "w")
    json.dump(item, json_out)
    json_out.close()


# A function to read in a json file
def read_json(file_name: str):
    json_in = open(file_name, "r")
    item = json.load(json_in)
    json_in.close()
    return item
