# Домашнее задание: подсчёт гласных + PyTest

## Цель

Сделать небольшую функцию `count_vowels(text)`, которая считает количество гласных в строке, и написать автоматические тесты на **pytest**, чтобы проверить корректность работы функции.

## Что должно быть в результате

В репозитории должны появиться:

- Функция `count_vowels` (один Python-файл).
- Набор тестов на pytest (отдельный файл в папке `tests/`).

## Подготовка проекта в Cursor на Windows 11

### 1) Создай папку проекта и открой её в Cursor

- Создай папку, например `vowel-counter`.
- Открой её в Cursor: **File → Open Folder...**
- Открой встроенный терминал: **Terminal → New Terminal**

### 2) Виртуальное окружение и установка pytest

В терминале PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -U pip
py -m pip install pytest
```

Проверка, что pytest доступен:

```powershell
py -m pytest --version
```

> Примечание: не запускай никакие серверы на `localhost:8000` (порт занят vLLM). Для этой домашки сервер не нужен.

## Как реализовать функцию

### Рекомендованная спецификация функции

- Функция принимает строку `text`.
- Считает гласные **без учёта регистра**.
- Возвращает целое число.
- Рекомендуемый набор гласных для учебного задания:

  - Английские: `a, e, i, o, u`
  - Русские: `а, е, ё, и, о, у, ы, э, ю, я`

Пример (ориентир, не обязательно копировать один в один):

```python
# vowel_counter.py

VOWELS = set("aeiouаеёиоуыэюя")

def count_vowels(text: str) -> int:
    if not isinstance(text, str):
        raise TypeError("text must be a str")

    return sum(1 for ch in text.casefold() if ch in VOWELS)
```

## Как написать тесты на pytest

### Структура

- Создай папку `tests/`.
- Внутри создай файл `test_vowel_counter.py`.

### Проверки из задания

Тестами нужно покрыть:

- Строка, содержащая только гласные.
- Строка без гласных (ожидаем `0`).
- Смешанные строки (включая **прописные и строчные**).

Удобный формат в pytest — параметризация:

```python
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
def test_only_vowels(text, expected):
    assert count_vowels(text) == expected

@pytest.mark.parametrize(
    "text",
    [
        "",
        "bcdfg",
        "12345",
        "!?.,",
        "йцкнгшщзхфвпрлджчсмтб",
    ],
)
def test_no_vowels(text):
    assert count_vowels(text) == 0

@pytest.mark.parametrize(
    "text, expected",
    [
        ("Hello, World!", 3),  # e, o, o
        ("PyTeSt", 1),         # e
        ("ПрИвЕт, Мир!", 3),   # И, Е, И
    ],
)
def test_mixed_strings(text, expected):
    assert count_vowels(text) == expected
```

## Как выполнять домашку через Cursor-агента

Если используешь **Agent / Auto** режим:

- Положи в корень репозитория файлы `genai-readme.md` и `.cursorrules`.
- В чате Cursor дай короткую команду, например:

```text
Сделай домашку по genai-readme.md. Обязательно:
- используй pytest и параметризацию
- учти Windows 11 (PowerShell команды)
- не запускай сервер на localhost:8000
- используй MCP context7 для проверки pytest-деталей
- в конце запусти py -m pytest -q и исправь ошибки
```

## Проверка перед сдачей

Запусти тесты:

```powershell
py -m pytest -q
```

Ожидаемый результат: все тесты проходят, `FAILED` отсутствует.

## Что сдавать

Обычно достаточно:

- `vowel_counter.py`
- `tests/test_vowel_counter.py`

Если сдаёшь ссылкой на GitHub, добавь в README краткую инструкцию запуска тестов.
