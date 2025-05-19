import matplotlib.pyplot as plt
import matplotlib
from collections import Counter

# 字体设置
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
matplotlib.rcParams['axes.unicode_minus'] = False

# 你的原始长文本数据粘贴在这里（为节省篇幅我简写为 raw_text）
raw_text = """
环境毒理学（聚焦生殖毒性与内分泌干扰）。
环境工程
生态毒理学
环境化学（涉及环境毒理学与公共健康）
环境工程（侧重污染物去除技术）
环境化学
环境化学（聚焦吸附机制与材料改性）
环境化学（涉及cVMS生成机制）
环境毒理学（涉及硅氧烷材料的辐射降解及毒性评估）
环境化学（涉及环境毒理学）
环境化学
环境工程
环境工程
环境化学（涉及硅氧烷的环境行为与化学特性）。
环境工程（涉及cVMS的环境排放、处理技术及生物降解）
环境工程（涉及沼气净化技术）
环境工程（涉及吸附技术、沼气净化）。
环境化学
环境化学
环境化学
环境毒理学
环境化学
环境化学
环境化学
环境化学（侧重大气污染物监测与趋势分析）
环境化学（涉及环境毒理学与生态毒理学）
环境化学
环境工程（涉及化学链燃烧技术及硅氧烷的环境影响）
环境化学（侧重硅氧烷结构分析与环境行为）
环境化学（涉及分析化学方法开发）
环境工程（涉及废水处理与污染物去除）。
环境化学
环境工程（涉及填埋气处理与硅氧烷去除）
分析化学（聚焦于cVMS的分析方法开发）。
环境化学（涵盖环境毒理学、生态毒理学内容）。
环境工程（侧重生物技术去除VMS）
环境化学（涉及生物气中硅氧烷的分析与去除技术）。
环境工程
环境化学
环境毒理学（涉及硅氧烷的毒理效应与健康风险）
环境工程
环境毒理学（兼涉生态毒理学）
环境化学（侧重分析化学方法）
环境工程（侧重气体采样与分析技术）
分析化学
环境毒理学
环境化学
环境化学（侧重环状硅氧烷的合成与热稳定性分析）
环境毒理学
环境工程（涉及吸附材料开发与污染物去除）
环境毒理学
环境工程（涉及硅氧烷在工业发动机中的毒理与化学行为）
环境工程（涉及生物过滤技术对VMS的去除）
环境工程（涉及燃料电池中硅氧烷污染物的降解机制）
环境工程（涉及吸附材料合成与污染物去除）
环境毒理学
环境工程（涉及燃料电池阳极降解机制与硅氧烷污染）
环境工程
环境工程（涉及燃料电池阳极降解机制与污染物沉积）
环境工程
环境工程
环境化学（涉及硅氧烷合成与改性）
环境工程
环境工程
环境工程（侧重污染物去除技术）
环境工程（涉及生物降解技术）
环境化学（涉及硅氧烷的环境行为与化学转化）
环境工程（涉及燃料电池阳极降解机制与硅氧烷污染）
环境毒理学（涉及硅氧烷的生物蓄积性与潜在毒性）
环境化学（涉及硅氧烷涂层材料的稳定性与反应特性）
环境工程（聚焦沼气中硅氧烷的去除技术）
环境毒理学
生态毒理学
环境毒理学
环境毒理学-
环境化学
环境工程
环境毒理学
环境毒理学
环境毒理学
生态毒理学
环境毒理学
环境毒理学
环境工程
环境毒理学
环境化学
环境毒理学
环境毒理学
环境化学
环境毒理学
环境毒理学
环境毒理学
环境毒理学
环境化学
生态毒理学
环境毒理学
环境化学
环境毒理学
环境毒理学-
环境毒理学-
环境毒理学-
环境工程（涉及吸附与再生技术）
环境毒理学
环境毒理学
环境工程（涉及沼气处理与吸附技术）
环境工程
环境工程
环境毒理学
环境化学
环境化学
环境化学
环境毒理学
环境毒理学
环境化学
环境工程
环境毒理学
环境毒理学
环境毒理学（涉及生殖毒性与内分泌干扰）
环境化学
环境毒理学（涉及生物蓄积、食物网传递及生态风险评估）。
环境工程（聚焦废水处理技术）
环境化学（侧重分析技术与吸附材料开发）
环境毒理学（聚焦皮肤暴露与吸收机制）。
环境化学（侧重大气迁移与转化）
分析化学
环境化学（涉及环境毒理学与生态毒理学）
环境毒理学
环境毒理学
生态毒理学
生态毒理学
环境化学
环境工程
环境工程
环境毒理学
环境化学
环境毒理学
环境毒理学
环境毒理学
环境毒理学
环境化学（侧重硅氧烷材料的合成与表征）
环境工程（涉及生物滴滤技术及污染物降解）
环境工程（涉及沼气处理与污染物监测技术）
环境毒理学
环境化学
环境毒理学
环境化学
环境工程（涉及燃烧产物对设备性能的影响）
环境化学（聚焦于硅氧烷的热力学性质测量）
环境工程（侧重ORC系统工质降解与回收技术）。

"""

# 处理文本，按行拆分并去除标点和空格
entries = [line.strip().strip('。') for line in raw_text.strip().split('\n') if line.strip()]

# 分类函数
def classify(field):
    if '环境毒理学' in field:
        return '环境毒理学'
    elif '环境化学' in field:
        return '环境化学'
    elif '环境工程' in field:
        return '环境工程'
    elif '生态毒理学' in field:
        return '生态毒理学'
    elif '分析化学' in field:
        return '分析化学'
    else:
        return '其他'

# 分类统计
categories = [classify(field) for field in entries]
counter = Counter(categories)

# 按数量降序排列
sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
labels, counts = zip(*sorted_items)

# 色彩（绿色渐变：深→浅）
cmap = plt.cm.Greens
colors = [cmap(i / len(labels)) for i in range(len(labels))][::-1]

# 绘图
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(labels, counts, color=colors, edgecolor='black')

# 设置标题和标签
ax.set_title("文献所属领域统计", fontsize=20, fontname='KaiTi', pad=20)
ax.set_ylabel("文献数量", fontsize=14, fontname='KaiTi')
ax.set_xlabel("研究领域", fontsize=14, fontname='KaiTi')

# 坐标轴标签字体
ax.set_xticklabels(labels, fontsize=12, fontname='KaiTi')
ax.set_yticklabels(ax.get_yticks(), fontsize=12, fontname='Times New Roman')

# 柱上数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 1, str(height),
            ha='center', va='bottom', fontsize=11, fontname='Times New Roman')

# 保存图像
fig.tight_layout()
fig.savefig("文献领域柱状图.png", dpi=300, bbox_inches='tight')
plt.show()
