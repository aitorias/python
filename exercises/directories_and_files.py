# Check if is a directory or file inside a given directory
import os


def check_if_is_directory_or_file(directory):
    for name in os.listdir(directory):
        fullname = os.path.join(directory, name)
        print(f'{fullname} is a directory') if os.path.isdir(
            fullname) else print(f'{fullname} is a file')
