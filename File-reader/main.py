import csv

with open('New_persons.txt', 'r') as file_r:
    csv_reader = csv.DictReader(file_r)
    data = list(csv_reader)

    # Get the list of all available columns from the CSV file
    available_columns = csv_reader.fieldnames
    all_chosen_columns = []

    # Ask the user to choose columns or type 'stop' to finish
    while True:
        chosen_column = input(f"Please choose a column or type 'stop':\n{available_columns}: ")
        if chosen_column in available_columns:
            available_columns.remove(chosen_column)
            all_chosen_columns.append(chosen_column)
        elif chosen_column.lower() == 'stop':
            break
        else:
            print("There is no such column!")
        if not available_columns:
            print("You have exhausted the available columns.")
            break

    print(f"\nChosen columns: {all_chosen_columns}")

    # List of available operations for the user to choose from
    available_operations_li = ['1) Read and print chosen columns from the file',
                               '2) Save chosen columns to another file',
                               '3) Read and print as a table',
                               '4) Save to a new file as a table']
    joined_a_op_li = '\n'.join(available_operations_li)
    print(f"Select an operation to perform:\n{joined_a_op_li}")
    read_or_what = input('Your option: ')

    if read_or_what.lower() == '1':
        # Option 1: Read and print chosen columns from the file
        with open('New_persons.txt', 'r') as file_r2:
            csv_reader = csv.DictReader(file_r2)
            for line in csv_reader:
                selected_data = [line[column] for column in all_chosen_columns]
                print(', '.join(selected_data))

    elif read_or_what.lower() == '2':
        # Option 2: Save chosen columns to another file
        print(all_chosen_columns)
        new_file_name = input('Name for your new file: ')
        with open(new_file_name, 'w', newline='') as file_f3:
            fieldnames = all_chosen_columns
            csv_writer = csv.DictWriter(file_f3, fieldnames=fieldnames)

            csv_writer.writeheader()
            for line in data:
                csv_writer.writerow({column: line[column] for column in all_chosen_columns})

    elif read_or_what.lower() == '3':
        # Option 3: Read and print as a table
        with open('New_persons.txt', 'r') as file_r4:
            csv_reader = csv.DictReader(file_r4)

            # Assign column lengths for all chosen columns
            column_lengths = {
                'f_names': 10,
                'l_names': 10,
                'jobs': 5,
                'salary': 7,
                'age': 4
            }
            # Calculate the width for the whole table, considering only the chosen columns
            total_width = sum(column_lengths[column] for column in all_chosen_columns) + len(all_chosen_columns) * 3 + 1

            # Display heading for the table
            print('-' * total_width)
            print('|', end=' ')
            for column in all_chosen_columns:
                print(f'{column.ljust(column_lengths[column])}', end=' | ')
            print()
            print('-' * total_width)

            # Display data for each row in the chosen columns
            for row in csv_reader:
                selected_data = [row[column] for column in all_chosen_columns]
                for i, column in enumerate(all_chosen_columns):
                    print(f'| {selected_data[i].ljust(column_lengths[column])}', end=' ')
                print('|')

            print('-' * total_width)

    elif read_or_what.lower() == '4':
        # Option 4: Save to a new file as a table
        new_file_name2 = input('Name for your new file: ')
        with open(new_file_name2, 'w', newline='') as file_f5:
            fieldnames = all_chosen_columns
            csv_writer = csv.DictWriter(file_f5, fieldnames=fieldnames)

            column_lengths = {
                'f_names': 10,
                'l_names': 10,
                'jobs': 5,
                'salary': 7,
                'age': 4
            }
            total_width = sum(column_lengths[column] for column in all_chosen_columns) + len(all_chosen_columns) * 2 + 1

            #writing header to new file as a table
            file_f5.write('-' * total_width + '\n')
            file_f5.write('|')
            for column in all_chosen_columns:
                file_f5.write(f' {column.ljust(column_lengths[column])}|')
            file_f5.write('\n')
            file_f5.write('-' * total_width + '\n')

            #writing lines to new file as a table
            for line in data:
                selected_data = [line[column] for column in all_chosen_columns]
                for i, column in enumerate(all_chosen_columns):
                    file_f5.write(f'| {selected_data[i].ljust(column_lengths[column])}')
                file_f5.write('|')
                file_f5.write('\n')
            file_f5.write('-' * total_width + '\n')














