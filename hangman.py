import random
from json_data import word
from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase

# This is to ask at the end of a game to restart, or close the program


def restart_prompt():
    val = input("Play Again? (y/n):").lower()
    if(val == "y"):
        hangman()
    else:
        quit()


def get_hangman_word():
    return random.choice(word)


def valid_input(answer):
    # Allows single character answer only
    if(len(answer) > 1):
        return False
    # Ensures it is a english character
    try:
        answer.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


def hangman():
    word = get_hangman_word()
    chosen_letters = []
    lives = 8
    answer_string = []
    i = 0
    while i < len(word):
        answer_string.append("_")
        i = i + 1
    while True:
        print('--------HANGMAN--------')
        print("Lives Left:{}".format(lives))
        print("Letters Chosen So Far:", ' '.join(chosen_letters))
        print(" ".join(answer_string))
        val = input("Enter your letter: ").lower()

        # Must Pass answer requirements to continue
        if(valid_input(val) == False):
            print("---Invalid Input---")
        # Duplicate Choice Check
        elif(val in chosen_letters):
            print("You have used this letter already.")
        # After this check, see if its in the word or not and act accordingly
        else:
            # Correct Guess
            if(val in word):
                chosen_letters.append(val)
                # Update Answer String - find index in word and replace index in string with letter
                counter = 0
                for x in word:
                    if(x == val):
                        answer_string[counter] = val
                        counter = counter + 1
                    else:
                        counter = counter + 1
            # Incorrect Guess
            else:
                chosen_letters.append(val)
                lives = lives - 1
        # Check Lives and word, if ones complete break, and ask to repeat or close\
        if(lives <= 0):
            print("You Lose")
            print("The word was: {}".format(word))

            restart_prompt()

        elif("_" not in answer_string):
            print("The word was: {}".format(word))
            print("You Won!!!!!")
            restart_prompt()

        print('-----------------------')


# Command Line only ^ just needs hangman() - And to comment out the tkinter version below
# hangman()
# Building this out with Tkinter Instead below
window = Tk()
window.title("Hangman")


def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    global lives_left
    global the_word
    assignButtons()
    lives_left.set(10)
    numberOfGuesses = 0
    the_word = get_hangman_word().lower()
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))


def guess(letter):
    global numberOfGuesses
    global lives_left
    txt = list(the_word_withSpaces)
    guessed = list(lblWord.get())

    counter = 0
    for c in ascii_lowercase:
        if(c == letter):
            buttonlist[counter].config(state="disabled")
        else:
            counter = counter + 1

    if the_word_withSpaces.count(letter) > 0:
        for c in range(len(txt)):
            if txt[c] == letter:
                guessed[c] = letter
            lblWord.set("".join(guessed))
    else:
        numberOfGuesses += 1
        lives_left.set(lives_left.get() - 1)
    # Check lives, if zero, lose
    if lives_left.get() <= 0:
        response = messagebox.askquestion(title="You Have Lost",
                                          message=" The Word was: {} - Do you wish to play again".format(the_word))
        if(response == "no"):
            window.destroy()
        else:
            # Restart Game
            newGame()
    # Check Word, if filled, Win
    if "_" not in lblWord.get():
        response = messagebox.askquestion(title="You Have WON!!!!!!!",
                                          message="Do you wish to play again")
        if(response == "no"):
            window.destroy()
        else:
            # Restart Game
            newGame()

# Made this to solve the buttons being disabled even into new games


def assignButtons():
    global buttonlist
    buttonlist = []
    n = 0
    for c in ascii_lowercase:
        btn = Button(window, text=c, command=lambda c=c: guess(c), font=(
            "Helvetica 18"), width=4)
        btn.grid(row=2+n//9, column=n % 9)
        buttonlist.append(btn)
        n += 1


# Answer displayed as guessing
lblWord = StringVar()
WordLabel = Label(window, textvariable=lblWord, font=("Consoles 24 bold"))
WordLabel.grid(row=0, column=3, columnspan=6, padx=10)

# Phrase before the lives variable are shown
lives_string = "Lives Left: "
LivesLabel = Label(window, text=lives_string,
                   font=("Consoles 18 bold"))
LivesLabel.grid(row=0, column=0, columnspan=2)

# Displaying Lives Left
lives_left = IntVar()
LivesCounterLabel = Label(window, textvariable=lives_left,
                          font=("Consoles 24 bold"))
LivesCounterLabel.grid(row=0, column=2, columnspan=1)


# Run Game
newGame()
window.mainloop()
# hangman()
