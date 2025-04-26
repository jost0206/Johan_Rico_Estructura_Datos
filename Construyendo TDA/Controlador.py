from tkinter import messagebox
from Modelo import ListaDoble1

class Controlador:
    def __init__(self, vista):
        self.vista=vista
        self.lista=ListaDoble1()

    def insertar_cliente(self):
        cedula, nombre=self.vista.obtener_datos()
        if not cedula.isdigit() or not nombre:
            messagebox.showwarning("Entrada inválida", "Ingresa los datos correctamente para continuar.")
            return
        self.lista.inserta_lista_ordenada(int(cedula), nombre)
        self.vista.mostrar_resultados(["Cliente insertado correctamente."])

    def listar_a_derecha(self):
        resultado = self.lista.listar_a_derecha()
        self.vista.mostrar_resultados(resultado)

    def listar_a_izquierda(self):
        resultado = self.lista.listar_a_izquierda()
        self.vista.mostrar_resultados(resultado)
