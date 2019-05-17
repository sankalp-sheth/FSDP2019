# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:16:43 2019

@author: KIIT
"""

import pandas as pd
from selenium import webdriver
from collections import OrderedDict
bid="https://bidplus.gem.gov.in/bidlists"
driver=webdriver.Chrome("C:/Users/KIIT/Desktop/forsk/chromedriver.exe")
driver.get(bid)
bid_no=[]
items=[]
quantity=[]
dept_name=[]
start_date=[]
end_date=[]
for i in range(1,11):
    x_bid_no='//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a'
    bid_no.append(driver.find_element_by_xpath(x_bid_no).text)
    x_items='//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span'
    items.append(driver.find_element_by_xpath(x_items).text)
    x_quantity='//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span'
    quantity.append(driver.find_element_by_xpath(x_quantity).text)
    x_dept_name='//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]'
    dept_name.append(driver.find_element_by_xpath(x_dept_name))
    x_start_date='//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span'
    start_date.append(driver.find_element_by_xpath(x_start_date).text)
    x_end_date='//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span'
    end_date.append(driver.find_element_by_xpath(x_end_date).text)
col_name=['Bid No','Item','Quantity','Department','Start Date','End Date']
col_data=OrderedDict(zip(col_name,[bid_no,items,quantity,dept_name,start_date,end_date]))
df=pd.DataFrame(col_data)
df.to_csv("bid_plus.csv")

