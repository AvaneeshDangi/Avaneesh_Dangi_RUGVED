arr = list(map(int, input("Enter the elements: ").split()))

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            print("First repeating element:", arr[i])
            found = True
            break

    if found:
        break

if not found:
    print("No repeating element")
