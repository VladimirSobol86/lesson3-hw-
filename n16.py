A = [0, -1, 5, 2, 3, 2, 8, 9, 3, 4, 3, 3, 3, 3]
x = int(input("Введите искомое число: "))
count = 0

for i in range(len(A)):
    if x == A[i]:
        count += 1
print("Число", x, "встречается", count, "раз(а)")