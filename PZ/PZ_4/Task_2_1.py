#  Решить следующие задачи на оценку: 
# 1.  Ввести 4 числа. Найти и вывести на экран сумму и количество отрицательных чисел


# Задача 1: Ввод 4 чисел. Нахождение суммы и количества отрицательных чисел.
try:
    print("Задача 1: Введите 4 числа для проверки на отрицательность")
    negative_count = 0  # Счетчик отрицательных чисел
    negative_sum = 0  # Сумма отрицательных чисел

    for i in range(4):
        number = float(input(f"Введите число {i + 1}: "))
        if number < 0:
            negative_count += 1
            negative_sum += number

    print(f"Сумма отрицательных чисел: {negative_sum}")
    print(f"Количество отрицательных чисел: {negative_count}")

except ValueError:
    print("Ошибка: необходимо ввести числовое значение.")


