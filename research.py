import csv
import re

# Remove numbers from review.txt and AI-review.txt
def remove_numbers_from_file(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for line in lines:
            cleaned_line = re.sub(r'\b([1-9][0-9]{0,2}|1000)\b', '', line)
            cleaned_line = cleaned_line[1:]
            file.write(cleaned_line.strip() + '\n')

# Remove numbers from review.txt and AI-review.txt
remove_numbers_from_file('review.txt', 'review_cleaned.txt')
remove_numbers_from_file('AI-review.txt', 'AI-review_cleaned.txt')

#create csv file from review.txt and AI-review.txt
def create_csv_from_files(review_file, ai_review_file, output_csv):
    with open(output_csv, mode='w', newline='') as csv_file:
        fieldnames = ['text', 'label']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        
        # Write human reviews
        with open(review_file, 'r') as file:
            for line in file:
                writer.writerow({'text': line.strip(), 'label': 'human'})
        
        # Write AI reviews
        with open(ai_review_file, 'r') as file:
            for line in file:
                writer.writerow({'text': line.strip(), 'label': 'ai'})


create_csv_from_files('review_cleaned.txt', 'AI-review_cleaned.txt', 'review-human-ai.csv')

