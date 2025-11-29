"""
This module provides functionality to validate filenames in the translations directory.

It checks if the files in the specified directory follow the expected naming convention
`README.<language_code>.md`. This helps in maintaining consistency across the
repository's documentation structure.
"""

import os
import re
from typing import List, Tuple

def get_files_in_directory(directory_path: str) -> List[str]:
    """
    Retrieves a list of filenames from a specified directory.

    This function scans the given directory path and returns a list containing
    the names of all files found within it. It does not recursively search
    subdirectories.

    Args:
        directory_path (str): The path to the directory to search.

    Returns:
        List[str]: A list of filenames found in the directory. Returns an empty
                   list if the directory does not exist or is empty.
    """
    if not os.path.exists(directory_path):
        return []

    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
    return files

def validate_filename_pattern(filename: str) -> bool:
    """
    Checks if a filename matches the expected `README.<code >.md` pattern.

    The expected pattern is `README.` followed by a language code (alphanumeric
    characters, hyphens, or underscores) and ending with `.md`.
    Exception: `Translations.md` is also considered valid.

    Args:
        filename (str): The filename to validate.

    Returns:
        bool: True if the filename matches the pattern or is an exception, False otherwise.
    """
    if filename == "Translations.md":
        return True

    pattern = r"^README\.[a-zA-Z0-9_\-]+\.md$"
    return bool(re.match(pattern, filename))

def scan_and_validate(directory_path: str) -> Tuple[List[str], List[str]]:
    """
    Scans a directory and validates all filenames against the naming convention.

    This function combines file retrieval and pattern validation to produce
    two lists: one for valid filenames and one for invalid filenames.

    Args:
        directory_path (str): The path to the directory to scan.

    Returns:
        Tuple[List[str], List[str]]: A tuple containing two lists:
            - The first list contains valid filenames.
            - The second list contains invalid filenames.
    """
    files = get_files_in_directory(directory_path)
    valid_files = []
    invalid_files = []

    for filename in files:
        if validate_filename_pattern(filename):
            valid_files.append(filename)
        else:
            invalid_files.append(filename)

    return valid_files, invalid_files

def main():
    """
    The main entry point of the script.

    It defines the target directory, runs the validation process, and prints
    a summary report to the console.
    """
    target_directory = os.path.join("docs", "translations")

    # Check if we are running from the root of the repo
    if not os.path.exists(target_directory):
        # Try adjusting if we are running inside scripts/
        if os.path.exists(os.path.join("..", target_directory)):
            target_directory = os.path.join("..", target_directory)
        else:
            print(f"Error: Directory '{target_directory}' not found.")
            return

    print(f"Scanning directory: {target_directory}")
    valid, invalid = scan_and_validate(target_directory)

    print(f"\nFound {len(valid)} valid files.")
    print(f"Found {len(invalid)} invalid files.")

    if invalid:
        print("\nInvalid files found:")
        for f in invalid:
            print(f" - {f}")
    else:
        print("\nAll files follow the naming convention.")

if __name__ == "__main__":
    main()
