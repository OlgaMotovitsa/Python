# Треугольник существует только тогда, когда сумма
# любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

side_a = int(input("введите сторону a: "))
side_b = int(input("введите сторону b: "))
side_c = int(input("введите сторону c: "))

if side_a <= side_b + side_c \
    and side_b <= side_a + side_c \
    and side_c <= side_a + side_b:
        if side_a == side_b == side_c:
            print("равносторонний")
        elif side_a != side_b != side_c:
            print("разносторонний")
        else:
            print("равнобедренный")
else:
    print("такого треугольника не существует")













