import os
def validation(num, min, max):
    while True:
        if num>= min and num<= max:
            return num
        else:
            print(f"Número incorrecto, por favor recuerde que sus valores van desde {min} hasta {max}")
            num = int(input())
            
def agregar_mission(ruta, mission: object):
    guns = [_.name for _ in mission.guns]
    characters = [_.name for _ in mission.characters]
    with open(ruta, "a", encoding= "UTF-8") as db:
        db.write(f"{mission.name};{mission.destiny.name};{mission.star_ship.name};{guns};{characters};\n")