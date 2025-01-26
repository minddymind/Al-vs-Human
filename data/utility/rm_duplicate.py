import sys

def remove_duplicates(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        lines = file.readlines()

    # Remove duplicates by converting lines to a set and back to a list
    unique_lines = list(set(lines))

    # Write the unique lines to a new output file
    with open(output_file_path, 'w') as file:
        file.writelines(unique_lines)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rm_duplicate.py <input_file_path> <output_file_path>")
        sys.exit(1)
    
    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    remove_duplicates(input_file_path, output_file_path)
    print(f"Duplicate lines removed and saved to {output_file_path}")
