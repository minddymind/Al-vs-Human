import csv
import sys

def create_csv_from_files(review_file, ai_review_file, output_csv):
    with open(output_csv, mode='w', newline='') as csv_file:
        fieldnames = ['text', 'label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Open both files
        with open(review_file, 'r') as human_file, open(ai_review_file, 'r') as ai_file:
            # Read lines from both files
            human_lines = human_file.readlines()
            ai_lines = ai_file.readlines()

            # Interleave lines from both lists
            for human_line, ai_line in zip(human_lines, ai_lines):
                writer.writerow({'text': human_line.strip(), 'label': 'human'})
                writer.writerow({'text': ai_line.strip(), 'label': 'ai'})

# Check for correct arguments
if len(sys.argv) != 4:
    print("Usage: python3 create_csv.py <review_file> <ai_review_file> <output_csv>")
    sys.exit(1)

# Get file paths from command-line arguments
review_file = sys.argv[1]
ai_review_file = sys.argv[2]
output_csv = sys.argv[3]

# Create the CSV file
create_csv_from_files(review_file, ai_review_file, output_csv)
