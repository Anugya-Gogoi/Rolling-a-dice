import random
import time
minm = 1
maxm = 6

roll_dice = "yes"

while roll_dice == "yes" or roll_dice == "y":
    print("Rolling the dices now")
    time.sleep(1)
    print("Are you ready??????")
    time.sleep(1)
    print("The values are")
    time.sleep(1)
    print(random.randint(minm, maxm))
    print(random.randint(minm, maxm))

    roll_dice = input("Roll the dices again?")