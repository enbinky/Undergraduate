import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
from collections import Counter

# 字体设置
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
matplotlib.rcParams['axes.unicode_minus'] = False

# 1. 加载 Excel 数据
file_path = "ultimate.xlsx"  # 修改为你的实际路径
df = pd.read_excel(file_path)

# 2. 毒性字段定义
tox_columns = [
    "持久性", "生物蓄积性", "毒性", "迁移性",
    "生殖系统影响", "内分泌干扰作用", "体内代谢特征",
    "致畸性", "致癌性", "致突变性"
]

# 3. 筛选 D5 相关记录
d5_related = df[df["污染物种类"].astype(str).str.contains("D7", na=False)]

# 4. 构建三元组 (污染物, 毒性维度, 描述)
triples = []
for _, row in d5_related.iterrows():
    for col in tox_columns:
        val = str(row[col]).strip()
        if val and val.lower() != "no answer" and val.lower() != "nan":
            short_val = val.split("，")[0].split("。")[0].split("（")[0]
            triples.append(("D7", col, short_val))

# 5. 保留正向毒性描述
positive_keywords = ["有", "存在", "明确", "积累", "增强", "影响", "稳定"]
positive_triples = [
    (pollutant, tox_type, desc)
    for pollutant, tox_type, desc in triples
    if any(keyword in desc for keyword in positive_keywords)
]

# 6. 统计频率 ≥2 的毒性类型
tox_freq = Counter([t for _, t, _ in positive_triples])
high_freq_types = {t for t, c in tox_freq.items() if c >= 2}

# 7. 构建简化边（仅 D5 → 高频毒性维度）
edges = [(p, t) for p, t, d in positive_triples if t in high_freq_types]

# 8. 创建 NetworkX 图并可视化
G = nx.DiGraph()
G.add_edges_from(edges)

plt.figure(figsize=(8, 5))
pos = nx.spring_layout(G, seed=42, k=0.6)
nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=1600)
nx.draw_networkx_edges(G, pos, arrows=True, arrowstyle="-|>")
nx.draw_networkx_labels(G, pos, font_size=10)

plt.title("简化版 D7 毒性知识图谱（正向 + 高频）", fontsize=14)
plt.axis("off")
plt.tight_layout()
plt.savefig("D7_简化毒性知识图谱.png", dpi=300)
plt.show()
