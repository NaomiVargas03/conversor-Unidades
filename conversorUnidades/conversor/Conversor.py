import tkinter as tk
from tkinter import messagebox

valor_Conversion = 512.16

def ingresar_monto(): 
    try:
         monto = float(entrada_monto.get())
         if monto < 0:
             messagebox.showerror("Error", "El valor ingresado no debe ser negativo.")
         else:
             Conversiones = monto * valor_Conversion
             listaDeConversiones.config(text=f"{monto} USD = {Conversiones} CRC")
    except ValueError:
         messagebox.showwarning("Advertencia", "Por favor, ingresa un valor distinto D:")  
            
def eliminar_conver():
    entrada_monto.delete(0, tk.END)
    listaDeConversiones.config(text="")

def cerrar_ventana():
    preguntar = messagebox.askyesno("Advertencia", "¿Está seguro de querer salir de la ventana?")
    if preguntar:
        ventana.quit()
        messagebox.showwarning("Mensajito", "Gracias por usar el programa :D")

ventana = tk.Tk()
ventana.title("Aplicación de conversiones")

ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=0)
ventana.grid_rowconfigure(1, weight=0)
ventana.grid_rowconfigure(2, weight=0)  
ventana.grid_rowconfigure(3, weight=1)


frame_superior = tk.Frame(ventana)
frame_superior.pack(pady=10)

entrada_monto = tk.Entry(frame_superior, width=40)
entrada_monto.pack(side=tk.LEFT, padx=10)


boton_agregar = tk.Button(frame_superior, text="Ingrese el monto a convertir", command=ingresar_monto)
boton_agregar.pack(side=tk.LEFT)

listaDeConversiones = tk.Label(ventana)
listaDeConversiones.pack(pady=10)

frame_inferior = tk.Frame(ventana)
frame_inferior.pack(pady=10)

boton_eliminar = tk.Button(frame_inferior, text="Limpiar ventana.", command=eliminar_conver)
boton_eliminar.pack(side=tk.LEFT, padx=10)


ventana.mainloop()
