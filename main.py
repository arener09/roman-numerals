_NON_SUBTRACTIVE = [
    (1000, "M"),
    (500, "D"),
    (100, "C"),
    (50, "L"),
    (10, "X"),
    (5, "V"),
    (1, "I"),
]


def _from_glyph_table(n: int, table: list[tuple[int, str]]) -> str:
    parts: list[str] = []
    for value, symbol in table:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def transform_to_roman(n: int) -> str:
    """Konvertiert eine arabische Zahl in römische Notation (1–3999)."""
    return _from_glyph_table(n, _NON_SUBTRACTIVE)
