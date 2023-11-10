import tkinter as tk
import subprocess
import configparser
from tkinter import ttk
import os

from tkinter.messagebox import showerror, askyesno, showinfo

config = configparser.ConfigParser()
config.read('config.ini')
is_locale = config['database']['locale']


def change_variable(text):
    if text == 'Locale':
        text = 'True'
    elif text == 'Distante':
        text = 'False'
    else:
        text = "''"
    config = configparser.ConfigParser()
    config.read('config.ini')
    config['database']['locale'] = text
    with open('config.ini', 'w') as configfile:
        config.write(configfile)


if os.name == "nt":
    change_variable('Distante')
    data = subprocess.check_output("netsh wlan show interfaces").__repr__()
    list_reseau = ["eduroam", "exterieur", "eduspot"]
    for reaseau in list_reseau:
        if reaseau in data:
            change_variable('Locale')
            showerror(title='Erreur',
                      message='Vous êtes connecté à un réseau de l\'IUT.\nVeillez vous connecter à un réseau personnel ou utiliser un ordinateur de l\'IUT !')

else:
    class App(tk.Tk):
        def __init__(self):
            super().__init__()

            self.title('Gestion choix bases de données')
            window_width = self.winfo_reqwidth()
            window_height = self.winfo_reqheight()
            position_right = int(self.winfo_screenwidth() / 2 - window_width / 2 - 80)
            position_down = int(self.winfo_screenheight() / 2 - window_height - 100 / 2)
            self.geometry("+{}+{}".format(position_right, position_down))
            self.resizable(False, False)

            label = ttk.Label(self, text="Êtes vous à l'IUT ?", font=("Helvetica bold", 18))
            oui_button = ttk.Button(self, text='Oui', command=self.confirm)
            non_button = ttk.Button(self, text='Non', command=self.info)
            ask_button = ttk.Button(self, text='?', command=self.asks, width=2)

            label.grid(row=0, column=1, columnspan=1, rowspan=3, sticky='e', padx=10, pady=30)
            oui_button.grid(row=3, column=0, padx=10, pady=10, sticky='w')
            non_button.grid(row=3, column=2, padx=10, pady=10, sticky='e')
            ask_button.grid(row=1, column=2, sticky='w', padx=10, pady=30)

        def confirm(self):
            answer = askyesno(title='Confirmation',
                              message='Êtes vous sur un ordinateur de l\'IUT ?')
            if not answer:
                aswer2 = askyesno(title='Confirmation',
                                  message='Êtes vous sur un réseau personnel ?')
                if not aswer2:
                    showerror(title='Erreur',
                              message='Veillez vous connecter à un réseau personnel ou utiliser un ordinateur de l\'IUT !')
                    self.destroy()
                else:
                    self.info()
            else:
                showinfo(title='Information', message='Nous allons donc utilisé le base de donnée locale.')
                change_variable("Locale")
                self.destroy()

        def info(self):
            showinfo(title='Information', message='Nous allons donc utilisé le base de donnée distante.')
            change_variable("Distante")
            self.destroy()

        def asks(self):
            showinfo(title='Information',
                     message='Nous avons décidé d\'utiliser pour notre projet une base de données distante. \n'
                             'Le problème est que nous ne pouvons pas nous y connecter depuis un ordinateur de l\'IUT. \n')


    def change():
        # fenetre qui demande si l'utilisateur veut changer de configuration
        if is_locale:
            text = 'Locale'
        else:
            text = 'Distante'

        answer = askyesno(title='Confirmation',
                          message='Voulez vous changer de configuration de la base de donnée ? \n'
                                  'La configuration actuelle est : {}'.format(text))
        if answer:
            change_variable('')
            app = App()
            app.mainloop()


    if is_locale == '':
        app = App()
        app.mainloop()
    else:
        change()
