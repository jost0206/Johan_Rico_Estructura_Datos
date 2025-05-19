import tkinter as tk
import time

class TorreHanoiVisual:
    def __init__(self, root):
        self.root = root
        self.root.title("Torres de Hanoi")
        self.root.config(bg="#440D52")

        # Frame principal (para canvas y log)
        self.frame_principal = tk.Frame(root, bg="#440D52")
        self.frame_principal.pack()

        # Se diseñan e implementan los discos en el canvas (izquierda)
        self.canvas = tk.Canvas(self.frame_principal, width=600, height=400, bg="white")
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
   
        self.barra_ancho = 20
        self.torres_x = [150, 300, 450]  
        self.base_y = 350  

        self.discos = []
        self.num_discos = 0
        self.torres = [[], [], []]  # Estado de las tres torres

        # Ventana de pasos (derecha)
        self.texto_pasos = tk.Text(self.frame_principal, width=35, height=25, font=("Courier", 10), bg="#F3E5F5", fg="#4A148C")
        self.texto_pasos.pack(side=tk.RIGHT, padx=10, pady=10)
        self.texto_pasos.insert(tk.END, "📜 Registro de pasos:\n")

        # Botón ejecutar y entrada
        self.label = tk.Label(root, text="¿Cuántos discos desea colocar?", font=("Arial", 12), bg="#360E3A", fg="white")
        self.label.pack()
        self.entrada = tk.Entry(root, font=("Arial", 12))
        self.entrada.pack()

        self.btn = tk.Button(root, text="Ejecutar", font=("Arial", 12), bg="#2B0427", fg="white", command=self.iniciar)
        self.btn.pack(pady=10)

        self.dibujar_torres()  # Dibujar las torres al iniciar

    # Dibuja las 3 torres y la base negra
    def dibujar_torres(self):
        for x in self.torres_x:
            self.canvas.create_rectangle(x - 5, 150, x + 5, self.base_y, fill="sienna")  # Color madera
        self.canvas.create_rectangle(50, self.base_y, 550, self.base_y + 10, fill="black")

    # Crea e implementa los discos en la torre 1
    def crear_discos(self, n):
        self.num_discos = n
        ancho_max = 120
        altura = 20
        self.discos.clear()
        self.torres = [[], [], []]
        self.canvas.delete("disco")  # Borra discos anteriores
        self.texto_pasos.delete("1.0", tk.END)  # Limpia la ventana de texto
        self.texto_pasos.insert(tk.END, "📜 Registro de pasos:\n")

        for i in range(n):
            ancho = ancho_max - i * 15
            x0 = self.torres_x[0] - ancho // 2
            y0 = self.base_y - i * altura - altura
            x1 = self.torres_x[0] + ancho // 2
            y1 = y0 + altura
            disco = self.canvas.create_rectangle(x0, y0, x1, y1, fill="#A77D58", tags="disco")
            self.torres[0].append(disco)
            self.discos.append((disco, ancho, altura))

    # Mueve un disco visualmente de una torre a otra y lo registra en la ventana de texto
    def mover_disco(self, origen, destino):
        disco = self.torres[origen].pop()
        self.torres[destino].append(disco)

        idx = self.torres[destino].index(disco)
        _, ancho, alto = self.discos[self.canvas.find_withtag("disco").index(disco)]
        x = self.torres_x[destino]
        x0 = x - ancho // 1.7
        x1 = x + ancho // 1.7
        y1 = self.base_y - idx * alto
        y0 = y1 - alto
        self.canvas.coords(disco, x0, y0, x1, y1)  # Reposiciona el disco

        # Agregar texto del paso a la ventanita
        texto_paso = f"🟣 Mover disco de torre {origen + 1} → torre {destino + 1}\n"
        self.texto_pasos.insert(tk.END, texto_paso)
        self.texto_pasos.see(tk.END)  # Scroll automático al final
        self.root.update()
        time.sleep(1)

    # Algoritmo recursivo
    def hanoi(self, n, origen, auxiliar, destino):
        if n == 1:
            self.mover_disco(origen, destino)
        else:
            self.hanoi(n - 1, origen, destino, auxiliar)
            self.mover_disco(origen, destino)
            self.hanoi(n - 1, auxiliar, origen, destino)

    # Función que se llama al presionar "Ejecutar"
    def iniciar(self):
        try:
            n = int(self.entrada.get())
            if n <= 0 or n > 8:
                raise ValueError
        except ValueError:
            self.label.config(text="Por favor, ingresa un número válido (1 a 8).", fg="red")
            return

        self.crear_discos(n)
        self.root.after(500, lambda: self.hanoi(n, 0, 1, 2))

# Crear ventana principal
ventana = tk.Tk()
app = TorreHanoiVisual(ventana)
ventana.mainloop()