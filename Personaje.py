class Personaje:
    def __init__(self, nombre, planeta_origen, episodios, genero, especie, naves, vehiculos):
        self.nombre = nombre
        
        self.planeta_origen = planeta_origen
        self.episodios = episodios
        self.genero = genero
        self.especie = especie
        self.naves = naves
        self.vehiculos = vehiculos

    def showPersonaje(self):
        print(f"Nombre: {self.nombre}\nPlaneta de origen: {self.planeta_origen}\nEpisodios: {self.episodios}\n"
              f"Género: {self.genero}\nEspecie: {self.especie}\nNaves: {self.naves}\nVehículos: {self.vehiculos}\n")
        