﻿//https://www.acmicpc.net/problem/9086

int n = int.Parse(Console.ReadLine());
for(int i = 0; i < n; i++)
{
    string s = Console.ReadLine();
    Console.WriteLine($"{s.First()}{s.Last()}");
}