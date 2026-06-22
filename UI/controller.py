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
        pass

    def handleCammino(self, e):
        pass