#################################################################
# Nombre      : Entorno                                         #
# Version     : 0.05.03.2017                                    #
# Autor       : Victor                                          #
# Descripcion : Clase Agentes con Adversarios                   #
##################################################################


from AgenteIA.Agente import Agente
from collections import namedtuple


ElEstado = namedtuple('ElEstado', 'jugador, get_utilidad, tablero, movidas')


class AgenteJugador(Agente):

    def __init__(self):
        Agente.__init__(self)
        self.estado = None
        self.juego = None
        self.utilidad = None

    def jugadas(self, estado):
        raise Exception("Error: No se implemento")

    def get_utilidad(self, estado, jugador):
        raise Exception("Error: No se implemento")

    def testTerminal(self, estado):
        return not self.jugadas(estado)

    def getResultado(self, estado, m):
        raise Exception("Error: No se implemento")

    def programa(self):

        # self.acciones = self.minimax(self.estado, self.estado.jugador)
        self.acciones = self.podaAlphaBeta(self.estado, self.estado.jugador)
        # self.acciones = self.podaalphaBetaFunEval(self.estado, self.estado.jugador)

    def minimax(self, estado, juego):
        jugador = estado.jugador

        def valorMax(e):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = -100
            for a in self.jugadas(e):
                v = max(v, valorMin(self.getResultado(e, a)))
            return v

        def valorMin(e):
            if self.testTerminal(e):
                return self.get_utilidad(e, self.estado.jugador)
            v = 100
            for a in self.jugadas(e):
                v = min(v, valorMax(self.getResultado(e, a)))
            return v

        return max(self.jugadas(estado), key=lambda a: valorMin(self.getResultado(estado, a)))

    def podaAlphaBeta(self, estado, juego):
        jugador = estado.jugador

        def max_value(e, alpha, beta):
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            v = -100
            for a in self.jugadas(e):
                v = max(v, min_value(self.getResultado(e, a), alpha, beta))
                if v >= beta:
                    return v
                alpha = max(alpha, v)
            return v

        def min_value(e, alpha, beta):
            if self.testTerminal(e):
                return self.get_utilidad(e, jugador)
            v = 100
            for a in self.jugadas(e):
                v = min(v, max_value(self.getResultado(e, a), alpha, beta))
                if v <= alpha:
                    return v
                beta = min(beta, v)
            return v

        mejorScore = -100
        beta = 100
        mejorAccion = None
        for a in self.jugadas(estado):
            v = min_value(self.getResultado(estado, a), mejorScore, beta)
            if v > mejorScore:
                mejorScore = v
                mejorAccion = a
        return mejorAccion
