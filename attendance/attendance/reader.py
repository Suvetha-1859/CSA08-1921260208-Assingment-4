def read_attendance(path):
    """Return (records, errors). records = [(reg, date, status)]."""
    records, errors = [], []
    try:
        with open(path, "r", encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                if not line.strip():
                    continue
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3 or parts[2] not in ("P", "A"):
                    errors.append((n, line.strip()))
                else:
                    records.append(tuple(parts))
    except (FileNotFoundError, PermissionError, UnicodeDecodeError) as e:
        errors.append((0, f"{type(e).__name__}: {path}"))
    return records, errors
