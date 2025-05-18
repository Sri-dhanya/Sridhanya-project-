
import random
import string

def generate_password(length=12):
    if length < 4:
        return "Password length should be at least 4"

    # Define character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each set is included
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length
    all_chars = upper + lower + digits + symbols
    password += random.choices(all_chars, k=length - 4)

    # Shuffle to make the password random
    random.shuffle(password)

    return ''.join(password)

# Example usage
if __name__ == "__main__":
    print("Generated password:", generate_password(12))
