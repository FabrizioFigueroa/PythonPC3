def cargar_alumnos():
    n = int(input("Ingrese cantidad de alumnos: "))
    alumnos = []
    for i in range(n):
        nombre = input(f"Nombre completo del alumno {i+1}: ")
        notas = []
        for j in range(3):
            while True:
                nota = float(input(f"Nota {j+1} para {nombre}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                print("La nota debe estar entre 0 y 10")
        alumnos.append({"nombre": nombre, "notas": notas})
    return alumnos

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class CUADRADO(RECTANGULO):
    def __init__(self, lado):
        super().__init__(lado, lado)

def evaluar_aprobados(alumnos):
    aprobados = 0
    desaprobados = 0
    for alumno in alumnos:
        promedio = sum(alumno["notas"]) / len(alumno["notas"])
        if promedio >= 4:
            aprobados += 1
        else:
            desaprobados += 1
    return aprobados, desaprobados

def promedio_curso(alumnos):
    suma_promedios = 0
    for alumno in alumnos:
        suma_promedios += sum(alumno["notas"]) / len(alumno["notas"])
    return suma_promedios / len(alumnos)

def mejores_peores(alumnos):
    promedios = []
    for alumno in alumnos:
        promedio = sum(alumno["notas"]) / len(alumno["notas"])
        promedios.append((alumno["nombre"], promedio))
    
    mejor = max(promedios, key=lambda x: x[1])
    peor = min(promedios, key=lambda x: x[1])
    return mejor, peor

def buscar_alumno(alumnos, nombre_buscar):
    encontrados = []
    for alumno in alumnos:
        if nombre_buscar.lower() in alumno["nombre"].lower():
            promedio = sum(alumno["notas"]) / len(alumno["notas"])
            encontrados.append({
                "nombre": alumno["nombre"],
                "notas": alumno["notas"],
                "promedio": promedio
            })
    return encontrados

alumnos = cargar_alumnos()

print("\n--- LISTADO DE ALUMNOS ---")
for i, alumno in enumerate(alumnos):
    print(f"{i+1}. {alumno['nombre']} - Notas: {alumno['notas']}")

largo = float(input("\nIngrese largo del rectangulo: "))
ancho = float(input("Ingrese ancho del rectangulo: "))
rectangulo = RECTANGULO(largo, ancho)

lado = float(input("Ingrese lado del cuadrado: "))
cuadrado = CUADRADO(lado)

print(f"Area del rectangulo: {rectangulo.calcular_area()}")
print(f"Area del cuadrado: {cuadrado.calcular_area()}")

aprobados, desaprobados = evaluar_aprobados(alumnos)
print(f"\nAprobados: {aprobados}, Desaprobados: {desaprobados}")

print(f"Promedio del curso: {promedio_curso(alumnos):.2f}")

mejor, peor = mejores_peores(alumnos)
print(f"Mayor promedio: {mejor[0]} ({mejor[1]:.2f})")
print(f"Menor promedio: {peor[0]} ({peor[1]:.2f})")

nombre_buscar = input("\nIngrese nombre a buscar: ")
encontrados = buscar_alumno(alumnos, nombre_buscar)
if encontrados:
    print("Alumnos encontrados:")
    for alumno in encontrados:
        print(f"{alumno['nombre']} - Notas: {alumno['notas']} - Promedio: {alumno['promedio']:.2f}")
else:
    print("No se encontraron alumnos con ese nombre")