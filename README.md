# Базовый шаблон aiogram бота

Запуск через докер:
```bash
docker build -t aiogram-bot .
docker run -d aiogram-bot 
```

---

Установка без докера: <br>
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
│   main.py  # основной файл бота
│   requirements.txt  # необходимые для работы библиотеки
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
```

Автор: Yarovich
