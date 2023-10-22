import PySimpleGUI as sg
import ana
import giris
cut_data = [[150, 24, 100, 'Ç-1050', 'Dolu', 'Var', 'YOK', 'Var']]

sg.set_options()
sg.theme('Light Gray 3')

def pencere():

    # Menu add
    menu_def = [
    ['File', ['Open', 'Save', 'Exit']],
    ['Edit', ['Cut', 'Copy', 'Paste']],
    ['View', ['View1', 'View2']],
    ['History', ['History1', 'History2']],
    ['Application', ['App1', 'App2']],
    ['Windows', ['Window1', 'Window2']],
    ['Help', ['About']]
]

    layout=[
        [sg.Menu(menu_definition=menu_def)],
        [sg.Push(), 
         sg.Button(' Ana Pencere ', key='-ANA-',
                                            image_filename='/Users/hakankilicaslan/GitHub/T150/T150/icons8-arrow-quill-3/icons8-arrow-100.png'),
                                              sg.Push()],
        [
        [sg.Button(' Ana Pencere ', key='-ANA-',
                                            image_filename='/Users/hakankilicaslan/GitHub/T150/T150/icons8-arrow-quill-3/icons8-arrow-100.png'),
        sg.Button(' Kesim Listesi Giriş', key='-GIRIS-',
                                            image_filename='/Users/hakankilicaslan/GitHub/T150/T150/icons8-drawing-compass-quill/icons8-drawing-compass-100.png'),
        sg.Button(' Kesim Listesi Giriş', key='-GIRIS-',
                                            image_filename='/Users/hakankilicaslan/GitHub/T150/T150/icons8-caliper-quill/icons8-caliper-100.png'),
        sg.Button(' Kesim Listesi Giriş', key='-GIRIS-',
                                            image_filename='/Users/hakankilicaslan/GitHub/T150/T150/icons8-saw-blade-quill-1/icons8-saw-blade-100.png')]
        ]
]

    window = sg.Window('T150 Giriş Ekranı',layout=layout)
    while True:
        
        event,values = window.read()
        print("event:", event, "values:", values)

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-ANA-' or event == 'App1':
            ana.ana()
        if event == '-GIRIS-' or event == 'App2':
            giris.giris()
        

if __name__ == "__main__":
    pencere()