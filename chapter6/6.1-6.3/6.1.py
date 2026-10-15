# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:19:16 2026

@author: a
"""

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']= ['SimHei']
plt.rcParams['axes.unicode_minus']= False
df= pd.read_csv('newbj_lianjia.csv', encoding= 'gbk')

# 按照城区进行分组，统计租金的平均值
df1= df.groupby('district') ['rent'].mean()
# 获取城区名
region= df1.index.tolist()
# 获取各城区的平均租金
rent= [round(x,2) for x in df1.values.tolist()]
# 绘制各城区房屋租金折线图
plt.figure(figsize= (12, 6))
plt.plot(region, rent, c= 'r', marker= 'o', linestyle= '--')
for x,y in zip(region, rent):
    plt.text(x,y, '% .0f' % y,ha= 'center', fontsize= 11)
# 设置坐标轴标签文本
plt.ylabel('租金/元', fontproperties= 'simhei')
plt.xlabel('城区', fontproperties= 'simhei')
# 设置图形标题
plt.title('各城区房屋平均租金折线图', fontproperties= 'stkaiti',
          fontsize= 14)
# 设置横坐标字体倾斜角度
plt.xticks(rotation= 15)
# 显示图形
plt.show()
