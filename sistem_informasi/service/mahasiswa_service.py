mahasiswa_db = {}


def tambah(mahasiswa):
    nim = mahasiswa["nim"]

    if nim in mahasiswa_db:
        return False

    mahasiswa_db[nim] = mahasiswa
    return True


def tampilkan_semua():
    return list(mahasiswa_db.values())


def cari(nim):
    return mahasiswa_db.get(nim)


def ubah(nim, nama, jurusan):
    if nim not in mahasiswa_db:
        return False

    mahasiswa_db[nim]["nama"] = nama
    mahasiswa_db[nim]["jurusan"] = jurusan
    return True


def hapus(nim):
    return mahasiswa_db.pop(nim, None) is not None