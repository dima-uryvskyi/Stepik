"""
Выведите таблицу размером n×n, заполненную целыми числами от 1 до n^2
по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.
Формат ввода:
Одна строка, содержащая одно целое число n n, n > 0 n>0.
Формат вывода:
Таблица из n n строк, значения в строках разделены пробелом.

Sample Input:
5

Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9
"""


n = int(input())
result = [[0] * n for i in range(n)]
i, j = 0, 0
for k in range(1, n * n + 1):
    result[i][j] = k
    if k == n * n:
        break
    if i <= j+1 and i + j < n - 1:
        j += 1
    elif i < j and i + j >= n-1:
        i += 1
    elif i >= j and i + j > n-1:
        j -= 1
    elif i > j + 1 and i+j <= n-1:
        i -= 1
for i in range(n):
    print(*result[i])
