import re
import sys
from nltk.corpus import stopwords
import unicodedata
import contractions
def remove_non_words_from_file(input_file, output_file):
    # Function to clean the content of the file
    def clean_text(text):
        # Remove non-alphanumeric characters (including special symbols like &#^!) and emojis
        text = re.sub(r'[^\w\s]', '', text)  # Remove non-word characters (excluding spaces)
        text = re.sub(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F700-\U0001F77F\U0001F780-\U0001F7FF\U0001F800-\U0001F8FF\U0001F900-\U0001F9FF\U0001FA00-\U0001FA6F\U0001FA70-\U0001FAFF\U00002702-\U000027B0]', '', text)  # Remove emojis
        #remove stop words
        text = contractions.fix(text)
        stop_words = set(stopwords.words('english'))
        words = text.split()
        
        return ' '.join([word for word in words if word not in stop_words])



    # Read the content from the input file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = ""
        for line in file:
            normalized_line = unicodedata.normalize('NFKC', line.lower())
            cleaned_line = clean_text(normalized_line)
            content += cleaned_line + "\n"

    # Write the cleaned content to the output file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_data.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
remove_non_words_from_file(input_file, output_file)

print(f"Content has been cleaned and saved to {output_file}")
