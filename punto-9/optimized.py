from datetime import datetime, timedelta
import time
import uuid
import random
import threading

class OrdersManager:
    def __init__(self, num_workers=10, num_orders=1_000):
        # Generación de órdenes de manera eficiente sin necesidad de métodos separados
        self.orders = [(uuid.uuid4(), x) for x in range(num_orders)]
        self.orders_processed = 0
        self.last_printed_log = datetime.now()
        self.lock = threading.Lock()  # Lock para evitar condiciones de carrera en los contadores
        self.num_workers = num_workers
        self.semaphore = threading.Semaphore(num_workers)  # Semáforo para limitar el número de hilos activos
        print(f"{datetime.now()} > {len(self.orders)} orders generated...")

    def _fake_save_on_db(self, order):
        with self.semaphore:
            time.sleep(random.uniform(0, 1))  # simula un retardo en la base de datos
            print(f"{datetime.now()} > Order [{order[0]}] {order[1]} was successfully processed.")
            
            with self.lock:  # Protege la actualización del contador
                self.orders_processed += 1
                # Se optimiza la frecuencia de logs para reducir sobrecarga innecesaria
                if datetime.now() > self.last_printed_log:
                    self.last_printed_log = datetime.now() + timedelta(seconds=5)
                    print(f"{datetime.now()} > Total orders executed: {self.orders_processed}/{len(self.orders)}")

    def process_orders(self):
        threads = []
        for order in self.orders:
            thread = threading.Thread(target=self._fake_save_on_db, args=(order,))
            threads.append(thread)
            thread.start()

        # Esperar a que todos los hilos terminen
        for t in threads:
            t.join()

if __name__ == "__main__":
    orders_manager = OrdersManager()
    start_time = time.time()
    orders_manager.process_orders()
    print(f"{datetime.now()} > Execution time: {time.time() - start_time} seconds...")
