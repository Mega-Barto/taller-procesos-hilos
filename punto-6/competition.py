import threading
import random

def sumar_numeros(thread_id, resultados):

    suma = 0

    print(f"Hilo {thread_id}: sumando...")

    for _ in range(1, 101): # Hecho así para que ver el progreso de los hilos
        print(f"Hilo {thread_id}: suma parcial #{_} = {suma}")
        suma += random.randint(1, 1000)
    resultados[thread_id] = suma
    print(f"Hilo {thread_id}: suma total = {suma}")

if __name__ == "__main__":
    num_hilos = 10
    resultados = {}  # Diccionario para almacenar los resultados de cada hilo
    hilos = []
    
    for i in range(1, num_hilos + 1):
        hilo = threading.Thread(target=sumar_numeros, args=(i, resultados))
        hilos.append(hilo)
        hilo.start()
    
    for hilo in hilos:
        hilo.join()
    
    # Determinar el hilo ganador
    hilo_ganador = max(resultados, key=resultados.get)
    print(f"El hilo ganador es el {hilo_ganador} con una suma de {resultados[hilo_ganador]}")
