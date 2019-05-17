# -*- coding: utf-8 -*-
"""
Created on Sat May 11 11:50:58 2019

@author: KIIT
"""

for number in range(1,101):
    if number%3==0 and number%5==0:
        print("FizzBuzz")
        continue
    if number%3==0:
        print("fizz")
        continue
    if number %5==0:
        print("buzz")
        continue
    print(number)
        