import keyboard
import subprocess
import sys

def on_key_press(event):
    if event.name == 'c':
        print("Tecla 'C' presionada. Abriendo Google Chrome...")
        try:
            if sys.platform == "win32":
                # Ruta por defecto para Google Chrome en Windows
                subprocess.run(["start", "chrome"], shell=True)
            elif sys.platform == "darwin":
                # Ruta por defecto para Google Chrome en macOS
                subprocess.run(["open", "-a", "Google Chrome"])
            elif sys.platform == "linux":
                # Ruta por defecto para Google Chrome en Linux
                subprocess.run(["google-chrome"])
            else:
                print("Sistema operativo no soportado.")
        except Exception as e:
            print(f"Error al intentar abrir Google Chrome: {e}")
    
    if event.name == 'f':
            print("Tecla 'F' presionada. Abriendo Mozilla Firefox...")
            try:
                
                firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
                if sys.platform == "win32":
                    subprocess.run([firefox_path])

                else:
                    print("Sistema operativo no soportado.")
            except Exception as e:
                print(f"Error al intentar abrir Mozilla Firefox: {e}")

print("Presiona la tecla 'C' para abrir Google Chrome o la tecla 'F' para abrir Mozilla Firefox. Presiona 'esc' para salir.")

# Configura el manejador para todas las teclas
keyboard.on_press(on_key_press)

# Mantén el programa en ejecución hasta que se presione 'esc'
keyboard.wait('esc')

