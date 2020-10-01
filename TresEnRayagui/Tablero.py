from AgenteIA.Entorno import Entorno
from AgenteIA.AgenteJugador import ElEstado
import pygame as pg
import sys
from pygame.locals import *


class Tablero(Entorno):

    def __init__(self, h=3, v=3):
        Entorno.__init__(self)
        movidas = [(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]
        self.juegoActual = ElEstado(jugador='X', get_utilidad=0, tablero={}, movidas=movidas)
        self.ancho = 400
        self.alto = 400
        pg.init()
        self.ventana = pg.display.set_mode((self.ancho, self.alto + 100), 0, 32)
        pg.display.set_caption("Sistemas Inteligentes - 3 en Raya")

    def percibir(self, agente):
        agente.estado = self.juegoActual
        if agente.estado.movidas:
            agente.programa()
        if agente.testTerminal(agente.getResultado(self.juegoActual, agente.acciones)):
            agente.vive = False

    def ejecutar(self, agente):
        print("Agente ", agente.estado.jugador, " juega ", agente.acciones)
        self.juegoActual = agente.getResultado(self.juegoActual, agente.acciones)
        agente.mostrar(self.juegoActual)
        print("Utilidad ", self.juegoActual.get_utilidad)

    def iniciar_pantalla(self):
        color_linea = (0, 0, 0)
        self.ventana.fill((255, 255, 255))
        # lineas verticales
        pg.draw.line(self.ventana, color_linea, (self.ancho / 3, 0), (self.ancho / 3, self.alto), 7)
        pg.draw.line(self.ventana, color_linea, (self.ancho / 3 * 2, 0), (self.ancho / 3 * 2, self.alto), 7)
        # lineas horizontales
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 3), (self.ancho, self.alto / 3), 7)
        pg.draw.line(self.ventana, color_linea, (0, self.alto / 3 * 2), (self.ancho, self.alto / 3 * 2), 7)

    def marcar(self, row, col, jugador):
        x_img = pg.image.load("img/X_modified.png")
        y_img = pg.image.load("img/o_modified.png")
        x_img = pg.transform.scale(x_img, (80, 80))
        o_img = pg.transform.scale(y_img, (80, 80))
        posx, posy = 0, 0
        if row == 1:
            posx = 30
        if row == 2:
            posx = self.ancho / 3 + 30
        if row == 3:
            posx = self.ancho / 3 * 2 + 30
        if col == 1:
            posy = 30
        if col == 2:
            posy = self.alto / 3 + 30
        if col == 3:
            posy = self.alto / 3 * 2 + 30
        if jugador == 'X':
            self.ventana.blit(x_img, (posy, posx))
        else:
            self.ventana.blit(o_img, (posy, posx))
        pg.display.update()

    def accion_humano(self, age):
        x, y = pg.mouse.get_pos()
        # obtener columna del click
        if x < self.ancho / 3:
            columna = 1
        elif x < self.ancho / 3 * 2:
            columna = 2
        elif x < self.ancho:
            columna = 3
        else:
            columna = None
        # obtener fila del click
        if y < self.alto / 3:
            fila = 1
        elif y < self.alto / 3 * 2:
            fila = 2
        elif y < self.alto:
            fila = 3
        else:
            fila = None
        # acciones del agente humano = fila columna seleccionada
        age.acciones = fila, columna

    def run(self):
        self.iniciar_pantalla()
        actual = 0
        fps = 30
        tiempo = pg.time.Clock()
        victoriaXImg = pg.image.load('img/victoriaX.png')
        victoriaOImg = pg.image.load('img/victoriaO.png')
        victoriaEmpate = pg.image.load('img/victoriaEmpate.png')
        while True:
            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()
                if self.agentes[actual].__class__.__name__ == "HumanoTresEnRaya":
                    if event.type is MOUSEBUTTONDOWN:
                        self.agentes[actual].estado = self.juegoActual
                        if self.agentes[actual].estado.movidas:
                            self.accion_humano(self.agentes[actual])
                        if self.agentes[actual].testTerminal(self.agentes[actual].getResultado(self.juegoActual, self.agentes[actual].acciones)):
                            self.agentes[actual].vive = False
                        self.ejecutar(self.agentes[actual])
                        actual = 1
                else:
                    self.percibir(self.agentes[actual])
                    self.ejecutar(self.agentes[actual])
                    actual = 0
            tablero = self.juegoActual.tablero
            for x, y in tablero.keys():
                self.marcar(x, y, tablero.get((x, y)))
            if self.finalizado():
                a = self.juegoActual.get_utilidad
                if a != 0:
                    if a > 0:
                        self.ventana.blit(victoriaXImg, (400, 250))
                        print("Victoria X ")
                    else:
                        self.ventana.blit(victoriaOImg, (400, 250))
                        print("Victoria O ")
                else:
                    self.ventana.blit(victoriaEmpate, (400, 250))
                    print("Empate")
                pg.quit()
                sys.exit()
            pg.display.update()
            tiempo.tick(fps)
