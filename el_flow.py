x = 0
while x < 10:
    print("Voy por la vuelta " + str(x))
    x = x + 1
print(x)

# number = int(input("Dime un numero decimal ")) 
raw_text = input("Dime un numero decimal ")
raw_text.isnumeric()
print(raw_text.isnumeric())

if raw_text.isnumeric() == True:
    number = int(raw_text)
    if number % 2 == 0:
        print("Tu numero es par.")
    else:
        print("Tu numero es impar.")

while raw_text.isnumeric() == False:
    raw_text = input("Dime otro numero ")
    raw_text.isnumeric()
    if raw_text.isnumeric() == True:
        number = int(raw_text)
        if number % 2 == 0:
            print("Tu numero es par.")
        else:
            print("Tu numero es impar.")

########################################## Solution ###########################################
#is_resolved = False

#while not is_resolved:
while True:
    raw_text = input("Dime un numero decimal ")
    if raw_text.isnumeric():
        number = int(raw_text)
        if number % 2 == 0:
            print("Tu numero es par.")
        else:
            print("Tu numero es impar.")
        break
    else:
        print("El valor introducido '" + raw_text + "' no es un numero decimal")