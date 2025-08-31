Упрощённая версия исходного кода:

- Использован `AtomicInteger` для потокобезопасной обработки (этот подход более читабельный)
- Избавился от магического числа -> создана константа `MAX_POSSIBLE_RANDOM_VALUE`

```java
import java.util.Random;
import java.util.concurrent.atomic.AtomicInteger;

public class SimpleMultiThreadProcessing {
    private static final int SIZE = 1000000;
    private static final int THREADS = 4;
    private static final int MAX_POSSIBLE_RANDOM_VALUE = 100;
    private static final int[] data = new int[SIZE];
    private static volatile int sumOfValues = 0;

    public static void main(String[] args) throws InterruptedException {
        Random random = new Random();
        for (int i = 0; i < SIZE; i++) {
            data[i] = random.nextInt(MAX_POSSIBLE_RANDOM_VALUE);
        }
        
        AtomicInteger sum = new AtomicInteger(0);
        Thread[] threads = new Thread[THREADS];
        int chunk = SIZE / THREADS;
        
        for (int i = 0; i < THREADS; i++) {
            final int start = i * chunk;
            final int end = (i + 1) * chunk;
            
            threads[i] = new Thread(() -> {
                for (int j = start; j < end; j++) {
                    sumOfValues += data[j];
                }
            });
            threads[i].start();
        }
        
        for (Thread t : threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
        
        System.out.println("Сумма: " + sumOfValues);
    }
}

```
