# Project 2: Affine Cipher GUI

Folder ini berisi implementasi **Affine Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Affine Cipher?

Affine Cipher adalah algoritma kriptografi klasik berbasis **Substitusi Sederhana** yang menggunakan dua kunci numerik, `a` dan `b`, untuk melakukan enkripsi dan dekripsi karakter pada alfabet. Algoritma ini merupakan pengembangan dari Caesar Cipher dengan menambahkan operasi perkalian.

- **Rumus Enkripsi**:
  \[
    C = (aX + b) \bmod 26
  \]
- **Rumus Dekripsi**:
  \[
    P = a^{-1}(Y - b) \bmod 26
  \]
  di mana $a^{-1}$ adalah invers modulo dari $a$ terhadap 26.

---
## 🧩 Fitur Program

- Input `plaintext` dan kunci `a` serta `b` untuk proses enkripsi
- Input `ciphertext` dan kunci `a` serta `b` untuk proses dekripsi
- Validasi agar kunci `a` harus coprime (relatif prima) dengan 26
- Tampilan GUI terstruktur dengan dua panel: Enkripsi dan Dekripsi
- Tombol **Enkripsi/Dekripsi** untuk memproses input
- Tombol **Clear** untuk mereset masing-masing panel

📄 File: `AffineEncryption.py`

---
## 📦 File dalam Folder Ini

| File                | Deskripsi                                      |
|---------------------|------------------------------------------------|
| `AffineEncryption.py` | Program utama Affine Cipher dengan GUI         |
| `README.md`         | Penjelasan tentang proyek ini                  |

---
## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:
   ```bash
   cd "Affine Cipher"
   ```
2. Jalankan program dengan perintah:
   ```bash
   python AffineEncryption.py
   ```

---

## 📝 Catatan
- Pastikan nilai `a` yang dimasukkan adalah coprime dengan 26 (misal: 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
- Jika bukan coprime, program akan menampilkan pesan error
- Program ini hanya mendukung alfabet A-Z (case-insensitive)
