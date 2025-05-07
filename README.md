# Базовый шаблон aiogram бота

Установка:

```bash
git clone https://github.com/yaroniks/aiogram-base.git
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

---

Структура файлов:

```
│   .env  # переменные
│   bot.py  # бот и диспетчер
│   config.py  # настройки, доступ к .env
│   docker-compose.yml
│   Dockerfile
│   main.py  # основной файл бота
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
    │   │   base.py  # базовый класс
    │   │
    │   └───models  # модели sqlaclhemy и запросы в бд
    │
    ├───states  # обработчики состояний
    │
    └───utils  # разные инструменты
            enums.py  # все Enum'ы
            general.py
```
