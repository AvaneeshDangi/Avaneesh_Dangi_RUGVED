def caesarcipher(string, shift):
    result = ""

    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for char in string:
        if char.isalpha():
            if char.islower():
                position = lowercase.index(char)
                new_position = (position + shift) % 26
                new_char = lowercase[new_position]
            else:
                position = uppercase.index(char)
                new_position = (position + shift) % 26
                new_char = uppercase[new_position]

            result = result + new_char
        else:
            result = result + char

    return result


string = input("Enter a string: ")
shift = int(input("Enter the shift value: "))

encrypted = caesarcipher(string, shift)

print("Encrypted string:", encrypted)