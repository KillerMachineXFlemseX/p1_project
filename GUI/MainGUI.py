import tkinter as tk
from tkinter import ttk
import MainGUI
import Resultat
import Test
import InfoScreen
import Alder
import Gender

geom=""


TITLE_FONT = ("Verdana", 20, "bold")


class Window(tk.Tk): # definere en class som inharits fra tk.TK

    def __init__(self, *args, **kwargs): #Method som altid køre når class er i brug
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #definere en container
        container.pack() #indsætter container
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        #  Destroys the old frame and packs new frame  #
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack(fill="both", expand=True)


class StartPage(tk.Frame):# definere en class som inharits fra tk.TK

    def __init__(self, master):#Method som altid køre når class er i brug
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text="Høretester V.1",
                         font=TITLE_FONT) #definere et label (text)
        label.pack(padx=10, pady=10) #indsætter det definerede label

        button1 = tk.Button(self, text="Kom Igang",
                            command=lambda: master.switch_frame(
                                Gender.GenderPick)) #definere en knap og dens funktion
        button1.pack()#indsætter den definerede knap



app = Window()
app.wm_attributes('-fullscreen','true')
app.mainloop()#Holder det definerede vindue åben.
