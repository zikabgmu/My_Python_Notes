import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import linear_model
df1=pd.read_csv('newbj_LianJia.csv', header=0,
                usecols=[1,2,3,4,5,6,7,8,9,10], encoding='gbk')
print(df1)
def apart_room(x):
    '''
    分割字符串，提取“室”
    '''
    room=x.split('室')[0]
    return int(room)
def apart_hall(x):
    '''
    分割字符串,提取"厅"
    '''
    hall=x.split('厅')[0].split('室')[1]
    return int(hall)
def apart_wc(x):
    '''
    分割字符串,提取"卫"
    '''
    wc=x.split('卫')[0].split('厅')[1]
    return int(wc)

df1['bedroom']=df1['model'].map(apart_room)
df1['livingroom']=df1['model'].map(apart_hall)
df1['bathroom']=df1['model'].map(apart_wc)
df1.drop(columns=['model'],inplace=True)       #删除原数据集中的 model 列

# 对floot和lift属性进行自定义编码
map1= {'地下室':0, '低楼层':1, '中楼层':2, '高楼层':3}
df1['floor']= df1['floor'].map(map1)
map2= {'未知':3, '有':1, '无':2}
df1['lift']=df1['lift'].map(map2)

#对 district,street,community 和 toward 属性使用 LabelEncoder 进行编码
labelE=LabelEncoder()

labelE.fit(df1['district'])
df1['district']=labelE.transform(df1['district'])

labelE.fit(df1['street'])
df1['street']=labelE.transform(df1['street'])

labelE.fit(df1['community'])
df1['community']=labelE.transform(df1['community'])

labelE.fit(df1['toward'])
df1['toward']=labelE.transform(df1['toward'])

# 将重新编码后的数据保存为 rent.csv 文件
df1.to_csv('rent.csv', index=False)

df2=df1.drop(columns=['rent'])
y=df1['rent'].values
colname=df2.columns
plt.rcParams['font.sans-serif']=['SimHei']           #调整字体设置
plt.figure(figsize=(18,20))
plt.subplots_adjust(wspace=0)
xlabel_dicts={"floor":"楼层","lift":"有无电梯","district":"城区名","street":"街道名",
              "community":"小区名","area":"面积","toward":"房屋朝向","totalfloor":"总楼层",
              "bedroom":"卧室数","livingroom":"客厅数","bathroom":"卫生间数"}
                                                              #设置图中特征属性名为中文

for i in range(11):
    plt.subplot(6,2,i+1)
    plt.scatter(df2[colname[i]],y)
    plt.xlabel(xlabel_dicts[colname[i]])
    plt.ylabel('租金/元')
plt.tight_layout()
plt.show()

corr = df1[['floor', 'lift', 'district', 'street', 'community', 'area', 'toward',
            'totalfloor','bedroom', 'livingroom', 'bathroom', 'rent']].corr()
print(corr)

x=df1['area']
y=df1['rent']
x=np.array([x]).T
y=np.array([y]).T

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, test_size=0.20)

lr = linear_model.LinearRegression()
lr.fit(x_train, y_train)

# 截距 b
b = lr.intercept_

# 斜率 k
k = lr.coef_

print('线性方程的截距为：', b)
print('线性方程的斜率为：', k)

# 输出线性回归方程
print('rent=', '(', round(k[0,0], 2), ')', ' * ', 'area', '+', '(', round(b[0], 2), ')')

plt.rcParams['font.sans-serif'] = ['SimHei']    #调整字体设置
plt.plot(x_train, y_train, 'k.')
y1 = k * x_train + b
plt.plot(x_train, y1, 'r-')
plt.xlabel('面积')
plt.ylabel('租金/元')
plt.show()


from sklearn.metrics import r2_score

y_pred_test = lr.predict(x_test)

print("测试集的决定系数={:.3f}".format(lr.score(x_test, y_test)))
print("测试集的决定系数={:.3f}".format(r2_score(y_test, y_pred_test)))

print("训练集的决定系数={:.3f}".format(lr.score(x_train, y_train)))


