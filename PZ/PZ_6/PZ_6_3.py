# 3. Дан список размера N. Осуществить сдвиг элементов списка вправо на одну
# позицию (при этом A1 перейдет в A2, A2 — в A3, ..., AN-1 — в AN, a исходное значение
# последнего элемента будет потеряно). Первый элемент полученного списка
# положить равным 0.

# Функция для сдвига элементов списка вправо
def shift_list_right(A):
    # Проверка, что список не пустой
    if len(A) == 0:
        raise ValueError("Список не должен быть пустым.")

    # Создаем новый список, где первый элемент равен 0
    B = [0] * len(A)  # Инициализация нового списка B нулями

    # Сдвигаем элементы списка A вправо на одну позицию
    for i in range(1, len(A)):
        B[i] = A[i - 1]

    return B


try:
    # Ввод размера списка
    N = int(input("Введите размер списка A: "))

    # Проверка на положительное значение
    if N <= 0:
        raise ValueError("Размер списка должен быть положительным.")

    # Ввод элементов списка A
    A = []
    print(f"Введите {N} целых чисел:")
    for _ in range(N):
        element = int(input())
        A.append(element)

    # Вывод исходного списка
    print("Исходный список A:", A)

    # Получаем результирующий список B
    B = shift_list_right(A)

    # Вывод результирующего списка
    print("Результирующий список B:", B)

except ValueError as ve:
    print("Ошибка:", ve)
except Exception as e:
    print("Произошла ошибка:", e)