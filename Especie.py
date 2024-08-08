class Especie:

    def __init__(self, name, uid, height, classification, homeworld, language, people, episodes):
        self.name = name
        self.uid = uid
        self.height = height
        self.classification = classification
        self.homeworld = homeworld
        self.language = language
        self.people = people
        self.episodes = episodes

    #Yo definiria esta funcion para mostrar todas las especies
    def showEspecie(self):
        print(f"Nombre: {self.name}\nID: {self.uid}\nAltura: {self.height}\nClasificación: {self.classification}\nPlaneta de origen: {self.homeworld}\nLenguaje: {self.language}\nPersonajes que pertenecen a esta especie: {self.people}\nEpisodios: {self.episodes}\n")



       


            