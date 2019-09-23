import random
dice = input()
amount, sides = dice.split("d")
amount = int(amount)
sides = int(sides)
roll = 0
if amount >= 1 and sides <= 100:
    if sides >= 2 and sides <= 100:
        for x in range(amount):
            roll += random.randint(1, sides)
print(roll)

