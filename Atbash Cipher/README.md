# Project 3: Atbash Cipher GUI

Folder ini berisi implementasi **Atbash Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Atbash Cipher?

Atbash Cipher adalah algoritma kriptografi klasik berbasis **Substitusi Sederhana** yang sangat sederhana, di mana setiap huruf pada alfabet digantikan dengan pasangannya dari urutan terbalik alfabet. Misal: A ↔ Z, B ↔ Y, C ↔ X, dst. Algoritma ini tidak memerlukan kunci khusus.

- **Rumus Enkripsi/Dekripsi**:
  
  Setiap huruf diganti dengan pasangannya dari urutan terbalik alfabet:
  
  - A ↔ Z
  - B ↔ Y
  - C ↔ X
  - ...
  - Z ↔ A

Karena sifatnya yang simetris, proses enkripsi dan dekripsi menggunakan algoritma yang sama.

---
## 🧩 Fitur Program

- Input `plaintext` untuk proses enkripsi
- Input `ciphertext` untuk proses dekripsi
- Hasil enkripsi dan dekripsi dapat diblok dan dicopy (menggunakan Entry widget readonly) 'New Features'
- Tampilan GUI terstruktur dengan dua panel: Enkripsi dan Dekripsi
- Tombol **Enkripsi/Dekripsi** untuk memproses input
- Tombol **Clear** untuk mereset masing-masing panel

📄 File: `AtbashGUI.py`

---
## 📦 File dalam Folder Ini

| File           | Deskripsi                                 |
|----------------|--------------------------------------------|
| `AtbashGUI.py` | Program utama Atbash Cipher dengan GUI     |
| `README.md`    | Penjelasan tentang proyek ini              |

---
## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:
   ```bash
   cd "Atbash Cipher"
   ```
2. Jalankan program dengan perintah:
   ```bash
   python AtbashGUI.py
   ```

---

## 📝 Catatan
- Program ini hanya mendukung alfabet A-Z (case-insensitive)
- Karakter selain huruf alfabet akan tetap ditampilkan apa adanya
- Tidak memerlukan kunci apapun untuk enkripsi/dekripsi (otomatis)
