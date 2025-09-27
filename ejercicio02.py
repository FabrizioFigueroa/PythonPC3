def carga_alumnos():
    try:
        n = int(input("Numero de alumnos: "))
        alumnos = []
        for i in range(n):
            nombre = input(f"Nombre de alumno {i+1}: ")
            notas = []
            for j in range(3):
                while True:
                    try:
                        nota = float(input(f"Nota {j+1}: "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("La nota debe estar entre 0 y 10")
                    except:
                        print("Ingrese un numero valido")
            alumnos.append([nombre, notas])
        
        print("\n=== LISTA DE ALUMNOS ===")
        for nombre, notas in alumnos:
            print(f"{nombre}: {notas}")
    except:
        print("Error en numero de alumnos")

carga_alumnos()