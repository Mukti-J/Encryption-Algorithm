import tkinter as tk
from tkinter import ttk, messagebox
from math import gcd

# Helper: Modular inverse 
def modinv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

# Affine Cipher Encrypt
def affine_encrypt(text, a, b):
    result = ''
    m = 26
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            c = (a * x + b) % m
            result += chr(c + ord('A'))
        else:
            result += char
    return result

# Affine Cipher Decrypt
def affine_decrypt(text, a, b):
    result = ''
    m = 26
    a_inv = modinv(a, m)
    if a_inv is None:
        return "No modular inverse for a!"
    for char in text.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            p = (a_inv * (y - b)) % m
            result += chr(p + ord('A'))
        else:
            result += char
    return result

# GUI Setup
root = tk.Tk()
root.title("Affine Cipher")
root.geometry("700x480")

# Encryption Frame
encrypt_frame = ttk.Frame(root)
encrypt_frame.pack(padx=10, pady=10)
tk.Label(encrypt_frame, text="Enkripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))

tk.Label(encrypt_frame, text="Plaintext:").pack(anchor="w", padx=5)
plaintext_entry = tk.Entry(encrypt_frame, width=50)
plaintext_entry.pack(padx=5)

tk.Label(encrypt_frame, text="Key a:").pack(anchor="w", padx=5)
encrypt_a_entry = tk.Entry(encrypt_frame, width=50)
encrypt_a_entry.pack(padx=5)

tk.Label(encrypt_frame, text="Key b:").pack(anchor="w", padx=5)
encrypt_b_entry = tk.Entry(encrypt_frame, width=50)
encrypt_b_entry.pack(padx=5)

ciphertext_label = tk.Label(encrypt_frame, text="Hasil Enkripsi:")
ciphertext_label.pack(anchor="w", padx=5, pady=5)

def handle_encrypt():
    try:
        a = int(encrypt_a_entry.get())
        b = int(encrypt_b_entry.get())
        if gcd(a, 26) != 1:
            messagebox.showerror("Error", "Key a harus coprime(bilangan prima) dengan 26!")
            return
        plaintext = plaintext_entry.get()
        ciphertext = affine_encrypt(plaintext, a, b)
        ciphertext_label.config(text=f"Hasil Enkripsi: {ciphertext}")
    except ValueError:
        messagebox.showerror("Error", "Key harus berupa angka bulat!")

def clear_encrypt():
    plaintext_entry.delete(0, tk.END)
    encrypt_a_entry.delete(0, tk.END)
    encrypt_b_entry.delete(0, tk.END)
    ciphertext_label.config(text="Hasil Enkripsi:")

button_frame_encrypt = tk.Frame(encrypt_frame)
button_frame_encrypt.pack(pady=5)
tk.Button(button_frame_encrypt, text="Enkripsi", command=handle_encrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_encrypt, text="Clear", command=clear_encrypt, width=15).grid(row=0, column=1, padx=5)

# Decryption Frame
decrypt_frame = ttk.Frame(root)
decrypt_frame.pack(padx=10, pady=5)
tk.Label(decrypt_frame, text="Dekripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))

tk.Label(decrypt_frame, text="Ciphertext:").pack(anchor="w", padx=5)
ciphertext_entry = tk.Entry(decrypt_frame, width=50)
ciphertext_entry.pack()

tk.Label(decrypt_frame, text="Key a:").pack(anchor="w", padx=5)
decrypt_a_entry = tk.Entry(decrypt_frame, width=50)
decrypt_a_entry.pack()

tk.Label(decrypt_frame, text="Key b:").pack(anchor="w", padx=5)
decrypt_b_entry = tk.Entry(decrypt_frame, width=50)
decrypt_b_entry.pack()

decrypted_label = tk.Label(decrypt_frame, text="Hasil Dekripsi:")
decrypted_label.pack(anchor="w", pady=5)

def handle_decrypt():
    try:
        a = int(decrypt_a_entry.get())
        b = int(decrypt_b_entry.get())
        if gcd(a, 26) != 1:
            messagebox.showerror("Error", "Key a harus coprime dengan 26!")
            return
        ciphertext = ciphertext_entry.get()
        plaintext = affine_decrypt(ciphertext, a, b)
        decrypted_label.config(text=f"Hasil Dekripsi: {plaintext}")
    except ValueError:
        messagebox.showerror("Error", "Key harus berupa angka bulat!")

def clear_decrypt():
    ciphertext_entry.delete(0, tk.END)
    decrypt_a_entry.delete(0, tk.END)
    decrypt_b_entry.delete(0, tk.END)
    decrypted_label.config(text="Hasil Dekripsi:")

button_frame_decrypt = tk.Frame(decrypt_frame)
button_frame_decrypt.pack(pady=5)
tk.Button(button_frame_decrypt, text="Dekripsi", command=handle_decrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_decrypt, text="Clear", command=clear_decrypt, width=15).grid(row=0, column=1, padx=5)

root.mainloop()