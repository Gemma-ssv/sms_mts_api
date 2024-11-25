"""
Модуль примера вызова класса Sms для 
использования возможности отправки смс
с помощью API MTS Communicator
"""

from config import LOGIN_MTS, PASSW_MTS, ALPHA_NAME
from sms_mts import Sms
from utils import input_phone_number, print_sierpinski


# Создание объекта Sms
SMS = Sms(LOGIN_MTS, PASSW_MTS)  

# Вводим номер телефона
PHONE_NUMBER: str = input_phone_number()

# Вводим текст для смс
TEXT: str = input("Введите текст сообщения, который следует отправить:")

try:
    # Отправка смс пользователю
    SMS.send(ALPHA_NAME, PHONE_NUMBER, TEXT)
except Exception as e:
    # Вывод ошибки
    print(e)
finally:
    print("Удачи в подключении!")
    print_sierpinski(4)
