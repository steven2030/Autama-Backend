"""
This file contains code to download and cache a personality data set
from HuggingFace Inc.
"""

from Nucleus.nucleus import Nucleus
from Nucleus.utils import get_dataset
from random import choice
from itertools import chain


def main():
    print("Downloading and caching the pre-trained language could take 15 minutes or more.")
    nucleus = Nucleus()
    tokenizer = nucleus.get_tokenizer()
    args = nucleus.get_args()
    dataset = get_dataset(tokenizer, args.dataset_path, args.dataset_cache)
    personalities = [dialog["personality"] for dataset in dataset.values() for dialog in dataset]
    personality = choice(personalities)
    encoded_personality_string = tokenizer.decode(chain(*personality))
    decoded_personality_list = [i + "." for i in encoded_personality_string.split(".")]
    decoded_personality_list.pop()
    print("The process is done.")
    print('There should now be a file named "dataset_cache_OpenAIGPTTokenizer" in the same directory the "manage.py" file is in.')
    print("Here is an example personality:")
    print(decoded_personality_list)


if __name__ == '__main__':
    main()
