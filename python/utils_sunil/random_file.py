#!python
import sys
import os
import random


def main():
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        files = filter(os.path.isfile, map(lambda f: os.path.join(directory, f), os.listdir(directory)))
        file = random.choice(list(files))
        print("Starting {}".format(file))
        os.system("call " + '"' + file + '"')


if __name__ == "__main__":
    main()
