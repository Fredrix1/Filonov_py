# 4.  Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).

# Задача 4: Нахождение суммы факториалов от 1 до n (n > 1).
try:
    n = int(input("\nЗадача 4: Введите число n (> 1) для подсчёта факториалов: "))
    if n <= 1:
        raise ValueError("N должно быть больше 1.")

    factorial_sum = 0  # Сумма факториалов
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i  # Вычисляем факториал
        factorial_sum += factorial

    print(f"Сумма факториалов от 1 до {n}: {factorial_sum}")

except ValueError as ve:
    print(f"Ошибка: {ve}")
