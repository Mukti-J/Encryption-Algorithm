# Project: Beaufort & Variant Beaufort Cipher GUI

Folder ini berisi implementasi **Beaufort Cipher** dan **Variant Beaufort Cipher** dengan antarmuka grafis (GUI) menggunakan `tkinter`.

## 🧠 Apa itu Beaufort Cipher & Variant Beaufort Cipher?

- **Beaufort Cipher** adalah cipher polialfabetik klasik yang mirip dengan Vigenère, namun rumusnya:
  - **Enkripsi/Dekripsi (resiprokal):**
    
    $C_i = (K_i - P_i + 26) \bmod 26$
    
    $P_i = (K_i - C_i + 26) \bmod 26$
    
    - $C_i$ = huruf ke-i pada ciphertext
    - $P_i$ = huruf ke-i pada plaintext
    - $K_i$ = huruf ke-i pada key (diulang/autokey)

- **Variant Beaufort Cipher** adalah varian yang rumusnya:
  - **Enkripsi:**
    
    $C_i = (P_i - K_i + 26) \bmod 26$
    
  - **Dekripsi:**
    
    $P_i = (C_i + K_i) \bmod 26$
    
    - $C_i$ = huruf ke-i pada ciphertext
    - $P_i$ = huruf ke-i pada plaintext
    - $K_i$ = huruf ke-i pada key (diulang/autokey)
  - Tidak resiprokal, dan secara matematis mirip Vigenère tapi urutan operasi berbeda.

### Perbedaan Kunci Penting
- **Beaufort Cipher**: Key digunakan dengan rumus $K_i - P_i$.
- **Variant Beaufort Cipher**: Key digunakan dengan rumus $P_i - K_i$.
- Keduanya mendukung dua mode key:
  - **Repeat**: Key diulang hingga sepanjang pesan.
  - **Autokey**: Key diperpanjang dengan plaintext (saat enkripsi) atau hasil dekripsi (saat dekripsi).

---

## 🧩 Fitur Program
- Input `plaintext` dan `key` untuk enkripsi
- Input `ciphertext` dan `key` untuk dekripsi
- Pilihan **Key Mode**: Repeat & Autokey
- Hasil bisa dicopy, GUI terstruktur dua panel
- Tersedia dua file utama:
  - `BeaufortGUI.py` (Beaufort klasik)
  - `VariantBeaufortGUI.py` (Variant Beaufort)

---

## 📦 File dalam Folder Ini

| File                  | Deskripsi                                         |
|-----------------------|---------------------------------------------------|
| `BeaufortGUI.py`      | Program utama Beaufort Cipher dengan GUI          |
| `VariantBeaufortGUI.py`| Program utama Variant Beaufort Cipher dengan GUI |
| `README.md`           | Penjelasan tentang proyek ini                    |

---

## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:
   ```bash
   cd "Beaufort Cipher"
   ```
2. Jalankan program sesuai kebutuhan:
   ```bash
   python BeaufortGUI.py
   python VariantBeaufortGUI.py
   ```

---

## 📝 Catatan
- Program hanya mendukung alfabet A-Z
- Key harus huruf dan tidak boleh kosong
- Mode key bisa dipilih manual (Repeat/Autokey)
- **Variant Beaufort** bukan sekadar penamaan, tapi benar-benar berbeda di rumus dan cara kerja key-nya!
