# Project 4: Bacon's Cipher GUI

Folder ini berisi implementasi **Bacon's Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Bacon's Cipher?

Bacon's Cipher adalah metode steganografi klasik yang dikembangkan oleh Francis Bacon. Setiap huruf alfabet dikodekan menjadi lima karakter menggunakan dua simbol berbeda (umumnya 'A' dan 'B'). Setiap huruf memiliki kombinasi unik lima karakter tersebut.

- **Rumus Enkripsi/Dekripsi**:
  - Setiap huruf alfabet (A-Z) diubah menjadi 5 karakter 'A' dan 'B' sesuai tabel Bacon.
  - Proses dekripsi mengembalikan 5 karakter 'A'/'B' menjadi huruf alfabet.

### Catatan Sejarah:
Secara historis, pada versi asli Bacon's Cipher, huruf I/J dan U/V menggunakan kode 5-digit biner yang sama karena mengikuti alfabet Latin klasik. Pada implementasi ini, setiap huruf A-Z (26 huruf) memiliki kode unik masing-masing, dan spasi diwakili oleh kode khusus.
> Referensi dan penjelasan lebih lanjut tentang Baconian Cipher dapat dibaca di:
> [privacycanada.net/baconian-cipher/](https://privacycanada.net/baconian-cipher/)

## 🧩 Fitur Program

- Input `plaintext` untuk proses enkripsi
- Input `ciphertext` untuk proses dekripsi
- Hasil enkripsi dan dekripsi dapat diblok dan dicopy (menggunakan Entry widget readonly)
- Tampilan GUI terstruktur dengan dua panel: Enkripsi dan Dekripsi
- Tombol **Enkripsi/Dekripsi** untuk memproses input
- Tombol **Clear** untuk mereset masing-masing panel
- **Fitur Khusus:**
  - Program ini dapat mengenkripsi dan mendekripsi spasi antar kata dengan kode khusus (misal: 'BBABB'), sehingga hasil enkripsi tetap dapat memisahkan kata dengan benar saat didekripsi kembali.
  - Validasi input: hanya huruf A-Z dan spasi yang diperbolehkan. Jika pengguna memasukkan angka atau simbol, akan muncul pesan peringatan bahwa algoritma ini kuno dan tidak mendukung karakter tersebut.
  - Pesan error/penjelasan yang ramah pengguna jika input tidak valid.

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
- Karakter selain huruf alfabet dan spasi tidak didukung, dan akan memunculkan peringatan
- Tidak memerlukan kunci apapun untuk enkripsi/dekripsi (otomatis)
- **Spasi antar kata akan tetap terjaga pada proses enkripsi dan dekripsi berkat fitur khusus kode spasi ('BBABB')**
- Pesan error akan muncul jika input mengandung angka atau simbol, sesuai dengan keterbatasan algoritma kuno ini
- Pada versi asli Bacon's Cipher, I/J dan U/V menggunakan kode yang sama, namun pada implementasi ini setiap huruf memiliki kode unik.
