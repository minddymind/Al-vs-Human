#!/bin/bash

#1. extract data from the dataset and save it to original_review.txt for 10500 reviews
#python3 extract_data.py 

#2. removing duplicate reviews from the original_review.txt
python3 utility/rm_duplicate.py original_review.txt cleaned_original_review.txt

#3. split file into 10 files that each contains 1000 reviews from into cleaned_original_review.txt use_this_review folder
python3 utility/split_to_file.py cleaned_original_review.txt use_this_review 1000
# after this step, we have 11 files in use_this_review folder but we only need 10 files, so we remove the last file
rm -v use_this_review/review11.txt
# *จริงๆถ้าสร้างไฟล์ use_this_review_ai ด้วยตรงนี้จะดีมาก แต่งานมันเร่งเดะทำ

#4. add line number to each review in use_this_review folder
python3 utility/add_line_number.py use_this_review

#5. use generative ai to generate reviews from ai and store it in use_this_ai_review folder

#6. clean text in use_this_ai_review folder and use_this_review folder to remove special characters, emoji, and non important words

