import time
# Este programa ayuda a saber si podemos hacer un triangulo 
# dadas tres longitudes

print("hola. te voy ayudar con eso de los triángulos")
l1 = int(input("ingrese la longitud uno\n"))
l2 = int(input("ingrese la longitud dos\n"))
l3 = int(input("ingrese la longitud tres\n"))

print("Las longitudes entregadas hasta el momento son:")

print(l1,l2,l3)

if (l1 <= l2+l3):
    print("vamos bien revisemos los otros casos ")
    time.sleep(0.5)
    if(l2 <= l1+l3):
        print("Seguimos bien")
        time.sleep(0.5)
        if(l3 <= l2+l1):
            print("Si es posible el triangulo")
        else:
          print("no es posible el triangulo")
    else:
      print("no es posible el triangulo")
else:
    print("no es posible el triangulo:", l1, "no es menos que", l2, "+", l3) 


