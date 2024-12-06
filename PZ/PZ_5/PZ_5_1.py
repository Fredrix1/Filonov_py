# Составить функцию, которая напечатает сорок любых символов.

def print_forty_characters():
    """
    Функция напечатает 40 любых символов.
    В случае возникновения ошибки выводится сообщение об ошибке.
    """
    try:
        # Генерируем 40 символов
        characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()'

        # Выбираем 40 случайных символов из строки characters
        import random
        selected_characters = random.choices(characters, k=40)

        # Печатаем результат
        print(''.join(selected_characters))

    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Вызываем функцию
print_forty_characters()
