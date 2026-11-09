import statistics
import math


def hitung_statistik(data):
    if not data:
        return {"error": "Data tidak boleh kosong"}

    modus = statistics.multimode(data)

    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "modus": modus,
        "range": max(data) - min(data),
        "standard_deviation": statistics.pstdev(data)
    }


if __name__ == "__main__":
    nilai = [80, 85, 90, 80, 95, 70]
    hasil = hitung_statistik(nilai)

    for nama, nilai_hasil in hasil.items():
        print(f"{nama}: {nilai_hasil}")