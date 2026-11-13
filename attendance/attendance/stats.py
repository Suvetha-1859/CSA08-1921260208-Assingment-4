def percentage(present, total):
    return round(100 * present / total, 2) if total else 0.0


def compute_stats(records):
    counts = {}
    for reg, date, status in records:
        p, t = counts.get(reg, (0, 0))
        counts[reg] = (p + (status == "P"), t + 1)
    return {reg: (p, t, percentage(p, t)) for reg, (p, t) in counts.items()}


def below(stats, limit=75):
    return sorted(reg for reg, (p, t, pc) in stats.items() if pc < limit)
