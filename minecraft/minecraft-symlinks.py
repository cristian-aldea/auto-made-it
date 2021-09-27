# =============================================================================
# This script allows you to store your minecraft game data somewhere other
# than the default directory by creating symlinks.
#
# These symlinks are stored within the .minecraft directory and point to other
# folders on your computer
#
# One cool thing about doing this is that you can have your minecraft
# saves on the cloud!
# =============================================================================

import argparse
import os


def confirm() -> bool:
    """
    Ask user to enter Y or N (case-insensitive).
    :return: True if the answer is Y.
    :rtype: bool
    """
    answer = ""
    while answer not in ["y", "n"]:
        answer = input("Continue? [y/n]? ").lower()
    return answer == "y"


parser = argparse.ArgumentParser(
    description='Create symbolic links for minecraft saves')

parser.add_argument("--src", type=str, required=True)
parser.add_argument("--dest", type=str, required=True)

args = parser.parse_args()

src = args.src
dest = args.dest

game_dirs = ["saves", "resourcepacks", "screenshots", "shaderpacks"]

if not os.path.isdir(src):
    print("ERROR: Source path \"{}\" is not valid".format(src))
    exit()
elif set(os.listdir(src)) != set(game_dirs):
    print("ERROR: Source path {} must contain dirs {}".format(src, game_dirs))

if not os.path.isdir(dest):
    print("ERROR: Destination (i.e. the link path) \"{}\" is not valid".format(dest))
    exit()
elif not os.path.basename(dest) == ".minecraft":
    print("ERROR: Destination (i.e. the link path) \"{}\" must be a \".minecraft\" folder".format(dest))
    exit()

print("Creating symbolic links with the following configuration:")
print("Source directory: {}".format(src))
print("Link directory: {}".format(dest))
print("Folders to link: {}".format(game_dirs))
cont = confirm()

if not cont:
    exit()

for game_dir in game_dirs:
    srcDir = os.path.join(src, game_dir)
    destDir = os.path.join(dest, game_dir)

    print("\nCreating a symbolic link at \"{}\" pointing to \"{}\"".format(dest, src))

    os.symlink(srcDir, destDir)

print("\nOperation complete!")
