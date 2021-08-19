print("WELCOME TO THE GUESSING GAME")
print()
print("RULES:-")
print("1) A random 4 digit number with distinct digits will be generated and you have to guess it")
print("2) After each guess the computer will display the number of cows and bulls")
print("3) Cows means the digit is guessed correctly and it is in the correct place")
print("4) Bulls means the digit is guessed correctly but it is in the incorrect place")
print("5) If you want to give up type 'pass'.")
print("6) if you want to leave type 'exit'.")
print("7) if you want help then type 'hint'. \n")
print("The computer will display one of the digits of the number. \n")
print("However, hint can be used only once. \n")
print("Difficulty Level:-\n")
print("1) Easy (30 attempts)\n")
print("2) Medium (20 attempts)\n")
print("3) Difficult (10 attempts)\n")
lvl = int(input("Enter the difficulty lvl (1,2,3)\n"))
print()
if lvl == 1:
    max = 30
elif lvl == 2:
    max = 20
elif lvl == 3:
    max = 10
import random
num = ''.join(random.sample("0123456789", 4))
guess = 0
count = 1
a=1
while guess != num and guess != "exit":
    if count > max:
        print(max, "tries completed")
        print("The number is:", num)
        print("Better luck next time")
        break
    count += 1
    guess = input("What's your guess ?\n")
    cows = 0
    bulls = 0
    if guess == "pass":
        print("The number is:", num)
        break
    if guess == "exit":
        break
    num = str(num)
    if num == guess:
        print("You got it and it took you", count, "tries")
        break
    if guess == "hint":
        while a == 1:

            print(num[a],"is one of the digits")
            a += 1
        continue
    for i in range(4):
        if num[i] == guess[i]:
            cows += 1
    if num[0] == guess[1] or num[0] == guess[2] or num[0] == guess[3]:
        bulls += 1
    if num[1] == guess[0] or num[1] == guess[2] or num[1] == guess[3]:
        bulls += 1
    if num[2] == guess[1] or num[2] == guess[0] or num[2] == guess[3]:
        bulls += 1
    if num[3] == guess[1] or num[3] == guess[2] or num[3] == guess[0]:
        bulls += 1
    print("cows=", cows)
    print("bulls=", bulls)
    c = max-count+1
    if c != 1 and c != 0:
        print(c, "tries left")
    elif c == 1:
        print("Last try")