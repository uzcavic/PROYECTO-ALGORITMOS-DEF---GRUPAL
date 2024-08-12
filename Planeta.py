class Planeta:
    def __init__(self, uid, nombre, periodo_orbita, periodo_rotacion, habitantes, clima, lista_episodios="ninguno", lista_personajes="ninguno"):
        self.uid = uid
        self.nombre = nombre
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.habitantes = habitantes
        self.clima = clima
        self.episodios = lista_episodios
        self.personajes = lista_personajes

    def showPlaneta(self):
        print(f"ID: {self.uid}\n"
            f"Nombre: {self.nombre}\nPeriodo de Orbita: {self.periodo_orbita}\n"
            f"Periodo de Rotación: {self.periodo_rotacion}\n"
            f"Habitantes: {self.habitantes}\n"
            f"Clima: {self.clima}\n"
            f"Episodios: {self.episodios}\n"
            f"Personajes: {self.personajes}\n")