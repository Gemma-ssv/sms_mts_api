"""
Модуль для дополнительных функций.
"""

import re
from typing import List

def validate_phone_format(value: str) -> str:
    """
    Проверяет, что телефонный номер соответствует формату +375000000000.

    Параметры:
        value (str): Строка, представляющая телефонный номер.

    Возвращаемое значение:
        str: Отредактированный номер телефона, если формат корректен.

    Исключения:
        ValueError: Если формат некорректен.
    """
    pattern: str = r'^\+375\d{9}$'
    if not re.match(pattern, value):
        raise ValueError("Некорректный формат телефонного номера. Ожидается формат +375000000000.")
    return re.sub(r'\D', '', value)

def input_phone_number() -> str:
    """
    Запрашивает у пользователя ввод телефонного номера и проверяет его формат.

    Возвращаемое значение:
        str: Отредактированный номер телефона, если формат корректен.
    """
    phone: str = input("Введите номер телефона в формате +375XXYYYYYYY:")
    try:
        return validate_phone_format(phone)
    except ValueError as e:
        print(e)
        return input_phone_number()

def sierpinski_triangle(n: int) -> List[str]:
    """
    Генерирует треугольник Серпинского с заданной глубиной.

    Параметры:
        n (int): Глубина треугольника Серпинского.

    Возвращаемое значение:
        List[str]: Список строк, представляющих треугольник Серпинского.
    """
    def sierpinski(n: int) -> List[str]:
        if n == 0:
            return ["*"]
        else:
            prev: List[str] = sierpinski(n - 1)
            space: str = " " * (2 ** (n - 1))
            result: List[str] = []
            for line in prev:
                result.append(space + line + space)
            for line in prev:
                result.append(line + " " + line)
            return result

    return sierpinski(n)

def print_sierpinski(n: int) -> None:
    """
    Выводит треугольник Серпинского с заданной глубиной.

    Параметры:
        n (int): Глубина треугольника Серпинского.
    """
    lines: List[str] = sierpinski_triangle(n)
    for line in lines:
        print(line)
