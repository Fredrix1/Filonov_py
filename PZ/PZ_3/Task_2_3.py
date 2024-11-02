#  Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2, в противном случае уменьшить на 2.

# Задача 3: Ввод двухзначного числа и обработка суммы его цифр

try:
    two_digit_number = int(input("Введите двухзначное число: "))

    if 10 <= two_digit_number <= 99:
        digit_sum = (two_digit_number // 10) + (two_digit_number % 10)  # Сумма цифр

        if digit_sum % 2 == 0:
            result = two_digit_number + 2  # Увеличить на 2, если сумма четная
        else:
            result = two_digit_number - 2  # Уменьшить на 2, если сумма нечетная
        print(f"Результат задачи 3: {result}")
    else:
        print("Ошибка: число не является двухзначным.")

except ValueError:
    print("Ошибка ввода: пожалуйста, введите целое число.")
