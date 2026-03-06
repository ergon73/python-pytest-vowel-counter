"""Подсчёт гласных в строке."""

VOWELS = frozenset("aeiouаеёиоуыэюя")


def count_vowels(text: str) -> int:
    """Возвращает количество гласных в строке без учёта регистра."""
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return sum(1 for ch in text.casefold() if ch in VOWELS)
