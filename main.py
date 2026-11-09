from sistem_informasi.model.mahasiswa import buat_mahasiswa
from sistem_informasi.service import mahasiswa_service as service
from sistem_informasi.utils.format_data import format_mahasiswa


if __name__ == "__main__":
    mhs = buat_mahasiswa(
        "20241320021", "Khanaya", "Sistem Informasi"
    )

    print("Tambah:", service.tambah(mhs))

    data = service.cari("20241320021")
    print(format_mahasiswa(data))

    service.ubah(
        "20241320021", "Khanaya Salsabila", "Sistem Informasi"
    )

    print("Setelah diubah:")
    for item in service.tampilkan_semua():
        print(format_mahasiswa(item))

    print("Hapus:", service.hapus("20241320021"))
    print("Data akhir:", service.tampilkan_semua())