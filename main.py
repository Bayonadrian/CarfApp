from tkinter import *
import customtkinter

class CarfMain:

    def __init__(self) -> None:

        customtkinter.set_appearance_mode('System')
        customtkinter.set_default_color_theme('blue')

        self.root= customtkinter.CTk()

    def start(self):

        self.root.title("Carf App")

        return self.root.mainloop()
    
if __name__ == '__main__':

    CarfMain().start()