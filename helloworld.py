print("hello world")
print(25)
greeting = input("Bienvenido al playground, quieres jugar? ")
if greeting == "no":
    print("Perfecto, no me apetecia para nada.")
elif greeting == "si":
    print("Pues se me pasaron las ganas.") #todo:Texto para pulir 
else:
    print("No me importa tu respuesta, siguiente...")
name = input("Para empezar, como te llamas? ")
print ("Bienvenid@ " + name)