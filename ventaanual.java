import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class ventaanual {
    private List<String> departamentos;
    private List<String> meses;
    private double[][] ventas;

    public VentaAnual(List<String> departamentos, List<String> meses) {
        this.departamentos = departamentos;
        this.meses = meses;
        this.ventas = new double[departamentos.size()][meses.size()];

        for (int i = 0; i < departamentos.size(); i++) {
            Arrays.fill(ventas[i], 0);
        }
    }

    public void ingresos(String departamento, String mes, double dinero) {
        if (!departamentos.contains(departamento) || !meses.contains(mes)) {
            System.out.println("Departamento o mes no válidos.");
            return;
        }

        int depaIndex = departamentos.indexOf(departamento);
        int mesIndex = meses.indexOf(mes);

        ventas[depaIndex][mesIndex] = dinero;
        System.out.println("Venta del monto " + dinero + " del mes " + mes + " del departamento " + departamento);
    }

    public Double buscarVenta(String departamento, String mes) {
        if (!departamentos.contains(departamento) || !meses.contains(mes)) {
            System.out.println("Departamento o mes no válidos.");
            return null;
        }

        int depaIndex = departamentos.indexOf(departamento);
        int mesIndex = meses.indexOf(mes);

        return ventas[depaIndex][mesIndex];
    }

    public void eliminarVenta(String departamento, String mes) {
        if (!departamentos.contains(departamento) || !meses.contains(mes)) {
            System.out.println("Departamento o mes no válidos.");
            return;
        }

        int depaIndex = departamentos.indexOf(departamento);
        int mesIndex = meses.indexOf(mes);

        ventas[depaIndex][mesIndex] = 0;
        System.out.println("Venta eliminada del departamento " + departamento + " del mes de " + mes);
    }

    public void tabla() {
        System.out.println("Ventas");
        System.out.printf("%-25s", "Departamento");

        for (String mes : meses) {
            System.out.printf("%-12s", mes);
        }
        System.out.println();

        for (int i = 0; i < departamentos.size(); i++) {
            System.out.printf("%-25s", departamentos.get(i));
            for (double venta : ventas[i]) {
                System.out.printf("%-12.2f", venta);
            }
            System.out.println();
        }
    }

    public void ingresarDatos() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Menú de acceso a la venta anual de una tienda departamental.");
            System.out.println("\nOpciones:");
            System.out.println("1. Ingresar ventas");
            System.out.println("2. Eliminar ventas");
            System.out.println("3. Buscar ventas");
            System.out.println("4. Salir");

            String opcion = scanner.nextLine();

            if (opcion.equals("1")) {
                System.out.print("Ingrese el nombre del departamento: ");
                String departamento = scanner.nextLine();
                System.out.print("Ingrese el mes: ");
                String mes = scanner.nextLine();

                System.out.print("¿Cuánto dinero generó el mes " + mes + " para el departamento " + departamento + "?: ");
                try {
                    double dinero = Double.parseDouble(scanner.nextLine());
                    if (dinero < 0) {
                        System.out.println("El monto no puede ser negativo, intente de nuevo.");
                        continue;
                    }
                    ingresos(departamento, mes, dinero);
                } catch (NumberFormatException e) {
                    System.out.println("Ha ocurrido un error, verifica que esté ingresando números");
                }

            } else if (opcion.equals("2")) {
                System.out.print("Ingrese el nombre del departamento para eliminar la venta: ");
                String departamento = scanner.nextLine();
                System.out.print("Ingrese el mes para eliminar la venta: ");
                String mes = scanner.nextLine();
                eliminarVenta(departamento, mes);

            } else if (opcion.equals("3")) {
                System.out.print("Ingrese el nombre del departamento para buscar la venta: ");
                String departamento = scanner.nextLine();
                System.out.print("Ingrese el mes para buscar la venta: ");
                String mes = scanner.nextLine();
                Double venta = buscarVenta(departamento, mes);
                if (venta != null) {
                    System.out.println("La venta del mes de " + mes + " para el " + departamento + " es " + venta);
                } else {
                    System.out.println("No se encontró ninguna venta para el departamento y mes especificados.");
                }

            } else if (opcion.equals("4")) {
                break;

            } else {
                System.out.println("Opción no válida, intente de nuevo.");
            }
        }
        System.out.println("Operación terminada.");
    }

    public static void main(String[] args) {
        List<String> departamentos = new ArrayList<>(Arrays.asList("Departamento de Ropa", "Departamento de Deportes", "Departamento de Juguetería"));
        List<String> meses = new ArrayList<>(Arrays.asList("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"));

        VentaAnual ventas = new VentaAnual(departamentos, meses);
        ventas.tabla();
        ventas.ingresarDatos();
        ventas.tabla();
    }
}
