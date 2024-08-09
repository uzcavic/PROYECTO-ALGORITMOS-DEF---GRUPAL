import requests
from Pelicula import Pelicula
from Especie import Especie
from Personaje import Personaje
from Planeta import Planeta
from Nave import Nave

class APP:
    especie_lista = []
    pelicula_lista = []
    personaje_lista = []
    planeta_lista = []
    nave_lista = []
    personaje_especie = {}
    personaje_naves = {}    
    
    def start(self):
         #ESTO ES PARA MOSTRAR LAS FUNCIONES cuando se ejecute el codigo, tal cual así con el for   
        '''self.crear_pelicula() #completada
        for pelicula in self.pelicula_lista:
            self.crear_pelicula()
        for pelicula in self.pelicula_lista:
            pelicula.showPelicula()
        self.crear_especies() #completada
        for especie in self.especie_lista:
            especie.showEspecie()'''
        self.crear_planeta() #en curso
        for  planeta in self.planeta_lista:
            planeta.showPlaneta()
        self.crear_personaje() #en curso
        for personaje in self.personaje_lista:
            personaje.showPersonaje()
        self.crear_nave() #en curso
        for nave in self.nave_lista:
            nave.showNave()


  
                    



  

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
                    
                    for personaje_url in people: #SUJETO A CAMBIOSSSSSSS
                        personaje_response = requests.get(personaje_url)
                        if personaje_response.status_code == 200:
                            personaje_id = personaje_url.split("/")[-1] #esto es para obtener el id del personaje
                            self.personaje_especie[personaje_id] = name #esto es para relacionar el id del personaje con la especie

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

                especie = self.personaje_especie.get(id_personaje)

                nave = self.personaje_naves.get(id_personaje)

                response_planeta = requests.get(planeta_origen)
                if response_planeta.status_code == 200:
                    datos_planeta = response_planeta.json()['result']['properties']
                    nombre_planeta = datos_planeta['name']
                else:
                    nombre_planeta = "Desconocido"

                lista_episodios = self.obtener_episodios_de_personaje(id_personaje)
                nuevo_personaje = Personaje(nombre, nombre_planeta, lista_episodios, genero, especie, nave, 0)
                self.personaje_lista.append(nuevo_personaje)

                

            else:  #personaje que no existe
                '''print(f"Error {response_personaje.status_code} al obtener la información del personaje con ID {id_personaje}")'''
                continue  # Salta al siguiente personaje

           
    def crear_nave(self):
        for nave_id in range(1, 38):
            nave_id = str(nave_id)
            url = f"https://www.swapi.tech/api/starships/{nave_id}"
            response_nave = requests.get(url)
            if response_nave.status_code == 200:
                datos_nave = response_nave.json()['result']['properties']
                nombre = datos_nave['name']
                longitud = datos_nave['length']
                capacidad_carga = datos_nave['cargo_capacity']
                clasificacion_hiperimpulsor = datos_nave['hyperdrive_rating']
                mgl = datos_nave['MGLT']
                pilotos = datos_nave['pilots'] #esto es una lista de urls de los personajes que pilotan la nave

                for nave_id in pilotos:
                        personaje_response = requests.get(nave_id)
                        if personaje_response.status_code == 200:
                            personaje_id = nave_id.split("/")[-1] #esto es para obtener el id del personaje
                            self.personaje_especie[personaje_id] = nombre #esto es para relacionar el id del personaje con la especie


                nueva_nave = Nave(nombre, longitud, capacidad_carga, clasificacion_hiperimpulsor, mgl)
                self.nave_lista.append(nueva_nave)
            else:
                continue

    def obtener_episodios_de_personaje(self, id_personaje):
            episodios = []
            response_peliculas = requests.get("https://www.swapi.tech/api/films")
            if response_peliculas.status_code == 200:
                peliculas = response_peliculas.json()['result']
                for pelicula in peliculas:
                    personajes_en_pelicula = pelicula['properties']['characters']
                    if f"https://www.swapi.tech/api/people/{id_personaje}" in personajes_en_pelicula:
                        episodios.append(pelicula['properties']['title'])
            return episodios



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
                url_personajes = "https://www.swapi.tech/api/films/" #por completar
                
                

                nuevo_planeta = Planeta(uid, name, periodo_orbita, periodo_rotacion, habitantes, clima, lista_planeta_en_episodio, lista_personajes_en_planeta)
                self.planeta_lista.append(nuevo_planeta)
                        



