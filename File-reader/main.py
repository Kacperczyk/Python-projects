import csv

with open('New_persons.txt', 'r') as file_r:
    csv_reader = csv.DictReader(file_r)

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

    read_or_what = input("\nSelect the operation you want to perform ?: \n1) Read chosen columns from the file\nOpcja nr: ")
    if read_or_what.lower() == '1':


        with open('New_persons.txt', 'r') as file_r2:
            csv_reader = csv.DictReader(file_r2)
            for row in csv_reader:
                selected_data = [row[column] for column in all_chosen_columns]
                print(', '.join(selected_data))
