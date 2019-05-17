# -*- coding: utf-8 -*-
"""
Created on Mon May 13 13:22:14 2019

@author: KIIT
"""

week_days=('Monday', 'Wednesday', 'Thursday', 'Saturday')
new_days=(week_days[0],)+("Tuesday",)+week_days[1:3]+("Friday",)+(week_days[-1],)+("Sunday",)
print(new_days)
