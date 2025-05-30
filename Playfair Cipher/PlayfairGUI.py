import tkinter as tk
from tkinter import messagebox
from random import sample
import re

# --- Playfair Cipher Logic (with custom matrix) ---
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None, None

def playfair_prepare_text(text):
    text = text.upper().replace('J', 'I')
    prepared = ''
    i = 0
    while i < len(text):
        if text[i].isalpha():
            a = text[i]
            b = ''
            if i+1 < len(text) and text[i+1].isalpha():
                b = text[i+1]
            if a == b:
                prepared += a + 'X'
                i += 1
            else:
                if b:
                    prepared += a + b
                    i += 2
                else:
                    prepared += a + 'X'
                    i += 1
        else:
            i += 1
    return prepared

def playfair_encrypt_custom(plaintext, matrix_chars):
    matrix = [matrix_chars[i*5:(i+1)*5] for i in range(5)]
    prepared = playfair_prepare_text(plaintext)
    result = ''
    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 is None or row2 is None:
            result += a + b
            continue
        if row1 == row2:
            result += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
        elif col1 == col2:
            result += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

def validate_matrix(entries):
    chars = [e.get().upper() for e in entries]
    chars = [c for c in chars if c.isalpha()]
    if len(chars) != 25:
        return False, 'Matrix harus diisi 25 huruf.'
    if len(set(chars)) != 25:
        return False, 'Huruf pada matrix tidak boleh ada yang sama tanpa "J".'
    allowed = set('ABCDEFGHIKLMNOPQRSTUVWXYZ')
    if not all(c in allowed for c in chars):
        return False, 'Matrix hanya boleh berisi huruf A-Z tanpa "J".'
    return True, chars

def random_matrix():
    return sample(list('ABCDEFGHIKLMNOPQRSTUVWXYZ'), 25)

# --- GUI ---
root = tk.Tk()
root.title('Playfair Cipher - Custom Matrix')
root.geometry('500x500')

# Plaintext input
frame_top = tk.Frame(root)
frame_top.pack(pady=10)
label_plain = tk.Label(frame_top, text='Plaintext:')
label_plain.pack(anchor='w')
plaintext_entry = tk.Entry(frame_top, width=40)
plaintext_entry.pack()

# Matrix input
frame_matrix = tk.Frame(root)
frame_matrix.pack(pady=10)
tk.Label(frame_matrix, text='Isi Matrix 5x5 (A-Z tanpa "J", tidak boleh ada huruf sama):').pack()
matrix_entries = []
grid = tk.Frame(frame_matrix)
grid.pack()
for i in range(5):
    for j in range(5):
        e = tk.Entry(grid, width=2, font=("Consolas", 16), justify="center")
        e.grid(row=i, column=j, padx=2, pady=2)
        matrix_entries.append(e)

def do_random():
    chars = random_matrix()
    for idx, c in enumerate(chars):
        matrix_entries[idx].delete(0, tk.END)
        matrix_entries[idx].insert(0, c)

def do_encrypt():
    valid, chars = validate_matrix(matrix_entries)
    if not valid:
        messagebox.showerror('Error', chars)
        return
    pt = plaintext_entry.get()
    if not pt.strip():
        messagebox.showerror('Error', 'Plaintext tidak boleh kosong.')
        return
    ct = playfair_encrypt_custom(pt, chars)
    ciphertext_entry.config(state='normal')
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, ct)
    ciphertext_entry.config(state='readonly')

# Tambahkan mode toggle (Encrypt/Decrypt)
mode_var = tk.StringVar(value='encrypt')

def switch_mode():
    if mode_var.get() == 'encrypt':
        label_plain.config(text='Plaintext:')
        label_result.config(text='Ciphertext:')
        btn_encrypt.config(text='Enkripsi', command=do_encrypt)
        ciphertext_entry.config(state='readonly')
        ciphertext_entry.delete(0, tk.END)
    else:
        label_plain.config(text='Ciphertext:')
        label_result.config(text='Plaintext:')
        btn_encrypt.config(text='Dekripsi', command=do_decrypt)
        ciphertext_entry.config(state='readonly')
        ciphertext_entry.delete(0, tk.END)

# Decrypt logic

def playfair_decrypt_custom(ciphertext, matrix_chars):
    matrix = [matrix_chars[i*5:(i+1)*5] for i in range(5)]
    prepared = playfair_prepare_text(ciphertext)
    result = ''
    for i in range(0, len(prepared), 2):
        a, b = prepared[i], prepared[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 is None or row2 is None:
            result += a + b
            continue
        if row1 == row2:
            result += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            result += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            result += matrix[row1][col2] + matrix[row2][col1]
    return result

# Ganti label pada hasil output agar bisa diubah
frame_bottom = tk.Frame(root)
frame_bottom.pack(pady=10)
label_result = tk.Label(frame_bottom, text='Ciphertext:')
label_result.pack(anchor='w')
ciphertext_entry = tk.Entry(frame_bottom, width=40, state='readonly')
ciphertext_entry.pack()

# Perbaiki hasil dekripsi agar menghilangkan X penyisipan otomatis
def clean_playfair_decrypt(plaintext):
    # Hilangkan X yang disisipkan di tengah digraf yang sama, kecuali X asli
    # 1. Hapus X di antara dua huruf sama (kecuali di awal/akhir)
    cleaned = re.sub(r'([A-Z])X(?=[A-Z])', lambda m: m.group(1) if m.group(1) == plaintext[plaintext.index(m.group(1))+2] else m.group(0), plaintext)
    # 2. Jika X di akhir, hapus X (karena X di akhir hanya hasil padding Playfair)
    if cleaned.endswith('X'):
        cleaned = cleaned[:-1]
    return cleaned

def do_decrypt():
    valid, chars = validate_matrix(matrix_entries)
    if not valid:
        messagebox.showerror('Error', chars)
        return
    ct = plaintext_entry.get()
    if not ct.strip():
        messagebox.showerror('Error', 'Ciphertext tidak boleh kosong.')
        return
    pt = playfair_decrypt_custom(ct, chars)
    pt_clean = clean_playfair_decrypt(pt)
    ciphertext_entry.config(state='normal')
    ciphertext_entry.delete(0, tk.END)
    ciphertext_entry.insert(0, pt_clean)
    ciphertext_entry.config(state='readonly')

# Tambahkan radio button untuk mode
frame_mode = tk.Frame(root)
frame_mode.pack(pady=5)
tk.Label(frame_mode, text='Mode:').pack(side='left')
tk.Radiobutton(frame_mode, text='Encrypt', variable=mode_var, value='encrypt', command=switch_mode).pack(side='left')
tk.Radiobutton(frame_mode, text='Decrypt', variable=mode_var, value='decrypt', command=switch_mode).pack(side='left')

btn_random = tk.Button(frame_matrix, text='Randomisasi Matrix', command=do_random)
btn_random.pack(pady=2)

btn_encrypt = tk.Button(root, text='Enkripsi', command=do_encrypt, width=20)
btn_encrypt.pack(pady=10)

root.mainloop()
