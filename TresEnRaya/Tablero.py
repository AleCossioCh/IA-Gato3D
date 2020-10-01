from AgenteIA.Entorno import Entorno
from AgenteIA.AgenteJugador import ElEstado


class Tablero(Entorno):

    def __init__(self, h=3, v=3):
        Entorno.__init__(self)
        movidas = [(x, y) for x in range(1, h + 1) for y in range(1, v + 1)]
        self.juegoActual = ElEstado(jugador='X', get_utilidad=0, tablero={}, movidas=movidas)

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
        resul = self.juegoActual.get_utilidad
        if resul != 0:
            if resul > 0:
                print("Victoria para X")
            else:
                print("Victoria para O")

