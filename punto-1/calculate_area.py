import threading

def area_triangulo(base, altura, resultado, index):
    resultado[index] = (base * altura) / 2

def area_rectangulo(base, altura, resultado, index):
    resultado[index] = base * altura

def calcular_area_total():
    resultado = [0, 0, 0, 0]  # Almacenará los resultados de cada hilo
    
    # Definir dimensiones de cada sección
    base_triangulo1, altura_triangulo1 = 10, 12
    base_rectangulo1, altura_rectangulo1 = 8, 12
    base_rectangulo2, altura_rectangulo2 = 6, 5
    base_triangulo2, altura_triangulo2 = 2, 5
    
    # Crear hilos
    t1 = threading.Thread(target=area_triangulo, args=(base_triangulo1, altura_triangulo1, resultado, 0))
    t2 = threading.Thread(target=area_rectangulo, args=(base_rectangulo1, altura_rectangulo1, resultado, 1))
    t3 = threading.Thread(target=area_rectangulo, args=(base_rectangulo2, altura_rectangulo2, resultado, 2))
    t4 = threading.Thread(target=area_triangulo, args=(base_triangulo2, altura_triangulo2, resultado, 3))
    
    # Iniciar hilos
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    
    # Esperar a que los hilos terminen
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    
    # Calcular área total
    area_total = sum(resultado)
    print(f"El área total de la figura es: {area_total} m²")

if __name__ == "__main__":
    calcular_area_total()
