import random
import string
def specialcheck():
    while True:
        choice = input("Include special characters? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def generate():
    length = int(input("Enter password length: "))
    use_special = specialcheck()

    chars = string.ascii_letters + string.digits
    if use_special:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password:", password)