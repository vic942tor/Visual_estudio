import subprocess
import sys

# Función para instalar la biblioteca 'cryptography'
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Intentar instalar 'cryptography'
try:
    import cryptography
except ImportError:
    print("La biblioteca 'cryptography' no está instalada. Instalando...")
    install('cryptography')

from cryptography.fernet import Fernet

# Generar una clave y crear un objeto Fernet
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# La contraseña que deseas proteger
password = "7412"
cipher_text = cipher_suite.encrypt(password.encode())

# Para mostrar cómo se almacena la contraseña cifrada
print(f"Contraseña cifrada: {cipher_text}")

# Para descifrar la contraseña más tarde
decrypted_password = cipher_suite.decrypt(cipher_text).decode()
print(f"Contraseña descifrada: {decrypted_password}")