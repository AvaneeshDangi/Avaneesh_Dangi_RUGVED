string = input("Enter a string: ")


sorted_string = sorted(string)

print("Sorted string:", "".join(sorted_string))


for char in sorted_string:
    if sorted_string.count(char) == sorted_string.index(char) + 1:
        print(char, ":", sorted_string.count(char))