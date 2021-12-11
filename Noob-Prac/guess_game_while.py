secret_number = 7
guess_num = 0
guess_limit = 5
while (guess_num <= guess_limit):
    guess = int(input("Enter your guess number: "))
    guess_num = guess_num + 1
    if (guess == secret_number):
        print("Congrats you win")
        break
else : print("sorry bro you loose")