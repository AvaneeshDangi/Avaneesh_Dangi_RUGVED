n = int(input("Enter the size of matrix: "))

matrix = []

print("Enter the matrix:")

for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)



rotated = []

for i in range(n):
    row = []

    for j in range(n - 1, -1, -1):
        row.append(matrix[j][i])

    rotated.append(row)


print("Matrix after 90 degree clockwise rotation:")

for row in rotated:
    print(*row)



print("Spiral order:")

top = 0
bottom = n - 1
left = 0
right = n - 1

while top <= bottom and left <= right:

    # Left to right
    for j in range(left, right + 1):
        print(rotated[top][j], end=" ")

    top = top + 1

    # Top to bottom
    for i in range(top, bottom + 1):
        print(rotated[i][right], end=" ")

    right = right - 1

    # Right to left
    if top <= bottom:
        for j in range(right, left - 1, -1):
            print(rotated[bottom][j], end=" ")

        bottom = bottom - 1

    # Bottom to top
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(rotated[i][left], end=" ")

        left = left + 1