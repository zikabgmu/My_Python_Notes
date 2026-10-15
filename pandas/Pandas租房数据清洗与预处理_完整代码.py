import pandas as pd
import re
# 步骤一：读取数据
# 读取列

df = pd.read_csv('bj_lianJia.csv', encoding='gbk', header=0,
                 usecols=[1, 2, 3, 4, 5, 6, 7, 8, 9])

# 打印 DataFrame 查看前几行
print("=" * 60)
print("【步骤一：读取数据】")
print("=" * 60)
print(f"读取到 {len(df)} 行数据")
print(f"列名: {list(df.columns)}")
print("\n前5行数据:")
print(df.head().to_string())

# 步骤二：重复值处理
# 使用 df.duplicated() 
# 打印删除后的行数

print("\n" + "=" * 60)
print("【步骤二：重复值处理】")
print("=" * 60)

# 检测重复行
dup_count = df.duplicated().sum()
print(f"检测到的重复行数: {dup_count}")

# 删除重复行（保留第一次出现的行）
df.drop_duplicates(inplace=True)
print(f"删除重复行后剩余行数: {len(df)}")
print("\n删除重复行后的数据:")
print(df.head().to_string())

# 步骤三：缺失值处理
# 使用 df.isnull().sum() 统计各列缺失值,
# 使用 reset_index(drop=True) 重置索引
print("\n" + "=" * 60)
print("【步骤三：缺失值处理】")
print("=" * 60)

# 统计各列缺失值
print("各列缺失值统计:")
print(df.isnull().sum())

# lift列缺失值：用'未知'填充
df['lift'] = df['lift'].fillna('未知')
print('\nlift列缺失值已用未知填充')

# rent列缺失值：删除该行
before_drop = len(df)
df = df.dropna(subset=['rent'])
print(f"删除rent列缺失行: {before_drop} -> {len(df)} 行")

# 重置索引
df = df.reset_index(drop=True)
print("\n索引已重置")
print("\n缺失值处理后的数据:")
print(df.head().to_string())

# 步骤四：内容格式清洗
print("\n" + "=" * 60)
print("【步骤四：内容格式清洗】")
print("=" * 60)
# ① area列：提取数字，去除单位
print("\n--- area列清洗 ---")
print("清洗前:")
print(df['area'].head().to_string())

def extract_number(s):
    """从字符串中提取数字"""
    match = re.findall(r'\d+\.?\d+', str(s))
    return match[0] if match else s

df['area'] = df['area'].apply(extract_number)
# 将area列转换为数值类型
df['area'] = pd.to_numeric(df['area'], errors='coerce')
print("清洗后:")
print(df['area'].head().to_string())

# ② toward列：删除空格
print("\n--- toward列清洗 ---")
print("清洗前:")
print(df['toward'].head().to_string())

df['toward'] = df['toward'].str.replace(r'\s+', '', regex=True)
print("清洗后:")
print(df['toward'].head().to_string())

# ③ model列：统一为 *室*厅*卫 格式
print("\n--- model列清洗 ---")
print("清洗前:")
print(df['model'].head().to_string())

def clean_model(s):
    """清洗model列，统一为 *室*厅*卫 格式"""
    # 将'未知'替换为'0'
    if s == '未知':
        s = '0'
    # 使用正则提取数字
    nums = re.findall(r'\d+', str(s))
    # 长度为3则拼接为 m[0]室 m[1]厅 m[2]卫
    if len(nums) == 3:
        return f"{nums[0]}室{nums[1]}厅{nums[2]}卫"
    # 长度为2则拼接为 m[0]室 0厅 m[1]卫
    elif len(nums) == 2:
        return f"{nums[0]}室0厅{nums[1]}卫"
    elif len(nums) == 1:
        return f"{nums[0]}室0厅0卫"
    return s

df['model'] = df['model'].apply(clean_model)
print("清洗后:")
print(df['model'].head().to_string())
# 步骤五：属性重构造，
# 使用 df['floor'].str.split('/', expand=True) 拆分 floor 列
print("\n" + "=" * 60)
print("【步骤五：属性重构造】")
print("=" * 60)

print("\n拆分前 floor 列:")
print(df['floor'].head().to_string())

# 使用 str.split 拆分 floor 列
split_result = df['floor'].str.split('/', expand=True)

# 查看拆分结果
floor_part0 = split_result.iloc[:, 0]
floor_part1 = split_result.iloc[:, 1]

# 第0列写回 df['floor']
df['floor'] = floor_part0
totalfloor_extracted = floor_part1.str.replace('层', '', regex=False)
df['totalfloor'] = totalfloor_extracted.str.extract(r'(\d+)')[0]
df['totalfloor'] = pd.to_numeric(df['totalfloor'], errors='coerce')

print("\n拆分后:")
print("floor列:", df['floor'].head().to_string())
print("totalfloor列:", df['totalfloor'].head().to_string())

# 步骤六：数据保存
print("\n" + "=" * 60)
print("【步骤六：数据保存】")
print("=" * 60)

df.index.name = 'ID'
df.to_csv('newbj_lianJia.csv', encoding='gbk', index=True)
print("数据已保存到 newbj_lianJia.csv")
print("\n最终数据预览:")
print(df.to_string())





# Numpy 综合操作
print("\n" + "=" * 60)
print("【Numpy综合操作 - 练习1】")
print("=" * 60)

# 使用指定的参数读取数据（usecols指定列名，index_col指定索引列）
try:
    df5_4 = pd.read_csv('bj_lianJia.csv', encoding='gbk',
                        usecols=['ID', 'floor', 'lift', 'district', 'area', 'rent'],
                        index_col='ID')
    print("使用指定列名读取数据成功:")
    print(df5_4.head().to_string())
    print(f"\n数据形状: {df5_4.shape}")
    print(f"索引名称: {df5_4.index.name}")
except Exception as e:
    print(f"直接读取失败: {e}")
    print("尝试先读取再设置索引:")
    df5_4 = pd.read_csv('bj_lianJia.csv', encoding='gbk',
                        usecols=['ID', 'floor', 'lift', 'district', 'area', 'rent'])
    df5_4.set_index('ID', inplace=True)
    print(df5_4.head().to_string())

# --- 练习2 ---
print("\n" + "=" * 60)
print("【Numpy综合操作 - 练习2】")
print("=" * 60)

def summary_statistics(df, column):
    # 自定义函数：汇总DataFrame指定列的所有统计指标
    # 确保列是数值类型
    series = pd.to_numeric(df[column], errors='coerce').dropna()

    stats = {
        '列名': column,
        '计数(count)': series.count(),
        '均值(mean)': round(series.mean(), 2),
        '标准差(std)': round(series.std(), 2),
        '最小值(min)': round(series.min(), 2),
        '25%分位数': round(series.quantile(0.25), 2),
        '50%分位数(中位数)': round(series.quantile(0.50), 2),
        '75%分位数': round(series.quantile(0.75), 2),
        '最大值(max)': round(series.max(), 2),
        '极差(range)': round(series.max() - series.min(), 2),
    }
    return stats

# 对rent列调用统计函数
rent_stats = summary_statistics(df, 'rent')
print("rent列统计指标:")
for key, value in rent_stats.items():
    print(f"  {key}: {value}")

# 对area列调用统计函数
area_stats = summary_statistics(df, 'area')
print("\narea列统计指标:")
for key, value in area_stats.items():
    print(f"  {key}: {value}")

# --- 练习3 ---
print("\n" + "=" * 60)
print("【Numpy综合操作 - 练习3】")
print("=" * 60)

# 读取income.csv
df_income = pd.read_csv('income.csv', encoding='gbk')
print("\n原始income.csv数据:")
print(df_income.to_string())

# ① 将性别列中的男、女分别替换为数值1、0
print("\n--- ① 性别列替换 ---")
df_income['性别'] = df_income['性别'].map({'男': 1, '女': 0})
print("替换后:")
print(df_income.to_string())

# ② 年龄列缺失值用该列均值代替
print("\n--- ② 年龄缺失值填充 ---")
print(f"填充前缺失值数量: {df_income['年龄'].isnull().sum()}")
age_mean = df_income['年龄'].mean()
df_income['年龄'] = df_income['年龄'].fillna(age_mean)
print(f"用均值 {age_mean:.2f} 填充缺失值")
print("填充后:")
print(df_income.to_string())

# ③ 删掉收入值小于1000的数据
print("\n--- ③ 删除收入<1000的数据 ---")
before = len(df_income)
df_income = df_income[df_income['收入'] >= 1000]
print(f"删除前: {before} 行 -> 删除后: {len(df_income)} 行")
print("过滤后:")
print(df_income.to_string())

# ④ 输出收入最多的前5行记录
print("\n--- ④ 收入最多的前5行 ---")
top5_income = df_income.nlargest(5, '收入')
print(top5_income.to_string())

# ⑤ 输出收入低于总平均值的人员ID
print("\n--- ⑤ 收入低于总平均值的人员ID ---")
avg_income = df_income['收入'].mean()
print(f"平均收入: {avg_income:.2f}")
low_income = df_income[df_income['收入'] < avg_income]
print("收入低于平均值的人员:")
print(low_income[['ID', '性别', '年龄', '学历', '收入']].to_string())

print("\n" + "=" * 60)
print("所有步骤执行完毕!")
print("=" * 60)
