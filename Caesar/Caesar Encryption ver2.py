import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Fungsi Caesar Cipher Umum
def encrypt(text, key):
    result = ''
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            c = (x + key) % 26
            result += chr(c + ord('A'))
        else:
            result += char
    return result

def decrypt(text, key):
    result = ''
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            p = (x - key + 26) % 26
            result += chr(p + ord('A'))
        else:
            result += char
    return result

# Setup GUI
root = tk.Tk()
root.title("Caesar Cipher (User Key)")
root.geometry("700x400")

# Enkripsi Frame 
encrypt_frame = ttk.Frame(root)
encrypt_frame.pack(padx=10, pady=10)
tk.Label(encrypt_frame, text="Enkripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))

tk.Label(encrypt_frame, text="Plaintext:").pack(anchor="w", padx=5)
plaintext_entry = tk.Entry(encrypt_frame, width=50)
plaintext_entry.pack(padx=5)

tk.Label(encrypt_frame, text="Key:").pack(anchor="w", padx=5)
encrypt_key_entry = tk.Entry(encrypt_frame, width=50)
encrypt_key_entry.pack(padx=5)

ciphertext_label = tk.Label(encrypt_frame, text="Hasil Enkripsi:")
ciphertext_label.pack(anchor="w", padx=5, pady=5)

def handle_encrypt():
    try:
        key = int(encrypt_key_entry.get())
        plaintext = plaintext_entry.get()
        ciphertext = encrypt(plaintext, key)
        ciphertext_label.config(text=f"Hasil Enkripsi: {ciphertext}")
    except ValueError:
        messagebox.showerror("Error", "Key harus berupa angka bulat!")

def clear_encrypt():
    plaintext_entry.delete(0, tk.END)
    encrypt_key_entry.delete(0, tk.END)
    ciphertext_label.config(text="Hasil Enkripsi:")

button_frame_encrypt = tk.Frame(encrypt_frame)
button_frame_encrypt.pack(pady=5)
tk.Button(button_frame_encrypt, text="Enkripsi", command=handle_encrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_encrypt, text="Clear", command=clear_encrypt, width=15).grid(row=0, column=1, padx=5)

# Dekripsi Frame
decrypt_frame = ttk.Frame(root)
decrypt_frame.pack(padx=10, pady=5)
tk.Label(decrypt_frame, text="Dekripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))


tk.Label(decrypt_frame, text="Ciphertext:").pack(anchor="w", padx=5)
ciphertext_entry = tk.Entry(decrypt_frame, width=50)
ciphertext_entry.pack()

tk.Label(decrypt_frame, text="Key:").pack(anchor="w", padx=5)
decrypt_key_entry = tk.Entry(decrypt_frame, width=50)
decrypt_key_entry.pack()

decrypted_label = tk.Label(decrypt_frame, text="Hasil Dekripsi:")
decrypted_label.pack(anchor="w", pady=5)

def handle_decrypt():
    try:
        key = int(decrypt_key_entry.get())
        ciphertext = ciphertext_entry.get()
        plaintext = decrypt(ciphertext, key)
        decrypted_label.config(text=f"Hasil Dekripsi: {plaintext}")
    except ValueError:
        messagebox.showerror("Error", "Key harus berupa angka bulat!")

def clear_decrypt():
    ciphertext_entry.delete(0, tk.END)
    decrypt_key_entry.delete(0, tk.END)
    decrypted_label.config(text="Hasil Dekripsi:")

button_frame_decrypt = tk.Frame(decrypt_frame)
button_frame_decrypt.pack(pady=5)
tk.Button(button_frame_decrypt, text="Dekripsi", command=handle_decrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_decrypt, text="Clear", command=clear_decrypt, width=15).grid(row=0, column=1, padx=5)

root.mainloop()
