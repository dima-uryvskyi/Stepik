"""
Напишите программу, которая находит все позиции вхождения подстроки в строку.
Формат ввода:
На первой строке содержится исходная строка, на второй строке ввода указана подстрока, позиции которой требуется найти.
Строки состоят из символов латинского алфавита.
Формат вывода:
Строка, содержащая индексы (индексация начинается с нуля) вхождения подстроки в строку, разделённые пробелом или
число -1 в случае, когда подстрока не найдена.

Sample Input 1:
abacabadaba
aba

Sample Output 1:
0 4 8

Sample Input 2:
aaaa
aa

Sample Output 2:
0 1 2

Sample Input 3:
abc
d

Sample Output 3:
-1
"""


string, word = input(), input()
index = string.find(word)
if index == -1:
    print(index)
else:
    while index != -1:
        print(index, end=" ")
        index = string.find(word, (index+1))
