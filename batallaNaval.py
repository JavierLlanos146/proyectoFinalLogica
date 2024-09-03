import random

def crearTablero(dimension):
    return [["~" for _ in range(dimension)] for _ in range(dimension)]

def mostrarTableros(tablerosDisparosJugador, tableroDisparosOponente):
    print("\n Tablero de disparos: ")
    for fila in tablerosDisparosJugador:
        print(" ".join(fila))
    print("\n Tablero de disparo de oponente: ")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))
    
def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"Colocando {barco ['nombre']} de tamaño {barco['dimension']}")
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                orientacion = input("Ingrese la orientacion (H para horizontal, V para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero)-1)
                columna = random.randint(0, len(tablero)-1)
                orientacion = random.choice(['h', 'v']) # random.choice es para decir: eliga de manera aletoria entre....
            
            if validarColocacion(tablero, fila, columna, barco['dimension'], orientacion):
                colocarBarco(tablero, fila, columna, barco['dimension'], orientacion)
                colocado=True
            elif jugador == "jugador":
                print("Colocacion es invalida. Intente de nuevo")

def validarColocacion(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        if columna + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila][columna+i] != "~":  #lo que hace el +i es hacer que solo se mueva la columna
                return False
    else:
        if fila + dimension > len(tablero):
            return False
        for i in range(dimension):
            if tablero[fila+i][columna] != "~":  #Lo que hace el +i es hacer que solo se mueva la fila 
                return False
    return True

def colocarBarco (tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        for i in range(dimension):
            tablero[fila][columna+i]="B"
    else:
        for i in range(dimension):
            tablero[fila+i][columna]="B"

def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"
        return "Impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] = "O"
        return "Agua"
    return "Ya disparaste aqui"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True

def jugarContraComputadora():
    dimension = 5
    tableroJugador = crearTablero(dimension)
    tableroComputadora = crearTablero(dimension)
    tableroDisparoJugador = crearTablero(dimension)
    tableroDisparoComputadora = crearTablero(dimension)
    barcos = [
        {"nombre":"PortaAviones", "dimension":3},
        {"nombre":"Submarino", "dimension":2}
    ]
    print("Coloca tus barcos")
    colocarBarcos(tableroJugador, barcos, "jugador")
    colocarBarcos(tableroComputadora, barcos, "computadora")
    turnoJugador=True
    while True:
        if turnoJugador: 
            print("\n Tu turno")
            mostrarTableros(tableroDisparoJugador, tableroDisparoComputadora)
            fila = int(input("Ingresa la fila de disparo: "))
            columna = int(input("Ingresa la columna de disparo: "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparoJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("Ganaste")
                return "Jugador"
        else:
            print("\n Turno de la computadora")
            fila = random.randint(0, dimension-1)
            columna = random.randint(0, dimension-1)
            resultado = realizarDisparo(tableroJugador, tableroDisparoComputadora, fila, columna)
            print(f"La computadora disparo en ({fila}, {columna}): {resultado} ")
            if verificarVictoria(tableroJugador):
                print("La computadora gano ")
                return "Computadora"
        turnoJugador = not turnoJugador

def jugarDosJugadores():
    dimension = 5
    tableroJugador1 = crearTablero(dimension)
    tableroJugador2 = crearTablero(dimension)
    tableroDisparoJugador1 = crearTablero(dimension)
    tableroDisparoJugador2 = crearTablero(dimension)
    barcos = [
        {"nombre":"PortaAviones", "dimension":3},
        {"nombre":"Submarino", "dimension":2}
    ]
    print("Jugador 1 coloca tus barcos")
    colocarBarcos(tableroJugador1, barcos, "jugador")
    print("Jugador 2 coloca tus barcos")
    colocarBarcos(tableroJugador2, barcos, "jugador")
    turnoJugador1=True
    while True:
        if turnoJugador1: 
            print("\n Tu turno")
            mostrarTableros(tableroDisparoJugador1, tableroDisparoJugador2)
            fila = int(input("Ingresa la fila de disparo: "))
            columna = int(input("Ingresa la columna de disparo: "))
            resultado = realizarDisparo(tableroJugador2, tableroDisparoJugador1, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("Jugador 1, Ganaste!!")
                return "Jugador 1"
        else:
            print("\n Turno del Jugador 2")
            mostrarTableros(tableroDisparoJugador2, tableroDisparoJugador1)
            fila = int(input("Ingresa la fila de disparo: "))
            columna = int(input("Ingresa la columna de disparo: "))
            resultado = realizarDisparo(tableroJugador1, tableroDisparoJugador2, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador1):
                print("Jugador 2, Ganaste!!! ")
                return "Jugador 2"
        turnoJugador1 = not turnoJugador1
def mostrarMenu():
    print("Bienvenido a Batalla Naval!!!")
    print("Selecciona contra quien jugaras ")
    print("1. Contra Computadora")
    print("2. Contra otro Jugador")
    print("3. Salir")
    
def iniciarJuego():
    while True:
        mostrarMenu()
        modo = input("Elige una opcion: ")
        if modo == "1":
            ganador = jugarContraComputadora()
        elif modo == "2":
            ganador = jugarDosJugadores()
        elif modo == "3":
            print("Gracias por jugar con pio pio")
            break
        else:
            print("Opcion invalida, por favor elija una opcion valida")
            continue
        print(f"El ganador es {ganador}")
        jugarDeNuevo = input("Quieres jugar de nuevo? (s/n): ").lower()
        if jugarDeNuevo !="s":
            print("Gracias por jugar, Hasta la vista Baby!!!")
            break

iniciarJuego()
            
          
                    