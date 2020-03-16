"""
This file contains useful functions to cut down copying and pasting similar code.
"""

import json
import os


# A function to check if file exists. Return true if it exists else false
def file_exists(name: str):
    file_name = name + ".json"
    return os.path.exists(file_name)


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
