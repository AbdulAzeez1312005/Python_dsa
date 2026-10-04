import secrets
import string

def generate_password(length: int = 16) -> str:
    """Generate a strong, cryptographically secure password."""
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    while True:
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Ensure password contains at least one lower, upper, digit, and special char
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in "!@#$%^&*" for c in password)):
            return password

def generate_passphrase(num_words: int = 4) -> str:
    """Generate a memorable multi-word passphrase."""
    word_list = [
        "apple", "brave", "breeze", "castle", "dragon", "falcon", "forest",
        "galaxy", "harbor", "island", "jungle", "knight", "legend", "mountain",
        "ocean", "planet", "river", "shadow", "silver", "thunder", "valley"
    ]
    return "-".join(secrets.choice(word_list) for _ in range(num_words))

print("Secure Password:  ", generate_password(16))
print("Memorable Passphrase:", generate_passphrase(4))
