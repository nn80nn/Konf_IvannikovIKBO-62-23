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


