import re
import sys

# Remove numbers from the beginning of each line in the input file
def remove_numbers_from_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(input_file, 'w') as file:
        for line in lines:
            # Remove any number followed by a period or a colon (e.g., "1. ", "200. ", "441: ")
            cleaned_line = re.sub(r'^\d+[\.:]\s*', '', line)

            file.write(cleaned_line)

# Check if the script is being called with a filename argument
if len(sys.argv) != 2:
    print("Usage: python3 rm_line_number.py <input_file>")
    sys.exit(1)

# Get the filename from the command line argument
input_file = sys.argv[1]
remove_numbers_from_file(input_file)
