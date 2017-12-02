import random
guess_taken=0
number=random.randint(1,20)
print("guess my number between 1-20")
while guess_taken<10:
    guess=input()
    guess=int(guess)

    guess_taken=guess_taken+1

    if guess<number:
        print("your guess is too low")
    if guess>number:
        print("your guess is too high")
    if guess==number:
        break
if guess==number:
    guess_taken=str(guess_taken)
    print("the number of guesses are"+guess_taken)
if guess!=number:
    number=str(number)
    print('the number is'+number)
