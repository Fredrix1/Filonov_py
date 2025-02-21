# Книжные магазины предлагают следующие коллекции книг.
# Магистр – Лермонтов, Достоевский, Пушкин, Тютчев
# ДомКниги – Толстой, Грибоедов, Чехов, Пушкин.
# БукМаркет – Пушкин, Достоевский, Маяковский.
# Галерея – Чехов, Тютчев, Пушкин.
# Определить в каких магазинах
# нельзя приобрести книги Грибоедова и Маяковского

# Определяем множества книг для каждого магазина
magistr = {'Лермонтов', 'Достоевский', 'Пушкин', 'Тютчев'}
domknigi = {'Толстой', 'Грибоедов', 'Чехов', 'Пушкин'}
bookmarket = {'Пушкин', 'Достоевский', 'Маяковский'}
galereya = {'Чехов', 'Тютчев', 'Пушкин'}

# Книги, которые мы ищем
griboedov_mayakovsky = {'Грибоедов', 'Маяковский'}

# Определяем, в каких магазинах нельзя приобрести книги Грибоедова и Маяковского
stores_without_griboedov_mayakovsky = []

if not griboedov_mayakovsky.issubset(magistr):
    stores_without_griboedov_mayakovsky.append('Магистр')
if not griboedov_mayakovsky.issubset(domknigi):
    stores_without_griboedov_mayakovsky.append('ДомКниги')
if not griboedov_mayakovsky.issubset(bookmarket):
    stores_without_griboedov_mayakovsky.append('БукМаркет')
if not griboedov_mayakovsky.issubset(galereya):
    stores_without_griboedov_mayakovsky.append('Галерея')

print('Магазины, где нельзя приобрести книги Грибоедова и Маяковского:', stores_without_griboedov_mayakovsky)
