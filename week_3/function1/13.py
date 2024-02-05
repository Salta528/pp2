import random
random_number = random.randint(1, 20)
first= input("Hello!What is your name?\n")
print("Well, {fname}, I am thinking of a number between 1 and 20.\nTake a guess.\n".format(fname=first))
def game(guess, cnt):
    if guess < random_number:
        print("Your guess is too low.\n")
        print("Take a guess.\n")
        return False
    elif guess > random_number:
        print("Your guess is too more.\n")
        print("Take a guess.\n")
        return False
    else:
        print("Good job, " +name+ "! You guessed my number in " +str(cnt)+ " guesses!")
        return True
tries=1
while True:
    number = int(input())
    if game(number, tries):
        break
    tries += 1