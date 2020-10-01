from Tablero import Tablero

class Tablero3d():

    def __init__(self):
        self.tableros = []
        for i in range (1,4):
            self.tableros.append(Tablero)
    
    def mostrar(self):
        for x in range(1, 4):
            for y in range(1, 4):
                print(self.tableros[y].juegoActual.tablero.get((x, y), '.')+" ", end="")
            print()
        