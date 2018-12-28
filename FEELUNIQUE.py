# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 19:56:29 2018

@author: Aouissat_salsabil
"""
import pandas as pd 
feelunique=pd.read_csv('base_feelunique.txt',sep=";",encoding = "latin1")
feelunique.describe()
feelunique.info()
feelunique.isnull().sum()
#first commentaire