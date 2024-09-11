import random
import os

# Nombre del archivo donde se guardará el puntaje
archivo_puntaje = 'puntaje.txt'

def cargar_puntaje():
    """Cargar el puntaje desde el archivo, si existe."""
    if os.path.exists(archivo_puntaje):
        with open(archivo_puntaje, 'r') as archivo:
            try:
                return int(archivo.read())
            except ValueError:
                return 0
    return 0

def guardar_puntaje(puntaje):
    """Guardar el puntaje en el archivo."""
    with open(archivo_puntaje, 'w') as archivo:
        archivo.write(str(puntaje))

def mostrar_tienda(puntaje, objetos):
    """Mostrar el menú de la tienda y permitir compras."""
    print("\n--- TIENDA ---")
    for objeto, (precio, _) in objetos.items():
        print(f"{objeto}: {precio} puntos")
    
    eleccion = input("\n¿Qué te gustaría comprar? (Escribe el nombre del objeto o 'salir' para regresar): ").lower()
    
    if eleccion == 'salir':
        return None, puntaje

    if eleccion in objetos:
        precio, efecto = objetos[eleccion]
        if puntaje >= precio:
            puntaje -= precio
            print(f"¡Has comprado {eleccion}!")
            guardar_puntaje(puntaje)  # Guardar el puntaje después de la compra
            print(f"Puntaje actual: {puntaje}")  # Mostrar puntaje actualizado
            return efecto, puntaje
        else:
            print("No tienes suficientes puntos para comprar esto.")
    else:
        print("Objeto no válido.")
    
    return None, puntaje

def jugar_piedra_papel_tijera(efecto):
    opciones = ['piedra', 'papel', 'tijera']
    puntaje = cargar_puntaje()  # Cargar el puntaje inicial
    
    tiene_espada = (efecto == 'espada')
    usado_espada = False
    
    while True:
        print(f"\nPuntaje actual: {puntaje}")
        
        eleccion_usuario = input("Elige piedra, papel o tijera: ").lower()
        
        if eleccion_usuario not in opciones:
            print("Opción no válida. Por favor elige entre piedra, papel o tijera.")
            continue

        eleccion_computadora = random.choice(opciones)
        print(f"La computadora eligió: {eleccion_computadora}")

        if eleccion_usuario == eleccion_computadora:
            print("¡Es un empate!")
        elif (eleccion_usuario == 'piedra' and eleccion_computadora == 'tijera') or \
             (eleccion_usuario == 'papel' and eleccion_computadora == 'piedra') or \
             (eleccion_usuario == 'tijera' and eleccion_computadora == 'papel'):
            print("¡Ganaste!")
            puntaje += 100
            if efecto == 'pocion':
               print("La pocion duplico tus puntos.")
               puntaje += 100
        else:
            print("Perdiste.")
            if efecto == 'escudo':
               print("tienes escudo, no pierdes puntos")
               puntaje += 40
            if tiene_espada and not usado_espada:
                print("¡Pero tienes una espada! No pierdes puntos y tienes otro intento.")
                usado_espada = True
                continue  # Volver a intentar sin restar puntos
            else:
                puntaje -= 40  # Restar puntos si no tienes espada

        guardar_puntaje(puntaje)
        print(f"Puntaje actualizado: {puntaje}")  # Mostrar puntaje actualizado

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_de_nuevo != 'si':
            break

    return puntaje

def mostrar_puntaje():
    """Mostrar el puntaje actual."""
    puntaje = cargar_puntaje()
    print(f"Puntaje actual: {puntaje}")

def menu_principal():
    """Mostrar el menú principal y manejar la navegación."""
    objetos = {
        'espada': (300, 'espada'),      # La espada da un segundo intento sin perder puntos
        'escudo': (200, 'escudo'),      # El escudo previene la pérdida de puntos
        'pocion': (100, 'pocion')       # La poción podría restaurar puntos o tener otros efectos
    }

    efecto = None

    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Jugar Piedra, Papel o Tijera")
        print("2. Ir a la tienda")
        print("3. Mostrar puntaje")
        print("4. Salir")

        eleccion_menu = input("Elige una opción (1, 2, 3, 4): ")

        if eleccion_menu == '1':
            puntaje = jugar_piedra_papel_tijera(efecto)
            print(f"\nPuntaje final de la sesión: {puntaje}")

        elif eleccion_menu == '2':
            puntaje = cargar_puntaje()
            nuevo_efecto, puntaje = mostrar_tienda(puntaje, objetos)
            if nuevo_efecto:
                efecto = nuevo_efecto
                if efecto == 'espada':
                    print("¡Ahora tienes una espada! Puedes usarla para evitar perder puntos en una ronda.")
            guardar_puntaje(puntaje)  # Guardar el puntaje después de la compra

        elif eleccion_menu == '3':
            mostrar_puntaje()

        elif eleccion_menu == '4':
            puntaje = cargar_puntaje()
            print(f"¡Gracias por jugar! Tu puntaje final es: {puntaje}")
            break

        else:
            print("Opción no válida. Por favor elige 1, 2, 3 o 4.")

# Ejecutar el menú principal
menu_principal()
