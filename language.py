"""
This file contains code to download and cache a pre-trained language model
from HuggingFace Inc.
"""

from Nucleus.bacon import Bacon


def main():
    print("Downloading and caching the pre-trained language could take 20 minutes or more.")
    bacon = Bacon()
    personality = bacon.generate_full_personality()
    print("The process is done.")
    print('There should now be a file named "dataset_cache_OpenAIGPTTokenizer" in the same directory the "manage.py" file is in.')
    print("Here is an example personality:")
    print(personality)


if __name__ == '__main__':
    main()
