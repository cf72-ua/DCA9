# Proyecto realizado por Carolina Fernández, NIE: X5435988F

import random
import string

# Generador de contraseñas con una longitud de 12 caracteres
def generate_password(length, include_digits=True, include_punctuation=True):
    characters = string.ascii_letters
    if include_digits:
        # BUG: Excluye siempre los dígitos por una condición incorrecta
        characters = string.ascii_letters
    if include_punctuation:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter the desired password length: "))
    print("Generated password:", generate_password(length))