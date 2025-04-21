 import java.util.Scanner;

class Cliente {
    int cedula;
    String nombre;
    Cliente anterior;
    Cliente siguiente;

    public Cliente(int cedula, String nombre) {
        this.cedula=cedula;
        this.nombre=nombre;
        this.anterior=null;
        this.siguiente=null;
    }
}

class ListaDoble {
    private Cliente cabeza;

    public ListaDoble() {
        this.cabeza = null;
    }

    // Insertar ordenadamente por orden numérico de cédula
    public void insertarOrdenado(int cedula, String nombre) {
        Cliente nuevo=new Cliente(cedula, nombre);
        if (cabeza==null || cabeza.cedula>cedula) {
            nuevo.siguiente=cabeza;
            if (cabeza != null) {
                cabeza.anterior=nuevo;
            }
            cabeza=nuevo;
        } else {
            Cliente actual=cabeza;
            while (actual.siguiente != null && actual.siguiente.cedula < cedula) {
                actual=actual.siguiente;
            }
            nuevo.siguiente=actual.siguiente;
            if (actual.siguiente != null) {
                actual.siguiente.anterior=nuevo;
            }
            actual.siguiente=nuevo;
            nuevo.anterior=actual;
        }
    }

    // Listar hacia la derecha (desde el primero al último)
    public void listarDerecha() {
        if (cabeza == null) {
            System.out.println("La lista está vacía.");
            return;
        }
        Cliente actual=cabeza;
        while (actual != null) {
            System.out.println("Cédula: " + actual.cedula + ", Nombre: " + actual.nombre);
            if (actual.siguiente == null) break; // Se guarda el último para recorrer al revés luego
            actual = actual.siguiente;
        }
    }

    // Listar hacia la izquierda (del último al primero)
    public void listarIzquierda() {
        if (cabeza == null) {
            System.out.println("La lista está vacía.");
            return;
        }
        // Ir hasta el final
        Cliente actual = cabeza;
        while (actual.siguiente != null) {
            actual = actual.siguiente;
        }
        // Volver al inicio
        while (actual != null) {
            System.out.println("Cédula: " + actual.cedula + ", Nombre: " + actual.nombre);
            actual = actual.anterior;
        }
    }
}

public class ListaDobleCliente {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ListaDoble lista = new ListaDoble();
        int opcion;

        do {
            System.out.println("\n Menú de opciones:");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Listar clientes hacia la derecha");
            System.out.println("3. Listar clientes hacia la izquierda");
            System.out.println("4. Salir");
            System.out.print("Seleccione una opción: ");
            opcion = scanner.nextInt();
            scanner.nextLine(); // Limpiar el buffer

            switch (opcion) {
                case 1:
                    System.out.print("Ingrese la cédula del cliente: ");
                    int cedula = scanner.nextInt();
                    scanner.nextLine();
                    System.out.print("Ingrese el nombre del cliente: ");
                    String nombre = scanner.nextLine();
                    lista.insertarOrdenado(cedula, nombre);
                    System.out.println("Cliente añadido satisfactoriamente. ");
                    break;
                case 2:
                    System.out.println("Lista de clientes (de izquierda a derecha):");
                    lista.listarDerecha();
                    break;
                case 3:
                    System.out.println("Lista de clientes (de derecha a izquierda):");
                    lista.listarIzquierda();
                    break;
                case 4:
                    System.out.println("Saliendo de la aplicación. Nos vemos pronto.");
                    break;
                default:
                    System.out.println("Opción no válida. Intente de nuevo.");
            }
        } while (opcion != 4);

        scanner.close();
    }
}
