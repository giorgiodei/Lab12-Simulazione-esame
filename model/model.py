import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._actors = []
        self._idMapActors = {}

    def creaGrafo(self, rmin,rmax):
        self._grafo.clear()
        self._actors = DAO.getNodes(rmin,rmax)
        self._idMapActors = {a.id: a for a in self._actors}
        self._grafo.add_nodes_from(self._actors)

        coppie = DAO.getEdges(rmin,rmax)

        for c in coppie:
            idA = c["idA"]
            idB = c["idB"]
            a1 = self._idMapActors[idA]
            a2 = self._idMapActors[idB]
            income = self.cleanIncome(c["peso"])
            if self._grafo.has_edge(a1, a2):
                self._grafo[a1][a2]["weight"] += income
            else:
                self._grafo.add_edge(a1, a2, weight=income)


    def getAllRatings(self):
        return DAO.getAllRatings()

    def getGraphDetails(self):
        return len(self._grafo.nodes), len(self._grafo.edges)

    def cleanIncome(self,income):
        if income is None:
            return 0
        else:
            income = income.replace("$", "")
            income = income.replace(",", "")
            income = income.strip()

            return int(income)

    def getTop5Archi(self):
        archi = list(self._grafo.edges(data=True))

        archi_ordinati = sorted(
            archi,
            key=lambda x: x[2]["weight"],
            reverse=True
        )

        return archi_ordinati[:5]

    def getInfoComponenti(self):
        componenti = list(nx.connected_components(self._grafo))

        if len(componenti) == 0:
            return 0, []

        componente_maggiore = max(componenti, key=len)

        return len(componenti), componente_maggiore
