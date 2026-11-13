from fest import processor

DEPARTMENTS = ["CSE", "ECE", "MECH", "CIVIL", "IT"]

if __name__ == "__main__":
    result, index = processor.run("input", "output", DEPARTMENTS)
    print("Valid registrations :", len(result["master"]))
    print("Rejected            :", len(result["errors"]))
    for e in result["errors"]:
        print("  ", e)
    print("Events              :", {k: len(v) for k, v in sorted(index.items())})
