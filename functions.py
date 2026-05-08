FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """
        Return list of todos from file
    """

    # Mejora la gestión de ficheros porque no debes cerrar el file
    with open(filepath, "r", encoding='utf-8') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath=FILEPATH ):
    """ Escribir todos en fichero de texto"""
    # Mejora la gestión de ficheros porque no debes cerrar el file
    with open(filepath, "w", encoding='utf-8') as file:
        file.writelines(todos_arg)

""""# __name__ es la variable oculta. S
- Si ejecutas el archivo directamente (ej. python functions.py), Python le asigna a __name__ el valor de "__main__".
- Si importas el archivo desde otro (ej. import functions), Python le asigna a __name__ el nombre del archivo 
(en este caso, "functions").
"""
if __name__ == "__main__":
    print("Hola mundo")