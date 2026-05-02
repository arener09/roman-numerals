"""Tests für arabische → römische Umwandlung (siehe testfaelle.md)."""

import pytest

from main import transform_to_roman


@pytest.mark.parametrize(
    "arabic,roman",
    [
        (1, "I"),
        (5, "V"),
        (10, "X"),
        (50, "L"),
        (100, "C"),
        (500, "D"),
        (1000, "M"),
    ],
)
def test_basiswerte(arabic, roman):
    assert transform_to_roman(arabic) == roman


@pytest.mark.parametrize(
    "arabic,roman",
    [
        (2, "II"),
        (6, "VI"),
        (60, "LX"),
        (600, "DC"),
    ],
)
def test_wiederholung_und_addition(arabic, roman):
    assert transform_to_roman(arabic) == roman


@pytest.mark.parametrize(
    "arabic,roman",
    [
        (4, "IV"),
        (9, "IX"),
        (40, "XL"),
        (90, "XC"),
        (400, "CD"),
        (900, "CM"),
    ],
)
def test_subtraktion(arabic, roman):
    assert transform_to_roman(arabic) == roman


@pytest.mark.parametrize(
    "arabic,roman",
    [
        (42, "XLII"),
        (99, "XCIX"),
        (2013, "MMXIII"),
        (3999, "MMMCMXCIX"),
    ],
)
def test_zusammengesetzt(arabic, roman):
    assert transform_to_roman(arabic) == roman


@pytest.mark.parametrize("arabic", [0, 4000])
def test_ausserhalb_bereich_leeres_ergebnis(arabic):
    assert transform_to_roman(arabic) == ""
