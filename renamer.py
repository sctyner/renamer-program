#! /usr/bin/env python
"""
Sequentially show all images in a folder and allow them to be renamed.

TODO: Keep first plot from changing focus from the terminal window.

Author: Jason Saporta
Date: 3/19/2018
"""
"""
line below is necessary for python 2 (i think it's a 2 v 3 issue. it wouldn't run on my system without it.) 
from __future__ import print_function
"""
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from glob import glob

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

parser = ArgumentParser(description="Display images in a folder and " +
                        "easily rename them.",
                        formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("extension", type=str, default="png", nargs="?",
                    help="Extension of files you would like to rename.")
args = parser.parse_args()


def main():
    """Run only when this is executed from the command line."""
    print("For each image, type the new name of the file." +
          " No extension necessary!", end="\n\n")
    file_list = glob("*." + args.extension)
    plt.ion()

    for pic in file_list:
        img = mpimg.imread(pic)
        plt.imshow(img)
        plt.draw()
        plt.pause(0.001)
        new_name = input(
            "Please enter a new filename. Press [enter] to skip: ")
        if not new_name == "":
            if not new_name.endswith(args.extension):
                new_name += "." + args.extension
            plt.savefig(new_name, format=args.extension)


if __name__ == '__main__':
    main()
