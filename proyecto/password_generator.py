# Proyecto realizado por Carolina Fernández, NIE: X5435988F

import random
import string

# Generador de contraseñas con una longitud de 12 caracteres
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("Generated password: ", generate_password())