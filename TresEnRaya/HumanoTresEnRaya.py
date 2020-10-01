from AgenteTresEnRaya import AgenteTresEnRaya


class HumanoTresEnRaya(AgenteTresEnRaya):
    def __init__(self):
        AgenteTresEnRaya.__init__(self)

    def programa(self):
        print("Jugadas permitidas: {}".format(self.jugadas(self.estado)))
        print("")
        cad_movida = input('jugada? ')
        movida = eval(cad_movida)
        self.acciones = movida
