import json
import random

LIFE = 10
HINT_NUMBER = 0  # Start from 0 to access the first hint correctly


def lose_life():
    global LIFE
    LIFE -= 1
    print(f"Lives left: {LIFE}")


def check_life():
    return LIFE == 0


def load_list():
    try:
        with open("input.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return {"list": []}
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return {"list": []}


def get_random_word(data):
    word_obj = random.choice(data["list"])
    return word_obj["word"], word_obj["hints"]


def get_hints(hints):
    global HINT_NUMBER
    if HINT_NUMBER < len(hints):
        hint = hints[HINT_NUMBER]
        HINT_NUMBER += 1
        return hint
    return "No more hints available."


def rules_and_greetings():
    print("Welcome!! to the Hangman Game.\n"
          "Here are the Rules:\n"
          "1. I have chosen a word; you have 10 lives.\n"
          "2. You have to guess the word.\n"
          "3. Every wrong guess will decrease your life by 1.\n"
          "4. After every three incorrect guesses, a hint will be provided.\n")


def main():
    global LIFE, HINT_NUMBER
    data = load_list()
    ai_choice, hints = get_random_word(data)
    rules_and_greetings()
    word_length = len(ai_choice)
    guess_list = ["_"] * word_length
    ai_list = list(ai_choice)
    incorrect_guesses = 0
    print(ai_choice)

    print("Word to guess:", " ".join(guess_list))
    print("_" * 100)
    print()

    while True:
        user_guess = input("Enter Your Guess: ").lower()

        if user_guess in ai_list:
            for idx, item in enumerate(ai_list):
                if item == user_guess:
                    guess_list[idx] = user_guess
            print("You guessed correctly!")
        else:
            print("Incorrect Guess!")
            lose_life()
            incorrect_guesses += 1

            if LIFE == 0:
                print(f"No lives left! You lost. The correct word was: {ai_choice}")
                break

            if incorrect_guesses % 3 == 0:  # Provide a hint every 3 wrong guesses
                print("HINT:", get_hints(hints))

        print(" ".join(guess_list))
        print("Lives Left:", LIFE)
        print("_" * 100)
        print()

        if guess_list == ai_list:
            print("Congrats!! You guessed the word correctly!")
            break


if __name__ == "__main__":
    main()

