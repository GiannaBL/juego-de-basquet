import random

def jugar_tiro():
    """Simula un tiro al aro y actualiza la puntuación."""
    es_exitoso = random.choice([True, False, False])

    if es_exitoso:
        print("¡Enceeeeeestó! Se suman 10 puntos.")
        return 10
    else:
        print("¡Falló! Se restan 2 puntos.")
        return -2

def juego_basquet_infantil():
    """Función principal del juego de baloncesto."""
    puntuacion_actual = 0
    print("¡Bienvenido al juego de baloncesto! El objetivo es encestar la pelota.")
    
    jugar = True
    while jugar:
        print(f"Puntuación actual: {puntuacion_actual}")
        input("Presiona Enter para lanzar la pelota...")
        
        puntuacion_cambio = jugar_tiro()
        puntuacion_actual += puntuacion_cambio
        
        continuar = input("¿Quieres lanzar de nuevo? (s/n): ").lower()
        if continuar != 's':
            jugar = False
    
    print("\n--- ¡Juego terminado! ---")
    print(f"Puntuación final: {puntuacion_actual}")

# Inicia el juego
juego_basquet_infantil()