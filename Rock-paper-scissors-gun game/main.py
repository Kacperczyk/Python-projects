import random
score = 0
history_of_choices = {'cpu_choice': [],
                      'player_choice': [],
                      'results': []}

def new_game():
    global score

    posibility = ['rock', 'paper', 'scissors']
    cpu = random.choice(posibility)
    history_of_choices['cpu_choice'].append(cpu)
    player = None

    print("Welcome to the game, make a choice")
    for i, item in enumerate(posibility):
        print(f'{i+1}) {item}')

    while True:
        try:
            player = input("").lower()
            if player in ['1', '2', '3']:
                player_index = int(player) - 1
                player = posibility[player_index]
                history_of_choices['player_choice'].append(player)
                break
            elif player in posibility:
                history_of_choices['player_choice'].append(player)
                break
            elif player == 'gun':
                history_of_choices['player_choice'].append(player)
                break
            else:
                print("Incorrected choice. Please choose one of below options: ")
                for i, item in enumerate(posibility):
                    print(f'{i + 1}) {item}')
        except ValueError:
            print("Incorrected choice (wrong value). Please try again.")

    if player == cpu:
        print(f'Your choice: {cpu}\nComputer choice: {cpu} ')
        print("DRAW!")
        history_of_choices['results'].append('Draw')
    elif player == 'paper' and cpu == 'rock':
        print(f'Your choice: {player}\nComputer choice: {cpu} ')
        print('VICTORY!')
        history_of_choices['results'].append('Victory')
        score += 1
    elif player == 'scissors' and cpu == 'paper':
        print(f'Your choice: {player}\nComputer choice: {cpu} ')
        print('VICTORY!')
        history_of_choices['results'].append('Victory')
        score += 1
    elif player == 'rock' and cpu == 'scissors':
        print(f'Your choice: {player}\nComputer choice: {cpu} ')
        print('VICTORY!')
        history_of_choices['results'].append('Victory')
        score += 1
    elif player == 'paper' and cpu == 'scissors':
        print(f'Your choice: {player}\nComputer choice: {cpu} ')
        print('YOU LOSE!')
        history_of_choices['results'].append('Lose')
    elif player == 'scissors' and cpu == 'rock':
        print(f'Your choice: {player}\nComputer choice: {cpu} ')
        print('YOU LOSE!')
        history_of_choices['results'].append('Lose')
    elif player == 'rock' and cpu == 'paper':
        print(f'Your choice: {player}\nComputer choice: {cpu} ')
        print('YOU LOSE!')
        history_of_choices['results'].append('Lose')
    elif player == 'gun':
        print(f'Your choice: {player}\nComputer choice: {cpu} ')
        print('YOU ARE CHEATER!\nBut you win..')
        history_of_choices['results'].append('Cheater')
        score += 1

while (response := input("Do you want to play?(yes/no): ").lower()) in ['y', 'yes']:
    new_game()
print(f'Your final score: {score}')
print(f"Computer choices: {' '.join(history_of_choices['cpu_choice'])}")
print(f"Player choices: {' '.join(history_of_choices['player_choice'])}")
print(f"Game Results: {' '.join(history_of_choices['results'])}")


def save_results_to_file():
    with open("game_review.txt", "w") as file:
        file.write('Round_number | Player_choice | Cpu_choice | Results |\n')
        for i in range(len(history_of_choices['player_choice'])):
            round_number = i + 1
            player_choice = history_of_choices['player_choice'][i]
            cpu_choice = history_of_choices['cpu_choice'][i]
            result = history_of_choices['results'][i]
            file.write(f"{round_number:^13}| {player_choice:^14}| {cpu_choice:^10} | {result:^8}|\n")
        file.write(f"{'-'*53}\nFinal score: {score}")

save_results_to_file()