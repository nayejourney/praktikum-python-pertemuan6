from utilitas_akademik import (
    hitung_ipk,
    konversi_nilai_huruf,
    generate_transkrip
)


if __name__ == "__main__":
    nilai = [85, 90, 78, 92]

    print("IPK:", hitung_ipk(nilai))
    print("Nilai huruf:", konversi_nilai_huruf(85))

    transkrip = generate_transkrip("Naya", nilai)
    print("Transkrip:", transkrip)