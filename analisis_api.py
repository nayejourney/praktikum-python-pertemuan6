import requests
import json


def main():
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    users = response.json()

    # map: mengambil nama pengguna
    nama_users = list(
        map(lambda u: u["name"], users)
    )

    # filter: memilih pengguna dengan email .biz
    pengguna_biz = list(
        filter(lambda u: u["email"].endswith(".biz"), users)
    )

    # sorted: mengurutkan pengguna berdasarkan nama
    pengguna_urut = sorted(
        users, key=lambda u: u["name"]
    )

    hasil = {
        "total_pengguna": len(users),
        "nama_pengguna": nama_users,
        "pengguna_email_biz": [
            {
                "nama": u["name"],
                "email": u["email"]
            }
            for u in pengguna_biz
        ],
        "pengguna_urut": [
            {
                "nama": u["name"],
                "email": u["email"]
            }
            for u in pengguna_urut
        ]
    }

    with open("hasil_api.json", "w", encoding="utf-8") as file:
        json.dump(hasil, file, indent=4, ensure_ascii=False)

    print("Total pengguna:", len(users))
    print("Hasil tersimpan di hasil_api.json")


if __name__ == "__main__":
    main()