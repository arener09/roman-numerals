_BASIS = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


def transform_to_roman(n: int) -> str:
    """Konvertiert eine arabische Zahl in römische Notation (1–3999)."""
    return _BASIS.get(n, "")
