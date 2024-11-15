# Даны положительные числа A, B, C. На прямоугольнике размера A х B размещено 
# максимально возможное количество квадратов со стороной C (без наложений). 
# Найти количество квадратов, размещенных на прямоугольнике. Операции 
# умножения и деления не использовать.

# Вводим значения сторон прямоугольника и квадрата
try:
    A = float(input("Введите длину прямоугольника A (>0): "))
    B = float(input("Введите ширину прямоугольника B (>0): "))
    C = float(input("Введите сторону квадрата C (>0): "))

    # Проверяем, что все введённые числа положительные
    if A <= 0 or B <= 0 or C <= 0:
        raise ValueError("Все значения должны быть положительными числами")

    # Инициализируем счётчики количества квадратов
    count_A = 0  # Количество квадратов по стороне A
    count_B = 0  # Количество квадратов по стороне B

    # Подсчёт количества квадратов вдоль длины A
    remaining_length = A
    while remaining_length >= C:
        count_A += 1
        remaining_length -= C  # Вычитаем сторону квадрата

    # Подсчёт количества квадратов вдоль ширины B
    remaining_width = B
    while remaining_width >= C:
        count_B += 1
        remaining_width -= C  # Вычитаем сторону квадрата

    # Общее количество квадратов — произведение количества по сторонам
    total_squares = 0
    for _ in range(count_A):
        total_squares += count_B

    print(f"Максимально возможное количество квадратов на прямоугольнике: {total_squares}")

except ValueError as ve:
    print(f"Ошибка ввода: {ve}")
except Exception as e:
    print(f"Произошла ошибка: {e}")