# main.py - Practicas - BACK PYTHON - Visual Studio Code
# registrar alumnos
# generar fichas de matrícula
# mostrar la lista de todos los matriculados
# filtrar matriculados por programa de estudio

lista_alumnos = []

while True:
    opcion = input("Elije lo que deseas hacer: \n"
                   "escribe (s) si deseas registrar un alumno\n"
                   "escribe (n) si deseas salir del programa\n"
                   "escribe tu respuesta: ")
    if opcion.lower() == "s":
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        alumno = {
            "nombre": nombre,
            "apellido": apellido
        }
        lista_alumnos.append(alumno)
    elif opcion.lower() == "n":
        break

print(lista_alumnos)
