password = input("Enter a password: ")
special_characters = "$#@"
if len(password) < 6 or len(password) > 16:
    print("Invalid Password: Length should be between 6 and 16 characters.")
else:
    lower_count = 0
    upper_count = 0
    digit_count = 0
    special_count = 0

    for char in password:
        if 'a' <= char <= 'z':
            lower_count += 1
        elif 'A' <= char <= 'Z':
            upper_count += 1
        elif '0' <= char <= '9':
            digit_count += 1
        elif char in special_characters:
            special_count += 1

    if lower_count > 0 and upper_count > 0 and digit_count > 0 and special_count > 0:
        print("Valid Password")
    else:
        print("Invalid Password")
