import os
from Crypto.Cipher import AES
import tkinter as tk
from tkinter import messagebox

# Default decryption key
DEFAULT_KEY = "anonymoushere"

def decrypt_file(file_path, key=DEFAULT_KEY):
    key = key.ljust(32)[:32].encode()

    with open(file_path, 'rb') as file:
        encrypted_data = file.read()

    nonce = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    decrypted_data = cipher.decrypt(ciphertext)

    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

    print(f"Decrypted {file_path}")

def decrypt_directory(directory, key=DEFAULT_KEY):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            decrypt_file(file_path, key)

def show_decryption_message():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Decryption Complete", "All files have been decrypted, world is not safe my friend be careful.")
    root.destroy()

if __name__ == "__main__":
    directory = "/home/naveena/Businessfiles"
    decrypt_directory(directory)
    show_decryption_message()

