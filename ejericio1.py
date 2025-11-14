import csv
import random

class Venta:
    def __init__(self, caja, monto_venta):
        self.caja = caja
        self.monto_venta = monto_venta
        self.monto_donado = self.calcular_donacion()
        self.monto_final = round(monto_venta + self.monto_donado, 2)

    def calcular_donacion(self):
        paso = 0.05
        base = round(self.monto_venta / paso)
        siguiente_multiplo = (base + 1) * paso
        donacion = round(siguiente_multiplo - self.monto_venta, 2)
        return donacion if donacion != 0 else 0.0

    def info(self):
        return {
            'Caja': self.caja,
            'Monto Venta': self.monto_venta,
            'Monto Donado': self.monto_donado,
            'Monto Final': self.monto_final
        }


def imprimir_encabezado():
    print("="*40)
    print("I - P - S")
    print("Institución: Instituto Peruano Superior")
    print("Programa: Supervisión de Donaciones en Ventas")
    print("Docente: Ing. Juan Pérez")
    print("="*40)
    print()


def simular_ventas():
    ventas = []
    cajas = [1, 2, 3, 4, 5]

    for _ in range(20):
        caja = random.choice(cajas)
        monto_venta = round(random.uniform(1, 100), 2)
        venta = Venta(caja, monto_venta)
        ventas.append(venta)

    return ventas


def mostrar_datos(ventas):
    print(f"{'Caja':<6} {'Monto Venta':<12} {'Monto Donado':<13} {'Monto Final':<12}")
    print("-"*45)
    for v in ventas:
        print(f"{v.caja:<6} S/ {v.monto_venta:<10.2f} S/ {v.monto_donado:<11.2f} S/ {v.monto_final:<10.2f}")
    print()


def grabar_csv_ventas(ventas, archivo_ventas="ape_paterno.csv", archivo_info="ape_materno.csv"):
    with open(archivo_ventas, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Caja', 'Monto Venta', 'Monto Donado', 'Monto Final'])
        for v in ventas:
            writer.writerow([v.caja, f"{v.monto_venta:.2f}", f"{v.monto_donado:.2f}", f"{v.monto_final:.2f}"])

    resumen = {}
    for v in ventas:
        if v.caja not in resumen:
            resumen[v.caja] = {'Ventas': 0, 'Total Donado': 0.0, 'Total Final': 0.0}
        resumen[v.caja]['Ventas'] += 1
        resumen[v.caja]['Total Donado'] += v.monto_donado
        resumen[v.caja]['Total Final'] += v.monto_final

    with open(archivo_info, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Caja', 'Cantidad Ventas', 'Total Donado', 'Total Final'])
        for caja, datos in resumen.items():
            writer.writerow([caja, datos['Ventas'], f"{datos['Total Donado']:.2f}", f"{datos['Total Final']:.2f}"])

    print(f"Datos guardados en '{archivo_ventas}' y resumen en '{archivo_info}'\n")


def leer_csv(archivo):
    print(f"Contenido del archivo '{archivo}':")
    try:
        with open(archivo, mode='r') as f:
            reader = csv.reader(f)
            for fila in reader:
                print(", ".join(fila))
        print()
    except FileNotFoundError:
        print(f"Archivo '{archivo}' no encontrado.\n")


def menu():
    ventas = None
    while True:
        print("----- Menú del Laboratorio -----")
        print("1. Simular ventas y mostrar reporte")
        print("2. Guardar datos en archivos CSV")
        print("3. Leer archivos CSV y mostrar contenido")
        print("4. Salir")
        opcion = input("Seleccione opción: ")

        if opcion == '1':
            ventas = simular_ventas()
            imprimir_encabezado()
            mostrar_datos(ventas)
        elif opcion == '2':
            if ventas:
                grabar_csv_ventas(ventas)
            else:
                print("Primero debe simular las ventas (opción 1).\n")
        elif opcion == '3':
            leer_csv("ape_paterno.csv")
            leer_csv("ape_materno.csv")
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")


if __name__ == "__main__":
    menu()
