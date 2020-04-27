"""
This file contains code to download and cache a pre-trained language model
from HuggingFace Inc.
"""

from Nucleus.bacon import Bacon


def main():
    print("Downloading and caching the pre-trained language could take 20 minutes or more.")
    bacon = Bacon()
    personality = bacon.generate_full_personality()
    print("The process is done. Here is an example personality: ")
    print(personality)


if __name__ == '__main__':
    main()
