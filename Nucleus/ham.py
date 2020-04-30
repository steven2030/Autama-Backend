"""
HAM = Human Autama Messaging

This file contains a class to handle conversing with an Autama.
"""

import torch

from itertools import chain
from Nucleus.interact import sample_sequence
from Nucleus.tools import read_pickle


class Ham:
    def __init__(self, first_name: str, last_name: str, personality: list):
        # For creating a conversation environment
        self.__nucleus = read_pickle("nucleus.pickle")
        self.__args = self.__nucleus.get_args()
        self.__logger = self.__nucleus.get_logger()
        self.__model = self.__nucleus.get_model()
        self.__tokenizer = self.__nucleus.get_tokenizer()
        # Autama's identifiers
        self.__first_name = first_name
        self.__last_name = last_name
        self.__full_name = first_name + " " + last_name
        self.__personality = personality
        # An identity is a list containing a name and a personality
        self.__identity = self.__tokenize_and_encode(personality)
        self.__history = []

    # A method that returns Autama's output by taking in user's input
    def converse(self, user_input: str):
        self.__history.append(self.__tokenizer.encode(user_input))
        with torch.no_grad():
            out_ids = sample_sequence(self.__identity, self.__history, self.__tokenizer, self.__model, self.__args)
        self.__history.append(out_ids)
        self.__history = self.__history[-(2 * self.__args.max_history + 1):]
        nucleus_output = self.__tokenizer.decode(out_ids, skip_special_tokens=True)
        return nucleus_output

    # A method that checks for name before conversing
    def check_converse(self, user_input: str):
        if "what is your name" in user_input or "your name?" in user_input:
            return "my name is " + self.__first_name
        elif "who are you" in user_input or "who dis" in user_input:
            return "i'm " + self.__first_name
        else:
            return self.converse(user_input)

    # A method to display the Autama's identity
    def display_identity(self):
        print("Identity: " + self.__tokenizer.decode(chain(*self.__identity)))

    # A method to tokenize and encode an identity
    def __tokenize_and_encode(self, identity: list):
        def tokenize(obj):
            if isinstance(obj, str):
                return self.__tokenizer.convert_tokens_to_ids(self.__tokenizer.tokenize(obj))
            if isinstance(obj, dict):
                return dict((n, tokenize(o)) for n, o in obj.items())
            return list(tokenize(o) for o in obj)

        return tokenize(identity)
