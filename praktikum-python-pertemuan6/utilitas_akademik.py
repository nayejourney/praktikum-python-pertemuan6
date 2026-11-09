def hitung_ipk(nilai):
    if not nilai:
        return 0.0
    return sum(nilai) / len(nilai)


def konversi_nilai_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 50:
        return "D"
    return "E"


def generate_transkrip(mahasiswa, nilai):
    return {
        "nama": mahasiswa,
        "nilai": nilai,
        "ipk": round(hitung_ipk(nilai), 2),
        "nilai_huruf": [
            konversi_nilai_huruf(n) for n in nilai
        ]
    }


if __name__ == "__main__":
    print("Modul akademik siap diuji")