import json 
import re 
import random

review_file = "Health_and_Personal_Care.jsonl"
metadata_file = "meta_Health_and_Personal_Care.jsonl"



def read_file(filename):
    with open(filename, 'r') as fp:
        for line in fp:
            print(json.loads(line.strip()))
            print({"-----endline-----"})

def clean_review_file(filename):
    with open(filename, 'r') as fp:
        result = []
        set_of_product_id = set()
        
        # Read and process each line in the file
        for line in fp:
            this_line = json.loads(line.strip())
            product_id = this_line["parent_asin"]
            if product_id in set_of_product_id:  # Choose only one review for the product
                continue
            else:
                title = this_line["title"]
                review_text = re.sub(r'[\\/]', '', re.sub(r'<[^>]*>', '', this_line["text"]))  # Remove HTML tags and slashes
                cleaned_data = [title, product_id, review_text]
                set_of_product_id.add(product_id)
                result.append(cleaned_data)
    
    # Generate random numbers for indices 1000 items
    random_numbers = random.sample(range(0, len(result)), 1000)

    selected_results = [result[i] for i in random_numbers]

    # Format the output
    product_id_in_use = set()
    formatted_output = []
    for review in selected_results:
        title, product_id, review_text = review
        product_id_in_use.add(product_id)
        formatted_output.append({
            "product_id": product_id,
            "title": title,
            "review": review_text
        })
    
    formatted_output = json.dumps(formatted_output, indent=4)
    with open('cleaned_reviews.json', 'w') as outfile:
        outfile.write(formatted_output)
    product_in_use(product_id_in_use)

    return formatted_output

def product_in_use(set_of_product):
    formatted = ""
    formatted = json.dumps(list(set_of_product), indent=4)
    with open('cleaned_product_in_use.json', 'w') as outfile:
        outfile.write(formatted)

# I think run this function only once to generate the cleaned file
clean_review_file(review_file)

