# Project 1: Caesar Cipher GUI

Folder ini berisi dua versi pada implementasi **Caesar Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Caesar Cipher?

Caesar Cipher adalah algoritma kriptografi klasik berbasis **Substitusi Sederhana**, di mana setiap huruf digeser sebanyak `k` atau key di dalam posisi pada alfabet.

---
## 🧩 Versi yang Tersedia

### 🔐 Versi 1: Caesar Encrypt (Fixed Key)

- **Rumus Enkripsi**:
  \[
    C = (3X + 4) \bmod 26
  \]
- **Rumus dekripsi**:  
  \[
    P = (9X - 10) \bmod 26
  \]
- Kunci `3` dan `4` sudah tetap (tidak bisa diubah pengguna)
- **Fitur GUI**:  
  - Dua panel: Enkripsi dan Dekripsi  
  - Input `plaintext` & tombol **Enkripsi** → menampilkan `ciphertext`  
  - Input `ciphertext` & tombol **Dekripsi** → menampilkan `plaintext`  
  - Tombol **Clear** untuk mereset masing‑masing panel
- Cocok untuk memahami dasar konsep kriptografi modular

📄 File: `Caesar Encryption.py`

---

### 🧩 Versi 2: Caesar Encrypt (Custom Key) 

- — **[Versi Ini]** User bisa memasukkan sendiri nilai **key** untuk proses enkripsi dan dekripsi
- Rumus dasar:
  - Enkripsi:  
    \[
      C = (X + k) \bmod 26
    \]
  - Dekripsi:  
    \[
      P = (X - k + 26) \bmod 26
    \]
- Input plaintext atau ciphertext dan nilai `key` sebagai bilangan bulat
- GUI dengan tampilan terstruktur:
  - Form input `plaintext`/`ciphertext` dan `key`
  - Tombol **Enkripsi/Dekripsi**
  - Tombol **Clear** untuk reset tiap panel

📄 File: `Caesar Encryption ver2.py`

---

## 📦 File dalam Folder Ini

| File | Deskripsi |
|------|-----------|
| `Caesar Encryption.py` | Versi Caesar Cipher dengan key tetap (versi 1) |
| `Caesar Encryption ver2.py` | Versi dengan input key dari pengguna (versi 2 - ini) |
| `README.md` | Penjelasan tentang proyek ini |

---
## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:  
   ```bash
   cd Caesar
