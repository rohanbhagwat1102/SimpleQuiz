def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0

    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("correct answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2 :
                guess = input("Sorry wrong answer, try again : ")
            attempt = attempt + 1

    if attempt == 3:
        print("\nThe correct answer is ",answer)


score = 0
print("\nGuess the Animal")
print("*************************")
guess1 = input("Which bear lives at the North Pole ? : ")
check_guess(guess1,"Polar Bear")

guess2 = input("\nWhich is the fastest land animal ? : ")
check_guess(guess2,"cheetah")

guess3 = input("\nWhich is the largest animal ? : ")
check_guess(guess3,"Blue Whale")

print("\nYour score is : ", score)

