import os
import sys

def add_line_numbers_to_folder(folder_path):
    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Check if it's a file (and optionally check for a specific extension, e.g., .txt)
        if os.path.isfile(file_path) and filename.endswith('.txt'):  # Adjust the file extension if necessary
            print(f"Adding line numbers to {filename}...")
            add_line_numbers(file_path)

def add_line_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Open the file for writing the new content
    with open(file_path, 'w') as file:
        for index, line in enumerate(lines, start=1):
            file.write(f"{index}. {line}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python add_line_numbers.py <folder_path>")
        sys.exit(1)
    
    folder_path = sys.argv[1]
    add_line_numbers_to_folder(folder_path)
    print("Line numbering completed for all files in the folder.")
