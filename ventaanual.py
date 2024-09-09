class VentaAnual:
    def _init_(self):
        self.departamentos= ['Departamento de Ropa', 'Departamento de Deportes', 'Departamento de Juguetería']
        self.meses= ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.ventas= [[0 for i in range(len(self.meses))] for i in range(len(self.departamentos))]

    def ingresos(self,departamento,mes,dinero):
        depa_index = self.departamentos.index(departamento)
        mes_index = self.meses.index(mes)

        self.ventas[depa_index][mes_index] = dinero
        print(f"Venta del monto {dinero} del mes {mes} del departamento {departamento}")
    
    def buscar_venta(self, departamento,mes):
        depa_index = self.departamentos.index(departamento)
        mes_index = self.meses.index(mes)
        return self.ventas[depa_index][mes_index]
    
    def eliminar_venta(self,departamento,mes):
        depa_index = self.departamentos.index(departamento)
        mes_index = self.meses.index(mes)
        self.ventas[depa_index][mes_index] = 0
        print(f"Venta eliminada del departamento {departamento} del mes{mes}")

    def tabla(self):
        print("Ventas")
        print("Departamento y meses")
        for mes in self.meses:
            print(f"{mes:>12}")
        print()
    
        for i, depa in enumerate(self.departamentos):
            print(f"{depa:>15}")
            for venta in self.ventas[i]:
                print(f"{venta:>12}")
            print()
    
    def ingresar_datos(self):
        for depa in self.departamentos:
            print(f"\nIngrese las ventas para el departamento: {depa}")
            for mes in self.meses:
                try:
                    dinero=float(input(f"¿Cuánto dinero generó el mes {mes}?: "))
                    if dinero < 0:
                        print("El monto no puede ser negativo, intenta de nuevo.")
                    else:
                        depa_index = self.departamentos.index(depa)
                        mes_index = self.meses.index(mes)
                        self.ventas[depa_index][mes_index] = dinero
                        break
                except ValueError:
                    print("Ha ocurrido un error, verifica que esté ingresando números")
    print("Agregado correctamente.")

ventas = VentaAnual()
ventas.ingresos()
ventas.buscar_venta()
ventas.eliminar_venta()
ventas.tabla()
ventas.ingresar_datos()