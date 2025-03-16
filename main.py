import tkinter as tk
from tkinter import messagebox

# Función para agregar un dato a la lista
def agregar_dato():
    dato = entry.get()  # Obtener el valor del campo de texto
    if dato:  # Si el campo de texto no está vacío
        lista_datos.insert(tk.END, dato)  # Insertar el dato en la lista
        entry.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Debe ingresar un dato.")  # Mostrar advertencia si el campo está vacío

# Función para limpiar la lista
def limpiar_datos():
    lista_datos.delete(0, tk.END)  # Eliminar todos los datos de la lista

# Función para eliminar un dato seleccionado
def eliminar_dato():
    try:
        # Obtener el índice de la selección actual y eliminarlo
        indice = lista_datos.curselection()
        lista_datos.delete(indice)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione un dato para eliminar.")  # Avisar si no hay selección

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Gestión de Datos")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:")
etiqueta.pack(pady=10)

# Crear un campo de texto
entry = tk.Entry(ventana, width=30)
entry.pack(pady=5)

# Crear un botón para agregar el dato
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Crear un botón para limpiar la lista
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Crear un botón para eliminar el dato seleccionado
boton_eliminar = tk.Button(ventana, text="Eliminar seleccionado", command=eliminar_dato)
boton_eliminar.pack(pady=5)

# Crear una lista donde se mostrarán los datos agregados
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# Iniciar el bucle de la ventana principal
ventana.mainloop()

