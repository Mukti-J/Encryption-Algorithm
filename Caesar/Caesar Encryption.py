import tkinter as tk
from tkinter import ttk

# Fungsi enkripsi dan dekripsi sesuai rumus khusus
def encrypt(text):
    result = ''
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            c = (3 * x + 4) % 26
            result += chr(c + ord('A'))
        else:
            result += char
    return result

def decrypt(text):
    result = ''
    for char in text.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            p = (9 * x - 10) % 26
            result += chr(p + ord('A'))
        else:
            result += char
    return result

# Membuat GUI dengan tkinter
root = tk.Tk()
root.title("Caesar Encryption (Fix Key)")
root.geometry("700x400")
root.anchor

# Enkripsi Frame
encrypt_frame = ttk.LabelFrame(root)
encrypt_frame.pack(fill="x", padx=10, pady=10)
tk.Label(encrypt_frame, text="Enkripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))

tk.Label(encrypt_frame, text="Plaintext:").pack(anchor="w", padx=5)
plaintext_entry = tk.Entry(encrypt_frame, width=50)
plaintext_entry.pack(padx=5)

ciphertext_label = tk.Label(encrypt_frame, text="Hasil Enkripsi:")
ciphertext_label.pack(anchor="w", padx=5, pady=5)

def handle_encrypt():
    plaintext = plaintext_entry.get()
    ciphertext = encrypt(plaintext)
    ciphertext_label.config(text=f"Hasil Enkripsi: {ciphertext}")

def clear_encrypt():
    plaintext_entry.delete(0, tk.END)
    ciphertext_label.config(text="Hasil Enkripsi:")

button_frame_encrypt = tk.Frame(encrypt_frame)
button_frame_encrypt.pack(pady=5)

tk.Button(button_frame_encrypt, text="Enkripsi", command=handle_encrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_encrypt, text="Clear", command=clear_encrypt, width=15).grid(row=0, column=1, padx=5)


# Dekripsi Frame
decrypt_frame = ttk.LabelFrame(root)
decrypt_frame.pack(fill="x", padx=10, pady=10)
tk.Label(decrypt_frame, text="Dekripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))

tk.Label(decrypt_frame, text="Ciphertext:").pack(anchor="w", padx=5)
ciphertext_entry = tk.Entry(decrypt_frame, width=50)
ciphertext_entry.pack(padx=5)

decrypted_label = tk.Label(decrypt_frame, text="Hasil Dekripsi:")
decrypted_label.pack(anchor="w", padx=5, pady=5)

def handle_decrypt():
    ciphertext = ciphertext_entry.get()
    plaintext = decrypt(ciphertext)
    decrypted_label.config(text=f"Hasil Dekripsi: {plaintext}")

def clear_decrypt():
    ciphertext_entry.delete(0, tk.END)
    decrypted_label.config(text="Hasil Dekripsi:")

button_frame_decrypt = tk.Frame(decrypt_frame)
button_frame_decrypt.pack(pady=5)

tk.Button(button_frame_decrypt, text="Dekripsi", command=handle_decrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_decrypt, text="Clear", command=clear_decrypt, width=15).grid(row=0, column=1, padx=5)

root.mainloop()