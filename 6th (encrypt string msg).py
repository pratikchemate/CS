from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher_suite = Fernet(key)

message = input("Enter: ")
encrypted_message = cipher_suite.encrypt(message.encode())

print("Encrypted Message:", encrypted_message)

decrypted_message = cipher_suite.decrypt(encrypted_message).decode()

print("Decrypted Message:", decrypted_message)