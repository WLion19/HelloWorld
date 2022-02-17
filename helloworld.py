print("hello world")
greeting = input("Bienvenido al playground, quieres jugar? ")
if greeting == "no":
    print("Perfecto, no me apetecia para nada.")
elif greeting == "si":
    print("Pues se me pasaron las ganas.") 
else:
    print("No me importa tu respuesta, siguiente...")
name = input("Para empezar, como te llamas? ")
print("Bienvenid@ " + name)
print()
print("Me gustaria conocerte, ¿Que tal una ronda de preguntas?")  
#### to do
# informacion tiene que ser correcta (estar validada) ej: age tiene que ser numero, altura float etc
# 

print()
age = input("Que edad tienes? ")
is_numeric = age.isnumeric()
while is_numeric == False:
    print("Este numero no es valido.")
    age = input("Introduce otro número, por favor. ")
    is_numeric = age.isnumeric()
print("Tu edad es " + str(age) + " años")

print()
nation = input("Donde creciste? ")
print("Interesante, asi que creciste en un maravilloso lugar llamado " + str(nation))

print()
height = input("Cual es tu altura? En metros, porfavor. ")
try:
    h_float = float(height) 
    is_float = True
   
except ValueError:
    print ("No es una altura valida")
    is_float = False

while is_float == False :
    height = input("Esta altura no es valida, dame otra ")
    try:
        h_float = float(height)
        is_float = True
        print("Esta altura es valida ")

    except ValueError:
        is_float = False

print(h_float)
print("{:.2f}".format(h_float))


print()
birthday_day = input("En que dia naciste? ")
birthday_month = input("En que mes naciste? ")
birthday_year = input ("En que año naciste? Escribelo en 4 digitos ")

import datetime
x = datetime.datetime( int(birthday_year), int(birthday_month), int(birthday_day))
print("Apuntare tu cumpleaños en mi calendario. Es el " + x + " , verdad? ")
day_year = x.strftime("%j")
print("Vaya! Solo quedan " + + " dias!")                                                        #!ERROR DATE

#import datetime
#daysleft = datetime.datetime(int(birthday_day)) #no funciona:()
#print(daysleft)


print()
breath = input("Estas respirando? ") # Aceptar una respuesta valida

while not (breath.casefold() == "si" or breath.casefold() == "no"):
    print("Esta respuesta no es valida")
    breath = input("Introduzca una respuesta de si o no. ")


if breath.casefold() == "si":
    is_breathing = True
else:
    is_breathing = False

print(is_breathing)