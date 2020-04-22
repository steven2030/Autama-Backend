"""
This file contains code to build a Nucleus. Run this file by entering
"python build.py" to generate a nucleus.pickle file.
"""

from Nucleus.nucleus import Nucleus
from Nucleus.tools import write_pickle


def main():
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


if __name__ == '__main__':
    main()