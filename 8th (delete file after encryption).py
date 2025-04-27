import os
from cryptography.fernet import Fernet

# Encrypt the file
key = Fernet.generate_key()
cipher_suite = Fernet(key)

with open(r"C:\Users\Admin\OneDrive\Documents\important_data.txt", "rb") as file:
    file_data = file.read()

encrypted_data = cipher_suite.encrypt(file_data)
decrypt = cipher_suite.decrypt(encrypted_data)

with open(r"C:\Users\Admin\OneDrive\Documents\important_data_encrypted.txt", "wb") as file:
    file.write(encrypted_data)
    #file.write("\n")
    file.write(decrypt)

with open(r"C:\Users\Admin\OneDrive\Documents\important_data.txt", "wb") as file:
    file.write(os.urandom(len(file_data)))  # Random bytes

# Delete the original file
os.remove(r"C:\Users\Admin\OneDrive\Documents\important_data.txt")

print("File encrypted, overwritten, and deleted securely.")