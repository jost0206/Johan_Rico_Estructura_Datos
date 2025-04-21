import java.util.Scanner;
class Datos { // Esta parte del codigo representa los datos de cada cliente dentro de la lista
int cedula;
String nombre;
Datos siguiente;

public Datos (int cedula, String nombre) {
  this.cedula=cedula;
  this.nombre=nombre;
  this.siguiente=null; }
}

class Lista { //Acá se maneja el tema de la lista simple
    private Datos cabeza;
    public Lista() {
        this.cabeza=null; }
    public void ListaOrdenada (int cedula, String nombre) { //Con este método, cada vez que agreguemos clientes, se añadirán en orden numérico, respecto a la cédula
    Datos nuevo=new Datos (cedula, nombre);
    if (cabeza==null || cabeza.cedula>cedula){
        nuevo.siguiente=cabeza;
        cabeza=nuevo; }
        else {
            Datos actual=cabeza;
            while (actual.siguiente!=null && actual.siguiente.cedula<cedula){
                actual=actual.siguiente; } 
                nuevo.siguiente=actual.siguiente;
                actual.siguiente=nuevo; }
} 
public void EnlistarClientes() { //Acá se enlistan los clientes, como si fueran nodos
    if (cabeza==null) {
        System.out.println("La lista se encuentra vacia. Inserte nuevos clientes para que aparezcan.");
        return; }
        Datos actual=cabeza;
    while(actual!=null) {
        System.out.println("Cedula: " + actual.cedula + ", nombre: " + actual.nombre);
        actual=actual.siguiente;}
    }
}

public class GestionarClientes { //En esta clase, que es la principal, se gestiona el tema de la aplicación
    public static void main(String[] args) {
        Scanner scanner=new java.util.Scanner(System.in);
        Lista lista=new Lista();
        int opciones;
        do { // Acá se crea el menú
            System.out.println("\n Menu:Opciones");
            System.out.println("1. Insertar cliente");
            System.out.println("2. Listar clientes hacia la derecha");
            System.out.println("3. Salir");
            System.out.println("Seleccione una opcion: ");
            opciones=scanner.nextInt();
        switch(opciones){
            case 1: //Acá se maneja las acciones que realiza cada opción
            System.out.println("Ingrese la cedula del nuevo cliente que desea inscribir a la lista: ");
            int cedula=scanner.nextInt();
            scanner.nextLine();
            System.out.println("Ahora, ingrese su nombre: ");
            String nombre=scanner.nextLine();
            lista.ListaOrdenada(cedula, nombre);
            System.out.println("Listo. Cliente ingresado al sistema de manera satisfactoria. ");
            break;
        
            case 2:
            System.out.println("Así se encuentra la lista de clientes: ");
            lista.EnlistarClientes();
            break;

            case 3:
            System.out.println("Saliendo de la aplicación... Nos vemos pronto, hasta luego! ");
            break;
         
            default: 
            System.out.println("Opcion no valida. Intentelo de nuevo. "); } }   
            while (opciones!=3);
            scanner.close(); }
}