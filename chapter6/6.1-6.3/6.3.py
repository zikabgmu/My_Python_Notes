import matplotlib.pyplot as plt
import pandas as pd

# =================================================
# 1. 全局环境与数据加载
# =================================================
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

data_path = 'newbj_lianJia.csv'
df = pd.read_csv(data_path, encoding='gbk')

print("--- 正在生成 Matplotlib 综合绘图，请稍候... ---")

# =================================================
# 题目 1：基础绘图 - 各城区房源数量统计
# =================================================
plt.figure(figsize=(14, 6))
district_counts = df.groupby('district')['district'].count().sort_values(ascending=False)
plt.bar(district_counts.index, district_counts.values, color='#3498DB')
plt.title('各城区房源数量分布', fontsize=18)
plt.ylabel('房源数量', fontsize=14)
plt.xticks(fontsize=12, rotation=45, ha='right')
plt.yticks(fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('task1_district_quantity.png', dpi=150, bbox_inches='tight')
plt.show()

# =================================================
# 题目 2：多线绘制 - 各城区平均租金与最大租金对比
# =================================================
plt.figure(figsize=(14, 6))
district_rent_stats = df.groupby('district')['rent'].agg(['mean', 'max']).sort_values(by='mean', ascending=False)

plt.plot(district_rent_stats.index, district_rent_stats['mean'], marker='o', color='#E74C3C', linewidth=2, label='平均租金')
plt.plot(district_rent_stats.index, district_rent_stats['max'], marker='s', color='#27AE60', linewidth=2, linestyle='--', label='最高租金')

plt.title('各城区平均租金与最高租金对比', fontsize=18)
plt.ylabel('租金 (元)', fontsize=14)
plt.xticks(fontsize=12, rotation=45, ha='right')
plt.yticks(fontsize=12)
plt.legend(fontsize=14)
plt.grid(True, linestyle=':', alpha=0.5)
plt.tight_layout()
plt.savefig('task2_rent_line_compare.png', dpi=150, bbox_inches='tight')
plt.show()


# 朝向分布 - 房屋数量横向柱状图
plt.figure(figsize=(10, 8))
toward_counts = df['toward'].value_counts()
plt.barh(toward_counts.index, toward_counts.values, color='#F1C40F')
plt.title('房屋朝向分布统计', fontsize=18)
plt.xlabel('房屋数量', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
for i, v in enumerate(toward_counts.values):
    plt.text(v + 20, i, str(v), va='center', fontsize=12)
plt.tight_layout()
plt.savefig('task3_toward_barh.png', dpi=150, bbox_inches='tight')
plt.show()

# 电梯配置 - 饼图占比展示
plt.figure(figsize=(8, 8))
lift_counts = df['lift'].value_counts()
plt.pie(lift_counts, labels=lift_counts.index, autopct='%1.1f%%', startangle=90, 
        colors=['#2ECC71', '#E67E22'], textprops={'fontsize': 14})
plt.title('房屋电梯配置占比', fontsize=18)
plt.axis('equal')
plt.tight_layout()
plt.savefig('task4_lift_pie.png', dpi=150, bbox_inches='tight')
plt.show()

# =================================================
# 题目 5：户型分布词云图
# =================================================

try:
    from wordcloud import WordCloud
    text = ' '.join(df['model'].dropna().astype(str).tolist())
    wordcloud = WordCloud(font_path='msyh.ttc', background_color='white', width=1200, height=800).generate(text)
    
    plt.figure(figsize=(12, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('房源户型词云图', fontsize=20)
    plt.tight_layout()
    plt.savefig('task5_model_wordcloud.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("所有综合操作绘图已全部完成！")
except Exception as e:
    print(f"词云图生成失败（可能缺少库）：{e}")
    print("已为您成功生成前4张综合操作图片！")