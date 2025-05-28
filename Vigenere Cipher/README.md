# Project 5: Vigenère Cipher GUI

Folder ini berisi implementasi **Vigenère Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Vigenère Cipher?

Vigenère Cipher adalah algoritma kriptografi klasik berbasis **Substitusi Polialfabetik** yang menggunakan sebuah kata kunci (key) untuk mengenkripsi dan mendekripsi pesan. Setiap huruf pada plaintext digeser sesuai urutan huruf pada key, sehingga lebih aman dibanding Caesar Cipher.

- **Rumus Enkripsi**:
  
  Setiap huruf pada plaintext digeser sebanyak nilai alfabet pada huruf key (berulang jika key lebih pendek dari plaintext).
  
  $C_i = (P_i + K_i) \bmod 26$
  
  - $C_i$ = huruf ke-$_i pada ciphertext
  - $P_i$ = huruf ke-$_i pada plaintext (dalam bentuk indeks 0-25)
  - $K_i$ = huruf ke-$_i pada key (dalam bentuk indeks 0-25, diulang atau autokey)

- **Rumus Dekripsi**:
  
  Setiap huruf pada ciphertext digeser mundur sebanyak nilai alfabet pada huruf key.
  
  $P_i = (C_i - K_i + 26) \bmod 26$
  
  - $P_i$ = huruf ke-$_i pada plaintext
  - $C_i$ = huruf ke-$_i pada ciphertext
  - $K_i$ = huruf ke-$_i pada key

---

## 🧩 Fitur Program

- Input `plaintext` dan `key` untuk proses enkripsi
- Input `ciphertext` dan `key` untuk proses dekripsi
- Hasil enkripsi dan dekripsi dapat diblok dan dicopy (menggunakan Entry widget readonly)
- Tampilan GUI terstruktur dengan dua panel: Enkripsi dan Dekripsi
- Tombol **Enkripsi/Dekripsi** untuk memproses input
- Tombol **Clear** untuk mereset masing-masing panel
- **Key Mode**: Mendukung dua mode key: `New Features`
  - **Repeat**: Key diulang hingga sepanjang plaintext/ciphertext
  - **Autokey**: Key diperpanjang dengan plaintext (saat enkripsi) atau plaintext hasil dekripsi (saat dekripsi)
- **VigenereGUI.py**: Mode dekripsi otomatis menyesuaikan dengan mode enkripsi (tidak perlu memilih mode saat dekripsi)
- **VigenereGUIver2.py**: Pengguna dapat memilih mode key (Repeat/Autokey) baik saat enkripsi maupun dekripsi (fleksibel, cocok untuk eksperimen)

📄 File: `VigenereGUI.py`, `VigenereGUIver2.py`

---

## 📦 File dalam Folder Ini

| File                | Deskripsi                                               |
|---------------------|--------------------------------------------------------|
| `VigenereGUI.py`    | Program utama Vigenère Cipher dengan GUI (mode default)|
| `VigenereGUIver2.py`| Versi lanjutan: user bisa pilih key mode saat dekripsi |
| `README.md`         | Penjelasan tentang proyek ini                          |

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
   # atau untuk versi 2
   python VigenereGUIver2.py
   ```

---

## 📝 Catatan
- Program ini hanya mendukung alfabet A-Z (case-insensitive)
- Karakter selain huruf alfabet akan tetap ditampilkan apa adanya
- Key harus berupa huruf (A-Z/a-z) dan tidak boleh kosong
- Pada versi 2, mode key saat dekripsi bisa dipilih manual (Repeat/Autokey) sesuai kebutuhan/eksperimen
