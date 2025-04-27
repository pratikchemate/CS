from cryptography.fernet import Fernet

key = Fernet.generate_key()
with open("my_secret_key.key", "wb") as key_file:
    key_file.write(key)

print("Key saved successfully.")

with open("my_secret_key.key", "rb") as key_file:
    loaded_key = key_file.read()

cipher_suite = Fernet(loaded_key)

message = "Encryption after loading key!"
encrypted_message = cipher_suite.encrypt(message.encode())

print("Encrypted after loading key:", encrypted_message)