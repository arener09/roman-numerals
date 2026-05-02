from collections.abc import Sequence

# Absteigend nach Wert: Greedy wählt größtmögliche Teile zuerst.
_ROMAN_GLYPHS_DESC: tuple[tuple[int, str], ...] = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def _from_glyph_table(n: int, table: Sequence[tuple[int, str]]) -> str:
    parts: list[str] = []
    for value, symbol in table:
        while n >= value:
            parts.append(symbol)
            n -= value
    return "".join(parts)


def transform_to_roman(n: int) -> str:
    """Konvertiert eine arabische Zahl in römische Notation (1–3999)."""
    if not (1 <= n <= 3999):
        return ""
    return _from_glyph_table(n, _ROMAN_GLYPHS_DESC)
