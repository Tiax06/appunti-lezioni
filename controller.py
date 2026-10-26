from mvc.model import Model
from view import View


class Controller():
    def __init__(self, model: Model, view:ft.View):
        self.__model = model
        self.__view = view

    def handler_minus(self, e):
        print("-")
        #v = int(myText.value)
        #v = v-1
        #myText.value = v
        #myText.update()
        self.__model.valore -= 1
        #dovrei dire alla view/page di aggiornarsi
        self._view.aggiorna_GUI(self.__model.valore)


    def handler_plus(self, e):
        print("+")
        #v = int(myText.value)
        #v = v + 1
        #myText.value = v
        #myText.update()
        self.__model.valore += 1
        #dovrei dire alla view/page di aggiornarsi
        self._view.aggiorna_GUI(self.__model.valore)