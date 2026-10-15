import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']= ['SimHei']
plt.rcParams['axes.unicode_minus']= False
df= pd.read_csv('newbj_lianjia.csv', encoding= 'gbk')

df1= df.groupby('district')['ID'].count()
region= df1.index.tolist()
count= df1.values.tolist()

plt.figure(figsize= (12,6))
plt.bar(region, count, width= 0.8)
for x,y in zip (region,count):
    plt.text(x,y, '%.0f' %y, ha= 'center', fontsize= 10)
    
plt.ylabel('数量', fontproperties= 'simhei')
plt.xlabel('城区', fontproperties= 'simhei')

plt.title('各城区房屋数量柱状分布图', fontproperties= 'stkaiti',
          fontsize= 20)

plt.xticks(rotation= 15)

plt.show()