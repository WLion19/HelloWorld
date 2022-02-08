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
age = input("Que edad tienes? ")
nation = input("Donde creciste? ")
height = input("Cual es tu altura? En metros, porfavor. ")
birthday = input("Cuantas semanas quedan hasta tu cumpleaños? ")  # pidieras dia y mes de cumpleaños
breath = input("Estas respirando, verdad? ") # Aceptar una respuesta valida

# is_breathing = True o False

print()
print("Bien, creo haberte conocido lo sufiente. ¿No me crees? Veras...")
print("Tu nombre es " + str(name))
print("Tu edad es " + str(age) + " años")
print("Conozco incluso tu altura, mides " + str(height) + " metros") # 1.55 Exactamente 2 decimales
print("Creciste en un maravilloso lugar llamado " + str(nation))
print("De hecho, somos grandes amigos, ya he marcado las " + str(birthday) + " semanas que quedan hasta tu cumpleaños en mi calendario") # los dias que quedan
if breath == "verdad": # variable deberia ser if is_breathing
    print("Y tenemos cosas en común, ambos respiramos ")
if breath == "mentira":
    print("Aunque aun no consigo entender como existes, ")
print("Seamos amigos, disfrutemos del juego!")