import time
# Este programa ayuda a saber si podemos hacer un triangulo 
# dadas tres longitudes

print("hola. te voy ayudar con eso de los triángulos")
l1 = int(input("ingrese la longitud uno\n"))
l2 = int(input("ingrese la longitud dos\n"))
l3 = int(input("ingrese la longitud tres\n"))

print("Las longitudes entregadas hasta el momento son:")

print(l1,l2,l3)


if (l1 <= l2+l3) and (l2 <= l1+l3) and (l3 <= l2+l1):
    print("Si es posible formar un triangulo con ",l1,l2,l3)
else:
    print("No es posible formar un triangulo:",l1,l2,l3, "no cumplen la condicion")