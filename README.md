# Проект отправки SMS через API MTS Communicator

Этот проект предоставляет функциональность для отправки SMS-сообщений через API MTS Communicator. Он включает в себя модули для работы с конфигурацией, отправки сообщений, валидации телефонных номеров и генерации треугольника Серпинского.

## Структура проекта

- `main.py`: Основной скрипт, который инициализирует объект класса `Sms` и отправляет SMS-сообщение.
- `config.py`: Модуль для работы с переменными окружения, используя файл `.env`.
- `configs.env`: Файл с переменными окружения, такими как `ALPHA_NAME`, `LOGIN_MTS`, `PASSW_MTS`, и `ID_MTS`.
- `requirements.txt`: Список зависимостей проекта.
- `sms_mts.py`: Модуль, предоставляющий класс `Sms` для отправки SMS-сообщений через API MTS Communicator.
- `utils.py`: Модуль с дополнительными функциями, такими как валидация телефонных номеров и генерация треугольника Серпинского.

## Установка и настройка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/Gemma-ssv/sms_mts_api.git
   cd ваш-проект
   ```

2. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Настройте переменные окружения:**

   Создайте файл `.env` в корне проекта и добавьте в него следующие переменные:

   ```env
   ALPHA_NAME=TEST
   LOGIN_MTS=TEST
   PASSW_MTS=TEST
   ID_MTS=TEST
   ```

   Замените значения на реальные данные для доступа к API MTS Communicator.

## Использование

1. **Запустите основной скрипт:**

   ```bash
   python main.py
   ```

   Программа запросит у вас номер телефона и текст сообщения, который вы хотите отправить. После отправки сообщения будет выведен треугольник Серпинского.

2. **Проверьте логи:**

   После отправки сообщения информация о попытке отправки будет записана в файл `sms_logs.txt`.

## Зависимости

Проект использует следующие зависимости:

- `certifi==2024.8.30`
- `charset-normalizer==3.4.0`
- `idna==3.10`
- `python-dotenv==1.0.1`
- `requests==2.32.3`
- `setuptools==75.6.0`
- `urllib3==2.2.3`

## Лицензия

Этот проект лицензирован под [MIT License](LICENSE).

---

**Удачи в подключении!**
