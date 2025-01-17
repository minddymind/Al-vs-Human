def remove_newlines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip():
                file.write(line)


def create_file(file_path):
    with open(file_path, 'w') as file:
        file.write('')
    
# for i in range(1,11):
#     file_path = '/Users/sunson/coding/research 490/review' + str(i)+ '-ai' + '.txt'
#     create_file(file_path)
#     print(file_path)