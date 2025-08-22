
**Пример-1: Мьютекс**

Синхронизируем доступ к общему ресурсу (счётчику).

```python
import threading
  

class ThreadingCounter:
	def __init__(self, iterations: int, n_threads: int):
		if iterations <= 0:
			raise ValueError("It must be at least 1 iteration")
		self.iterations = iterations
		self.threads = [
			threading.Thread(target=self._increase, name=f"Thread-{i}")
			for i in range(n_threads)
		]
		self.lock = threading.Lock()
		self.counter = 0
		
	def _increase(self) -> None:
		for i in range(self.iterations):
			with self.lock:
				self.counter += 1
				
	def _clear(self) -> None:
		self.counter = 0
		
	def run(self) -> None:
		if self.counter != 0:
			self._clear()
		for t in self.threads:
			t.start() 
		for t in self.threads:
			t.join()
			
	def get_counter_value(self) -> int:
		return self.counter

  
def main():
	iterations = 5
	n_threads = 10
	
	threading_counter = ThreadingCounter(iterations, n_threads)
	threading_counter.run()
	print(threading_counter.get_counter_value())  
```


**Пример-2: Семафор**

Ограничим количество потоков, одновременно работающих с ресурсом (на примере доступа к БД).

```python
import time
import random
import threading


class DatabaseConnectionPool:
    def __init__(self, max_connections: int = 3):
        self.semaphore = threading.Semaphore(max_connections)

    def connect(self) -> None:
        with self.semaphore:
            thread_name = threading.current_thread().name
            # Имитируем работу с БД
            print(f"[{thread_name}] Подключение к БД...")
            work_time = random.uniform(1, 15)
            time.sleep(work_time)
            print(f"Подключение завершено: [{thread_name}]")
            print(f"Время работы: {work_time} секунд")


def worker(pool: DatabaseConnectionPool):
    pool.connect()


def main():
	max_connections = 3
	n_threads = 8

	pool = DatabaseConnectionPool(max_connections=max_connections)
	threads = [
		threading.Thread(target=worker, args=(pool,), name=f"Клиент-{i}") 
		for i in range(n_threads)
	]
	for t in threads:
        t.start()
    for t in threads:
        t.join()

	print("Все подключения к БД завершены")
	print("Общее кол-во подключений:", n_threads)

```


**Пример-3: Барьеры**

```python
import time
import threading

N_THREADS = 5

barrier = threading.Barrier(N_THREADS)

def worker():
    print(f"{threading.current_thread().name} находится в ожидании в барьере")
    barrier.wait()
    print(f"{threading.current_thread().name} поток прошёл через барьер")


def main():
	threads = [
		threading.Thread(target=worker, name=f"Thread-{i}") 
		for i in range(N_THREADS)
	]
	for t in threads:
	    t.start()
	for t in threads:
	    t.join()

```


**Пример-4: Фьючерсы**

```python
import time
import math
import random
from concurrent.futures import ThreadPoolExecutor, as_completed


def product_of_two_numbers(value_1: int, value_2: int) -> int:
	return value_1 * value_2


def parallel_product_of_two_numbers(n_workers: int, values_pairs_list: list):
	with ThreadPoolExecutor(max_workers=n_workers) as executor:
		futures_results = []
        for i, (value_1, value_2) in enumerate(values_pairs_list):
	        future = executor.submit(
		        product_of_two_numbers, value_1, value_2
            )
            futures_results.append(future.result())
        print("Сумма попарного произведения:", sum(futures_results))
	return sum(futures_results)


def main():
	n_workers = 3
	values_pairs_list = [(4, 9), (33, 2), (80, 5), (12, 69), (0, 11), (6, 209)]
	parallel_product_of_two_numbers(n_workers, values_pairs_list)

```


**Пример-5: Events**

```python
import time
import threading

calculation_complete_event = threading.Event()
result = 0


def calculator():
    global result
    for i in range(1, 1000):
        result += i
    calculation_complete_event.set()


def reporter():
    calculation_complete_event.wait()


calculator_thread = threading.Thread(target=calculator)
reporter_thread = threading.Thread(target=reporter)
reporter_thread.start()
calculator_thread.start()
reporter_thread.join()
calculator_thread.join()
```

