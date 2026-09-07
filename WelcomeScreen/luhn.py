def luhn_check(card_number):
    # Remove spaces and hyphens
    card_number = card_number.replace(" ", "")
    card_number = card_number.replace("-", "")

    # Check whether all characters are digits
    if not card_number.isdigit():
        return False

    total = 0
    double = False

    # Start from the right side
    for i in range(len(card_number) - 1, -1, -1):
        digit = int(card_number[i])

        if double:
            digit = digit * 2

            if digit > 9:
                digit = digit - 9

        total = total + digit
        double = not double

    return total % 10 == 0


card_number = input("Enter credit card number: ")

if luhn_check(card_number):
    print("Valid credit card number")
else:
    print("Invalid credit card number")

