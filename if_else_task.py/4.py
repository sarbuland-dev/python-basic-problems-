password = input("Enter your password: ")


special_chars = "!@#$%^&*"


has_lower = False
has_upper = False
has_digit = False
has_special = False


for ch in password:
    if ch.islower():
        has_lower = True
    elif ch.isupper():
        has_upper = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True


errors = []


if len(password) < 8:
    errors.append("Password kam az kam 8 characters lamba hona chahiye.")


if not has_lower:
    errors.append("Password mein kam az kam ek lowercase letter hona chahiye.")


if not has_upper:
    errors.append("Password mein kam az kam ek uppercase letter hona chahiye.")


if not has_digit:
    errors.append("Password mein kam az kam ek number hona chahiye.")

if not has_special:
    errors.append(f"Password mein kam az kam ek special character hona chahiye ({special_chars}).")


if errors:
    print("Invalid Password ")
    for e in errors:
        print("-", e)
else:
    print("Valid Password ")
