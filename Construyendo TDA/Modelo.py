class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula=cedula
        self.nombre=nombre
        self.anterior=None
        self.siguiente=None

class ListaCircular:
    def __init__(self):
        self.inicio=None

    def inserta_lista_ordenada(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        if self.inicio is None:
            nuevo.siguiente=nuevo.anterior=nuevo
            self.inicio=nuevo
        else:
            actual=self.inicio
        if cedula<actual.cedula:
            while actual.siguiente!=self.inicio:
                actual=actual.siguiente
                actual.siguiente.anterior=nuevo
            nuevo.siguiente=self.inicio
            nuevo.anterior=actual
            actual.siguiente=nuevo
            self.inicio.anterior=nuevo
            self.inicio=nuevo
              
        else:
            while (actual.siguiente!=self.inicio and actual.siguiente.cedula<cedula):
                actual=actual.siguiente
            nuevo.siguiente=actual.siguiente
            nuevo.anterior=actual
            actual.siguiente.anterior=nuevo
            actual.siguiente=nuevo

    def listar_a_derecha(self):
        resultado=[]
        if self.inicio is None:
            return ["Lista vacía."]
        actual=self.inicio
        while True:
            resultado.append(f"{actual.cedula} - {actual.nombre}")
            actual=actual.siguiente
            if actual == self.inicio:
                break
        return resultado

