questions = {
    "Who created python?": "A",
    "What year was python created?": "B",
    "Python is tributed to which comady group?": "C",
    "Is the Earth round ?": "A",
}


options = [
    ["A. Guido van Rossum", "В. Elon Musk", "С. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "В. 1991", "С. 2000", "D. 2016"],
    ["A. Lonely Island", "В. Smosh", "С. Monty Python", "D. SNL"],
    ["A. True", "В. False", "С. sometimes", "D. What's Earth?"],
]


def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------")
        print(key)
        for option in options[question_num - 1]:
            print(option)
        guess = input("enter your choice: ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


# ---------------------------------


def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0


# ---------------------------------


def display_score(correct_guesses, guesses):
    print("---------------------")
    print("Answers: ", end="")
    for answer in questions:
        print(questions.get(answer), end="")
    print()

    print("---------------------")
    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end="")
    print()
    print("---------------------")
    score = int((correct_guesses / len(guesses)) * 100)
    print(f"Your score is {score}%")


# ---------------------------------


def play_again():
    response = input("Do you want to play again ? (Yes/No)").upper()
    if response == "YES":
        return True
    else:
        return False


# ---------------------------------


new_game()
while play_again():
    new_game()
print("Byeeee!!! ")
