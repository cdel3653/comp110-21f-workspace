"""Flip Your Own Adventure."""

__author__ = "730320843"

import random
player: str
points: int
CELEBRATORY_EMOJI = "\U0001F973"
DUCK_EMOJI = "\U0001F986"
NOICE_EMOJI = "\U0001F44C"
CLOWN_EMOJI = "\U0001F921"

"""Greeting to Player."""
def greet() -> None:
    print("Hi! Welcone to Flip Your Own Adventure; the coin toss game where the fun is endless. You will be asked initially how many times you would like to flip your coin. You can try once and play it safe, or as many times as you would like to test your luck!")
    global player
    player = input("Enter Player ID: ")
    print(player)
    return None

"""Its Game Time!"""
def main() -> None:
    current_game = True
    greet()
    global points
    while current_game:

        num_guess_total = int(input("How many times would you like to guess? "))
        num_guess_cur = 1
        points_cur = 0
        while num_guess_cur <= num_guess_total:
            player_guess = "t"
            if (num_guess_cur == 1):
                player_guess = input("What is your 1st guess? (h/t) ")
            if (num_guess_cur == 2):
                player_guess = input("What is your 2nd guess? (h/t) ")
            if (num_guess_cur == 3):
                player_guess = input("What is your 3rd guess? (h/t) ")
            if (num_guess_cur >= 4):
                player_guess = input("What is your " + str(num_guess_total) + "th guess? (h/f) ")

            coin_toss = random.randint(0, 1)  # 0 is heads, 1 is tails
            if (player_guess == "h" and coin_toss == 0) or (player_guess == "t" and coin_toss == 1):
                print(f"You guessed correctly! {CELEBRATORY_EMOJI}")
                if points_cur == 0:
                    points_cur = 1
                else:
                    points_cur *= 2
            else:
                print(f"You guessed incorrectly! Sillygoose. {DUCK_EMOJI}")
                if points_cur != 0:
                    points_cur //= 2
            print(f"You currently have {points_cur} points! {NOICE_EMOJI} ")

            num_guess_cur += 1
        
        # set points as high score
        if points_cur > points:
            points = points_cur
        
        print(f"High score: {points}")
        continue_choice = input("Would you like to continue the game? (y/n)")
        if continue_choice == "n":
            current_game = False
    print(f"Game over! {CLOWN_EMOJI}")
    print(f"High score: {points}")
    return None


if __name__ == "__main__":
    main()