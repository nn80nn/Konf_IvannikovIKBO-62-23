Задача 1
Вывести служебную информацию о пакете matplotlib (Python). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
![image](https://github.com/user-attachments/assets/5f6fc0ae-d6b5-443a-8641-73b1cffb55ce)
![image](https://github.com/user-attachments/assets/15d25b2e-b8dc-4446-9f48-9c1ff371b7b8)

Задача 2
Вывести служебную информацию о пакете express (JavaScript). Разобрать основные элементы содержимого файла со служебной информацией из пакета. Как получить пакет без менеджера пакетов, прямо из репозитория?
![image](https://github.com/user-attachments/assets/862595a6-4fb0-4430-8dae-a5e6a2f0484b)

https://github.com/expressjs/express

![Uploading image.png…]()


Задача 3
Сформировать graphviz-код и получить изображения зависимостей matplotlib и express.

![image](https://github.com/user-attachments/assets/ad48c278-bb24-4b06-bfd5-ae82b8dcf150)
![graphviz](https://github.com/user-attachments/assets/fb595fc5-39eb-4ad2-a10c-19cc4ca16d00)

![image](https://github.com/user-attachments/assets/2f82c411-734b-4f57-8021-68cdacb04c82)
![graphviz (1)](https://github.com/user-attachments/assets/badefe28-1aa7-4dfc-8f81-ac7480244ab7)



Задача 4
Следующие задачи можно решать с помощью инструментов на выбор:

Решатель задачи удовлетворения ограничениям (MiniZinc).
SAT-решатель (MiniSAT).
SMT-решатель (Z3).
Изучить основы программирования в ограничениях. Установить MiniZinc, разобраться с основами его синтаксиса и работы в IDE.

Решить на MiniZinc задачу о счастливых билетах. Добавить ограничение на то, что все цифры билета должны быть различными (подсказка: используйте all_different). Найти минимальное решение для суммы 3 цифр.

Задача 5
Решить на MiniZinc задачу о зависимостях пакетов для рисунка, приведенного ниже.

![image](https://github.com/user-attachments/assets/24804dec-d179-416e-a90e-c2a3a4c66387)


Задача 6
Решить на MiniZinc задачу о зависимостях пакетов для следующих данных:

root 1.0.0 зависит от foo ^1.0.0 и target ^2.0.0.
foo 1.1.0 зависит от left ^1.0.0 и right ^1.0.0.
foo 1.0.0 не имеет зависимостей.
left 1.0.0 зависит от shared >=1.0.0.
right 1.0.0 зависит от shared <2.0.0.
shared 2.0.0 не имеет зависимостей.
shared 1.0.0 зависит от target ^1.0.0.
target 2.0.0 и 1.0.0 не имеют зависимостей.

![image](https://github.com/user-attachments/assets/9d337a9e-bef4-438b-8590-25a6f47d755c)



Задача 7
Представить задачу о зависимостях пакетов в общей форме. Здесь необходимо действовать аналогично реальному менеджеру пакетов. То есть получить описание пакета, а также его зависимости в виде структуры данных. Например, в виде словаря. В предыдущих задачах зависимости были явно заданы в системе ограничений. Теперь же систему ограничений надо построить автоматически, по метаданным.

![image](https://github.com/user-attachments/assets/5f771cea-f518-4af9-8adb-eb4e4af5a11a)

![image](https://github.com/user-attachments/assets/f9c97791-4ede-48a5-83c9-02dd1b0baf34)
