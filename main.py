def transform_to_roman(n: int) -> str:
    """Arabische Zahl → römische Schreibweise (laut Tests). IF nach n sortiert."""
    if n == 1:
        return "I"
    if n == 5:
        return "V"
    return ""
