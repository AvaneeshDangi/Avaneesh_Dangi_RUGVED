def coleman(text):
    letters = 0
    words = 0
    sentences = 0


    for char in text:
        if char.isalpha():
            letters = letters + 1


    words = len(text.split())



    for char in text:
        if char == '.' or char == '!' or char == '?':
            sentences = sentences + 1




    if words == 0:
        return 0

    L = (letters / words) * 100
    S = (sentences / words) * 100

    index = 0.0588 * L - 0.296 * S - 15.8

    return round(index)


text = input("Enter the text: ")

grade = coleman(text)

if grade < 1:
    print("Before Grade 1")
elif grade >= 16:
    print("Grade 16+")
else:
    print("Grade", grade)

