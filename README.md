# Vowel Counter — PyTest practice

Небольшой учебный проект на Python: функция для подсчёта гласных в строке + автотесты на **pytest**.

## Что реализуем

- `count_vowels(text: str) -> int` — считает количество гласных в строке без учёта регистра.
- Набор тестов на pytest, покрывающий случаи из задания:

  - строка только из гласных;
  - строка без гласных;
  - смешанные строки (включая верхний и нижний регистр).

## Поддерживаемые гласные

Функция считает гласные:

- латиница: `a, e, i, o, u`
- кириллица: `а, е, ё, и, о, у, ы, э, ю, я`

## Быстрый старт (Windows 11)

Создай и активируй виртуальное окружение:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -U pip
py -m pip install -r requirements.txt
```

Запусти тесты:

```powershell
py -m pytest -q
```

## Использование

```python
from vowel_counter import count_vowels

print(count_vowels("Hello, World!"))  # 3
print(count_vowels("ПрИвЕт, Мир!"))   # 3
```

## Структура проекта

- `vowel_counter.py` — реализация функции
- `tests/test_vowel_counter.py` — тесты pytest
- `requirements.txt` — зависимости (pytest)

## Как проверить, что всё готово

- Команда `py -m pytest -q` отрабатывает без `FAILED`.
- Все требования задания покрыты тестами.
