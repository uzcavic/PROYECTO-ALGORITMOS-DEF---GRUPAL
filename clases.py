'''
Aquí iran las clases bases para poder formaer los objetos necesarios para las misiones

- Se importan para el archivo del menú
- Se usan para creare los objetos a partir de la API (mediante pull requests y un constuctor de datos)
'''

class Character:
    def __init__(self, name, origin, gender, specie):
        self.name = name
        self.origin = origin #Objeto del planet aen el que nacio el personaje 
        self.episodes = [] #array de objetos donde estaran los episodioes en los que aparece
        self.gender = gender
        self.specie = specie
        self.star_ships = [] #array de objetos donde estaran las naves de su propiedad
        self.vehicles  = [] #array de objetos donde estaran los vehiculos de su propiedad
    def show_atrr(self):
        return "" #aquí se escrube el mensaje que muestra los atributos del objeto

class Gun:
    def __init__(self, name, damage):
        self.name = name
        self.damage: int = damage #el daño del arma debe de ser un entero.
    def show_atrr(self):
        return f"Nombre: {self.name}\nDaño: {self.damage}"

class StarShip:
    def __init__(self, long, capacity, hyper, MGLT):
        self.long = long
        self.capacity = capacity
        self.hyper = hyper
        self.MGLT = MGLT
    def graph(self):
        pass #Metodo para mostrar los graficos de las estadisticas de las naves     
    def stats(self):
        pass #Metodo para mostrar las estadisticas de la nave

class Planet:
    def __init__(self, name, orbit_per, rot_per, population, weather):
        self.name = name
        self.orbit_per = orbit_per
        self.rot_per = rot_per
        self.population: int = population
        self.weather = weather
        self.episodes = [] #array de objetos donde se guardaran los eposodios en los que aparece este planeta
        self.population_list = [] #array de objetos que contienen a los habitantes de ese planeta
