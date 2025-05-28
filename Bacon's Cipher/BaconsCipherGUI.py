import tkinter as tk
from tkinter import ttk, messagebox
import re

# Bacon's Cipher logic
def bacons_cipher_encrypt(text):
    bacon_dict = {
        'A': 'AAAAA', 'B': 'AAAAB', 'C': 'AAABA', 'D': 'AAABB', 'E': 'AABAA',
        'F': 'AABAB', 'G': 'AABBA', 'H': 'AABBB', 'I': 'ABAAA', 'J': 'ABAAB',
        'K': 'ABABA', 'L': 'ABABB', 'M': 'ABBAA', 'N': 'ABBAB', 'O': 'ABBBA',
        'P': 'ABBBB', 'Q': 'BAAAA', 'R': 'BAAAB', 'S': 'BAABA', 'T': 'BAABB',
        'U': 'BABAA', 'V': 'BABAB', 'W': 'BABBA', 'X': 'BABBB', 'Y': 'BBAAA', 'Z': 'BBAAB',
        ' ': 'BBABB'  # Add a special code for Space
    }
    result = ''
    for char in text.upper():
        if char in bacon_dict:
            result += bacon_dict[char] + ' '
        else:
            result += char + ' '
    return result.strip()

def bacons_cipher_decrypt(ciphertext):
    bacon_dict = {
        'AAAAA': 'A', 'AAAAB': 'B', 'AAABA': 'C', 'AAABB': 'D', 'AABAA': 'E',
        'AABAB': 'F', 'AABBA': 'G', 'AABBB': 'H', 'ABAAA': 'I', 'ABAAB': 'J',
        'ABABA': 'K', 'ABABB': 'L', 'ABBAA': 'M', 'ABBAB': 'N', 'ABBBA': 'O',
        'ABBBB': 'P', 'BAAAA': 'Q', 'BAAAB': 'R', 'BAABA': 'S', 'BAABB': 'T',
        'BABAA': 'U', 'BABAB': 'V', 'BABBA': 'W', 'BABBB': 'X', 'BBAAA': 'Y', 'BBAAB': 'Z',
        'BBABB': ' '
    }
    tokens = ciphertext.strip().split()
    result = ''
    for token in tokens:
        result += bacon_dict.get(token, '?')
    return result

# GUI Setup
root = tk.Tk()
root.title("Bacon's Cipher")
root.geometry("700x350")

# Encryption Frame
encrypt_frame = ttk.Frame(root)
encrypt_frame.pack(padx=10, pady=10)
tk.Label(encrypt_frame, text="Enkripsi", font=("Arial", 12, "bold")).pack(anchor="center", pady=(0, 5))

tk.Label(encrypt_frame, text="Plaintext:").pack(anchor="w", padx=5)
plaintext_entry = tk.Entry(encrypt_frame, width=50)
plaintext_entry.pack(padx=5)

encrypted_label = tk.Label(encrypt_frame, text="Hasil Enkripsi:")
encrypted_label.pack(anchor="w", padx=5)
ciphertext_result = tk.Entry(encrypt_frame, width=50, state="readonly")
ciphertext_result.pack(anchor="w", padx=5, pady=5)

def handle_encrypt():
    plaintext = plaintext_entry.get()
    # Only allow A-Z and space
    if not re.fullmatch(r'[A-Za-z ]*', plaintext):
        messagebox.showwarning(
            "Karakter Tidak Didukung",
            "Ini adalah algoritma enkripsi kuno yang pada zamannya tidak menggunakan angka atau simbol aneh.\nSilakan masukkan hanya huruf A-Z dan spasi."
        )
        return
    ciphertext = bacons_cipher_encrypt(plaintext)
    ciphertext_result.config(state="normal")
    ciphertext_result.delete(0, tk.END)
    ciphertext_result.insert(0, ciphertext)
    ciphertext_result.config(state="readonly")

def clear_encrypt():
    plaintext_entry.delete(0, tk.END)
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

decrypted_label = tk.Label(decrypt_frame, text="Hasil Dekripsi:")
decrypted_label.pack(anchor="w", padx=5)
decrypted_result = tk.Entry(decrypt_frame, width=50, state="readonly")
decrypted_result.pack(anchor="w", pady=5)

def handle_decrypt():
    ciphertext = ciphertext_entry.get()
    # Only allow A-Z, space, and the special code for space (BBABB)
    if not re.fullmatch(r'[A-Za-z ]*', ciphertext):
        messagebox.showwarning(
            "Karakter Tidak Didukung",
            "Ini adalah algoritma enkripsi kuno yang pada zamannya tidak menggunakan angka atau simbol aneh.\nSilakan masukkan hanya huruf A-Z, spasi, dan kode enkripsi yang valid."
        )
        return
    plaintext = bacons_cipher_decrypt(ciphertext)
    decrypted_result.config(state="normal")
    decrypted_result.delete(0, tk.END)
    decrypted_result.insert(0, plaintext)
    decrypted_result.config(state="readonly")

def clear_decrypt():
    ciphertext_entry.delete(0, tk.END)
    decrypted_result.config(state="normal")
    decrypted_result.delete(0, tk.END)
    decrypted_result.config(state="readonly")

button_frame_decrypt = tk.Frame(decrypt_frame)
button_frame_decrypt.pack(pady=5)
tk.Button(button_frame_decrypt, text="Dekripsi", command=handle_decrypt, width=15).grid(row=0, column=0, padx=5)
tk.Button(button_frame_decrypt, text="Clear", command=clear_decrypt, width=15).grid(row=0, column=1, padx=5)

root.mainloop()
