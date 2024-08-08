class Pelicula: 
    def __init__(self, title, episode_id, release_date, opening_crawl, director):
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director

    def showPelicula(self):
        print(f"Título: {self.title}\nEpisodio: {self.episode_id}\n"
            f"Fecha de Lanzamiento: {self.release_date}\n"
            f"Director: {self.director}\n"
            f"Opening Crawl: {self.opening_crawl}\n")
        


                
                
            
                 
        
        
