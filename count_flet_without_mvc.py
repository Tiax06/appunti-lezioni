import flet as ft

def main(page : ft.Page):
    # dimensioni della pagina
    page.window.width = 400
    page.window.height = 320
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def handler_minus(e):
        print("-")
        v = int(myText.value)
        v = v-1
        myText.value = v
        myText.update()

    def handler_plus(e):
        print("-")
        v = int(myText.value)
        v = v + 1
        myText.value = v
        myText.update()

    myBtnMinus = ft.IconButton(icon = ft.Icons.REMOVE,
                               icon_size = 50, #per l'icona vai su flet.device.icons tipo
                               on_click = handler_minus)
    myBtnPlus = ft.IconButton(icon = ft.Icons.ADD,
                              icon_size = 50,
                              on_click = handler_plus)
    myText = ft.TextField(value = 0,
                          disabled = True,
                          width = 100,
                          text_size = 50,
                          text_align = ft.TextAlign.CENTER
                          )






    myRow = ft.Row(myBtnMinus, myText, myBtnPlus)

    page.controls(myRow)

    #page.controls.append(myBtnMinus)
    #page.controls.append(myBtnPlus)
    #page.controls.append(myText)

    page.update()

    ft.main()