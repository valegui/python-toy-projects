import argparse
import os
import shutil
from datetime import datetime


def list_files(directory: str):
    return [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]


def copy_file(source, destination):
    shutil.copy2(source, destination)


def create_backup_directory(base_backup_dir):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_dir = os.path.join(base_backup_dir, timestamp)
    os.makedirs(backup_dir, exist_ok=True)
    return backup_dir


def backup_files(source_dir, backup_dir):
    files = list_files(source_dir)
    for file in files:
        source_path = os.path.join(source_dir, file)
        destination_path = os.path.join(backup_dir, file)
        copy_file(source_path, destination_path)
        print(f"Backed up {file}")


def write_log(backup_dir, log_file, files):
    with open(log_file, "a") as log:
        log.write(f"Backup created: {backup_dir}\n")
        for file in files:
            log.write(f" - {file}\n")
        log.write("\n")


def main():
    parser = argparse.ArgumentParser(description="Automated Backup Tool")
    parser.add_argument(
        "--source", type=str, required=True, help="Source directory to backup"
    )
    parser.add_argument("--backup", type=str, required=True, help="Backup directory")
    parser.add_argument("--log", type=str, required=True, help="Log file")
    args = parser.parse_args()
    backup_dir = create_backup_directory(args.backup)
    backup_files(args.source, backup_dir)
    write_log(backup_dir, args.log, list_files(args.source))


if __name__ == "__main__":
    main()
