import math

def pole_figury(*args):
    if len(args) == 1:
        return args[0]**2 * math.pi
    elif len(args) == 2:
        return args[0] * args[1]
    else:
        p = (args[0] + args[1] + args[2]) / 2
        pole = math.sqrt(p*(p-args[0])*(p-args[1])*(p-args[2]))
        return pole

pole_calkowite = 0
wykonane_iteracje = 0

liczba_figur = int(input())

for i in range(liczba_figur):
     wymiary = input().split()
     wymiary_int = map(float, wymiary)
     if len(wymiary) <= 3:
        aktualne_pole = pole_figury(*wymiary_int)
        pole_calkowite += aktualne_pole
        wykonane_iteracje += 1
     else:
        break

if wykonane_iteracje == liczba_figur:
    print(round(pole_calkowite,2))
else:
    print("Błąd: można podać maksymalnie 3 liczby")
