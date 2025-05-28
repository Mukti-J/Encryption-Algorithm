import tkinter as tk
from tkinter import ttk, messagebox

# Vigenère Cipher logic
def vigenere_encrypt(plaintext, key):
    result = ''
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                base = ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key):
    result = ''
    key = key.lower()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base - shift) % 26 + base)
            else:
                base = ord('a')
                result += chr((ord(char) - base - shift) % 26 + base)
            key_index += 1
        else:
            result += char
    return result

# GUI Setup
root = tk.Tk()
root.title("Vigenère Cipher")
root.geometry("700x450")

# Encryption Frame
encrypt_frame = ttk.Frame(root)
encrypt_frame.pack(padx=10, pady=10)
tk.Label(encrypt_frame, text="Enkripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))

tk.Label(encrypt_frame, text="Plaintext:").pack(anchor="w", padx=5)
plaintext_entry = tk.Entry(encrypt_frame, width=50)
plaintext_entry.pack(padx=5)

tk.Label(encrypt_frame, text="Key:").pack(anchor="w", padx=5)
key_entry = tk.Entry(encrypt_frame, width=50)
key_entry.pack(padx=5)

encrypted_label = tk.Label(encrypt_frame, text="Hasil Enkripsi:")
encrypted_label.pack(anchor="w", padx=5)
ciphertext_result = tk.Entry(encrypt_frame, width=50, state="readonly")
ciphertext_result.pack(anchor="w", padx=5, pady=5)

def handle_encrypt():
    plaintext = plaintext_entry.get()
    key = key_entry.get()
    if not key.isalpha() or not key:
        messagebox.showerror("Error", "Key harus berupa huruf dan tidak boleh kosong.")
        return
    ciphertext = vigenere_encrypt(plaintext, key)
    ciphertext_result.config(state="normal")
    ciphertext_result.delete(0, tk.END)
    ciphertext_result.insert(0, ciphertext)
    ciphertext_result.config(state="readonly")

def clear_encrypt():
    plaintext_entry.delete(0, tk.END)
    key_entry.delete(0, tk.END)
    ciphertext_result.config(state="normal")
    ciphertext_result.delete(0, tk.END)
    ciphertext_result.config(state="readonly")

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

tk.Label(decrypt_frame, text="Key:").pack(anchor="w", padx=5)
key_entry_decrypt = tk.Entry(decrypt_frame, width=50)
key_entry_decrypt.pack()

decrypted_label = tk.Label(decrypt_frame, text="Hasil Dekripsi:")
decrypted_label.pack(anchor="w", padx=5)
decrypted_result = tk.Entry(decrypt_frame, width=50, state="readonly")
decrypted_result.pack(anchor="w", pady=5)

def handle_decrypt():
    ciphertext = ciphertext_entry.get()
    key = key_entry_decrypt.get()
    if not key.isalpha() or not key:
        messagebox.showerror("Error", "Key harus berupa huruf dan tidak boleh kosong.")
        return
    plaintext = vigenere_decrypt(ciphertext, key)
    decrypted_result.config(state="normal")
    decrypted_result.delete(0, tk.END)
    decrypted_result.insert(0, plaintext)
    decrypted_result.config(state="readonly")

def clear_decrypt():
    ciphertext_entry.delete(0, tk.END)
    key_entry_decrypt.delete(0, tk.END)
    decrypted_result.config(state="normal")
    decrypted_result.delete(0, tk.END)
    decrypted_result.config(state="readonly")

button_frame_decrypt = tk.Frame(decrypt_frame)
button_frame_decrypt.pack(pady=5)
tk.Button(button_frame_decrypt, text="Dekripsi", command=handle_decrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_decrypt, text="Clear", command=clear_decrypt, width=15).grid(row=0, column=1, padx=5)

root.mainloop()
