def calcular_combustible():
    while True:
        try:
            fraccion = input("Ingrese la fraccion (X/Y): ")
            
            if '/' not in fraccion:
                raise ValueError("Formato invalido, Use X/Y")
            
            partes = fraccion.split('/')
            if len(partes) != 2:
                raise ValueError("Formato invalido, Use X/Y")
            
            x = int(partes[0])
            y = int(partes[1])
            
            if y == 0:
                raise ZeroDivisionError("El denominador no puede ser 0")
            
            if x > y:
                print("X debe ser menor o igual a Y, intente nuevamente.")
                continue
            
            if x < 0:
                print("X debe ser un numero positivo, intente nuevamente.")
                continue
            
            porcentaje = (x / y) * 100
            
            if porcentaje <= 1:
                return "E"
            elif porcentaje >= 99:
                return "F"
            else:
                return f"{round(porcentaje)}%"
                
        except ValueError:
            print("Error: Solo se permiten numeros enteros, intente nuevamente.")
        except ZeroDivisionError:
            print("Error: Division por cero no permitida, intente nuevamente.")

def main():
    print("=== INDICADOR DE COMBUSTIBLE ===")
    print("Ingrese una fracción X/Y para calcular el porcentaje de combustible")
    print("Casos especiales:")
    print("- E: cuando X/Y ≤ 1%")
    print("- F: cuando X/Y ≥ 99%")
    print("- Porcentaje redondeado en otros casos\n")
    
    resultado = calcular_combustible()
    print(f"Resultado: {resultado}")

if __name__ == "__main__":
    main()