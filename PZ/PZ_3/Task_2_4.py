#  Дано целое число. Если оно является положительным, то прибавить к нему 20, в
# противном случае вычесть из него 5.

# Задача 4: Ввод целого числа и выполнение условий

try:
    integer_number = int(input("Введите целое число: "))

    if integer_number > 0:
        result = integer_number + 20  # Если положительное, прибавить 20
    else:
        result = integer_number - 5  # В противном случае вычесть 5
    print(f"Результат: {result}")

except ValueError:
    print("Ошибка ввода: пожалуйста, введите целое число.")