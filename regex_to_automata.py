import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import random

rutaAutomata = ''
def verificar_texto():
    global rutaAutomata 
    rutaAutomata = './auts/'
    texto_ingresado = entrada_texto.get()
    if texto_ingresado.strip() == "":
        messagebox.showwarning("Cadena Vacía", "Introduzca una cadena no vacía.")
    elif texto_ingresado.lower() == "gamu":
        rutaAutomata += "1.png"
        ventana_principal.after(50, mostrar_ventana_carga)
    elif texto_ingresado.lower() == "gam":
        rutaAutomata += "2.png"
        ventana_principal.after(50, mostrar_ventana_carga)
    elif texto_ingresado.lower() == "ga":
        rutaAutomata += "3.png"
        ventana_principal.after(50, mostrar_ventana_carga)
    elif texto_ingresado.lower() == "g":
        rutaAutomata += "4.png"
        ventana_principal.after(50, mostrar_ventana_carga)
    else:
        messagebox.showinfo("No Coincide", "La expresión regular introducida no coincide con la expresión regular original.")

def mostrar_ventana_carga():
    ventana_carga = tk.Toplevel()
    ventana_carga.title("Cargando")
    etiqueta_carga = tk.Label(ventana_carga, text="Generando autómata...")
    etiqueta_carga.pack()
    
    ventana_carga.after(random.randint(2,4)*1000, lambda: mostrar_imagen(ventana_carga))

def mostrar_imagen(ventana_carga):
    ventana_carga.destroy()  
    global rutaAutomata
    ventana_imagen = tk.Toplevel()
    ventana_imagen.title("Autómata")
    
    imagen = Image.open(rutaAutomata)
    ancho, alto = imagen.size
    
    ventana_ancho, ventana_alto = ventana_imagen.winfo_screenwidth(), ventana_imagen.winfo_screenheight()
    
    factor_escala = min(1.0, min(ventana_ancho / ancho, ventana_alto / alto))
    
    nuevo_ancho = int(ancho * factor_escala)
    nuevo_alto = int(alto * factor_escala)
    imagen = imagen.resize((nuevo_ancho, nuevo_alto), Image.ANTIALIAS)
    imagen = ImageTk.PhotoImage(imagen)
    
    etiqueta_imagen = tk.Label(ventana_imagen, image=imagen)
    etiqueta_imagen.image = imagen
    etiqueta_imagen.pack(fill="both", expand=True)

ventana_principal = tk.Tk()
ventana_principal.title("Verificar Texto")

etiqueta_texto = tk.Label(ventana_principal, text="Ingrese un texto:")
etiqueta_texto.pack()
entrada_texto = tk.Entry(ventana_principal)
entrada_texto.pack()

boton_verificar = tk.Button(ventana_principal, text="Verificar", command=verificar_texto)
boton_verificar.pack()

ventana_principal.mainloop()
