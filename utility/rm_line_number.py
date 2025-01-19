import re
import sys
# Remove numbers from review.txt and AI-review.txt
def remove_numbers_from_file(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(input_file, 'w') as file:
        for line in lines:
            cleaned_line = re.sub(r'\b([1-9][0-9]{0,2}|1000)\b', '', line)

            file.write(cleaned_line.strip() + '\n')


# Check if the script is being called with a filename argument
if len(sys.argv) != 2:
    print("Usage: python3 rm_line_number.py <input_file>")
    sys.exit(1)

# Get the filename from the command line argument
input_file = sys.argv[1]
remove_numbers_from_file(input_file)