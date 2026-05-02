_NON_SUBTRACTIVE = [
    (1000, "M"),
    (500, "D"),
    (100, "C"),
    (50, "L"),
    (10, "X"),
    (5, "V"),
    (1, "I"),
]


def transform_to_roman(n: int) -> str:
    """Konvertiert eine arabische Zahl in römische Notation (1–3999)."""
    parts: list[str] = []
    remaining = n
    for value, symbol in _NON_SUBTRACTIVE:
        while remaining >= value:
            parts.append(symbol)
            remaining -= value
    return "".join(parts)
