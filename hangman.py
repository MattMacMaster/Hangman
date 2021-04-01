import random
from json_data import word

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


hangman()
