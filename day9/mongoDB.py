# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:21:26 2019

@author: KIIT
"""

import pymongo


client = pymongo.MongoClient("mongodb://root:Tushar.64@cluster0-shard-00-00-4dcew.mongodb.net:27017,cluster0-shard-00-01-4dcew.mongodb.net:27017,cluster0-shard-00-02-4dcew.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true")

mydb=client.sankalp
def add_student(student_name,student_age,student_roll_no,student_branch) :
    unique_student=mydb.students.find_one({"roll":student_roll_no})
    if unique_student:
        print("Student already exists")
    else:
        mydb.students.insert_one(
            {
             "Name":student_name,
             "Age":student_age,
             "RollNo":student_roll_no,
             "Branch":student_branch
            })
        print("Student added successfully")
def fetch_all_students():
    student=mydb.students.find()
    for i in student:
        print(i)
add_student("Sankalp Sheth",20,1706356,"IT")
add_student('Rohan Wadhwa',20,1706350,'IT')
add_student('Ronit Ray',19,1706353,'CSE')
add_student('Riddhi Paliwal',21,1406256,'ECE')
add_student('Shreya Sanjay',22,2745352,'ETC')
add_student('Aayush Shekhar',18,1306256,'CSE')
add_student('Rishav Jain',21,1706356,'CIVIL')
add_student('Aastha Jain',18,1806426,'MECH')
add_student('Urvi Mehta',21,1816362,'IT')
add_student('Juhi Sheth',20,1736156,'ETC')
fetch_all_students()