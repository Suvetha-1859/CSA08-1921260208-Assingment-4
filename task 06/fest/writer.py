import os


def _safe_name(event):
    return "".join(c if c.isalnum() else "_" for c in event.lower())


def write_master(master, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("RegNo,Name,Dept,Email,Events\n")
        for r in master:
            f.write(f"{r['regno']},{r['name']},{r['dept']},{r['email']},"
                    f"{';'.join(r['events'])}\n")


def write_event_files(index, folder):
    os.makedirs(folder, exist_ok=True)
    for event, people in sorted(index.items()):
        path = os.path.join(folder, _safe_name(event) + ".txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Participants for {event}\n")
            for regno, name in people:
                f.write(f"{regno},{name}\n")


def write_summary(result, index, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("FEST REGISTRATION SUMMARY\n")
        f.write(f"Lines read        : {result['lines']}\n")
        f.write(f"Valid (master)    : {len(result['master'])}\n")
        f.write(f"Rejected          : {len(result['errors'])}\n")
        f.write("Per department:\n")
        for dept, n in sorted(result["dept_counts"].items()):
            f.write(f"  {dept}: {n}\n")
        f.write("Per event:\n")
        for event, people in sorted(index.items()):
            f.write(f"  {event}: {len(people)}\n")


def write_errors(errors, path):
    with open(path, "w", encoding="utf-8") as f:
        for source, line_no, msg in errors:
            f.write(f"{source} | line {line_no} | {msg}\n")
