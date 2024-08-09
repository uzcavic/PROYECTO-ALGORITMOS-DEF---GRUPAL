from operator import index
import requests
from Pelicula import Pelicula
from Especie import Especie
from Personaje import Personaje
from Planeta import Planeta

class APP:
    especie_lista = []
    pelicula_lista = []
    personaje_lista = []
    planeta_lista = []
    
    def start(self):
         #ESTO ES PARA MOSTRAR LAS FUNCIONES cuando se ejecute el codigo, tal cual así con el for   
        '''self.crear_pelicula() #completada
        for pelicula in self.pelicula_lista:
            self.crear_pelicula()
        for pelicula in self.pelicula_lista:
            pelicula.showPelicula()
        self.crear_especies() #completada
        for especie in self.especie_lista:
            especie.showEspecie()
        self.crear_planeta() #en curso
        for  planeta in self.planeta_lista:
            planeta.showPlaneta()
        self.crear_personaje() #en curso
        for personaje in self.personaje_lista:
            personaje.showPersonaje()'''

<<<<<<< HEAD
        print(self.pelicula_lista())
        while True:
            menu= input("""Bienvenido viajero, indiqueme que decea saber del universo de star wars
    1. lista de peliculas
    2. lista de especies
    3. lista de planetas
    4. buscar personaje
    5. mision
    6. graficos
    7.Estadistica de las naves
    8. mision                   
    9. Terminar el programa
    ---> """).strip()
            if menu =="1":
                index=1
                for Peli in self.pelicula_lista:
                    Peli:Pelicula
                    print(f"""{index}-Título: {Peli.title}
Episodio: {Peli.episode_id}
Fecha de fecha de lanzamiento: {Peli.release_date}
opening de apertura: {Peli.opening_crawl}
Nombre del director {Peli.director}""")
                    index+=1
                break    
                    



  
         #para personajes

        #self.crear_personajes()
        
        #self.menu()...

    def crear_especies(self):

            for id_specie in range(1, 38): #hay 37 especies en total
                """print("Viendo especie: " + str(id_specie))"""
                id_specie = str(id_specie)
                url = f"https://www.swapi.tech/api/species/{id_specie}" #esto solo dará el nombre, id y la url de la especie
                response = requests.get(url)
                if response.status_code==200:
                    datos=response.json()
                    especie_info=datos['result']
                    name=especie_info['properties']['name']
                    uid=especie_info['uid']  
                    height=especie_info['properties']['average_height']
                    classification=especie_info['properties']['classification']
                    homeworld=especie_info['properties']['homeworld'] #url del planeta de origen
                    language =especie_info['properties']['language']
                    people=especie_info['properties']['people'] #esto es una lista de urls de los personajes que pertenecen a esa especie
                    
                    response_homeworld = requests.get(homeworld)
                    if response_homeworld.status_code == 200:
                        datos_homeworld = response_homeworld.json()['result']['properties']
                        homeworld=datos_homeworld['name']

                    lista_personajes=[]
                    for personaje in people:
                        response_personaje = requests.get(personaje)
                        if response_personaje.status_code == 200:
                            datos_personaje = response_personaje.json()['result']['properties']
                            people = datos_personaje['name']
                            lista_personajes.append(people) #personajes que pertenecen a la especie
                     
                
                lista_episodios = [] #eps en los que aparece la especie
                for id_episodio in range (1,7):
                    '''print("Viendo especie: " + str(id_episodio))'''
                    id_episodio = str(id_episodio)
                    url_episodio = f"https://www.swapi.tech/api/films/{id_episodio}/"
                    response_episodio = requests.get(url_episodio)
                    if response_episodio.status_code == 200:
                        datos_episodio = response_episodio.json()['result']['properties']
                        if url in datos_episodio['species']:
                            """print("Conectando especie con episodio: " + str(id_episodio))"""
                            lista_episodios.append(datos_episodio['title'])


                
                nueva_especie = Especie(name, uid, height, classification, homeworld, language, lista_personajes,lista_episodios)
                self.especie_lista.append(nueva_especie)
                               
    def crear_pelicula(self): 
        url = "https://swapi.dev/api/films/"
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()["results"]
            for pelicula in datos:
                title = pelicula["title"]
                episode = pelicula["episode_id"]
                director = pelicula["director"]
                release_date = pelicula["release_date"]
                opening_crawl = pelicula["opening_crawl"]
                nueva_pelicula = Pelicula(title, episode, release_date, opening_crawl, director)
                self.pelicula_lista.append(nueva_pelicula)  
            '''print("Pelicula: " + title + " creada")'''



    def crear_personaje(self):
        for id_personaje in range(1, 83):
            id_personaje = str(id_personaje)
            url = f"https://www.swapi.tech/api/people/{id_personaje}"
            response_personaje = requests.get(url)
            if response_personaje.status_code == 200:
                datos_personaje = response_personaje.json()['result']['properties']
                nombre = datos_personaje['name']
                planeta_origen = datos_personaje['homeworld']
                genero = datos_personaje['gender']

                response_planeta = requests.get(planeta_origen)
                if response_planeta.status_code == 200:
                    datos_planeta = response_planeta.json()['result']['properties']
                    nombre_planeta = datos_planeta['name']
                else:
                    nombre_planeta = "Desconocido"

                lista_personaje_en_episodio = []
                


                nuevo_personaje = Personaje(nombre, nombre_planeta, 0, genero, 0, 0, 0) 
                self.personaje_lista.append(nuevo_personaje)   #FALTA POR COMPLETAR

            else: 
                print("Error al obtener la información del personaje")
            




    def crear_planeta(self):
        for id_planeta in range(1, 61):
                id_planeta = str(id_planeta)
                url = f"https://www.swapi.tech/api/planets/{id_planeta}" #esto solo dará el nombre, id y la url del planeta
                response_planeta = requests.get(url)

                if response_planeta.status_code == 200:
                    datos=response_planeta.json()
                    planeta_info=datos['result']
                    uid=planeta_info['uid']
                    name=planeta_info['properties']['name']
                    periodo_orbita=planeta_info['properties']['orbital_period']
                    periodo_rotacion=planeta_info['properties']['rotation_period']
                    habitantes=planeta_info['properties']['population'] #numero de habitantes
                    clima=planeta_info['properties']['climate']
                    #falta Nombre de los personajes que pertenecen a la especie y Nombre de los episodios en los que aparecen.

                    lista_planeta_en_episodio=[] #episodios en los que aparece el planeta
                for id_episodio in range(1, 7):
                    id_episodio = str(id_episodio)

                    url_episodio = f"https://www.swapi.tech/api/films/{id_episodio}"
                    response_episodio = requests.get(url_episodio)
                    if response_episodio.status_code == 200:
                        print("Viendo episodio: " + str(id_episodio))
                        datos_episodio = response_episodio.json()['result']['properties']
                        if url in datos_episodio['planets']:
                            lista_planeta_en_episodio.append(datos_episodio['title'])

                lista_personajes_en_planeta = []
                url_personajes = "https://www.swapi.tech/api/films/"
                
                

                nuevo_planeta = Planeta(uid, name, periodo_orbita, periodo_rotacion, habitantes, clima, lista_planeta_en_episodio, lista_personajes_en_planeta)
                self.planeta_lista.append(nuevo_planeta)
                        
#BORRAR A PARTIR DE AQUI
'''lista_episodios = [] #eps en los que aparece la especie
                for id_episodio in range (1,7):
                    print("Viendo especie: " + str(id_episodio))
                    id_episodio = str(id_episodio)
                    url_episodio = f"https://www.swapi.tech/api/films/{id_episodio}/"
                    response_episodio = requests.get(url_episodio)
                    if response_episodio.status_code == 200:
                        datos_episodio = response_episodio.json()['result']['properties']
                        if url in datos_episodio['species']:
                            """print("Conectando especie con episodio: " + str(id_episodio))"""
                            lista_episodios.append(datos_episodio['title'])'''
            
