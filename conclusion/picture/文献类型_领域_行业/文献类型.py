import matplotlib.pyplot as plt
import matplotlib
from collections import Counter

# 字体设置
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']  # 中文楷体
matplotlib.rcParams['axes.unicode_minus'] = False

# 原始数据（复制粘贴你的长文本为字符串）
raw_data = """
实验研究（动物毒理学实验）。
综述
实验研究
实验研究（环境监测与暴露评估）
实验研究（吸附剂开发与现场应用）
实验研究
实验研究
实验研究
实验研究
实验研究（建模模拟）
实验研究
实验研究
实验研究
综述（Review）。
综述
综述
综述（Review）。
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究（长期大气监测数据分析）
实验研究（全球大气被动采样监测）
实验研究
实验研究
实验研究（SEM成像与化学表征）
实验研究
实验研究（微藻生物修复废水实验）。
实验研究
实验研究（结合建模与工艺开发）
实验研究（分析方法开发与优化）。
综述（Review）。
综述
综述（Review）。
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
综述（方法论评估）
实验研究（分析方法开发与验证）
实验研究
实验研究
实验研究（合成与性能表征）
实验研究
实验研究
实验研究（基于生理的药代动力学模型研究）
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究（合成与性能表征）
实验研究
实验研究（结合建模与实验验证）
实验研究
实验研究
实验研究
实验研究-
实验研究（计算模拟）
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究（PBPK模型开发）
实验研究
实验研究
实验研究
实验研究
综述
实验研究
综述
实验研究
实验研究
实验研究（PBPK模型开发与验证）
实验研究
实验研究
综述
实验研究
实验研究
实验研究-
实验研究-
实验研究-
实验研究
实验研究
综述
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究（建模模拟）
综述（证据权重分析）
综述（结合实验数据）
建模模拟研究
实验研究（环境监测与生态毒理学分析）。
实验研究
实验研究
综述（Review）。
建模模拟（大气化学传输模型CMAQ应用）
实验研究
实验研究（环境监测与污染评估）
实验研究
实验研究
实验研究
实验研究
实验研究（建模模拟）
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究
实验研究（更正声明，补充实验数据）
实验研究
实验研究
实验研究
实验研究（建模与验证）
实验研究
实验研究
实验研究
实验研究（长期监测与实验室模拟结合）。
"""  # 你需要完整粘贴你那段文本

# Step 1：按行拆分
lines = [line.strip().strip('。') for line in raw_data.strip().split('\n') if line.strip()]

# Step 2：分类函数
def classify(entry):
    if '综述' in entry or 'Review' in entry:
        return '综述'
    elif '建模' in entry or '模拟' in entry:
        if '实验研究' in entry:
            return '实验+建模模拟'
        else:
            return '建模模拟研究'
    elif '更正' in entry:
        return '其他'
    elif '实验研究' in entry:
        return '实验研究'
    else:
        return '其他'

# Step 3：统计
categories = [classify(line) for line in lines]
counter = Counter(categories)

# Step 4：绘制柱状图
fig, ax = plt.subplots(figsize=(8, 6))
labels = list(counter.keys())
counts = list(counter.values())

bars = ax.bar(labels, counts, color=plt.cm.Greens_r(range(len(labels))))

# 设置标题与坐标轴
ax.set_title("文献类型统计", fontsize=18, fontname='KaiTi')
ax.set_ylabel("数量", fontsize=14, fontname='KaiTi')
ax.set_xlabel("文献类型", fontsize=14, fontname='KaiTi')

# 显示数值标签
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height + 1, f'{height}',
            ha='center', va='bottom', fontsize=12, fontname='Times New Roman')

# 保存图片
fig.tight_layout()
fig.savefig("文献类型柱状图.png", dpi=300, bbox_inches='tight')
plt.show()
