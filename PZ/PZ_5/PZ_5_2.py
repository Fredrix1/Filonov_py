# Описать функцию Swap(X, Y), меняющую содержимое переменных X и Y (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными). С
# ее помощью для данных переменных A, B, C, D последовательно поменять
# содержимое следующих пар: A и B, C и D, B и C и вывести новые значения A, B, C, D.

def swap(x, y):
    """
    Функция для обмена значениями двух вещественных переменных.

    :param x: Первое вещественное число (входной и выходной параметр)
    :param y: Второе вещественное число (входной и выходной параметр)
    :return: Кортеж, содержащий новые значения x и y
    """
    return y, x  # Меняем местами значения x и y


# Ввод вещественных чисел A, B, C, D
try:
    A, B, C, D = input("Введите значение A: "), input("Введите значение B: "), \
        input("Введите значение C: "), input("Введите значение D: ")

    # Обмен значениями
    A, B = swap(A, B)  # Меняем A и B
    C, D = swap(C, D)  # Меняем C и D
    B, C = swap(B, C)  # Меняем B и C

    # Вывод новых значений
    print(f"Новые значения: A = {A}, B = {B}, C = {C}, D = {D}")

except ValueError:
    print("Ошибка ввода: Пожалуйста, введите вещественное число.")
except Exception as e:
    print(f"Произошла ошибка: {e}.")
