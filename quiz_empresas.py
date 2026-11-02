# quiz_empresas.py
# Quiz 1 - Fundamentos de programacion (Programacion Estructurada + POO)
# Tu tarea: completar todos los bloques marcados con "# TODO".
# Cada linea de empresas.txt tiene:  nombre, sector, num_empleados, ingresos_anuales
# Para ejecutar:  python quiz_empresas.py
#
# CONSEJO: ve completando un TODO a la vez y ejecuta el archivo para ver como
#          se va llenando la salida. Al inicio veras resultados vacios o en cero.


# 1) LA CLASE: representa UNA empresa (datos + comportamiento juntos)
class Empresa:
    """Representa una empresa: encapsula sus datos y su comportamiento."""

    # El CONSTRUCTOR se ejecuta al crear el objeto y guarda sus datos.
    # 'self' es el propio objeto que se esta construyendo.
    def __init__(self, nombre, sector, num_empleados, ingresos_anuales):
        self.nombre = nombre
        self.sector = sector
        # Se convierten a int porque al leer del archivo llegan como texto.
        self.num_empleados = int(num_empleados)
        self.ingresos_anuales = int(ingresos_anuales)

    def obtener_informacion(self):
        """Devuelve los datos de la empresa como un texto legible."""
        return (f"{self.nombre} | {self.sector} | "
                f"{self.num_empleados} empleados | ${self.ingresos_anuales}")


# 2) Leer el archivo y crear una LISTA DE OBJETOS Empresa
def leer_empresas(nombre_archivo):
    """Lee el archivo y crea un objeto Empresa por cada linea valida.

    Una linea es INVALIDA si num_empleados es menor o igual a 0:
    en ese caso NO se crea el objeto (se ignora el registro).
    """
    empresas = []
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            nombre, sector, num_empleados, ingresos_anuales = linea.strip().split(",")
            # Solo se crea el objeto si el registro es valido empleados > 0 , para ignorar la trampa.
            if int(num_empleados) > 0:
                empresas.append(Empresa(nombre, sector, num_empleados, ingresos_anuales))
    return empresas


# 3) Sumar los ingresos de todas las empresas
def calcular_total_ingresos(empresas):
    """Devuelve la suma de los ingresos_anuales de todas las empresas."""
    total = 0
    for empresa in empresas:
        total += empresa.ingresos_anuales
    return total


# 4) Quedarse solo con las empresas de un sector
def filtrar_por_sector(empresas, sector):
    """Devuelve una lista con las empresas cuyo sector coincide."""
    filtradas = []
    for empresa in empresas:
        if empresa.sector == sector:
            filtradas.append(empresa)
    return filtradas


# 5) Encontrar la empresa con mas empleados
def empresa_con_mas_empleados(empresas):
    """Devuelve el objeto Empresa que tiene mas empleados."""
    mejor = None
    for empresa in empresas:
        if mejor is None or empresa.num_empleados > mejor.num_empleados:
            mejor = empresa
    return mejor


# 6) Calcular el promedio de empleados
def promedio_empleados(empresas):
    """Devuelve el promedio de empleados de todas las empresas."""
    if len(empresas) == 0:
        return 0  # evita dividir entre cero
    total_empleados = 0
    for empresa in empresas:
        total_empleados += empresa.num_empleados
    # Se redondea a 2 decimales para coincidir con la salida esperada.
    return round(total_empleados / len(empresas), 2)


# 7) Funcion principal: usa todo lo anterior y muestra los resultados
def ejecutar_quiz():
    empresas = leer_empresas("empresas.txt")

    print("--- Empresas registradas ---")
    for empresa in empresas:
        print(empresa.obtener_informacion())

    print("\nTotal de ingresos:", calcular_total_ingresos(empresas))

    print("\n--- Empresas del sector TECNOLOGIA ---")
    for empresa in filtrar_por_sector(empresas, "TECNOLOGIA"):
        print(empresa.obtener_informacion())

    mejor = empresa_con_mas_empleados(empresas)
    if mejor is not None:
        print("\nEmpresa con mas empleados:", mejor.obtener_informacion())

    print("\nPromedio de empleados:", promedio_empleados(empresas))


# Iniciar el programa
ejecutar_quiz()
