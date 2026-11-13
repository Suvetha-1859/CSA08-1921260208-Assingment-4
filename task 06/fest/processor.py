import os
from . import reader, validator, writer


def process_all(input_dir, departments):
    """Read every department file; never stop for a bad line or missing file."""
    seen = set()
    result = {"master": [], "errors": [], "lines": 0, "dept_counts": {}}
    for dept in departments:
        path = os.path.join(input_dir, dept + ".txt")
        name = os.path.basename(path)
        try:
            for line_no, line in reader.read_lines(path):
                result["lines"] += 1
                try:
                    rec = validator.parse_record(line)
                    if rec["regno"] in seen:
                        raise validator.DuplicateRecord(
                            f"duplicate register number {rec['regno']}")
                    seen.add(rec["regno"])
                    result["master"].append(rec)
                    result["dept_counts"][rec["dept"]] = \
                        result["dept_counts"].get(rec["dept"], 0) + 1
                except validator.InvalidRecord as e:    # includes duplicates
                    result["errors"].append((name, line_no, str(e)))
        except FileNotFoundError:
            result["errors"].append((name, 0, "department file missing"))
        except PermissionError:
            result["errors"].append((name, 0, "permission denied"))
        except UnicodeDecodeError as e:
            result["errors"].append((name, 0, f"bad encoding: {e.reason}"))
    return result


def build_event_index(master):
    index = {}
    for r in master:
        for ev in r["events"]:
            index.setdefault(ev, []).append((r["regno"], r["name"]))
    return index


def run(input_dir, out_dir, departments):
    os.makedirs(out_dir, exist_ok=True)
    result = process_all(input_dir, departments)
    index = build_event_index(result["master"])
    writer.write_master(result["master"], os.path.join(out_dir, "master.csv"))
    writer.write_event_files(index, os.path.join(out_dir, "events"))
    writer.write_summary(result, index, os.path.join(out_dir, "summary.txt"))
    writer.write_errors(result["errors"], os.path.join(out_dir, "errors.log"))
    return result, index
