import threading
import time

# Evento para controlar el flujo de eventos
ev = threading.Event()
# Evento para indicar que debe terminar el programa
terminar_evento = threading.Event()

def genera_eventos():
    for _ in range(5):
        time.sleep(2)
        ev.set()
    # Indicar que se han generado todos los eventos y el programa debe finalizar
    terminar_evento.set()

def escribe_algo():
    while not terminar_evento.is_set():  # Verifica si debe terminar
        ev.wait()
        if terminar_evento.is_set():  # Revisión adicional para evitar imprimir al final
            break
        print("hola")
        ev.clear()
    print("Finalizando escribe_algo...")

T1 = threading.Thread(target=genera_eventos)
T2 = threading.Thread(target=escribe_algo)

T1.start()
T2.start()

T1.join()
T2.join()

print("Programa terminado.")
