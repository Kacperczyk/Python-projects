import csv

with open('New_persons.txt', 'r') as file_r:
    csv_reader = csv.DictReader(file_r)
    data = list(csv_reader)

    available_columns = csv_reader.fieldnames
    all_chosen_columns = []

    while True:
        chosen_column = input(f"Please chose column or type 'stop' :\n{available_columns}: ")
        if chosen_column in available_columns:
            available_columns.remove(chosen_column)
            all_chosen_columns.append(chosen_column)
        elif chosen_column.lower() == 'stop':
            break
        else:
            print("There is no such columns!")
        if not available_columns:
            print("You have exhausted the available columns ")
            break

    print(f"\nChosen columns: {all_chosen_columns}")

    available_operations_li = ['1) Read and print chosen columns from the file',
                               '2) Save chosen columns to another file']
    joined_a_op_li = '\n'.join(available_operations_li)
    print(f"Select operation to perform:\n{joined_a_op_li}")
    read_or_what = input('Your option: ')

    if read_or_what.lower() == '1':

        with open('New_persons.txt', 'r') as file_r2:
            csv_reader = csv.DictReader(file_r2)
            for line in csv_reader:
                selected_data = [line[column] for column in all_chosen_columns]
                print(', '.join(selected_data))

    elif read_or_what.lower() == '2':
        print(all_chosen_columns)
        new_file_name = input('Name for your new file: ')
        with open(new_file_name, 'w', newline='') as file_f3:
            fieldnames = all_chosen_columns
            csv_writer = csv.DictWriter(file_f3, fieldnames=fieldnames)

            csv_writer.writeheader()
            for line in data:
                csv_writer.writerow({column: line[column] for column in all_chosen_columns})

