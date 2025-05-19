import tkinter as tk
from tkinter import messagebox

# Nodo individual para la lista simple
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Bicola basada en lista enlazada simple
class Bicola:
    def __init__(self):
        self.frente = None
        self.final = None

    # Insertar por la derecha (final)
    def insertar_derecha(self, valor):
        nuevo = Nodo(valor)
        if self.frente is None:
            self.frente = self.final = nuevo
        else:
            self.final.siguiente = nuevo
            self.final = nuevo

    # Insertar por la izquierda (frente)
    def insertar_izquierda(self, valor):
        nuevo = Nodo(valor)
        if self.frente is None:
            self.frente = self.final = nuevo
        else:
            nuevo.siguiente = self.frente
            self.frente = nuevo

    # Atender (eliminar) por la derecha (final)
    def atender_derecha(self):
        if self.frente is None:
            return None
        elif self.frente == self.final:
            valor = self.final.valor
            self.frente = self.final = None
            return valor
        else:
            actual = self.frente
            while actual.siguiente != self.final:
                actual = actual.siguiente
            valor = self.final.valor
            actual.siguiente = None
            self.final = actual
            return valor

    # Atender (eliminar) por la izquierda (frente)
    def atender_izquierda(self):
        if self.frente is None:
            return None
        valor = self.frente.valor
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return valor

    # Obtener todos los elementos de la bicola
    def listar(self):
        elementos = []
        actual = self.frente
        while actual:
            elementos.append(str(actual.valor))
            actual = actual.siguiente
        return elementos

# Interfaz gráfica con Tkinter
class BicolaApp:
    def __init__(self, root):
        self.bicola = Bicola()
        self.root = root
        self.root.title("Bicola con Lista Simple")
        self.root.geometry("500x400")
        self.root.config(bg="#F0F0F0")

        # Entrada de datos
        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Botones
        botones = [
            ("Insertar por la derecha", self.insertar_derecha),
            ("Insertar por la izquierda", self.insertar_izquierda),
            ("Atender por la derecha", self.atender_derecha),
            ("Atender por la izquierda", self.atender_izquierda),
            ("Listar elementos", self.listar)
        ]

        for texto, comando in botones:
            tk.Button(root, text=texto, font=("Arial", 12), width=25, command=comando).pack(pady=5)

        # Área de resultados
        self.resultado = tk.Text(root, height=8, font=("Courier", 12), bg="white", fg="black")
        self.resultado.pack(pady=10)

    # Función para insertar por la derecha
    def insertar_derecha(self):
        valor = self.entry.get()
        if valor:
            self.bicola.insertar_derecha(valor)
            self.entry.delete(0, tk.END)
            self.mostrar_mensaje(f"Insertado por la derecha: {valor}")

    # Función para insertar por la izquierda
    def insertar_izquierda(self):
        valor = self.entry.get()
        if valor:
            self.bicola.insertar_izquierda(valor)
            self.entry.delete(0, tk.END)
            self.mostrar_mensaje(f"Insertado por la izquierda: {valor}")

    # Función para atender por la derecha
    def atender_derecha(self):
        valor = self.bicola.atender_derecha()
        if valor:
            self.mostrar_mensaje(f"Atendido por la derecha: {valor}")
        else:
            self.mostrar_mensaje("La bicola está vacía.")

    # Función para atender por la izquierda
    def atender_izquierda(self):
        valor = self.bicola.atender_izquierda()
        if valor:
            self.mostrar_mensaje(f"Atendido por la izquierda: {valor}")
        else:
            self.mostrar_mensaje("La bicola está vacía.")

    # Función para mostrar la lista de elementos
    def listar(self):
        elementos = self.bicola.listar()
        if elementos:
            self.mostrar_mensaje("Bicola: " + " -> ".join(elementos))
        else:
            self.mostrar_mensaje("La bicola está vacía.")

    # Mostrar mensaje en el área de texto
    def mostrar_mensaje(self, mensaje):
        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, mensaje)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = BicolaApp(root)
    root.mainloop()
    
