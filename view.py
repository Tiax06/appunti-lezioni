import flet as ft

class View():
    def __init__(self, page:ft.Page):
        self._page = page
        self._controller = None

    def imposta_controller(self, controller):
        self._controller=controller  # la inizializzo qui con la funzione imposta controller


    def inizializza_GUI(self):
        self.page.window.width = 400
        self.page.window.height = 320
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER


        myBtnMinus = ft.IconButton(icon=ft.Icons.REMOVE,
                                   icon_size=50,  # per l'icona vai su flet.device.icons tipo
                                   on_click=self._controller.handler_minus)
        myBtnPlus = ft.IconButton(icon=ft.Icons.ADD,
                                  icon_size=50,
                                  on_click=self._controller.handler_plus)
        self._myText = ft.TextField(value=0,
                              disabled=True,
                              width=100,
                              text_size=50,
                              text_align=ft.TextAlign.CENTER
                              )

        myRow = ft.Row([myBtnMinus, self._myText, myBtnPlus],
                       )

        self.__page.controls(myRow)


    def aggiorna_GUI(self):
        self._myText.value = v
        self._page.update()
