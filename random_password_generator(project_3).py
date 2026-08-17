import secrets
import string

def generate_password():
    print("--- DecodeLabs Random Password Generator ---")
    
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Character set including letters, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use secrets.choice for cryptographically secure selection
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    print(f"\nGenerated Secure Password: {password}\n")

if __name__ == "__main__":
    generate_password()