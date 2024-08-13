class Usuario:
    def __init__(self, nombre, uid, mision_lista = None):
        self.nombre = nombre
        self.id = uid
        self.mision_listas = mision_lista if mision_lista is not None else []