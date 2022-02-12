import random
import sys
from english_words import english_words_lower_alpha_set as all_words


def find_five_letter_words(words):
    five_letter_words = []
    for word in words:
        if len(word) == 5:
            five_letter_words.append(word)
    return five_letter_words


word_bank = find_five_letter_words(all_words)

solution = random.choice(word_bank)


def take_guess():
    guess = input("Take a guess: ")
    if guess in word_bank:
        return guess
    else:
        print("Error: Not a word. Please try again.")
        take_guess()


def check_guesses(guess, solution, tries):
    if guess == solution:
        print("Good Job! You got it on", tries, "try. The word is", solution)
    else:
        tries += 1
        if tries > 5:
            print("Oops, you used all 5 tries. The word is", solution)
            sys.exit(1)
        print("Wrong guess. Try again.")
        guess = take_guess()
        check_guesses(guess, solution, tries)


def main():
    TRY = 1
    print("CHEAT: " + solution)
    guess = take_guess()
    check_guesses(guess, solution, TRY)


if __name__ == "__main__":
    main()
