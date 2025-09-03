import random

#print(f'arvottu piste: {x}, {y}')

#kaikkien pisteiden määrä N
n = 0     #ympyrän sisään osuvien pisteiden lukumäärä
i = 0




N =int(input('Syötä arvottavien pisteiden määrä:'))



while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if ((x**2 + y**2) < 1) :
        n = n + 1
        i = i + 1
    else :
        i = i + 1

print(f'Piin likiarvo: {(4*n)/N}')


