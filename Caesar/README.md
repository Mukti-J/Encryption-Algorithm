# Project 1: Caesar Cipher GUI

Folder ini berisi implementasi **Caesar Cipher** dengan antarmuka grafis menggunakan `tkinter`.

## 🔍 Deskripsi

- **Algoritma**: Cipher substitusi klasik  
- **Rumus enkripsi**:  
  \[
    C = (3X + 4) \bmod 26
  \]
- **Rumus dekripsi**:  
  \[
    P = (9X - 10) \bmod 26
  \]
- **Fitur GUI**:  
  - Dua panel: Enkripsi dan Dekripsi  
  - Input `plaintext` & tombol **Enkripsi** → menampilkan `ciphertext`  
  - Input `ciphertext` & tombol **Dekripsi** → menampilkan `plaintext`  
  - Tombol **Clear** untuk mereset masing‑masing panel

## 📦 Berkas

- `Caesar Encryption.py`  
  Script Python lengkap dengan GUI (`tkinter`)

## ⚙️ Prasyarat

- Python 3.6 atau lebih tinggi  
- Modul `tkinter` (biasanya sudah terpasang di distribusi Python standar)

## 🚀 Cara Menjalankan

1. Pastikan kamu berada di folder ini:  
   ```bash
   cd Caesar
