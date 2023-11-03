import pygame
import sys

# Dimensiones de la pantalla
ANCHO = 700
ALTO = 600
BOLASIZE = 100
COLUMNA = 7
FILA = 6
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)

def crear_tablero():
    tablero = [[0 for _ in range(COLUMNA)] for _ in range(FILA)]
    return tablero

def dibujar_tablero(tablero, pantalla):
    for c in range(COLUMNA):
        for f in range(FILA):
            pygame.draw.rect(pantalla, AZUL, (c * BOLASIZE, f * BOLASIZE + BOLASIZE, BOLASIZE, BOLASIZE))
            pygame.draw.circle(pantalla, BLANCO, (int(c * BOLASIZE + BOLASIZE / 2), int(f * BOLASIZE + BOLASIZE + BOLASIZE / 2)), int(BOLASIZE / 2 - 5))

    for c in range(COLUMNA):
        for f in range(FILA):
            if tablero[f][c] == 1:
                pygame.draw.circle(pantalla, ROJO, (int(c * BOLASIZE + BOLASIZE / 2), ALTO - int(f * BOLASIZE + BOLASIZE / 2)), int(BOLASIZE / 2 - 5))
            elif tablero[f][c] == 2:
                pygame.draw.circle(pantalla, VERDE, (int(c * BOLASIZE + BOLASIZE / 2), ALTO - int(f * BOLASIZE + BOLASIZE / 2)), int(BOLASIZE / 2 - 5))

    pygame.display.update()

def drop_piece(tablero, fila, columna, pieza):
    tablero[fila][columna] = pieza

def es_valido(tablero, columna):
    return tablero[FILA - 1][columna] == 0

def obtener_fila_disponible(tablero, columna):
    for f in range(FILA):
        if tablero[f][columna] == 0:
            return f

def ganador(tablero, pieza):
    # Verificar horizontal
    for c in range(COLUMNA - 3):
        for f in range(FILA):
            if tablero[f][c] == pieza and tablero[f][c+1] == pieza and tablero[f][c+2] == pieza and tablero[f][c+3] == pieza:
                return True

    # Verificar vertical
    for c in range(COLUMNA):
        for f in range(FILA - 3):
            if tablero[f][c] == pieza and tablero[f+1][c] == pieza and tablero[f+2][c] == pieza and tablero[f+3][c] == pieza:
                return True

    # Verificar diagonal ascendente
    for c in range(COLUMNA - 3):
        for f in range(FILA - 3):
            if tablero[f][c] == pieza and tablero[f+1][c+1] == pieza and tablero[f+2][c+2] == pieza and tablero[f+3][c+3] == pieza:
                return True

    # Verificar diagonal descendente
    for c in range(COLUMNA - 3):
        for f in range(3, FILA):
            if tablero[f][c] == pieza and tablero[f-1][c+1] == pieza and tablero[f-2][c+2] == pieza and tablero[f-3][c+3] == pieza:
                return True

def main():
    pygame.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    tablero = crear_tablero()
    juego_terminado = False
    turno = 0

    pygame.display.set_caption("4 en raya")

    dibujar_tablero(tablero, pantalla)
    pygame.display.update()

    while not juego_terminado:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(pantalla, NEGRO, (0, 0, ANCHO, BOLASIZE))
                posx = event.pos[0]
                if turno == 0:
                    pygame.draw.circle(pantalla, ROJO, (posx, int(BOLASIZE / 2)), int(BOLASIZE / 2 - 5))
                else:
                    pygame.draw.circle(pantalla, VERDE, (posx, int(BOLASIZE / 2)), int(BOLASIZE / 2 - 5))

            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(pantalla, NEGRO, (0, 0, ANCHO, BOLASIZE))

                if turno == 0:
                    posx = event.pos[0]
                    columna = int(posx // BOLASIZE)

                    if es_valido(tablero, columna):
                        fila = obtener_fila_disponible(tablero, columna)
                        drop_piece(tablero, fila, columna, 1)
                        
                        if ganador(tablero, 1):
                            mensaje = pygame.font.SysFont("monospace", 75).render("Jugador 1 gana!", True, ROJO)
                            pantalla.blit(mensaje, (40, 10))
                            juego_terminado = True

                else:
                    posx = event.pos[0]
                    columna = int(posx // BOLASIZE)

                    if es_valido(tablero, columna):
                        fila = obtener_fila_disponible(tablero, columna)
                        drop_piece(tablero, fila, columna, 2)

                        if ganador(tablero, 2):
                            mensaje = pygame.font.SysFont("monospace", 75).render("Jugador 2 gana!", True, VERDE)
                            pantalla.blit(mensaje, (40, 10))
                            juego_terminado = True

                dibujar_tablero(tablero, pantalla)
                turno += 1
                turno %= 2

                if juego_terminado:
                    pygame.time.wait(3000)

if __name__ == "__main__":
    main()