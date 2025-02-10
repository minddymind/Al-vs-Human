import pandas as pd
import json
import math

# Load JSONL dataset correctly
data = []
with open("Health_and_Personal_Care.jsonl", "r", encoding="utf-8") as file:
    for line in file:
        data.append(json.loads(line))  # Read each line as a JSON object

# Convert to DataFrame
df = pd.DataFrame(data)

# Check if "rating" and "text" columns exist
if "rating" in df.columns and "text" in df.columns:
    # Calculate percentage of each rating
    rating_counts = df["rating"].value_counts(normalize=True) * 100
    print(rating_counts)
    
    # Function to calculate average review length and standard deviation
    def avg_review_length(df_subset):
        lengths = df_subset["text"].apply(lambda x: len(str(x).split()))
        avg_length = lengths.mean()
        std_dev = lengths.std()
        return avg_length, std_dev

    # Define rating categories
    positive_ratings = df[(df["rating"] >= 4.0) & (df["rating"] <= 5.0)]
    neutral_ratings = df[df["rating"] == 3.0]
    negative_ratings = df[(df["rating"] >= 1.0) & (df["rating"] <= 2.0)]

    # Calculate percentage of each category
    positive_percentage = (len(positive_ratings) / len(df)) * 100
    neutral_percentage = (len(neutral_ratings) / len(df)) * 100
    negative_percentage = (len(negative_ratings) / len(df)) * 100

    # Round percentages
    positive_percentage = math.ceil(positive_percentage) if positive_percentage % 1 >= 0.5 else math.floor(positive_percentage)
    neutral_percentage = math.ceil(neutral_percentage) if neutral_percentage % 1 >= 0.5 else math.floor(neutral_percentage)
    negative_percentage = math.ceil(negative_percentage) if negative_percentage % 1 >= 0.5 else math.floor(negative_percentage)

    print(f"POSITIVE (4.0 - 5.0): {positive_percentage}%")
    print(f"NEUTRAL (3.0): {neutral_percentage}%")
    print(f"NEGATIVE (1.0 - 2.0): {negative_percentage}%")

    # Calculate average review length and standard deviation for each category
    avg_positive_length, std_positive = avg_review_length(positive_ratings)
    avg_neutral_length, std_neutral = avg_review_length(neutral_ratings)
    avg_negative_length, std_negative = avg_review_length(negative_ratings)

    # Round average lengths and standard deviations
    avg_positive_length = math.ceil(avg_positive_length) if avg_positive_length % 1 >= 0.5 else math.floor(avg_positive_length)
    std_positive = math.ceil(std_positive) if std_positive % 1 >= 0.5 else math.floor(std_positive)
    
    avg_neutral_length = math.ceil(avg_neutral_length) if avg_neutral_length % 1 >= 0.5 else math.floor(avg_neutral_length)
    std_neutral = math.ceil(std_neutral) if std_neutral % 1 >= 0.5 else math.floor(std_neutral)
    
    avg_negative_length = math.ceil(avg_negative_length) if avg_negative_length % 1 >= 0.5 else math.floor(avg_negative_length)
    std_negative = math.ceil(std_negative) if std_negative % 1 >= 0.5 else math.floor(std_negative)

    # Print results with ± standard deviation
    print(f"Average review length - POSITIVE: {avg_positive_length:.2f} words ± {std_positive:.2f} words")
    print(f"Average review length - NEUTRAL: {avg_neutral_length:.2f} words ± {std_neutral:.2f} words")
    print(f"Average review length - NEGATIVE: {avg_negative_length:.2f} words ± {std_negative:.2f} words")

else:
    print("Error: Required columns ('rating' or 'text') not found in the dataset.")
