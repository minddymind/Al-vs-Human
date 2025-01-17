def add_line_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for index, line in enumerate(lines, start=1):
            file.write(f"{index}. {line}")


# for i in range(1,11):
#     file_path = '/Users/sunson/coding/research 490/review' +str(i) +'.txt'
#     add_line_numbers(file_path)
    # print(file_path)