def Validar(nota):
    try: 
        int(nota)
       
    except ValueError:
        print("Ingrese un numero entero")
  
Nota1 = input("Ingrese la primera nota: ")
Validar(Nota1)

Nota2 = input("Ingrese la segunda nota: ")
Validar(Nota2)

Nota3 = input("Ingrese la tercera nota: ")
Validar(Nota3)

Nota4 = input("Ingrese la cuarta nota: ")
Validar(Nota4)

Nota5 = input("Ingrese la quinta nota: ")
Validar(Nota5)







