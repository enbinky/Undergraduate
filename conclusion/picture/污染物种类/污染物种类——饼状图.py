import matplotlib.pyplot as plt
import matplotlib
import numpy as np

# 示例数据
labels = ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18',
          'D19', 'D20', 'D21']
out_labels = ['', 'D3', 'D4', 'D5', 'D6', 'D7', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
numbers = [1, 41, 135, 113, 61, 9, 4, 4, 0, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1]
custom_colors = ['#00441b', '#006d2c', '#238b45', '#41ae76', '#66c2a4', '#99d8c9', '#b2e2e2', '#ccece6', '#e0f3db',
                 '#edf8e9', '#f7fcf5', '#d9f0d3', '#c7e9c0', '#a1d99b', '#74c476', '#31a354', '#006d2c', '#00441b',
                 '#ccece6', '#f7fcf5']

matplotlib.rcParams['font.sans-serif'] = ['KaiTi']

# 准备画布
fig, ax = plt.subplots(figsize=(9, 9))


# 控制 autopct 只显示有标签项
def custom_autopct(pct, allvals):
    index = custom_autopct.index
    label = out_labels[index]
    custom_autopct.index += 1
    return f'{pct:.1f}%' if label != '' else ''


custom_autopct.index = 0

# 绘图
wedges, texts, autotexts = ax.pie(
    numbers,
    labels=out_labels,
    colors=custom_colors,
    startangle=90,
    labeldistance=1.1,
    wedgeprops={'edgecolor': 'white'},
    autopct=lambda pct: custom_autopct(pct, numbers),
    textprops={'fontsize': 14}
)

# 设置字体
for text in texts:
    if any('\u4e00' <= char <= '\u9fff' for char in text.get_text()):
        text.set_fontname('KaiTi')
    else:
        text.set_fontname('Times New Roman')
    text.set_fontsize(16)

for autotext in autotexts:
    autotext.set_fontname('Times New Roman')
    autotext.set_fontsize(16)

# 设置标题
ax.set_title("硅氧烷种类研究分析", fontsize=20, fontname='KaiTi', loc='center')

# 设置图例
ax.legend(
    labels,
    title='污染物种类',
    title_fontsize=14,
    prop={'family': 'KaiTi', 'size': 12},
    bbox_to_anchor=(1.05, 0.95),
    loc='upper left'
)

# 调整布局避免 legend 挤压图像
plt.subplots_adjust(right=0.8)

# 保存图像
fig.savefig("硅氧烷种类研究分析.png", dpi=300, bbox_inches='tight')

# 显示图像
plt.show()
