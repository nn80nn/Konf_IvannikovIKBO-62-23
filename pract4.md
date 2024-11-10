## Задача 1

**Цель:**  
С помощью команд эмулятора Git на сайте https://onlywei.github.io/explain-git-with-d3 или http://git-school.github.io/visualizing-git/ получить состояние проекта слиянием ветки `master` с веткой `first` и перебазированием ветки `second` на `master`.

**Выполнение:**  
Для выполнения задания были использованы команды:
```bash
git checkout master
git merge first
git checkout second
git rebase master
```

**Результат:**  
Ниже представлено изображение графа веток после выполнения команд:

![Git Graph](images/git.png)

---

## Задача 2

**Цель:**  
Создать локальный Git-репозиторий, настроить пользователя `coder1` и почту, добавить файл `prog.py`.

**Команды и вывод:**  
```bash
# Настройка пользователя
git config --global user.name "Coder 1"
git config --global user.email "coder1@example.com"

# Создание локального репозитория
git init my_project

# Переход в каталог проекта
cd my_project

# Создание файла и добавление его в репозиторий
echo "print('Hello, world!')" > prog.py
git add prog.py
git commit -m "Initial commit: add prog.py"
```

**Пример вывода команд:**  
```plaintext
[master (root-commit) 1a2b3c4] Initial commit: add prog.py
 1 file changed, 1 insertion(+)
 create mode 100644 prog.py
```

---

## Задача 3

**Цель:**  
Создать bare-репозиторий `server`, синхронизировать `coder1` и `coder2` с сервером, создать и обновить файл `readme.md`, разрешить конфликты.

**Команды и вывод:**  

```bash
# Создание bare-репозитория
cd ..
git clone --bare my_project server.git

# Подключение удалённого репозитория и отправка данных
cd my_project
git remote add origin ../server.git
git push -u origin master

# Клонирование репозитория и работа от имени coder2
cd ..
git clone server.git coder2_repo
cd coder2_repo
git config user.name "Coder 2"
git config user.email "coder2@example.com"

# Добавление файла readme.md
echo "# Описание программы" > readme.md
git add readme.md
git commit -m "Add readme.md"
git push origin master

# Обновление локального репозитория coder1 и добавление автора
cd ../my_project
git pull origin master
echo "Автор: Coder 1" >> readme.md
git add readme.md
git commit -m "Update readme.md with author information"
git push origin master

# Разрешение конфликта в coder2
cd ../coder2_repo
git pull origin master
# Редактирование readme.md для решения конфликта
echo "Автор: Coder 2" >> readme.md
git add readme.md
git commit -m "Resolve conflict and add Coder 2 information"
git push origin master
```

**Пример вывода `git log` после синхронизации:**  
```plaintext
*   commit a457d748f0dab75b4c642e964172887de3ef4e3e
|\  Merge: 48ce283 d731ba8
| | Author: Coder 2 <coder2@example.com>
| | Date:   Sun Oct 11 11:27:09 2023 +0300
| |
* | commit d731ba8d742a2b4c7f7f9dfd9a1f3a86e2d9e9c5
| | Author: Coder 1 <coder1@example.com>
| | Date:   Sun Oct 11 11:15:42 2023 +0300
| | 
| * commit 48ce2833e163a24847fcdcb9214a768c5d4036d2
|/  Author: Coder 2 <coder2@example.com>
|   Date:   Sun Oct 11 11:02:17 2023 +0300
|   
* commit 1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b
  Author: Coder 1 <coder1@example.com>
  Date:   Sun Oct 11 10:00:00 2023 +0300

Initial commit: add prog.py
```

---
