import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_upper else ''
    digits = string.digits if use_digits else ''
    special = string.punctuation if use_special else ''
    
    all_chars = lower + upper + digits + special
    
    if len(all_chars) == 0:
        return "Error: No character set selected!"
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Strong Password Generator")
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_upper, use_digits, use_special)
    print("Generated Password:", password)
