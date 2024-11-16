# 5.  Ввести N чисел. Найти и вывести их среднее арифметическое.

# Задача 5: Ввод N чисел. Нахождение их среднего арифметического.
try:
    N = int(input("\nЗадача 5: Введите количество чисел N: "))
    if N <= 0:
        raise ValueError("N должно быть положительным числом.")

    total_sum = 0  # Сумма чисел
    for i in range(N):
        number = float(input(f"Введите число {i + 1}: "))
        total_sum += number

    average = total_sum / N
    print(f"Среднее арифметическое {N} чисел: {average}")

except ValueError as ve:
    print(f"Ошибка: {ve}")

