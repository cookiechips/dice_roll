from random import randint
from time import sleep

dice1 = randint(1,6)
dice2 = randint(1,6)
print("Let's ROLL")

while True:
    sleep(1)
    print(f"Dice one is {dice1}")
    sleep(3)
    print(f"Dice two is {dice2}")
    sleep(1)

    roll_again = input("Do you want to roll again. [Y]es or [N]o ")

    if roll_again.lower()[0] == 'y':
        print("Great let's roll again!!!")
        continue
    else:
        print("See you later!")
        break