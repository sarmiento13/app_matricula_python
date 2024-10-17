from main import mensaje_menu
from ingresar_datos import ingresar_datos_alumnos

lista_alumnos = []  # La lista global

def ejecutar_menu():
    """Ejecuta el menú principal del programa."""
    while True:
        menu_opcion = input(mensaje_menu())
        if menu_opcion.lower() == "n":
            print("saliendo del sistema....")
            break
        elif menu_opcion.lower() == "s":
            ingresar_datos_alumnos()
        else:
            print("opcion erronia")

# Ejecuta el programa
ejecutar_menu()
print(lista_alumnos)