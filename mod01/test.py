from random import uniform as u

user_number = int(input('Enter your number: '))
n = 0
N = user_number

for i in range(user_number):
    x = u(-1, 1)
    y = u(-1, 1)

    num_bool = ((x**2 + y**2) < 1)
    if num_bool:
        n += 1
    else:
        pass

print(f'Piin likiarvo: {(4*n)/N}')
