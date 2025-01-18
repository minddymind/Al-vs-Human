import sys
def remove_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip():
                file.write(line)


def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')

# Check if the script is being called with a filename argument
if len(sys.argv) != 2:
    print("Usage: python3 rm-backspace.py <filename>")
    sys.exit(1)

# Get the filename from the command line argument
file_path = sys.argv[1]

# Call the remove_newlines function with the passed file path
remove_newlines(file_path)

# for i in range(1,11):
#     file_path = '/Users/sunson/coding/research 490/review' + str(i)+ '-ai' + '.txt'
#     create_file(file_path)
#     print(file_path)