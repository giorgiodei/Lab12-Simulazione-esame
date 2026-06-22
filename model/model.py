import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._stati = []
        self._idMapStati = {}

    """def creaGrafo(self, lat, lon, shape):
        self._grafo.clear()
        self._stati = DAO.getNodes(lat, lon, shape)
        self._idMapStati = {a.id: a for a in self._stati}
        self._grafo.add_nodes_from(self._stati)

        coppie = DAO.getEdges()
        for c in coppie:
            idA, idB = c["idA"], c["idB"]
            if idA in self._idMapStati and idB in self._idMapStati:
                peso = DAO.getPeso(idA, idB, shape)
                if peso is not None:
                    statoA = self._idMapStati[idA]
                    statoB = self._idMapStati[idB]
                    self._grafo.add_edge(statoA, statoB, weight=peso)"""


    def getAllRatings(self):
        return DAO.getAllRatings()

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)