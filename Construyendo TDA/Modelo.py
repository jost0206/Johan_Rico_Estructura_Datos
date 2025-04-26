class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula=cedula
        self.nombre=nombre
        self.anterior=None
        self.siguiente=None

class ListaDoble1:
    def __init__(self):
        self.inicio=None

    def inserta_lista_ordenada(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        if self.inicio is None or cedula<self.inicio.cedula:
            nuevo.siguiente=self.inicio
            if self.inicio:
                self.inicio.anterior=nuevo
            self.inicio=nuevo
        else:
            actual=self.inicio
            while actual.siguiente and actual.siguiente.cedula<cedula:
                actual=actual.siguiente
            nuevo.siguiente=actual.siguiente
            if actual.siguiente:
                actual.siguiente.anterior=nuevo
            actual.siguiente=nuevo
            nuevo.anterior=actual

    def listar_a_derecha(self):
        actual=self.inicio
        resultado=[]
        while actual:
            resultado.append(f"{actual.cedula} - {actual.nombre}")
            actual=actual.siguiente
        return resultado

    def listar_a_izquierda(self):
        actual=self.inicio
        while actual and actual.siguiente:
            actual=actual.siguiente
        resultado=[]
        while actual:
            resultado.append(f"{actual.cedula} - {actual.nombre}")
            actual=actual.anterior
        return resultado
