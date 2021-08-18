def Validar(nota):
    try: 
        int(nota)
        return True

    except ValueError:
        print("Ingrese un numero entero")

        return False


Nota1 = input("Ingrese la primera nota: ")
Validar(Nota1)

Nota2 = int(input("Ingrese la segunda nota: "))
Validar(Nota2)

Nota3 = int(input("Ingrese la tercera nota: "))
Validar(Nota3)

Nota4 = int(input("Ingrese la cuarta nota: "))
Validar(Nota4)

Nota5 = int(input("Ingrese la quinta nota: "))
Validar(Nota5)






