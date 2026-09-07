def selection_sort(string):
    characters = list(string)

    for i in range(len(characters)):
        min_index = i

        for j in range(i + 1, len(characters)):
            if characters[j] < characters[min_index]:
                min_index = j

        # Swap
        characters[i], characters[min_index] = characters[min_index], characters[i]

    return "".join(characters)


string = input("Enter a string: ")

result = selection_sort(string)

print("Sorted string:", result)