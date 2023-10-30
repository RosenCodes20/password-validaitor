def password(passwords):
    errors = []

    if len(passwords) < 6 or len(passwords) > 10:
        errors.append("Password must be between 6 and 10 characters")
    if not passwords.isalnum():
        errors.append("Password must consist only of letters and digits")
    dig_counter = 0
    for chars in passwords:
        if chars.isdigit():
            dig_counter += 1
    if dig_counter < 2:
        errors.append("Password must have at least 2 digits")
    return errors


pas = input()
validated_pas = password(pas)
if len(validated_pas) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_pas))
