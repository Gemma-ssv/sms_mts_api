"""
Этот модуль предоставляет функциональность для работы с переменными окружения.
Он использует стандартную библиотеку `os` для доступа к переменным окружения
и библиотеку `python-dotenv` для загрузки переменных из файла `.env`.
"""

import os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(__file__), '.', 'configs.env'))

# Альфа имя от мтс
ALPHA_NAME: str = os.getenv('ALPHA_NAME')

# Логин к доступу api мтс
LOGIN_MTS: str = os.getenv('LOGIN_MTS')

# Пароль к api мтс
PASSW_MTS: str = os.getenv('PASSW_MTS')

# id ссылки для доступа к api мтс
ID_MTS:str = os.getenv('ID_MTS')
