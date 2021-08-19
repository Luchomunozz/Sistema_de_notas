Nota1 = int(input("Ingrese la primera nota: "))
Nota2 = int(input("Ingrese la segunda nota: "))
Nota3 = int(input("Ingrese la tercera nota: "))
Nota4 = int(input("Ingrese la cuarta nota: "))
Nota5 = int(input("Ingrese la quinta nota: "))

#Se piden y capturan los datos del estudiante
def capturar_datos():
    nombre = input("Ingrese el nombre del estudiante: ")
    apellidos = input("Ingrese el apellidos del estudiante: ")
    grado = input("Ingrese el grado del estudiante: ")
    materia = input("Ingrese la materia: ")
    
    return nombre, apellidos, grado, materia
