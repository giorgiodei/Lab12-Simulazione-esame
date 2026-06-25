import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDsRating(self, dd: ft.Dropdown()):
        ratings= self._model.getAllRatings()
        for s in ratings:
            dd.options.append(ft.dropdown.Option(text=s))


    def handleCreaGrafo(self, e):
        vmin = self._view._ddrating1.value
        vmax = self._view._ddrating2.value

        if vmin is None or vmax is None:
            self._view.create_alert("Seleziona i valori dai DD")
            return

        if vmin > vmax :
            self._view.create_alert("Selezione correttamente vmin e vmax")
            return

        self._model.creaGrafo(vmin, vmax)
        n, m = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(
            ft.Text(f"Grafo correttamente creato! "
                    f"Il grafo è costituito di {n} nodi e {m} archi")
        )
        top5 = self._model.getTop5Archi()

        if len(top5) > 0:
            self._view.txt_result.controls.append(
                ft.Text("Top 5 archi per peso:", color="blue")
            )

            for a1, a2, dati in top5:
                peso = dati["weight"]
                self._view.txt_result.controls.append(
                    ft.Text(f"{a1} -> {a2}, peso: {peso}")
                )
        else:
            self._view.txt_result.controls.append(
                ft.Text("Nessun arco presente nel grafo.", color="red")
            )

        num_componenti, componente_maggiore = self._model.getInfoComponenti()

        self._view.txt_result.controls.append(
            ft.Text(f"Numero componenti connesse: {num_componenti}")
        )

        self._view.txt_result.controls.append(
            ft.Text(f"Componente connessa maggiore: {len(componente_maggiore)} nodi")
        )

        self._view.update_page()

    def handleCammino(self, e):
        pass