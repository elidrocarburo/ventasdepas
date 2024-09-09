class VentaAnual:
    def __init__(self,departamentos, meses):
        self.departamentos= departamentos
        self.meses= meses
        self.ventas= [[0 for i in range(len(self.meses))] for i in range(len(self.departamentos))]

    def ingresos(self,departamento,mes,dinero):
        if departamento not in self.departamentos or mes not in self.meses:
            print("Departamento o mes no válidos.")
            return
        
        depa_index = self.departamentos.index(departamento)
        mes_index = self.meses.index(mes)

        self.ventas[depa_index][mes_index] = dinero
        print(f"Venta del monto {dinero} del mes {mes} del departamento {departamento}")
    
    def buscar_venta(self, departamento,mes):
        if departamento not in self.departamentos or mes not in self.meses:
            print("Departamento o mes no válidos.")
            return
        
        depa_index = self.departamentos.index(departamento)
        mes_index = self.meses.index(mes)
        return self.ventas[depa_index][mes_index]
    
    def eliminar_venta(self,departamento,mes):
        if departamento not in self.departamentos or mes not in self.meses:
            print("Departamento o mes no válidos.")
            return
        
        depa_index = self.departamentos.index(departamento)
        mes_index = self.meses.index(mes)
        self.ventas[depa_index][mes_index] = 0
        
        print(f"Venta eliminada del departamento {departamento} del mes de {mes}")

    def tabla(self):
        print("Ventas")
        print(f"{'Departamento':<25}", end="")
        for mes in self.meses:
            print(f"{mes:<12}", end="")
        print()
    
        for i, depa in enumerate(self.departamentos):
            print(f"{depa:<25}", end="")
            for venta in self.ventas[i]:
                print(f"{venta:<12}", end="")
            print()
    
    def ingresar_datos(self):
        while True:
            print("Menú de acceso a la venta anual de una tienda departamental.")
            print("\nOpciones:")
            print("1. Ingresar ventas")
            print("2. Eliminar ventas")
            print("3. Buscar ventas")
            print("4. Salir")
            
            opcion = input("Elija una opción: ")
            
            if opcion == '1':
                departamento = input("Ingrese el nombre del departamento: ")
                mes = input("Ingrese el mes: ")

                try:
                    dinero = float(input(f"¿Cuánto dinero generó el mes {mes} para el departamento {departamento}?: "))
                    if dinero < 0:
                        print("El monto no puede ser negativo, intente de nuevo.")
                        continue
                    self.ingresos(departamento, mes, dinero)
                except ValueError:
                    print("Ha ocurrido un error, verifica que esté ingresando números")

            elif opcion == '2':
                departamento = input("Ingrese el nombre del departamento para eliminar la venta: ")
                mes = input("Ingrese el mes para eliminar la venta: ")
                self.eliminar_venta(departamento, mes)

            elif opcion == '3':
                departamento = input("Ingrese el nombre del departamento para buscar la venta: ")
                mes = input("Ingrese el mes para buscar la venta: ")
                venta = self.buscar_venta(departamento, mes)
                if venta is not None:
                    print(f"La venta del mes de {mes} para el {departamento} es {venta}")
                else:
                    print("No se encontró ninguna venta para el departamento y mes especificados.")

            elif opcion == '4':
                break

            else:
                print("Opción no válida, intente de nuevo.")
        
        print("Operación terminada.")

departamentos= ['Departamento de Ropa', 'Departamento de Deportes', 'Departamento de Juguetería ']
meses= ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
ventas = VentaAnual(departamentos,meses)

ventas.tabla()
ventas.ingresar_datos()
ventas.tabla()
