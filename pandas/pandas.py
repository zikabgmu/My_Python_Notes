import pandas as pd

"""
df1 = pd.read_csv ('bj_lianjia.csv', encoding= 'utf-8', usecols= ['ID','floor','lift','district','area','rent'])
print(df1)
"""

"""
df2 = pd.read_csv ('bj_lianjia.csv', encoding= 'utf-8', usecols= [0,1,2,3,6,9], index_col= 'ID' )
print(df2[:5])
"""

"""
df3 = pd.read_csv ('bj_lianjia.csv', encoding= 'utf-8', usecols= [0,1,2,3,6,9], names= ['编号','楼层','有无电梯','城区','面积','房租'], skiprows= 1) 
print(df3)
"""


df4 = pd.DataFrame ({'district': ['海淀','房山','顺义','大兴'], 'street': ['清河','良乡','后沙峪','西红门'], 'rent': [8500,3500,6900,3800]}, index= ['a','b','c','d'])
print(df4)
# df4.to_csv('save_df4.txt',sep= '\t')
# df4.to_csv('save_df4.txt', index= False)
df4.to_csv('save_df5.csv', encoding= 'utf-8', header= ['城区','街道','房租'])