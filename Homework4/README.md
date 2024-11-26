# 1. Клонирование репозитория

Склонируйте репозиторий с исходным кодом и тестами:

```bash
git clone <URL репозитория>
cd <директория проекта>
```

# 2. Установка зависимостей и запуске
Тесты не требуют внешних зависимостей

# Создайте виртуальное окружение
python -m venv venv

```bash
# Активируйте виртуальное окружение
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для MacOS/Linux:
source venv/bin/activate
```

## Запуск
```bash
python assembler.py program.asm program.bin log.yaml
python interpreter.py program.bin result.yaml
```

# 3. Структура проекта
Проект содержит следующие файлы и директории, связанные с тестированием:
```bash
assembler.py           # Файл с реализацией команд
interpreter.py      # Файл с тестами для команд
result.yaml        # Файл с результатами
log.yaml # лог файл      # Файл с логами
program.asm       # Исходные команды
program.bin       # Команды в бинарном формате
```

