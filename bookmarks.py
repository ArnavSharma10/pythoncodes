import tkinter as tk
import webbrowser

URL1 ='https://www.youtube.com'
URL2='https://www.google.co.in/?gws_rd=ssl'
URL3='https://trinket.io/library/trinkets/4380c65dae'



def open_1(event):
    webbrowser.open_new_tab(URL1)


def open_2(event):
    webbrowser.open_new_tab(URL2)


def open_3(event):
    webbrowser.open_new_tab(URL3)


window = tk.Tk()
window.geometry("600x400")

alabel = tk.Label(text="VIDEOS")
alabel.grid(column=0, row=0)

blabel = tk.Label(text="SEARCH")
blabel.grid(column=1, row=0)

clabel = tk.Label(text="CODE HERE")
clabel.grid(column=2, row=0)

button = tk.Button(window, text="YOUTUBE")
button.grid(column=0)

button2 = tk.Button(window, text="GOOGLE")
button2.grid(column=1, row=1)

button3 = tk.Button(window, text="TRINKET")
button3.grid(column=2, row=1)

button.bind("<Button-1>", open_1)
button2.bind("<Button-1>", open_2)
button3.bind("<Button-1>", open_3)

window.mainloop()

