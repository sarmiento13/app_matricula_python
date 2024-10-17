from guardar_alumno import guardar_datos_alumno

def ingresar_datos_alumnos():
    """Solicita al usuario los datos del alumno y los guarda en un diccionario."""
    id = len(lista_alumnos) + 1
    cui = int(input("ingre el numero de su dni: "))
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    numero_celular = int(input("ingrese su numero de telefono: "))
    programa_estudio = input("ingrese el prograna de estudio: ")
    ciclo_academico = input("ingrese su siclo academico: ")
    email = input("ingrese su correo electronico: ")
    guardar_datos_alumno(id, cui, nombre, apellido, numero_celular, programa_estudio, ciclo_academico, email)