def consistency(n):
    s = []
    num = 1

    while len(s) < n:
        s.extend([num] * num)
        num += 1

    return s[:n]


n = int(input("Введите количество элементов последовательности: "))
result = consistency(n)
print("Первые", n, "элементов последовательности:", result)
