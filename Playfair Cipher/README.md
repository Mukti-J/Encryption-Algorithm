# Project 7: Playfair Cipher GUI

Folder ini berisi implementasi **Playfair Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Playfair Cipher?

Playfair Cipher adalah algoritma kriptografi klasik berbasis **Substitusi Digraf** yang menggunakan sebuah kata kunci (key) untuk mengenkripsi dan mendekripsi pesan. Setiap pasangan huruf (digraf) pada plaintext dienkripsi menggunakan matriks 5x5 yang dibentuk dari key, sehingga lebih aman dibanding cipher sederhana seperti Caesar.

- **Rumus Enkripsi**:
  - Plaintext diubah menjadi pasangan huruf (digraf), huruf yang sama berurutan dipisah dengan 'X', dan jika jumlah huruf ganjil ditambah 'X' di akhir.
  - Setiap digraf dienkripsi berdasarkan posisi pada matriks Playfair:
    - Jika sebaris: geser ke kanan.
    - Jika sekolom: geser ke bawah.
    - Jika membentuk persegi: tukar kolom.

- **Rumus Dekripsi**:
  - Proses kebalikan enkripsi, dengan pergeseran ke kiri/atas.

---

## 🧩 Fitur Program

- Input `plaintext` dan matrix 5x5 custom (bukan key!) untuk proses enkripsi
- Input `ciphertext` dan matrix 5x5 custom untuk proses dekripsi
- Matrix 5x5 dapat diisi manual (A-Z tanpa J, tidak boleh ada huruf sama) atau diacak otomatis
- Validasi matrix: hanya 25 huruf unik, tanpa J
- Hasil enkripsi dan dekripsi dapat diblok dan dicopy (Entry widget readonly)
- Toggle mode Encrypt/Decrypt (label input dan output otomatis berubah)
- Hasil dekripsi otomatis menghilangkan padding X jika ada
- Tampilan GUI sederhana dan mudah digunakan

📄 File: `PlayfairGUI.py`

---

## 📦 File dalam Folder Ini

| File            | Deskripsi                                   |
|-----------------|---------------------------------------------|
| `PlayfairGUI.py`| Program utama Playfair Cipher dengan GUI    |
| `README.md`     | Penjelasan tentang proyek ini               |

---

## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:
   ```bash
   cd "Playfair Cipher"
   ```
2. Jalankan program dengan perintah:
   ```bash
   python PlayfairGUI.py
   ```

---

## 📝 Catatan
- Program ini hanya mendukung alfabet A-Z (case-insensitive, huruf J diganti I)
- Matrix harus diisi 25 huruf unik A-Z tanpa J
- Karakter selain huruf alfabet akan diabaikan dalam proses enkripsi/dekripsi
- Mode Encrypt: input plaintext, output ciphertext
- Mode Decrypt: input ciphertext, output plaintext (padding X otomatis dihapus jika perlu)
