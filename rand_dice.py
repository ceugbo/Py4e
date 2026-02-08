import random
def roll_dice1():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return (a, b)

a, b = roll_dice1()
print(a, b)
#print("Dice 1 rolled: " + str(roll_dice1()))
#print("Dice 2 rolled: " + str(roll_dice2()))