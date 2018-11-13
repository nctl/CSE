import random
active = True
money = 15
rounds_played = 0
while active and money > 0:
    rounds_played = rounds_played + 1
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print(dice_1 + dice_2)
    if dice_1 + dice_2 == 7:
        money = money + 5.1
        print("Lucky! You won $5 and now have $%d" % money)
    else:
        money = money - 1
        print("You have lost the $1 bet and now have $%d left" % money)

if money <= 0:
    print("Game over! You played for %d rounds before running out of money." % rounds_played)
    active = False
