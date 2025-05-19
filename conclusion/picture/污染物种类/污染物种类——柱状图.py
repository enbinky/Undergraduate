import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 数据
labels = ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12',
          'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20', 'D21']
numbers = [1, 41, 135, 113, 61, 9, 4, 4, 0, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1]

# 字体设置
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
matplotlib.rcParams['axes.unicode_minus'] = False

# 设置颜色（绿色从深到浅）
cmap = plt.cm.Greens
colors = [cmap(i / len(numbers)) for i in range(len(numbers))]
colors = colors[::-1]  # 深绿 → 浅绿

# 绘图
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(labels, numbers, color=colors, edgecolor='black')

# 设置标题和轴标签
ax.set_title("硅氧烷种类研究分析", fontsize=20, fontname='KaiTi', pad=20)
ax.set_xlabel("污染物种类", fontsize=14, fontname='KaiTi')
ax.set_ylabel("文献数量", fontsize=14, fontname='KaiTi')

# 设置坐标轴刻度字体
ax.set_xticklabels(labels, rotation=45, fontsize=12, fontname='Times New Roman')
ax.set_yticklabels(ax.get_yticks(), fontsize=12, fontname='Times New Roman')

# 添加柱上数值标签
for bar in bars:
    height = bar.get_height()
    if height > 0:
        ax.annotate(f'{int(height)}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 向上偏移
                    textcoords="offset points",
                    ha='center', va='bottom',
                    fontsize=10,
                    fontname='Times New Roman')

# 保存图像
fig.tight_layout()
fig.savefig("硅氧烷柱状图分析.png", dpi=300, bbox_inches='tight')

# 显示图像
plt.show()
