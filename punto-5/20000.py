import threading
import random
import time

# Lista compartida
numbers = []
lock = threading.Lock()
stop_event = threading.Event()

# Hilo para generar números aleatorios
def generate_numbers():
    while not stop_event.is_set():
        with lock:
            num = random.randint(1, 100)
            numbers.append(num)
        time.sleep(0.01)  # Simula una pausa entre inserciones

# Hilo para modificar la lista
def modify_numbers():
    index = 0
    while not stop_event.is_set():
        with lock:
            if numbers and numbers[index % len(numbers)] % 10 == 0:
                numbers[index % len(numbers)] = -1
        index += 1
        time.sleep(0.01)  # Simula una pausa entre modificaciones

# Hilo para monitorear la suma de los elementos
def monitor_sum():
    while True:
        with lock:
            total_sum = sum(numbers)
        if total_sum > 20000:
            stop_event.set()
            break
        time.sleep(0.05)  # Reduce la frecuencia de chequeo

# Crear y ejecutar hilos
thread1 = threading.Thread(target=generate_numbers)
thread2 = threading.Thread(target=modify_numbers)
thread3 = threading.Thread(target=monitor_sum)

thread1.start()
thread2.start()
thread3.start()

# Esperar la finalización del hilo de monitoreo
thread3.join()

# Asegurar que los otros hilos terminan
thread1.join()
thread2.join()

print("Lista final:", numbers)
print("Ejecución finalizada. Suma de elementos:", sum(numbers))
