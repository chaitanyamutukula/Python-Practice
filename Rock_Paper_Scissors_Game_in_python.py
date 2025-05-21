import random

def get_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
    print("WELCOME TO ROCK PAPER SCISSORS\n")
    print("You will play against the computer.")
    print("The rules are simple:")
    print("1. Rock crushes scissors")
    print("2. Scissors cuts paper")
    print("3. Paper covers rock")
    print("Type 'rock', 'paper', or 'scissors' to play.")
    print("To exit the game, type 'exit'\n")

    choices = ["rock", "paper", "scissors"]

    while True:
        user_input = input("Your choice: ").lower()

        if user_input == "exit":
            print("Thanks for playing! Goodbye.")
            break

        if user_input not in choices:
            print("Invalid choice, please try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        result = get_winner(user_input, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
