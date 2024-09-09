Задача 1
Вывести отсортированный в алфавитном порядке список имен пользователей в файле passwd (вам понадобится grep).

[mn@archlinux ~]$ grep -o '^[^:]*:' /etc/passwd | cut -d: -f1 | sort
![image](https://github.com/user-attachments/assets/07425d90-ae85-4b09-b405-133399315fb0)



Задача 2
Вывести данные /etc/protocols в отформатированном и отсортированном порядке для 5 наибольших портов, как показано в примере ниже:

cat /etc/services | sort -k 2 -n | tail -n 5
![image](https://github.com/user-attachments/assets/fbfbccf0-332e-4b8e-8fa7-dd24533305f1)


Задача 3
Написать программу banner средствами bash для вывода текстов, как в следующем примере (размер баннера должен меняться!):

[root@localhost ~]# ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
Перед отправкой решения проверьте его в ShellCheck на предупреждения.

 ./banner.sh "Hello from RTU MIREA!"
 ![image](https://github.com/user-attachments/assets/94e2662f-e4c2-400c-b0b4-d49e9e69b0a4)
![image](https://github.com/user-attachments/assets/931dc141-3716-4ed2-be60-ae790a0b3993)

Задача 4
Написать программу для вывода всех идентификаторов (по правилам C/C++ или Java) в файле (без повторений).

Пример для hello.c:

h hello include int main n printf return stdio void world
![image](https://github.com/user-attachments/assets/cde13384-d69e-4c35-a983-5a68b524925a)
![image](https://github.com/user-attachments/assets/433afe6f-6567-47e6-b217-018af8152f76)

Задача 5
Написать программу для регистрации пользовательской команды (правильные права доступа и копирование в /usr/local/bin).

Например, пусть программа называется reg:

./reg banner
В результате для banner задаются правильные права доступа и сам banner копируется в /usr/local/bin.
![image](https://github.com/user-attachments/assets/b7accc1c-fe57-45ed-9fae-48189bf757b3)
![image](https://github.com/user-attachments/assets/95450faa-c0bc-4364-9421-b4c102eb5d18)

Задача 6
Написать программу для проверки наличия комментария в первой строке файлов с расширением c, js и py.
![image](https://github.com/user-attachments/assets/b1da7926-b376-43af-9e5d-fe4bd813c33b)
![image](https://github.com/user-attachments/assets/79beab5a-0486-4593-968b-828e7356b011)

Задача 7
Написать программу для нахождения файлов-дубликатов (имеющих 1 или более копий содержимого) по заданному пути (и подкаталогам).
![image](https://github.com/user-attachments/assets/62c8f7e8-e424-4022-ad3f-174b28859416)
![image](https://github.com/user-attachments/assets/2e17e0bf-e585-47a8-a56d-56e5923df358)

Задача 8
Написать программу, которая находит все файлы в данном каталоге с расширением, указанным в качестве аргумента и архивирует все эти файлы в архив tar.
![image](https://github.com/user-attachments/assets/babac699-74f1-497a-ad27-e789be1835aa)
![image](https://github.com/user-attachments/assets/30f7bd94-37bb-42c3-aa4c-884e2f0da4af)

Задача 9
Написать программу, которая заменяет в файле последовательности из 4 пробелов на символ табуляции. Входной и выходной файлы задаются аргументами.
![image](https://github.com/user-attachments/assets/fdc72567-dd92-4265-836d-1f26910b260e)
![image](https://github.com/user-attachments/assets/1cd1825d-52a9-464f-8848-6974c43aac03)

Задача 10
Написать программу, которая выводит названия всех пустых текстовых файлов в указанной директории. Директория передается в программу параметром.
![image](https://github.com/user-attachments/assets/f1a8013f-8f79-4dcf-a05c-afef6c5478e1)
![image](https://github.com/user-attachments/assets/bea25192-25cc-4028-8360-0d756af11727)

