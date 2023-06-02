A = [1, 2, 3, 4, 5, 7, 15, 22, 7]
x = int(input("Задайте число: "))
number = A[0]
razn = abs(x-A[0])


for i in range(1, len(A)):
    if abs(x-A[i]) < razn:
        number = A[i]
        razn = abs(x-A[i])
        
print("Число", number, "самое близкое к", x)