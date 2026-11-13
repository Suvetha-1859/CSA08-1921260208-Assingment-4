class InvalidRecord(Exception):
    """Raised when a registration line is damaged or has bad data."""


class DuplicateRecord(InvalidRecord):
    """Raised when a register number has already been registered."""


def is_valid_email(email):
    """Check an e-mail address using only string methods."""
    if " " in email or email.count("@") != 1:
        return False
    local, domain = email.split("@")
    if not local or "." not in domain:
        return False
    if domain.startswith(".") or domain.endswith(".") or ".." in domain:
        return False
    return True


def parse_record(line):
    """'regno,name,dept,email,ev1;ev2' -> dict, or raise InvalidRecord."""
    parts = [p.strip() for p in line.strip().split(",")]
    if len(parts) != 5:
        raise InvalidRecord(f"expected 5 fields, found {len(parts)}")
    regno, name, dept, email, events = parts
    if not regno.isdigit():
        raise InvalidRecord(f"invalid register number '{regno}'")
    if not name or not dept:
        raise InvalidRecord("name or department is empty")
    email = email.lower()
    if not is_valid_email(email):
        raise InvalidRecord(f"invalid e-mail '{email}'")
    event_list = [e.strip().title() for e in events.split(";") if e.strip()]
    if not event_list:
        raise InvalidRecord("no events chosen")
    return {"regno": regno, "name": name, "dept": dept.upper(),
            "email": email, "events": event_list}
