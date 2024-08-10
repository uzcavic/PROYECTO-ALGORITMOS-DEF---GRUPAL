import os
def validation(num, min, max):
    while True:
        if num>= min and num<= max:
            return num
        else:
            print(f"Número incorrecto, porfavor recuerde que sus valores van desde {min} hasta {max}")
            num = int(input())
            