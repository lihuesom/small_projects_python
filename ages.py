def run ():
    print("Comparación de dos edades")
    print("Primer turno")

    user_1 = input("¿Cúal es tu nombre: ")
    age_1 = int(input("¿Cúal es tu edad: "))

    print("Segundo turno")

    user_2 = input("¿Cúal es tu nombre: ")
    age_2 = int(input("¿Cúal es tu edad: "))

    if age_1 < age_2:
        print(user_1 + " es menor comparado con" + user_2)
    elif age_1 > age_2:
        print(user_1 + " es mayor comparado con "+user_2)
    else:
        print(user_1 + "," + user_2 + " tienen la misma edad") 

if __name__ == "__main__":
    run()