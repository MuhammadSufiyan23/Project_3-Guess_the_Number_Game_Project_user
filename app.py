# PROJECT: 3
# GUESS THE NUMBER GAME BY USER

import random

print("🎯 Welcome to the Number Guessing Game!")
print("🤖 I have chosen a number between 1 and 100. Try to guess it!")

number = random.randint(1, 100)

while True:
    guess = int(input("🔢 Enter Your Guess Number: "))

    if guess < number:
        print("📉 Too Low! Try again. ⬆️")
    elif guess > number:
        print("📈 Too High! Try again. ⬇️")
    else:
        print("🎉🎊 Congratulations! You Got It Right! 🏆🥳")
        break  

              
         
    
