n = int(input("Enter the number of values: "))

a = 0
b = 1

print("Fibonacci sequence:")

for i in range(n):
    print(a, end=" ")

    c = a + b
    a = b
    b = c