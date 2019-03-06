# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 08:22:34 2019

@author: jdangulo
"""
#Importar librerias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns',20)
#Folder que contiene el proyecto
folder='C:/Data/proyectos/proyecto1/'
#Cargar datos
order_products=pd.read_csv(folder+'order_products_all')
orders=pd.read_csv(folder+'orders.csv')
aisles=pd.read_csv(folder+'aisles.csv')
departments=pd.read_csv(folder+'departments.csv')
products=pd.read_csv(folder+'products.csv')

aisles.shape
aisles.columns
aisles.head()

departments.shape
departments.columns
departments.head()

orders