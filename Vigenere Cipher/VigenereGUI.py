import tkinter as tk
from tkinter import ttk, messagebox

# Vigenère Cipher logic
def vigenere_encrypt(plaintext, key, mode="Repeat"):
    result = ''
    if mode == "Autokey":
        key_extended = extend_key_autokey(plaintext, key)
    else:
        key_extended = extend_key_repeat(plaintext, key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key_extended[i]) - ord('a')
            if char.isupper():
                base = ord('A')
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                base = ord('a')
                result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_decrypt(ciphertext, key, mode="Repeat"):
    result = ''
    if mode == "Autokey":
        key_extended = key.lower()
        key_index = 0
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shift = ord(key_extended[key_index]) - ord('a')
                if char.isupper():
                    base = ord('A')
                    plain_char = chr((ord(char) - base - shift) % 26 + base)
                else:
                    base = ord('a')
                    plain_char = chr((ord(char) - base - shift) % 26 + base)
                result += plain_char
                key_extended += plain_char.lower()
                key_index += 1
            else:
                result += char
        return result
    else:
        key_extended = extend_key_repeat(ciphertext, key)
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                shift = ord(key_extended[i]) - ord('a')
                if char.isupper():
                    base = ord('A')
                    result += chr((ord(char) - base - shift) % 26 + base)
                else:
                    base = ord('a')
                    result += chr((ord(char) - base - shift) % 26 + base)
            else:
                result += char
        return result

# Fungsi untuk memperpanjang key sesuai mode
def extend_key_repeat(text, key):
    key = key.lower()
    key_extended = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            key_extended += key[key_index % len(key)]
            key_index += 1
        else:
            key_extended += char
    return key_extended

def extend_key_autokey(text, key):
    key = key.lower()
    key_extended = key
    for char in text:
        if len(key_extended) >= len([c for c in text if c.isalpha()]):
            break
        if char.isalpha():
            key_extended += char.lower()
    # Build the final key string, skipping non-alpha in text
    result = ''
    key_index = 0
    for char in text:
        if char.isalpha():
            result += key_extended[key_index]
            key_index += 1
        else:
            result += char
    return result

# GUI Setup
root = tk.Tk()
root.title("Vigenère Cipher")
root.geometry("700x500")

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

# Tambahkan Key Mode Selection ke Encryption Frame
key_mode_var = tk.StringVar(value="Repeat")
tk.Label(encrypt_frame, text="Key Mode:").pack(anchor="w", padx=5)
key_mode_combo = ttk.Combobox(
    encrypt_frame, textvariable=key_mode_var, values=["Repeat", "Autokey"], state="readonly", width=15
)
key_mode_combo.pack(anchor="w", padx=5, pady=(0, 5))

encrypted_label = tk.Label(encrypt_frame, text="Hasil Enkripsi:")
encrypted_label.pack(anchor="w", padx=5)
ciphertext_result = tk.Entry(encrypt_frame, width=50, state="readonly")
ciphertext_result.pack(anchor="w", padx=5, pady=5)

def handle_encrypt():
    plaintext = plaintext_entry.get()
    key = key_entry.get()
    mode = key_mode_var.get()
    if not key.isalpha() or not key:
        messagebox.showerror("Error", "Key harus berupa huruf dan tidak boleh kosong.")
        return
    ciphertext = vigenere_encrypt(plaintext, key, mode)
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
    mode = key_mode_var.get()
    if not key.isalpha() or not key:
        messagebox.showerror("Error", "Key harus berupa huruf dan tidak boleh kosong.")
        return
    plaintext = vigenere_decrypt(ciphertext, key, mode)
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
