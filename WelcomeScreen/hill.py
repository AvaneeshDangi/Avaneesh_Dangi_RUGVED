def isHILL(number):
    digits = str(number)

    increasing = True

    for i in range(len(digits) - 1):
        if increasing:
            if digits[i] < digits[i + 1]:
                continue
            else:
                increasing = False

        if not increasing:
            if digits[i] <= digits[i + 1]:
                return False

    return True


number = input("Enter a number: ")

if isHILL(number):
    print("It is a Hill Number")
else:
    print("It is not a Hill Number")
