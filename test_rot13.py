from rot13 import rot13

"""
Этот модуль тестирует функцию шифрования алгоритмом rot13
"""

def test_1():
    assert rot13("hello") == "uryyb"

def test_2():
    assert rot13("uryyb") == "hello"