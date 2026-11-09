# Praktikum Python Pertemuan 6

Repository ini berisi dokumentasi dan hasil pengerjaan Praktikum Python Pertemuan 6 pada mata kuliah Pemrograman Python.

## Informasi Praktikum

| Keterangan | Detail |
|---|---|
| Pertemuan | 6 |
| Bahasa Pemrograman | Python |
| Editor | Visual Studio Code |
| Platform | GitHub |
| Materi | Function, Module, Package, dan Library |

## Tujuan Praktikum

Praktikum ini bertujuan untuk memahami penggunaan fungsi dalam Python, pengelolaan parameter dan nilai balik, ruang lingkup variabel, lambda, serta penerapan module, package, dan library dalam pembuatan program.

## Materi Praktikum

1. Function dan Parameter
2. Return Value
3. Variable Scope (LEGB)
4. Default Parameter
5. Lambda Function
6. Module dan Package
7. Python Standard Library dan External Library
8. Higher-Order Functions

## Hasil Pengerjaan Praktikum

### Praktikum 1. Function Statistik

Membuat fungsi `hitung_statistik()` untuk mengolah sekumpulan data angka.

Perhitungan yang dilakukan:
- Mean (rata-rata)
- Median (nilai tengah)
- Modus (nilai yang paling sering muncul)
- Range (jangkauan nilai)
- Standar deviasi

Library yang digunakan: `statistics`.

### Praktikum 2. Validasi Data

Membuat fungsi `validasi_data()` untuk memeriksa kesesuaian data berdasarkan aturan atau schema.

Fitur:
- Memeriksa tipe data.
- Memeriksa nilai minimum dan maksimum.
- Memeriksa kelengkapan data.
- Menghasilkan status validasi dan daftar kesalahan.

Materi yang diterapkan: `*args` dan `**kwargs`.

### Praktikum 3. Module Akademik

Membuat module `utilitas_akademik.py` yang berisi beberapa fungsi pengolahan data akademik.

Fungsi:
- `hitung_ipk()`
- `konversi_nilai_huruf()`
- `generate_transkrip()`

Program utama menggunakan `main.py` untuk mengimpor dan menjalankan fungsi dari module akademik.

### Praktikum 4. Package Sistem Informasi

Membuat package `sistem_informasi` dengan pembagian subpackage:
- `model`
- `service`
- `utils`

Program menerapkan operasi CRUD (Create, Read, Update, Delete) untuk mengelola data mahasiswa menggunakan dictionary sebagai penyimpanan sementara.

### Praktikum 5. Analisis Data API

Mengambil data dari REST API publik JSONPlaceholder menggunakan library `requests`.

Proses pengolahan:
- Mengambil data dari API.
- Mengolah data menggunakan `lambda`.
- Menggunakan `map()` untuk transformasi data.
- Menggunakan `filter()` untuk penyaringan data.
- Menggunakan `sorted()` untuk pengurutan data.
- Menyimpan hasil analisis ke dalam file JSON.

## Struktur Repository

```text
praktikum-python-pertemuan6/
│
├── README.md
├── statistik.py
├── validasi.py
├── analisis_api.py
├── hasil_api.json
├── main.py
│
└── sistem_informasi/
    ├── __init__.py
    ├── model/
    │   ├── __init__.py
    │   └── mahasiswa.py
    ├── service/
    │   ├── __init__.py
    │   └── mahasiswa_service.py
    └── utils/
        ├── __init__.py
        └── format_data.py
```

## Cara Menjalankan Program

Pastikan Python sudah terinstal di perangkat.

### 1. Menjalankan Function Statistik

```bash
python statistik.py
```

### 2. Menjalankan Validasi Data

```bash
python validasi.py
```

### 3. Menjalankan Module Akademik

Sesuaikan lokasi `main.py` dengan struktur file yang digunakan.

```bash
python main.py
```

### 4. Menjalankan Package Sistem Informasi

```bash
python main.py
```

### 5. Menjalankan Analisis Data API

Instal library requests:

```bash
python -m pip install requests
```

Kemudian jalankan:

```bash
python analisis_api.py
```

Program ini membutuhkan koneksi internet untuk mengambil data dari JSONPlaceholder.

## Dokumentasi Hasil Praktikum

Screenshot hasil pengerjaan dan output program dapat ditambahkan pada repository sebagai bukti pelaksanaan praktikum.

## Teknologi dan Tools

- Python
- Visual Studio Code
- Git
- GitHub
- Requests
- JSON

## Kesimpulan

Melalui praktikum ini, mahasiswa mempelajari penerapan function, parameter, return value, scope, lambda, module, package, dan library dalam Python. Materi diterapkan melalui program pengolahan statistik, validasi data, pengelolaan akademik, CRUD mahasiswa, serta pengolahan data dari REST API publik.

---

**Praktikum Python Pertemuan 6**