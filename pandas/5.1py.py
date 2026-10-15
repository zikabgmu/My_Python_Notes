# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:59:36 2026

@author: a
"""

import pandas as pd

"""
s1= pd.Series(['海淀','房山','顺义','大兴'])

print (s1)
"""


# s2= pd.Series(['海淀','房山','顺义','大兴'], index= ['a','b','c','d'])
# print (s2)
df5_6= pd.read_csv('bj_lianjia.csv', encoding= 'gbk', index_col= ['ID'])

df5_6.duplicated(subset= None, keep= 'first')
"""
print ('----总行数----')
print(len(df5_6))
print ('----重复行----')
print(df5_6[df5_6.duplicated()])
print ('----指定列的重复项----')
print(df5_6[df5_6.duplicated(['district', 'area', 'rent'])])
print ('----显示不重复地“district值”----')
print(df5_6[df5_6.duplicated('district') == False]['district'])
"""


"""
# (2)
print('----删除重复数据----')
print(df5_6.drop_duplicates (subset= None, keep= 'first', inplace= False))
"""


from copy import deepcopy

dff= deepcopy(df5_6)
print('----删除重复行（指定inplace参数）----')
df= dff.drop_duplicates(inplace= False)
print(len(df))

print('----打印含有空值的行数----')
print(df5_6.isnull().sum())


dff= deepcopy(df5_6)
print('----删除全为空值的那些行----')
dff.dropna(how= 'all', inplace= True)
print(dff.isnull().sum())
print('----删除lift列中有缺失值的行----')
dff.dropna(subset= ['lift'], inplace= True)
print(dff.isnull().sum())
























