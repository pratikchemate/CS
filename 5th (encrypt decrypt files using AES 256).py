from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open(r"C:\Users\Admin\OneDrive\Documents\AES.txt", "rb") as file:
    file_data = file.read()

encrypted_data = cipher_suite.encrypt(file_data)

with open(r"C:\Users\Admin\OneDrive\Documents\sample_encrypted.txt", "wb") as file:
    file.write(encrypted_data)

with open(r"C:\Users\Admin\OneDrive\Documents\sample_encrypted.txt", "rb") as file:
    encrypted_data = file.read()

decrypted_data = cipher_suite.decrypt(encrypted_data)

with open(r"C:\Users\Admin\OneDrive\Documents\sample_decrypted.txt", "wb") as file:
    file.write(decrypted_data)

print("Encryption and Decryption Done Successfully.")