string = input("Enter a string: ")
n = int(input("Enter the number of characters in each part: "))


if len(string) % n != 0:
    print("String cannot be divided into equal parts.")
else:
    parts = []

    for i in range(0, len(string), n):
        parts.append(string[i:i+n])



    same = True

    for i in range(1, len(parts)):
        if parts[i] != parts[0]:
            same = False
            break

    if same:
        print("Parts: ")
        for part in parts:
            print(part)
    else:
        print(" The sequence of all parts is not the same.")
