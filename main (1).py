import random
import time

def play_game():
    # Taking Inputs
    lower = input("Enter Lower bound:- ")
    if lower == "":
        print("Please enter a number")
        lower = int(input("Enter Lower bound:- "))
    else:
        lower = int(lower)

    # Taking Inputs
    upper = input("Enter Upper bound:- ")
    if upper == "":
        print("Please enter a number")
        upper = int(input("Enter Upper bound:- "))
    else:
        upper = int(upper)

    max_time = round(1 + 0.5 * (upper - lower))

    # generating random number between the bounds
    x = random.randint(lower, upper)
    print("\n\tYou've only got ", 
          round(0.1 * ((upper - lower + 3) * int(4))),
        "chances and ", 
          max_time, "seconds to guess the integer!\n")
    game_running = True
    count = 0

    # Initializing the number of guesses.
    count = 0  # Initialize count outside the loop
    start_time = time.time()
        # taking guessing number as input
    while game_running and time.time() - start_time < max_time:
        guess = int(input("Guess a number:- "))
        count += 1
    # Condition testing
        if x == guess:
            print("\nCongratulations you did it in ",
            count,
            " tries")
            return True  # Indicate successful guess
        elif time.time() - start_time >= max_time:
            print("\nTime's up!" + "🕐" )
            game_running = False
        elif x > guess:
            print("\nYour guess is too small!")
        elif x < guess:
            print("\nYour Guess is too high!")
        elif x == "":
            print("\n Enter a number!")

    # If Guessing is more than required guesses, shows this output.
    print("\nThe number is %d" % x)
    print("\nTime's up! Good Luck Next time!")
    return False  # Indicate unsuccessful guess

# Start the game loop
start_time = time.time()
while True:
    if play_game():
        # Player guessed correctly, ask if they want to play again
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again not in ("y", "yes"):
            print("\nThanks for Playing! Goodbye!" + "\U0001F44B")
            break  # Exit the loop if the player doesn't want to play again
    else:
            print("\nThanks for Playing! Goodbye!" + "\U0001F44B")
            break  # Exit the loop if the player doesn't want to try again