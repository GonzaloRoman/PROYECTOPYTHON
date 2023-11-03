# Juego de 4 en Raya de Gonzalo Román Palazón
Diseñado por Gonzalo Román Palazón 2º ASIR IES FRANCISCO ROMERO VARGAS

El juego "4 en raya" es un juego de estrategia para dos jugadores en un tablero vertical de 7 columnas y 6 filas. El objetivo del juego es ser el primero en formar una línea de cuatro fichas del mismo color, ya sea horizontal, vertical o diagonalmente.

## Reglas del Juego

- **Jugadores:** Dos jugadores, uno con fichas rojas y otro con fichas verdes.
- **Tablero:** Un tablero de 7 columnas y 6 filas.
- **Turnos:** Los jugadores colocan una ficha por turno en una columna vacía. Las fichas caen hasta el punto más bajo posible en la columna seleccionada.
- **Victoria:** El jugador que logre alinear cuatro de sus fichas en línea, ya sea horizontal, vertical o diagonal, gana la partida.

## Código Python del Juego

El juego de 4 en raya ha sido implementado en Python utilizando la biblioteca Pygame. Aquí está una descripción general del código:

- **Funciones:**
  - `crear_tablero()`: Crea un tablero vacío.
  - `dibujar_tablero()`: Dibuja el tablero y las fichas de los jugadores.
  - `drop_piece()`: Coloca una ficha en el tablero.
  - `es_valido()`: Verifica si una columna está disponible para colocar una ficha.
  - `obtener_fila_disponible()`: Obtiene la fila disponible para colocar una ficha en una columna.
  - `ganador()`: Verifica si hay un ganador en el tablero.

- **Ejecución del Juego:**
  - El juego se ejecuta en un bucle mientras los jugadores alternan turnos para colocar fichas en el tablero.
  - Se detecta si un jugador ha ganado o si se ha alcanzado un empate.

## Código Personalizado

El código Python proporcionado permite jugar 4 en raya en una interfaz gráfica básica. Se ha modificado el color de las fichas del "Jugador 2" para que sean verdes. Este cambio se realiza en la función `dibujar_tablero()`, donde se usa el color VERDE en lugar del color NEGRO para las fichas del "Jugador 2" ya que las probé con las fichas negras y no se lograba ver en que columna caía.