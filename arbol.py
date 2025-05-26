class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioOrdenado:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        self.raiz = self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        if nodo is None:
            return Nodo(dato)
        if dato < nodo.dato:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, dato)
        elif dato > nodo.dato:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, dato)
        return nodo

    def inorden(self):
        print("Recorrido Inorden:")
        self._inorden_recursivo(self.raiz)
        print()

    def _inorden_recursivo(self, nodo):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo)
            print(nodo.dato, end=" ")
            self._inorden_recursivo(nodo.derecho)

    def postorden(self):
        print("Recorrido Postorden:")
        self._postorden_recursivo(self.raiz)
        print()

    def _postorden_recursivo(self, nodo):
        if nodo:
            self._postorden_recursivo(nodo.izquierdo)
            self._postorden_recursivo(nodo.derecho)
            print(nodo.dato, end=" ")

    def preorden(self):
        print("Recorrido Preorden:")
        self._preorden_recursivo(self.raiz)
        print()

    def _preorden_recursivo(self, nodo):
        if nodo:
            print(nodo.dato, end=" ")
            self._preorden_recursivo(nodo.izquierdo)
            self._preorden_recursivo(nodo.derecho)

# 🧠 Menú interactivo
def menu():
    arbol = ArbolBinarioOrdenado()
    while True:
        print("\n MENÚ - Árbol Binario Ordenado")
        print("1. Insertar dato")
        print("2. Imprimir en Inorden")
        print("3. Imprimir en Postorden")
        print("4. Imprimir en Preorden")
        print("5. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                dato = int(input("Ingresa el número a insertar: "))
                arbol.insertar(dato)
                print("Dato insertado correctamente.")
            except ValueError:
                print("Por favor ingresa un número válido.")
        elif opcion == "2":
            arbol.inorden()
        elif opcion == "3":
            arbol.postorden()
        elif opcion == "4":
            arbol.preorden()
        elif opcion == "5":
            print("¡Gracias por usar el programa!")
            break
        else:
            print(" Opción inválida. Intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
