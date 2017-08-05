import argparse
import glob
import os

from builder import EnumBuilder, MessageBuilder, TypeBuilder

import sys

class ProgressBar:

    def __init__(self, max_=100, current=0, width=40):
        self.max = max_
        self.current = current
        self.width = width

    def print(self):
        percent = self.current / self.max
        activates = int(percent * self.width)
        sys.stdout.write("\r[{0}{1}] {2}% {3}/{4}".format(
            "+" * activates,
            " " * (self.width - activates),
            int(percent * 100),
            self.current,
            self.max
        ))
        sys.stdout.flush()

def get_actionscript_files(path):
    return list(glob.iglob(
        os.path.join(path, "**", "*.as"),
        recursive=True
    ))


def main():
    print("\n".join([
        r"      ::::::::::: ::::::::  :::::::::: :::    :::  :::::::: ",
        r"         :+:    :+:    :+: :+:        :+:    :+: :+:    :+: ",
        r"        +:+    +:+    +:+ +:+        +:+    +:+ +:+         ",
        r"       +#+    +#+    +:+ :#::+::#   +#+    +:+ +#++:++#++   ",
        r"      +#+    +#+    +#+ +#+        +#+    +#+        +#+    ",
        r"     #+#    #+#    #+# #+#        #+#    #+# #+#    #+#     ",
        r"########### ########  ###         ########   ########       ",
        r"             _               _      _       _ _   _         ",
        r" ___ ___ ___| |_ ___ ___ ___| |    | |_ _ _|_| |_| |___ ___ ",
        r"| . |  _| . |  _| . |  _| . | |    | . | | | | | . | -_|  _|",
        r"|  _|_| |___|_| |___|___|___|_|    |___|___|_|_|___|___|_|  ",
        r"|_|                                                         ",
        r"------------------------------------------------------------"
    ]))

    current_dir = os.path.dirname(os.path.realpath(__file__))
    parser = argparse.ArgumentParser(description="Build protocol for the iofus projet.")
    parser.add_argument(
        "-i",
        dest="input_dir",
        help="path to the input dir",
        default=os.path.join(current_dir, "input")
    )
    parser.add_argument(
        "-o",
        dest="output_dir",
        help="path to the output dir",
        default=os.path.join(current_dir, "output")
    )
    args = parser.parse_args()

    enums = get_actionscript_files(os.path.join(args.input_dir, "enums"))
    enums.append(os.path.join(args.input_dir, "Metadata.as"))
    print("{0} enum files found".format(len(enums)))

    messages = get_actionscript_files(os.path.join(args.input_dir, "messages"))
    print("{0} message files found".format(len(messages)))

    types = get_actionscript_files(os.path.join(args.input_dir, "types"))
    print("{0} type files found".format(len(types)))

    elapsed = 0
    print("\nBuilding enum files:")
    progress = ProgressBar(len(enums), 0)
    for elapsed in EnumBuilder.build(enums, os.path.join(args.output_dir, "denums.py")):
        progress.print()
        progress.current += 1
    print()
    print("Enum files built in {0}ms".format(round(elapsed * 1000, 1)))

    print("\nBuilding message files:")
    progress = ProgressBar(len(messages))
    for elapsed in MessageBuilder.build(messages, os.path.join(args.output_dir, "dmessages.py")):
        progress.print()
        progress.current += 1
    print()
    print("Message files built in {0}ms".format(round(elapsed * 1000, 1)))

    print("\nBuilding type files:")
    progress = ProgressBar(len(types))
    for elapsed in TypeBuilder.build(types, os.path.join(args.output_dir, "dtypes.py")):
        progress.print()
        progress.current += 1
    print()
    print("Type files built in {0}ms".format(round(elapsed * 1000, 1)))


if __name__ == "__main__":
    main()
