from Vista import VistaLista
from Controlador import Controlador

if __name__ == "__main__":
    controlador=Controlador(None)
    vista=VistaLista(controlador)
    controlador.vista=vista
    vista.inicio()