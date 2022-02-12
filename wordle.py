import random
import os
import sys
from english_words import english_words_lower_alpha_set as all_words
from rich import print as rprint
from rich.panel import Panel
from rich.text import Text
from colorama import Fore, Back, Style, init
import copy


# find all five letter words in english words and return a list of them
def find_five_letter_words(words):
    five_letter_words = []
    for word in words:
        if len(word) == 5:
            five_letter_words.append(word)
    return five_letter_words


# check user input and return error message if word is not a five letter word
def take_guess(bank):
    guess = input("Take a guess: ").lower()
    if guess in bank:
        return guess
    else:
        rprint(Panel(Text("Please enter a five-letter English word.",
               justify="center", style="red"), title="Error", subtitle="Try again"))
        return take_guess(bank)


# check if user guess if correct
def check_guesses(solution, tries, bank, guess=""):
    print_tries = ""
    feedback = ""
    match tries:
        case 1:
            print_tries = "first"
        case 2:
            print_tries = "second"
        case 3:
            print_tries = "third"
        case 4:
            print_tries = "fourth"
        case 5:
            print_tries = "fifth"
    if tries == 1:
        guess = take_guess(bank)
    if guess == solution:
        rprint(Panel(Text("You got it on {} try. The word is {}.".format(
            print_tries, solution), justify="center", style="green"), title="Well done"))
    else:
        tries += 1
        if tries > 5:
            rprint(Panel(Text("Oops, you used all five tries. The word is {}.".format(
                solution), justify="center", style="purple"), title="Better luck next time"))
            sys.exit(1)
        feedback = color_feedback(guess, solution)
        format_space = " " * (int(os.get_terminal_size().columns / 2 ) - 5)
        print("-" * int(os.get_terminal_size().columns) )
        print(format_space, end="")
        rprint(Text(feedback, style="black"))
        print("-" * int(os.get_terminal_size().columns))
        guess = take_guess(bank)
        check_guesses(solution, tries, bank, guess)


def color_feedback(word, solution):
    word_char = list(word)
    solution_char = list(solution)
    print_string = copy.deepcopy(word_char)
    for i in range(len(word_char)):
        print_string[i] = Back.WHITE + word_char[i]
        for j in range(len(solution_char)):
            if word_char[i] == solution_char[j] and i == j:
                print_string[i] = Back.GREEN + word_char[i]
                break
            elif word_char[i] == solution_char[j] and i != j:
                print_string[i] = Back.YELLOW + word_char[i]
    feedback = " ".join(print_string)
    return feedback

# clear terminal
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    init(autoreset=True)
    word_bank = find_five_letter_words(all_words)
    solution = random.choice(word_bank)
    cls()
    rprint(Panel(Text("Welcome to Wordle by FO", justify="center", style="thistle1")))
    instruction = '''
    Guess the WORDLE in five tries. Each guess must be a valid five-letter English word.
    After each guess, the color of the character will change to show how close your guess was to the word.    
    
    green: in the word and in the correct spot
    yellow: in the word but NOT in the correct spot
    white: not in the word
    '''
    rprint(Panel(Text(instruction, justify="center", style="orange_red1"), title="How to play", subtitle="Credit: Original Creator Josh Wardle"))
    TRY = 1
    # rprint("CHEAT: " + solution)
    check_guesses(solution, TRY, word_bank)


if __name__ == "__main__":
    main()
