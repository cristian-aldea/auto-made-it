import argparse
import os
import datetime
import shutil

# Command-line arguments
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--source', required=True,
                    help="The location of the minecraft world folder to backup")
parser.add_argument('--target', required=True,
                    help="The location where to save backups of the given world folder")
parser.add_argument('--num_backups', required=False, default=8,
                    help="The number of backups to keep")
args = parser.parse_args()

if not os.path.exists(args.target):
    print("Creating diretory {}".format(args.target))
    os.makedirs(args.target)

# Creating path name for new backup
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S:%f")
basename = os.path.basename(args.source)
backup_path = "{}/{}_{}".format(args.target, basename, timestamp)

print("\nSaving backup of \"{}\" to \"{}\"".format(args.source, backup_path))
shutil.copytree(args.source, backup_path)

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
