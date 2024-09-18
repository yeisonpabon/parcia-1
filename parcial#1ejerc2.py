#ejercicio 2 parcial 1
f = float(input("ingrese los grados farenheit que quiere convetir:"))


def celcius():
    c = (5/9)*(f-32)
    return c 

print(f'la convercion de farenheit a celsius : {celcius()}')