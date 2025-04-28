def is_very_long(password):
    return len(password) >= 12


def has_digit(password):
    return any(upass.isdigit() for upass in password)


def has_upper_letters(password):
    return any(upass.isupper() for upass in password)


def has_lower_letter(password):
    return any(upass.islower() for upass in password)


def has_symbols(password):
    return any(not upass.isalnum() for upass in password)


def main():
    score = 0
    password = input("Введите пароль: ")

    checks = [
        is_very_long, 
        has_digit,
        has_upper_letters, 
        has_lower_letter, 
        has_symbols
    ]

    for check in checks:
        if check(password):
            score += 2

    print("Надежность пароля: ", score)


if __name__ == "__main__":
    main()
