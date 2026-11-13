def read_lines(path):
    """Yield (line_number, line) one at a time; blank lines are skipped."""
    with open(path, "r", encoding="utf-8") as f:
        for n, line in enumerate(f, start=1):
            if line.strip():
                yield n, line
