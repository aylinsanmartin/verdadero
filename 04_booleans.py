# un tipo de valor con solo dos opciones 
# verdadero o falso 

is_real = True
un_real = False


# las comparaciones entregan o devuelven un booleano

print(10<9)

print(10>9)

print(10==9)

#ejemplo evaluado variables 

limit = 18
age = 21 

if age >= limit:
    print("es mayor de edad ")
else:
    print("es menos de edad ")

    #todos los valores tienen una representacion 
    #booleana.vamos a probarlo 
    zero = 0
    one = 1
    empty_str =''

    if zero:
        print(zero,"es verdadero")
    else:
        print(zero, 'es falso')

    if one:
        print(one,"es verdadero")
    else:
        print(one, 'es falso')

    if empty_str:
        print(empty_str, "es verdadero")
    else:
        print(empty_str, 'es falso')








