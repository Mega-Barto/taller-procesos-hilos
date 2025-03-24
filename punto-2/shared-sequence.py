import threading

def generar_secuencia(n1, n2):
    if n1 < n2:
        secuencia = list(range(n1, n2 + 1))
        print(f"Secuencia compartida: {secuencia}")

# Definir los números
n1 = 3
n2 = 10

# Crear un hilo
hilo = threading.Thread(target=generar_secuencia, args=(n1, n2))
hilo.start()

# Mientras el hilo secundario trabaja, el hilo principal muestra la resta
print(f"Resultado de la resta: {n2 - n1}")

# Esperar a que el hilo secundario termine
hilo.join()
