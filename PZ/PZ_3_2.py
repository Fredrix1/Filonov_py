# На числовой оси расположены три точки: A, B, C. Определить, какая из двух
# последних точек (B или C) расположена ближе к A, и вывести эту точку и ее расстояние от точки A.


try:
    # Ввод координат точек A, B и C
    A = float(input("Введите координату точки A: "))
    B = float(input("Введите координату точки B: "))
    C = float(input("Введите координату точки C: "))

    # Расчет расстояний от точки A до B и C
    distance_B = abs(A - B)
    distance_C = abs(A - C)

    # Определение, какая точка ближе к A
    if distance_B < distance_C:
        print(f"Точка B ближе к A, расстояние: {distance_B}")
    elif distance_C < distance_B:
        print(f"Точка C ближе к A, расстояние: {distance_C}")
    else:
        print(f"Точки B и C находятся на равном расстоянии от точки A: {distance_B}")

except ValueError as e:
    print(f"Ошибка ввода: {e}. Пожалуйста, введите числовые значения.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

