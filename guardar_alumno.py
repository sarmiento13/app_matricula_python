def guardar_datos_alumno(id, cui, nombre, apellido, numero_celular, programa_estudio, ciclo_academico, email):
    """Crea un diccionario con los datos del alumno y lo agrega a la lista de alumnos."""
    global lista_alumnos  # Necesario para modificar la lista global
    alumno = {
        "id": id,
        "cui": cui,
        "nombre": nombre,
        "apellido": apellido,
        "numero_celular": numero_celular,
        "programa_estudio": programa_estudio,
        "ciclo_academico": ciclo_academico,
        "email": email
    }
    lista_alumnos.append(alumno)