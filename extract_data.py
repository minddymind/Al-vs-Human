import json
import re
from langdetect import detect
import string

def normalize_and_compare(str1, str2):
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    cleaned_str1 = str1.translate(translator).lower().strip()
    cleaned_str2 = str2.translate(translator).lower().strip()
    
    # Compare the cleaned strings
    return cleaned_str1 == cleaned_str2

def read_file(filename):
    #format sentences and choose only english sentences for 10500 sentences
    with open(filename, 'r') as file:
        unique_senteces = set()
        sentence_count = 0
        for line in file:
            if sentence_count == 10500:
                break
            this_line = json.loads(line.strip())
            review_text = re.sub(r'[\\/]', '', re.sub(r'<[^>]*>', '', re.sub(r'\[\[.*?\]\]', '', re.sub(r'\(\d+ stars\)', '', this_line["text"]))))
            try:
                if detect(review_text) != 'en':
                    continue
            except:
                continue
            formatted_print = f"{review_text}\n"  
            if len(formatted_print) < 10:
                continue

            for unique_sent in unique_senteces:
                if normalize_and_compare(unique_sent, formatted_print):
                    continue
            
            with open('original_review.txt', 'a') as review_file:
                review_file.write(formatted_print)
                unique_senteces.add(formatted_print)
                sentence_count += 1
            print(sentence_count)




if __name__ == "__main__":
    read_file('Health_and_Personal_Care.jsonl')
