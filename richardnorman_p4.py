import sys
from random import randint
import richardnorman_p4_drawing

#open file and store words in array
words_file_name = sys.argv[1]
words_file = open(words_file_name)
words_with_whitespace = words_file.readlines()

#get rid of trailing whitespaces from  file
words_no_whitespace = list(map(str.strip, words_with_whitespace))

guesses_remaining = 8

guessed_word = []
previously_guessed_letters = []
bad_guesses = []

#checks if user already guessed letter
def already_guessed_letter(letter):
    if letter in previously_guessed_letters:
        return True
    return False

def valid_guess(guess):
    #check if user already guessed or is invalid guess
    if str.isdigit(guess) or len(guess) > 1 or guess == " " or already_guessed_letter(guess):
        return False
    return True

def select_random_word():
    while True:
        #select random number and get corresponding element in array
        index_of_randomly_chosen_word = randint(0,len(words_no_whitespace))
        randomly_chosen_word = words_no_whitespace[index_of_randomly_chosen_word]

        #word has to be at least four letters long
        if len(randomly_chosen_word) >= 4:
            return randomly_chosen_word
        else:
            continue

#checks if word contains guess, if so, replace underscore with letter guessed
def guess_operation(letter,word):
    global guesses_remaining
    global guessed_word

    if letter not in word:
        guesses_remaining -= 1
        print("Sorry, there is no \"" + letter + "\".")
        bad_guesses.append(letter)
        return
    else:
        #replace _ with letter that was found in word
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
        print("Nice guess!")
    

#prints the current state of the guessed word
def print_guessed_word():
    return " ".join(guessed_word)

#chosen word to guess
word_to_guess = select_random_word()

#populate guess_word with underscores
for i in range(len(word_to_guess)):
    guessed_word.append("_")

print("\nWelcome to Console Hangman!")

while guesses_remaining > 0:
    richardnorman_p4_drawing.clear_drawing()
    richardnorman_p4_drawing.draw_hanging_man(guesses_remaining)
    if "_" not in guessed_word:
        break
    richardnorman_p4_drawing.draw_initial(print_guessed_word())
    if len(bad_guesses) > 0:
        richardnorman_p4_drawing.draw_bad_guesses(bad_guesses)
    richardnorman_p4_drawing.draw_guesses_remaining(guesses_remaining)
    richardnorman_p4_drawing.show_drawing()

    letter_guessed = input("What's your next guess? ")
    #check if input is valid
    acceptable_guess = valid_guess(letter_guessed)
    if not acceptable_guess:
        print("INVALID GUESS! Please enter a LETTER that has NOT been entered before.")
        continue
    #if valid guess, add to guessed letters
    previously_guessed_letters.append(letter_guessed)

    #now that all checks are done on the validity of the guess, enter the guess in to the word
    guess_operation(letter_guessed, word_to_guess)

richardnorman_p4_drawing.clear_drawing()
richardnorman_p4_drawing.draw_hanging_man(guesses_remaining)
richardnorman_p4_drawing.draw_results(guesses_remaining, word_to_guess)