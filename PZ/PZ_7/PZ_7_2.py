# Дана строка, содержащая по крайней мере один символ пробела. Вывести подстроку,
# расположенную между первым и вторым пробелом исходной строки. Если строка
# содержит только один пробел, то вывести пустую строку.

def substring_between_spaces(S):
    """
    Извлекает подстроку между первым и вторым пробелом в строке S.

    :param S: строка, содержащая хотя бы один пробел.
    :return: подстрока между первым и вторым пробелом, или пустая строка, если пробелов меньше двух.
    """
    try:
        # Проверяем, что S — строка
        if not isinstance(S, str):
            raise ValueError("Входные данные должны быть строкой.")

        # Находим индекс первого пробела
        first_space = S.find(' ')

        # Если нет пробела, выбрасываем исключение
        if first_space == -1:
            raise ValueError("Строка должна содержать хотя бы один пробел.")

        # Находим индекс второго пробела
        second_space = S.find(' ', first_space + 1)

        # Если второго пробела нет, возвращаем пустую строку
        if second_space == -1:
            return ""

        # Возвращаем подстроку между первым и вторым пробелом
        return S[first_space + 1:second_space]

    except ValueError as e:
        # Обработка ошибок
        return f"Ошибка: {e}"


# Ввод данных с помощью input()
S = input("Введите строку, содержащую хотя бы один пробел: ")

# Выводим результат
print("Результат:", substring_between_spaces(S))
