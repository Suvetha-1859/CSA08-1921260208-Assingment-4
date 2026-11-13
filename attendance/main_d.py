def write_summary(stats, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("RegNo,Present,Total,Percent\n")
        for reg, (p, t, pc) in sorted(stats.items()):
            f.write(f"{reg},{p},{t},{pc}\n")


def write_list(items, path, title):
    with open(path, "w", encoding="utf-8") as f:
        f.write(title + "\n")
        for i in items:
            f.write(i + "\n")


def write_errors(errors, path, source):
    with open(path, "w", encoding="utf-8") as f:
        for n, msg in errors:
            f.write(f"{source} | line {n} | {msg}\n")
