entero = 5
decimal = 2.5
boleano = True
texto1 = ""
texto2 = "Hola"
texto3 = "Adios"
nulo = None

print(entero)
print(type(entero))
print(str(entero))
print(type(str(entero)))
print(decimal)
print(type(decimal))
print(boleano)
print(type(boleano))
print(texto1)
print(type(texto1))
print(nulo)
print(type(nulo))

print(entero + entero)
print("5+5=10")
texto4 = texto2 + texto3
print(texto2 + texto3)
print(texto4)


print(texto2 + str(entero))
print([texto2 , entero])

entero = entero + 3
print(str(entero) + "+" + str(entero) + "=" + str(entero + entero))


print(int("2"))
print(float("5.67"))
print(int(5.67))
print(float(2))
print(entero + decimal)
print()
print(bool(entero))
print(bool(decimal))
print(bool(texto1))
print(bool(texto2))
print(bool(nulo))

print()
print(bool(-1))
print(bool(0))
print(bool(5))
condicion = 0
if condicion:
    print("verdad")
else:
    print("mentira") 

print(texto2.startswith("Ho"))
print(texto2.startswith("ho"))
print(texto2.replace("la", "lo"))
print(texto2)

