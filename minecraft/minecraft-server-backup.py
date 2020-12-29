import argparse
import os
import datetime
import shutil


def backupFolder(source, target):
    if os.path.exists(source):
        print("Saving backup of \"{}\" to \"{}\"".format(source, target))
        shutil.copytree(source, target)
    else:
        print("Could not find \"{}\"".format(source))


# Command-line arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--source', required=True,
                    help="The location of the minecraft world folder to backup")
parser.add_argument('--target', required=True,
                    help="The location where to save backups of the given world folder")
parser.add_argument('--num_backups', required=False, default=10,
                    help="The number of backups to keep")
parser.add_argument('--paper', '-p', required=False, default=False, action='store_true',
                    help="If the current backup is being done for a paper server, which stores the world save in a slightly different format")
args = parser.parse_args()

print("\nArguments: {}".format(args))

if not os.path.exists(args.target):
    print("\nCreating directory {}".format(args.target))
    os.makedirs(args.target)

# Creating path name for new backup
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S:%f")
basename = os.path.basename(args.source)
backup_path = "{}/{}/{}".format(args.target, timestamp, basename)

print()
backupFolder(args.source, backup_path)

if args.paper:
    nether_suffix = '_nether'
    end_suffix = '_the_end'
    print('Paper flag set. Attempting to save nether and end folders.')

    backupFolder(args.source + nether_suffix, backup_path + nether_suffix)
    backupFolder(args.source + end_suffix, backup_path + end_suffix)


# Listing currently saved backups
backups = os.listdir(args.target)
backups.sort()
print("\nCurrent Backups:")
print("\n".join(backups))

# Delete old backups if there are more than the allowed number
while len(backups) > args.num_backups:
    print("\nThere are more than {} backups, deleting older backups".format(
        args.num_backups))
    backup_dir = "{}/{}".format(args.target, backups[0])
    print("Deleting \"{}\"".format(backup_dir))
    shutil.rmtree(backup_dir)
    del backups[0]
