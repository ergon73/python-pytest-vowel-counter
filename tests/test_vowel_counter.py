"""Тесты для vowel_counter."""

import pytest

from vowel_counter import count_vowels


@pytest.mark.parametrize(
    "text, expected",
    [
        ("aeiou", 5),
        ("AEIOU", 5),
        ("АЕЁИОУЫЭЮЯ", 10),
    ],
)
def test_only_vowels(text: str, expected: int) -> None:
    """Строка только из гласных."""
    assert count_vowels(text) == expected


@pytest.mark.parametrize(
    "text",
    [
        "",
        "bcdfg",
        "12345",
        "!?.,-",
        "йцкнгшщзхфвпрлджчсмтб",
    ],
)
def test_no_vowels(text: str) -> None:
    """Строка без гласных."""
    assert count_vowels(text) == 0


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello, World!", 3),
        ("PyTeSt", 1),
        ("ПрИвЕт, Мир!", 3),
    ],
)
def test_mixed_strings(text: str, expected: int) -> None:
    """Смешанные строки (гласные и негласные, разный регистр)."""
    assert count_vowels(text) == expected


def test_type_error() -> None:
    """TypeError при не-str аргументе."""
    with pytest.raises(TypeError):
        count_vowels(123)
