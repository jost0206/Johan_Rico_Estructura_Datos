import tkinter as tk

class VistaLista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.root = tk.Tk()
        self.root.title("Lista Circular Dinámica / MVC")
        self.root.configure(bg='purple')

        self.cedula_entry=tk.Entry(self.root)
        self.nombre_entry=tk.Entry(self.root)
        self.boton_insertar=tk.Button(self.root, text="Insertar dato", command=self.controlador.insertar_cliente)
        self.boton_listar_a_derecha=tk.Button(self.root, text="Listar hacia la derecha ->", command=self.controlador.listar_a_derecha)
        self.resultado=tk.Text(self.root, height=7, width=40)

        self.cedula_entry.insert(0, "Cédula")
        self.nombre_entry.insert(0, "Nombre")

        self.cedula_entry.pack(pady=5)
        self.nombre_entry.pack(pady=5)
        self.boton_insertar.pack(pady=5)
        self.boton_listar_a_derecha.pack(pady=5)
        self.resultado.pack(pady=10)

        self.cedula_entry.bind("<FocusIn>", self.clear_placeholder)
        self.nombre_entry.bind("<FocusIn>", self.clear_placeholder)

    def clear_placeholder(self, event):
        if event.widget.get() in ["Cédula", "Nombre"]:
            event.widget.delete(0, tk.END)

    def obtener_datos(self):
        return self.cedula_entry.get(), self.nombre_entry.get()

    def mostrar_resultados(self, lineas):
        self.resultado.delete(1.0, tk.END)
        for linea in texto:
            self.resultado.insert(tk.END, linea + "\n")

    def mostrar_mensje(self, mensaje):
        self.mostrar_mensje([mensaje])

    def inicio(self):
        self.root.mainloop()
