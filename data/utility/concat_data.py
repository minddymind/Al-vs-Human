import os
import sys

def concatenate_files(input_files, output_file):
    count = 1
    with open(output_file, 'w') as outfile:
        for fname in input_files:
            if os.path.isfile(fname):
                with open(fname) as infile:
                    for line in infile:
                        outfile.write(f"{count}. {line.strip()}\n")
                        count += 1
            else:
                print(f"File {fname} does not exist.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python concatenate_files.py <input_file1> <input_file2> ... <output_file>")
        sys.exit(1)
    
    input_files = sys.argv[1:-1]
    output_file = sys.argv[-1]
    concatenate_files(input_files, output_file)
    print(f"Files concatenated and saved to {output_file}")


# Example usage:
# input_files = ['file1.txt', 'file2.txt', 'file3.txt']
# output_file = 'concatenated_output.txt'
# concatenate_files(input_files, output_file)