import requests
import tkinter as tk
from PIL import Image, ImageTk

# titulo, encabezado, dimension y color de fondo
app = tk.Tk()
app.title("Consumir API e Interfaz Grafica")
# app.configure(background="#ffffff")
app.state('zoomed')

# Logo de la CUN, aqui utilice la libreria Pillow
image = Image.open(
    r"C:\Users\Javier-dev-3\Downloads\git\diplomado\Sabado02\Practica\logo.png")
img = ImageTk.PhotoImage(image)
l = tk.Label(image=img).pack()

# Componente
tk.Label(
    app,
    text="Practica 1",
    font=("Arial", 20, "bold"),
    fg="black"
).pack()

scrollbar = tk.Scrollbar(app)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

endpoint = 'https://jsonplaceholder.typicode.com/todos'
data = requests.get(endpoint)

mylist = tk.Listbox(app, yscrollcommand=scrollbar.set, font=("Arial", 16))

if data.status_code == 200:
    data = data.json()

for e in data:
    mylist.insert(tk.END, str([e['id'], e['title']]))

mylist.pack(fill=tk.BOTH, padx=50, pady=50)
scrollbar.config(command=mylist.yview)


tk.Button(
    app,
    text="Salir",
    font=("Arial", 14),
    bg="green",
    fg="white",
    width=30,
    borderwidth=0,
    command=app.destroy
).pack()

app.mainloop()