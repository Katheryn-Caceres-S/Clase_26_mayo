#conversion de temperatia  =sys.argv()

import sys

if len(sys.argv) != 2:
    print("python celsius.py 'celsius'")
    sys.exit(1)


celsius = float(sys.argv[1])
print(celsius) 

#diccionario

conversiones = {
    "Fahrenheit" :(celsius * 9/5) + 32,
    "kelvin" : celsius + 273.15,
    "rankine" : (celsius*9/5) + 491.67
}

print(f"{celsius} equivalen a : ")

for k,v in conversiones.items():
    print(k,v)
