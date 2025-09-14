Реализация классического алгоритма быстрой сортировки с использованием рекурсии.
(в качестве `pivot` берём первый элемент массива):

```python
def quick_sort(array: list) -> list:
	if len(array) <= 1:
        return array
	pivot = array[0]
	left = []
	right = []
	for x in array[1:]:
		if x < pivot:
			left.append(x)
		else:
			right.append(x)
	return quick_sort(left) + [pivot] + quick_sort(right)
```

Докажем корректность данного алгоритма с помощью троек Хоара.

**Предусловия и постусловия для основного цикла:**

`{P: array True}` (т.е. любой произвольный массив)
`quick_sort(array)` 
`{Q: result = array[0] <= array[1] <= ... <= array[n-1] <= array[n]` (где `n` - последний элемент массива)

Так как используется функциональная реализация на основе одной единственной функции `quick_sort(array)`, то рассмотрим доказательство для основного цикла.

**Базовый случай:** 
Если длина `array <= 1`, то возвращаем исходный `array`.

**Рекурсия:**
- Выбираем `pivot = array[0]`.
- Разбиваем `array[1:]` на два списка:
    - `left` — все элементы меньше `pivot`.
    - `right` — все элементы больше или равны `pivot`

```text
{P: array True}
    left = [x ∈ array[1:] | x < pivot]
    right = [x ∈ array[1:] | x ≥ pivot]
{left и right — подмножества элементов array без pivot}
```

Рекурсивно сортируем `left` и `right`.

```text
{left — помножество array}
    left_sorted = quick_sort(left)
{left_sorted — это отсортированная версия left}

{right — подмножество array}
    right_sorted = quick_sort(right)
{right_sorted — это отсортированная версия right}
```

Объединяем результат для элементов, отсортированных по следующему правилу:
- Все элементы в `sorted_left` < pivot
- `pivot` стоит на своём месте
- Все элементы в `sorted_right` ≥ pivot

```text
left_sorted + [pivot] + right_sorted
```

Таким образом, весь список является отсортированным, что соответствует постусловию.


