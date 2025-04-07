# Базовый шаблон aiogram бота

Установка:

```bash
git clone https://github.com/yaroniks/aiogram-base
cd aiogram-base
```

Настройте файл .env под себя и далее:

```bash
python -m venv .venv
.venv\scripts\activate  # для windows
source .venv/bin/activate  # для linux
pip install -r requirements.txt
```

Запуск:

```bash
python main.py
```

Структура файлов:

```
│   .env  # все переменные
│   bot.service
│   config.py
│   main.py  # основной файл
│   requirements.txt
│
└───app
    │   commands_handlers.py # обработчик команд
    │   keyboards.py  # кнопки
    │   messages_handlers.py  # обработчик сообщений
    │
    ├───buttons  # обработчик кнопок
    │
    ├───database
    │   │   base.py  # базовый класс sqlalchemy
    │   │
    │   └───models  # модели sqlalchemy
    │
    ├───states  # обработчики состояний
    │
    └───utils  # разные инструменты
            enums.py  # все Enum'ы
            general.py
```
