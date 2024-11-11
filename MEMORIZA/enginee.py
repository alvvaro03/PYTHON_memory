import random
emojis = {1:"😀",2:"🥰",3:"😨",4:"🥶",5:"🦍",6:"👾",7:"🐲",8:"😡",9:"🦘",10:"🐳",11:"🐼",12:"🐺",13:"🦃",14:"🤢",15:"😎"}

#Método para iniciar el tablero
def Inicio(colums, filas):
    tabla = colums * filas
    #No deja hacer tableros con un numero de celdas impares
    if(tabla % 2 != 0):
        print("No puede ser impar")
        Inicio()

    if(tabla > 30):
        print("El máximo número de celdas es 30, por favor cambie su elección")
        Inicio()
        
    #Random emojis
    cantidad_parejas = tabla // 2
    tablero_emojis = random.sample(list(emojis.values()), cantidad_parejas) * 2
    random.shuffle(tablero_emojis)

    tablero = []
    for i in range(filas):
        fila = []
        for j in range(colums):
            fila.append(tablero_emojis.pop())
        tablero.append(fila)

    tablero_vacio = []
    for _ in range(filas):
        fila = ["-"] * colums
        tablero_vacio.append(fila)
    return tablero_vacio, tablero

def Inicio_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# Método para que el jugador seleccione las celdas para jugar.
def seleccionar_celda(filas, columnas):
    while True:
            fila = int(input("Selecciona la fila: "))-1
            columna = int(input("Selecciona la columna: "))-1
            if 0 <= fila < filas and 0 <= columna < columnas:
                return fila, columna
            else:
                print("Coordenadas fuera de rango.")
def Modos_juego():
    while True:
        print("Dime que modo de juego quieres elegir: ", "\n1. Jugador 1 VS Jugador 2", "\n2. Jugador 1 VS CPU", "\n3. CPU VS CPU")
        usuario = int(input("Elige el modo de juego "))
        if(usuario == 1):
            colums = int(input("Dime cuantas columnas quieres para el tablero "))
            filas = int(input("Dime cuantas filas quieres para el tablero "))
            persona_vs_persona(colums, filas)
        elif(usuario == 2):
            colums = int(input("Dime cuantas columnas quieres para el tablero "))
            filas = int(input("Dime cuantas filas quieres para el tablero "))
            persona_vs_maquina(colums, filas)
        elif(usuario == 3):
            colums = int(input("Dime cuantas columnas quieres para el tablero "))
            filas = int(input("Dime cuantas filas quieres para el tablero "))
            maquina_vs_maquina(colums, filas)
        else:
            print("No existe ese modo de juego")
            Modos_juego()

def persona_vs_persona(colums, filas):
    tablero_vacio, tablero = Inicio(colums, filas)
    puntos_jugador1 = 0
    puntos_jugador2 = 0
    turno = True

    while True:
        print("\nTablero actual:")
        Inicio_tablero(tablero_vacio)
        
        if turno:
            jugador_actual = "Jugador 1"
        else:
            jugador_actual = "Jugador 2"
        print("\n" + jugador_actual + ", es tu turno.")

        fila1, col1 = seleccionar_celda(filas, colums)
        fila2, col2 = seleccionar_celda(filas, colums)

        while (fila1, col1) == (fila2, col2):
            print("No puedes elegir la misma celda, repite porfa.")
            fila2, col2 = seleccionar_celda(filas, colums)

        # Para ver las celdas que ha seleccionado el usuario
        tablero_vacio[fila1][col1] = tablero[fila1][col1]
        tablero_vacio[fila2][col2] = tablero[fila2][col2]
        Inicio_tablero(tablero_vacio)

        # Comprobar si las cartas coinciden
        if tablero[fila1][col1] == tablero[fila2][col2]:
            print(f"¡{jugador_actual} ha encontrado una pareja!")
        else:
            print("No coinciden, cambio de turno.")
            tablero_vacio[fila1][col1] = "-"
            tablero_vacio[fila2][col2] = "-"
            turno = not turno
            
        #Comprueba si la partida ha acabado
        juego_terminado = True 
        for f in tablero_vacio:
            for c in f:
                if c == "-":
                    juego_terminado = False
                    break
            if not juego_terminado:
                break
        if juego_terminado:
            print("\n¡El juego ha terminado!")
            break

def persona_vs_maquina(colums, filas):
    tablero_vacio, tablero = Inicio(colums, filas)
    memoria_maquina = {}
    turno_jugador = True

    while True:
        print("\nTablero actual:")
        Inicio_tablero(tablero_vacio)

        if turno_jugador:
            print("\nTurno del Jugador.")
            fila1, col1 = seleccionar_celda(filas, colums)
            fila2, col2 = seleccionar_celda(filas, colums)

            while (fila1, col1) == (fila2, col2):
                print("No puedes elegir la misma celda, repite porfa.")
                fila2, col2 = seleccionar_celda(filas, colums)

            tablero_vacio[fila1][col1] = tablero[fila1][col1]
            tablero_vacio[fila2][col2] = tablero[fila2][col2]
            Inicio_tablero(tablero_vacio)

            if tablero[fila1][col1] == tablero[fila2][col2]:
                print("¡Jugador ha encontrado una pareja!")
            else:
                print("No coinciden, cambio de turno.")
                tablero_vacio[fila1][col1] = "-"
                tablero_vacio[fila2][col2] = "-"
                turno_jugador = not turno_jugador 
        else:
            print("\nTurno de la Máquina.")
            pareja_encontrada = False
            ubicaciones_por_valor = {}

            # Agrupa las posiciones de las cartas por su valor
            for (fila, col), valor in memoria_maquina.items():
                if valor not in ubicaciones_por_valor:
                    ubicaciones_por_valor[valor] = []
                ubicaciones_por_valor[valor].append((fila, col))

            # Busca si existe alguna pareja en las agrupaciones
            for posiciones in ubicaciones_por_valor.values():
                if len(posiciones) >= 2:  # Si hay al menos dos posiciones con el mismo valor
                    fila1, col1 = posiciones[0]
                    fila2, col2 = posiciones[1]
                    pareja_encontrada = True
                    break

            if pareja_encontrada:
                print(f"La máquina recuerda una pareja en las posiciones ({fila1+1},{col1+1}) y ({fila2+1},{col2+1}).")
                tablero_vacio[fila1][col1] = tablero[fila1][col1]
                tablero_vacio[fila2][col2] = tablero[fila2][col2]
                Inicio_tablero(tablero_vacio)

                print("¡La máquina ha encontrado una pareja!")
                # Continua el bucle para que la máquina siga jugando
                continue  
            else:
                # Si no encuentra pareja conocida, elige celdas aleatorias que no haya descubierto
                desconocidas = []
                for f in range(filas):
                    for c in range(colums):
                        if tablero_vacio[f][c] == "-":
                            desconocidas.append((f, c))

                if len(desconocidas) < 2:
                    print("El juego ha terminado, ha ganado la CPU.")
                    break

                fila1, col1 = random.choice(desconocidas)
                desconocidas.remove((fila1, col1))
                fila2, col2 = random.choice(desconocidas)

                print(f"La máquina selecciona posiciones al azar: ({fila1+1},{col1+1}) y ({fila2+1},{col2+1}).")
                tablero_vacio[fila1][col1] = tablero[fila1][col1]
                tablero_vacio[fila2][col2] = tablero[fila2][col2]
                Inicio_tablero(tablero_vacio)

                if tablero[fila1][col1] == tablero[fila2][col2]:
                    print("¡La máquina ha encontrado una pareja!")
                    # Continua el bucle para que la máquina siga jugando
                    continue  
                else:
                    print("No coinciden, cambio de turno.")
                    tablero_vacio[fila1][col1] = "-"
                    tablero_vacio[fila2][col2] = "-"
                    #Cambio de turno
                    turno_jugador = True 

                # Actualiza la memoria de la máquina
                memoria_maquina[(fila1, col1)] = tablero[fila1][col1]
                memoria_maquina[(fila2, col2)] = tablero[fila2][col2]

        # Comprueba si la partida ha acabado
        juego_terminado = True
        for f in tablero_vacio:
            for c in f:
                if c == "-":
                    juego_terminado = False
                    break
            if not juego_terminado:
                break

        if juego_terminado:
            print("\n¡El juego ha terminado!")
            break  
    input()

def maquina_vs_maquina(colums, filas):
    tablero_vacio, tablero = Inicio(colums, filas)
    memoria_maquina1 = {}
    memoria_maquina2 = {}
    turno_maquina1 = True
    parejas_maquina1 = 0
    parejas_maquina2 = 0

    while True:
        print("\nTablero actual:")
        Inicio_tablero(tablero_vacio)

        if turno_maquina1:
            print("\nTurno de la Máquina 1.")
            memoria_actual = memoria_maquina1
            parejas_actual = parejas_maquina1
        else:
            print("\nTurno de la Máquina 2.")
            memoria_actual = memoria_maquina2
            parejas_actual = parejas_maquina2

        
Modos_juego()