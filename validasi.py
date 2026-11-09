def validasi_data(data, schema, *args, **kwargs):
    errors = []

    for field, aturan in schema.items():
        if field not in data:
            errors.append(f"{field} wajib tersedia")
            continue

        nilai = data[field]
        tipe = aturan.get("type")

        if tipe and not isinstance(nilai, tipe):
            errors.append(f"{field} harus bertipe {tipe.__name__}")
            continue

        if "min" in aturan and nilai < aturan["min"]:
            errors.append(f"{field} minimal {aturan['min']}")

        if "max" in aturan and nilai > aturan["max"]:
            errors.append(f"{field} maksimal {aturan['max']}")

    if kwargs.get("wajib_email") and "@" not in data.get("email", ""):
        errors.append("Email tidak valid")

    errors.extend(args)

    return len(errors) == 0, errors


if __name__ == "__main__":
    data = {
        "nama": "Naya",
        "umur": 20,
        "email": "naya@example.com"
    }

    schema = {
        "nama": {"type": str},
        "umur": {"type": int, "min": 17, "max": 60},
        "email": {"type": str}
    }

    valid, errors = validasi_data(
        data, schema, wajib_email=True
    )

    print("Valid:", valid)
    print("Errors:", errors)