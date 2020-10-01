from AgenteTresEnRaya import AgenteTresEnRaya
from Tablero import Tablero
from HumanoTresEnRaya import HumanoTresEnRaya

luis = AgenteTresEnRaya()
juan = HumanoTresEnRaya()
# juan = AgenteTresEnRaya()

tablero = Tablero()
tablero.insertar_objeto(juan)
tablero.insertar_objeto(luis)
tablero.run()
