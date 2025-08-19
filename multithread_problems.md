**Пример ошибки "Состояние гонки":**

В исходном коде 10 запущенных одновременно потоков увеличивают общий счётчик 100,000 раз каждый. Это всё продолжается до достижения значения 1,000,000.
Но так как `counter++` - это не атомарная операция, которая считывает текущее значение, добавляет к нему 1 и затем обновляет значение переменной, то при параллельной работе потоков они начинают мешать друг другу, что может приводить, соответственно, к потере значений.

В результате по итогам работы кода итоговое значение будет, как правило, меньше 1,000,000 из-за потери значений ввиду состояния гонки.

Исправленный вариант с добавлением атомарности:

```java
import java.util.concurrent.atomic.AtomicInteger;

public class RaceConditionExample {

    private static AtomicInteger counter = new AtomicInteger(0);

    public static void main(String[] args) {
        int numberOfThreads = 10;
        Thread[] threads = new Thread[numberOfThreads];

        for (int i = 0; i < numberOfThreads; i++) {
            threads[i] = new Thread(() -> {
                for (int j = 0; j < 100000; j++) {
                    counter.incrementAndGet();
                }
            });
            threads[i].start();
        }

        for (int i = 0; i < numberOfThreads; i++) {
            try {
                threads[i].join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println("Final counter value: " + counter.get());
    }
}
```


 

**Пример ошибки "deadlock":**

В исходном коде инициализируются два потока `lock1` и `lock2`.
Поток `lock1` пытается получить `lock2`, в то время как `lock2` пытается получить `lock1`.
Как следствие, оба потока блокируются, ожидая освобождения блокировок друг друга, что приводит к deadlock ошибке.

Исправленный вариант с изменением порядка захвата блокировок:

```java
public class DeadlockExample {

    private static final Object lock1 = new Object();
    private static final Object lock2 = new Object();

    public static void main(String[] args) {
        Thread thread1 = new Thread(() -> {
            synchronized (lock1) {
                System.out.println("Thread 1 acquired lock1");

                try { Thread.sleep(50); } 
                catch (InterruptedException e) { e.printStackTrace(); }

                synchronized (lock2) {
                    System.out.println("Thread 1 acquired lock2");
                }
            }
        });

        Thread thread2 = new Thread(() -> {
			// Изменения: теперь оба потока захватывают блокировки в одном порядке,
			// то есть сначала захватываем lock1, а затем lock2
            synchronized (lock1) {
                System.out.println("Thread 2 acquired lock1");

                try { Thread.sleep(50); } 
                catch (InterruptedException e) { e.printStackTrace(); }

                synchronized (lock2) {
                    System.out.println("Thread 2 acquired lock2");
                }
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Finished");
    }
}
```
