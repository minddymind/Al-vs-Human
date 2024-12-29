import os

def remove_empty_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip():
                file.write(line)

# Usage
# Usage
current_directory = os.getcwd()
file_path = os.path.join(current_directory, 'AI-review.txt')
remove_empty_lines(file_path)