# 6.  Ввести N чисел. Посчитать и вывести количество чисел равных нулю.

# Задача 6: Ввод N чисел. Подсчет количества чисел, равных нулю.
try:
    N = int(input("\nЗадача 6: Введите количество чисел N: "))
    if N <= 0:
        raise ValueError("N должно быть положительным числом.")

    zero_count = 0  # Счетчик нулей
    for i in range(N):
        number = float(input(f"Введите число {i + 1}: "))
        if number == 0:
            zero_count += 1

    print(f"Количество чисел, равных нулю: {zero_count}")

except ValueError as ve:
    print(f"Ошибка: {ve}")

