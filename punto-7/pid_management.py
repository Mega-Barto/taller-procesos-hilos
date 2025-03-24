import os
import subprocess
import sys

def listar_procesos():
    print("PID\tNombre del Proceso")
    print("-" * 40)

    if sys.platform.startswith("win"):
        comando = "tasklist"
    else:
        comando = "ps -eo pid,comm"

    try:
        resultado = subprocess.run(comando, shell=True, capture_output=True, text=True, check=True)
        lineas = resultado.stdout.splitlines()[1:]  # Omitir encabezado

        for linea in lineas:
            partes = linea.split()
            if sys.platform.startswith("win"):
                pid, nombre = partes[1], partes[0]  # En Windows, el PID está en la segunda columna
            else:
                pid, nombre = partes[0], " ".join(partes[1:])  # En Unix, el nombre está después del PID

            print(f"{pid}\t{nombre}")

    except subprocess.CalledProcessError as e:
        print(f"Error al listar procesos: {e}")

def eliminar_proceso(pid):
    try:
        if sys.platform.startswith("win"):
            os.system(f"taskkill /PID {pid} /F")
        else:
            os.system(f"kill {pid}")
        print(f"Proceso {pid} terminado exitosamente.")
    except Exception as e:
        print(f"Error al intentar eliminar el proceso: {e}")

def main():
    listar_procesos()
    try:
        pid = int(input("Ingrese el PID del proceso a eliminar: "))
        eliminar_proceso(pid)
    except ValueError:
        print("Error: Ingrese un número válido de PID.")

if __name__ == "__main__":
    main()
