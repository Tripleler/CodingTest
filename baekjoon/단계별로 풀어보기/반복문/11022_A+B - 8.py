# https://www.acmicpc.net/problem/11022

from sys import stdin

input = stdin.readline
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')
