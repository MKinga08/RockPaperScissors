import random


def get_computers_choice():
    computers_choice = random.choice(['rock', 'paper', 'scissors'])
    return computers_choice


def get_users_input():
    while True:
        opt = input('Enter rock/paper/scissors:').lower()
        if opt == "rock" or opt == "paper" or opt == "scissors":
            return opt
        else:
            print("Wrong input")


def announcing_winner(result, computers_choice):
    global count_player, count_computer
    if result == computers_choice:
        print('Its a draw')
    elif result == 'rock' and computers_choice == 'scissors' \
            or result == 'paper' and computers_choice == 'rock' \
            or result == 'scissors' and computers_choice == 'paper':
        print("You won")
        count_player += 1
    else:
        print("You lost")
        count_computer += 1


def playing_again():
    while True:
        play = input('Do you want to play again?')
        if play == 'yes':
            return True
        elif play == 'no':
            return False


count_player = 0
count_computer = 0


def main():
    again = True
    while again:
        result = get_users_input()
        print(f"Your choice is: {result}")
        computers_choice = get_computers_choice()
        print(f"The computers choice is: {computers_choice}")
        announcing_winner(result, computers_choice)
        print(f'The score of the game is: you:computer {count_player}:{count_computer}')
        again = playing_again()


if __name__ == "__main__":
    main()
