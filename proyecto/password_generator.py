# Proyecto realizado por Carolina Fernández, NIE: X5435988F

import random
import string

# Generador de contraseñas con una longitud de 12 caracteres
def generate_password(length, include_digits, include_punctuation):
    characters = string.ascii_letters
    if include_digits:
        # BUG: Arreglado después del bisect
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    
    include_digits_input = input("Include digits in the password? (yes/no): ").strip().lower()
    include_digits = True if include_digits_input == 'yes' else False
    
    include_punctuation_input = input("Include punctuation in the password? (yes/no): ").strip().lower()
    include_punctuation = True if include_punctuation_input == 'yes' else False
    
    print("Generated password:", generate_password(length, include_digits, include_punctuation))