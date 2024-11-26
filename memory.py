# Variable global para almacenar la memoria
memory_store = None

def ms_store(value):
    """
    Guarda un valor en la memoria.
    """
    global memory_store
    memory_store = value

def ms_recall():
    """
    Recupera el valor almacenado en la memoria.
    """
    global memory_store
    return memory_store
