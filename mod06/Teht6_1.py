
import random
no_6=True

def dice ():
    return random.randint(1, 6)

while no_6:
    throw = dice()
    if throw == 6:
        no_6 = False
        print(throw)
    else:
        print(throw)

print('throwing ends')