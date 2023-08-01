import csv

with open('Persons_creator.txt', 'r') as file_r:
    csv_reader = csv.DictReader(file_r)

    available_columns = csv_reader.fieldnames
    all_chosen_columns = []

    while True:
        chosen_column = input(f"Proszę wybrać kolumny lub wpisać STOP:\n{available_columns}: ")
        if chosen_column in available_columns:
            available_columns.remove(chosen_column)
            all_chosen_columns.append(chosen_column)
        elif chosen_column.lower() == 'stop':
            break
        else:
            print("Nie ma takiej kolumny!")
        if not available_columns:
            print("Wyczerpałeś dostępne kolumny.")
            break

    print(f"\nWybrane kolumny to: {all_chosen_columns}")

    read_or_what = input("\nCo chcesz teraz zrobić?: \n1) Wczytaj wybrane kolumny z pliku\nOpcja nr: ")
    if read_or_what.lower() == '1':

    #

        with open('Persons_creator.txt', 'r') as file_r2:
            csv_reader = csv.DictReader(file_r2)
            for row in csv_reader:
                selected_data = [row[column] for column in all_chosen_columns]
                print(', '.join(selected_data))
