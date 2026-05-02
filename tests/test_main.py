"""Ein konkreter Test je Fall — siehe testfaelle.md (kein parametrize)."""

from main import transform_to_roman

def arabisch_1_wird_I() -> None:
    assert transform_to_roman(1) == "I"

def arabisch_5_wird_V() -> None:
    assert transform_to_roman(5) == "V"
