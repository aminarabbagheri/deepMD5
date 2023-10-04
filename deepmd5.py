import hashlib
import glob
import sys
import os

def calculate_md5_checksum(file_path):
    """
    Calculate the MD5 checksum of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The MD5 checksum as a hexadecimal string.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()

def main():
    # Check if the output file already exists and remove it if it does
    output_path = sys.argv[2]
    if os.path.exists(output_path):
        os.remove(output_path)

    # Get the input path and expand it to include all files in the directory
    input_path = sys.argv[1]
    if input_path.endswith('/'):
        search_pattern = input_path + "*"
    else:
        search_pattern = input_path + "/*"

    file_list = glob.glob(search_pattern)
    print("List of files:", file_list)

    # Open the output file for writing
    with open(output_path, "x") as output_file:
        for file_path in file_list:
            md5_checksum = calculate_md5_checksum(file_path)
            output_file.write(md5_checksum + "\n")

if __name__ == "__main__":
    main()