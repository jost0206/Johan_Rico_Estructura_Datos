from Modelo import ListaCircular

class Controlador:
    def __init__(self, vista):
        self.vista=vista
        self.lista=ListaCircular()

    def insertar_cliente(self):
        cedula, nombre=self.vista.obtener_datos()
        if not cedula.isdigit() or not nombre:
            self.vista.mostrar_mensaje("Entrada inválida", "Ingresa los datos correctamente para continuar.")
            return
        self.lista.inserta_ordenada(int(cedula), nombre)
        self.vista.mostrar_mensaje(["Cliente insertado correctamente."])

    def listar_a_derecha(self):
        resultado = self.lista.listar_a_derecha()
        if not resultado:
            self.vista.mostrar_mensaje("Lista vacía.")
        else:
            self.vista.mostrar_resultados(resultado)