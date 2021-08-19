Nota1 = float(input("Ingrese la primera nota: "))
Nota2 = float(input("Ingrese la segunda nota: "))
Nota3 = float(input("Ingrese la tercera nota: "))
Nota4 = float(input("Ingrese la cuarta nota: "))
Nota5 = float(input("Ingrese la quinta nota: "))


def CalcularNota(Nota1,Nota2,Nota3,Nota4,Nota5):

    Nota1= Nota1*0.10
    print(Nota1)
    Nota2= Nota2*0.10
    print(Nota2)
    Nota3= Nota3*0.15
    print(Nota3)
    Nota4= Nota4*0.20
    print(Nota4)
    Nota5= Nota5*0.45
    print(Nota5)

    ponderado= (Nota1+Nota2+Nota3+Nota4+Nota5)

    return ponderado


CalcularNota(Nota1,Nota2,Nota3,Nota4,Nota5)



