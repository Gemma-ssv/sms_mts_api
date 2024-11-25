"""
Модуль Sms предоставляет класс для отправки SMS-сообщений через API MTS Communicator.
Класс включает методы для инициализации, отправки сообщений и логирования результатов.

Зависимости:
    json: Для сериализации данных в формат JSON.
    base64: Для кодирования учетных данных в формат Base64.
    requests: Для выполнения HTTP-запросов к API.
    config: Модуль, содержащий конфигурационные данные, такие как ID_MTS
"""

import json
import base64
from typing import Dict, List, Union
import requests
from config import ID_MTS


class Sms:
    """
    Класс Sms предоставляет функциональность для отправки SMS-сообщений
    через API MTS Communicator. Он включает методы для инициализации,
    отправки сообщений и логирования результатов.
    """
    def __init__(self, login: str, password: str) -> None:
        """
        Инициализирует объект класса Sms.

        Параметры:
            login (str): Логин для аутентификации в API.
            password (str): Пароль для аутентификации в API.
        """
        self.login = login
        self.password = password

    def send(self, form: str, phone: str, message: str) -> None:
        """
        Отправляет SMS-сообщение на указанный номер телефона.

        Параметры:
            form (str): Имя отправителя (alpha-name).
            phone (str): Номер телефона получателя.
            message (str): Текст сообщения.

        Действия:
            Формирует данные для отправки в формате JSON.
            Создает URL для запроса, используя константу ID_MTS из модуля config.
            Формирует заголовки запроса, включая аутентификацию.
            Отправляет POST-запрос к API.
            Логирует успешный ответ или ошибку.
        """
        data: Dict[str, Union[str, List[str], Dict[str, Dict[str, Union[str, int]]]]] = {
            'phone_number': phone,
            'channels': ['sms'],
            'channel_options': {
                'sms': {
                    'text': message,
                    'alpha_name': form,
                    'ttl': 4000,
                }
            }
        }

        url: str = f'https://api.communicator.mts.by/{ID_MTS}/json2/simple'

        api_username: str = self.login
        api_password: str = self.password

        headers: Dict[str, str] = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + base64.b64encode(
                f'{api_username}:{api_password}'.encode()
            ).decode()
        }

        try:
            response: requests.Response = requests.post(
                url,
                headers=headers,
                data=json.dumps(data),
                timeout=10
            )
            response.raise_for_status()
            self.set_logs(phone, message, response.text)
        except requests.exceptions.RequestException as e:
            if hasattr(e.response, 'status_code'):
                error_message: str = f'Ошибка HTTP: {e.response.status_code}'
            else:
                error_message: str = f'Ошибка cURL: {str(e)}'
            self.set_logs(phone, message, error_message)
            raise e

    def set_logs(self, phone: str, message: str, response: str) -> None:
        """
        Записывает информацию о попытке отправки SMS в файл sms_logs.txt.

        Параметры:
            phone (str): Номер телефона, на который было отправлено сообщение.
            message (str): Текст отправленного сообщения.
            response (str): Ответ от сервера или сообщение об ошибке.
        """
        with open('sms_logs.txt', 'a', encoding='utf-8') as f:
            f.write(
                f"Phone: {phone}, Message: {message}, Response: {response}\n"
            )
