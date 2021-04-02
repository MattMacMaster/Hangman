import random
from json_data import word
from tkinter import *
from tkinter import messagebox
from string import ascii_lowercase

# This is to ask at the end of a game to restart, or close the program


def restartPrompt():
    val = input("Play Again? (y/n):").lower()
    if(val == "y"):
        hangman()
    else:
        quit()


def getHangmanWord():
    return random.choice(word)


def validInput(answer):
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
    word = getHangmanWord()
    chosenLetters = []
    lives = 8
    answerString = []
    i = 0
    while i < len(word):
        answerString.append("_")
        i = i + 1
    while True:
        print('--------HANGMAN--------')
        print("Lives Left:{}".format(lives))
        print("Letters Chosen So Far:", ' '.join(chosenLetters))
        print(" ".join(answerString))
        val = input("Enter your letter: ").lower()

        # Must Pass answer requirements to continue
        if(validInput(val) == False):
            print("---Invalid Input---")
        # Duplicate Choice Check
        elif(val in chosenLetters):
            print("You have used this letter already.")
        # After this check, see if its in the word or not and act accordingly
        else:
            # Correct Guess
            if(val in word):
                chosenLetters.append(val)
                # Update Answer String - find index in word and replace index in string with letter
                counter = 0
                for x in word:
                    if(x == val):
                        answerString[counter] = val
                        counter = counter + 1
                    else:
                        counter = counter + 1
            # Incorrect Guess
            else:
                chosenLetters.append(val)
                lives = lives - 1
        # Check Lives and word, if ones complete break, and ask to repeat or close\
        if(lives <= 0):
            print("You Lose")
            print("The word was: {}".format(word))

            restartPrompt()

        elif("_" not in answerString):
            print("The word was: {}".format(word))
            print("You Won!!!!!")
            restartPrompt()

        print('-----------------------')


# Command Line only ^ just needs hangman() - And to comment out the tkinter version below
# hangman()
# Building this out with Tkinter Instead below
window = Tk()
window.title("Hangman")


def newGame():
    global theWordWithSpaces
    global numberOfGuesses
    global livesLeft
    global theWord
    assignButtons()
    livesLeft.set(10)
    numberOfGuesses = 0
    theWord = getHangmanWord().lower()
    theWordWithSpaces = " ".join(theWord)
    lblWord.set(" ".join("_"*len(theWord)))


def guess(letter):
    global numberOfGuesses
    global livesLeft
    txt = list(theWordWithSpaces)
    guessed = list(lblWord.get())

    counter = 0
    for c in ascii_lowercase:
        if(c == letter):
            buttonList[counter].config(state="disabled")
        else:
            counter = counter + 1

    if theWordWithSpaces.count(letter) > 0:
        for c in range(len(txt)):
            if txt[c] == letter:
                guessed[c] = letter
            lblWord.set("".join(guessed))
    else:
        numberOfGuesses += 1
        livesLeft.set(livesLeft.get() - 1)
    # Check lives, if zero, lose
    if livesLeft.get() <= 0:
        response = messagebox.askquestion(title="You Have Lost",
                                          message=" The Word was: {} - Do you wish to play again".format(theWord))
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
    global buttonList
    buttonList = []
    n = 0
    for c in ascii_lowercase:
        btn = Button(window, text=c, command=lambda c=c: guess(c), font=(
            "Helvetica 18"), width=4)
        btn.grid(row=2+n//9, column=n % 9)
        buttonList.append(btn)
        n += 1


# Answer displayed as guessing
lblWord = StringVar()
WordLabel = Label(window, textvariable=lblWord, font=("Consoles 24 bold"))
WordLabel.grid(row=0, column=3, columnspan=6, padx=10)

# Phrase before the lives variable are shown
livesString = "Lives Left: "
livesLabel = Label(window, text=livesString,
                   font=("Consoles 18 bold"))
livesLabel.grid(row=0, column=0, columnspan=2)

# Displaying Lives Left
livesLeft = IntVar()
livesCounterLabel = Label(window, textvariable=livesLeft,
                          font=("Consoles 24 bold"))
livesCounterLabel.grid(row=0, column=2, columnspan=1)


# Run Game
newGame()
window.mainloop()
# hangman()
