# main.py - Practicas - BACK PYTHON - Visual Studio Code
# registrar alumnos
# generar fichas de matrícula
# mostrar la lista de todos los matriculados
# filtrar matriculados por programa de estudio

lista_alumnos = []

def mensaje_menu():
    menu_opcion="""
     ----------Bienbenido al sistema--------
     -------Registra tu alumno----
    "escribe (s) si deseas registrar un alumno\n"
    "escribe (n) si deseas salir del programa\n"
    "escribe tu respuesta: """
    return menu_opcion

def ingresar_datos_alumnos():
    id=len(lista_alumnos)+1
    cui=int(input("ingre el numero de su dni: "))
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apellido del alumno: ")
    numero_celular=int(input("ingrese su numero de telefono: "))
    programa_estudio=input("ingrese el prograna de estudio: ")
    ciclo_academico=input("ingrese su siclo academico: ")
    email=input("ingrese su correo electronico: ")
    guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email)

def guardar_datos_alumno(id,cui,nombre,apellido,numero_celular,programa_estudio,ciclo_academico,email):
        alumnos:dict={
            "id":id,
            "cui":cui,
            "nombre":nombre,
            "apellido":apellido,
            "numero_celular":numero_celular,
            "programa_estudio":programa_estudio,
            "ciclo_academico":ciclo_academico,
            "email":email
        }
while True:
    menu_opcion=input(mensaje_menu())
    if menu_opcion.lower() == "n":
        print("saliendo del sistema....")
        break
    elif menu_opcion.lower() == "s":
        ingresar_datos_alumnos()
    else:
         print("opcion erronia")

print(lista_alumnos)
# crear un modulo por funcion ... modularizar 
