def areAnagrams(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if sorted(string1) == sorted(string2):
        return True
    else:
        return False


string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if areAnagrams(string1, string2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
