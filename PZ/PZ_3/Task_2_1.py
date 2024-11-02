# Решить следующие задачи на оценку:
#  Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, в противном

# Задача 1: Ввести 2 числа и обработать их произведение

try:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))

    product = num1 * num2  # Вычисление произведения

    if product < 0:
        product *= 8  # Если произведение отрицательное, умножить на 8
    else:
        product *= 1.5  # Иначе увеличить в 1.5 раза
    print(f"Результат задачи 1: {product}")

except ValueError:
    print("Ошибка ввода: пожалуйста, введите числовые значения.")