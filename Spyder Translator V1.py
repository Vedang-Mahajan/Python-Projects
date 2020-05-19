# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:17:39 2020

@author: Vedang Mahajan
"""

Sample={
        "Square":"Cube",
        "Triangle":"Cone",
        "Rectangle":"Cuboid",
        "Circle":"Sphere",
        }

shape_name=input("Enter the shape name: ")

if shape_name==Sample.keys():   
    print("Works!")
else:
    print("Bad Luck!")
