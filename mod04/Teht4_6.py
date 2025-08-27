import random

#kaikkien pisteiden määrä N
N = 10
#ympyrän sisään osuvien pisteiden lukumäärä

n = 0
i = 0
while i < N:
    i = i + 1

    #arvotaan satunnainen piste koordinaatistoon
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'arvottu piste: {x}, {y}')

    #todo testaa toteuttaako piste epäyhtälön x^2+y^2<1.
    #jos ehto on totta kasvata n laskurin arvoa

    #todo  Laske ja tulosta piin likiarvo käyttäen kaavaa π≈4n/N