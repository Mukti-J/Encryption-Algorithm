# Project 5: Vigenère Cipher GUI

Folder ini berisi implementasi **Vigenère Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Vigenère Cipher?

Vigenère Cipher adalah algoritma kriptografi klasik berbasis **Substitusi Polialfabetik** yang menggunakan sebuah kata kunci (key) untuk mengenkripsi dan mendekripsi pesan. Setiap huruf pada plaintext digeser sesuai urutan huruf pada key, sehingga lebih aman dibanding Caesar Cipher.

- **Rumus Enkripsi**:
  
  Setiap huruf pada plaintext digeser sebanyak nilai alfabet pada huruf key (berulang jika key lebih pendek dari plaintext).

- **Rumus Dekripsi**:
  
  Setiap huruf pada ciphertext digeser mundur sebanyak nilai alfabet pada huruf key.

---

## 🧩 Fitur Program

- Input `plaintext` dan `key` untuk proses enkripsi
- Input `ciphertext` dan `key` untuk proses dekripsi
- Hasil enkripsi dan dekripsi dapat diblok dan dicopy (menggunakan Entry widget readonly)
- Tampilan GUI terstruktur dengan dua panel: Enkripsi dan Dekripsi
- Tombol **Enkripsi/Dekripsi** untuk memproses input
- Tombol **Clear** untuk mereset masing-masing panel

📄 File: `VigenereGUI.py`

---

## 📦 File dalam Folder Ini

| File            | Deskripsi                                   |
|-----------------|---------------------------------------------|
| `VigenereGUI.py`| Program utama Vigenère Cipher dengan GUI    |
| `README.md`     | Penjelasan tentang proyek ini               |

---

## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:
   ```bash
   cd "Vigenere Cipher"
   ```
2. Jalankan program dengan perintah:
   ```bash
   python VigenereGUI.py
   ```

---

## 📝 Catatan
- Program ini hanya mendukung alfabet A-Z (case-insensitive)
- Karakter selain huruf alfabet akan tetap ditampilkan apa adanya
- Key harus berupa huruf (A-Z/a-z) dan tidak boleh kosong
