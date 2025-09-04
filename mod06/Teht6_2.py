import random
def dice (s):
    return random.randint(1, s)
num_sides = int(input('Kuinka monta tahkoa:'))

while True:
    throw = dice(num_sides)
    if throw == num_sides:
        print(throw)
        break
    else:
        print(throw)
    
print('throwing ends')