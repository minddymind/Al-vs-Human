import os
import sys

def split_file_by_lines(input_file_path, output_folder, lines_per_file=1000):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Read the input file
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Initialize variables
    file_count = 1
    current_lines = []
    
    # Iterate over the lines and split into new files
    for i, line in enumerate(lines):
        current_lines.append(line)
        
        # If we've reached the limit (1000 lines), write to a new file
        if len(current_lines) == lines_per_file:
            output_file_path = os.path.join(output_folder, f'review{file_count}.txt')
            with open(output_file_path, 'w') as output_file:
                output_file.writelines(current_lines)
            
            # Reset for the next file
            current_lines = []
            file_count += 1
    
    # Handle the last remaining lines (less than 1000)
    if current_lines:
        output_file_path = os.path.join(output_folder, f'review{file_count}.txt')
        with open(output_file_path, 'w') as output_file:
            output_file.writelines(current_lines)

    print(f"Files have been split and saved to {output_folder}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python split_file.py <input_file_path> <output_folder> <lines_per_file>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]  # Path to the input file
    output_folder = sys.argv[2]    # Folder to save the output files
    lines_per_file = int(sys.argv[3])  # Number of lines per file
    
    # Call the function to split the file
    split_file_by_lines(input_file_path, output_folder, lines_per_file)
