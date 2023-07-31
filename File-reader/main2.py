import random
import csv
def person_generator(x):
    for _ in range(x):
        f_names = random.choice(['Stefan', 'Mercury', 'Hang', 'Eren', 'Tobias'])
        l_names = random.choice(['Walker', 'Kowalski', 'Wodecki', 'Kenny', 'Marius'])
        jobs = random.choice(['IT', 'HR', 'UX', 'TSL', 'WMS'])
        age = random.randrange(20, 40, 5)
        salary = random.randrange(4000, 12500, 850)

        perons_dict = {'f_names': f_names,
                       'l_names': l_names,
                       'jobs': jobs,
                       'age': age,
                       'salary': salary}

        yield perons_dict

def persons_saver(x):
    with open('New_persons.txt', 'w', newline='') as file:
        fieldnames = ['f_names', 'l_names', 'jobs', 'age', 'salary']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        for line in person_generator(x):
            writer.writerow(line)

persons_saver(100)

