# Project 4: Bacon's Cipher GUI

Folder ini berisi implementasi **Bacon's Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Bacon's Cipher?

Bacon's Cipher adalah metode steganografi klasik yang dikembangkan oleh Francis Bacon. Setiap huruf alfabet dikodekan menjadi lima karakter menggunakan dua simbol berbeda (umumnya 'A' dan 'B'). Setiap huruf memiliki kombinasi unik lima karakter tersebut.

- **Rumus Enkripsi/Dekripsi**:
  - Setiap huruf alfabet (A-Z) diubah menjadi 5 karakter 'A' dan 'B' sesuai tabel Bacon.
  - Proses dekripsi mengembalikan 5 karakter 'A'/'B' menjadi huruf alfabet.

## 🧩 Fitur Program

- Input `plaintext` untuk proses enkripsi
- Input `ciphertext` untuk proses dekripsi
- Hasil enkripsi dan dekripsi dapat diblok dan dicopy (menggunakan Entry widget readonly)
- Tampilan GUI terstruktur dengan dua panel: Enkripsi dan Dekripsi
- Tombol **Enkripsi/Dekripsi** untuk memproses input
- Tombol **Clear** untuk mereset masing-masing panel
- **Fitur Khusus:**
  - Program ini dapat mengenkripsi dan mendekripsi spasi antar kata dengan kode khusus (misal: 'ACENG'), sehingga hasil enkripsi tetap dapat memisahkan kata dengan benar saat didekripsi kembali.

📄 File: `BaconsCipherGUI.py`

---
## 📦 File dalam Folder Ini

| File               | Deskripsi                                   |
|--------------------|----------------------------------------------|
| `BaconsCipherGUI.py` | Program utama Bacon's Cipher dengan GUI      |
| `README.md`        | Penjelasan tentang proyek ini                |

---
## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:
   ```bash
   cd "Bacon's Cipher"
   ```
2. Jalankan program dengan perintah:
   ```bash
   python BaconsCipherGUI.py
   ```

---

## 📝 Catatan
- Program ini hanya mendukung alfabet A-Z (case-insensitive)
- Karakter selain huruf alfabet akan tetap ditampilkan apa adanya
- Tidak memerlukan kunci apapun untuk enkripsi/dekripsi (otomatis)
- **Spasi antar kata akan tetap terjaga pada proses enkripsi dan dekripsi berkat fitur khusus kode spasi**
