import matplotlib.pyplot as plt
import networkx as nx
import matplotlib

# 设置字体，确保中文可以正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows 用户用 'SimHei'；Mac 可用 'Arial Unicode MS'
plt.rcParams['axes.unicode_minus'] = False   # 解决负号显示问题

# 定义每种物质及其高频毒性维度（正向+频次≥2）
toxicity_data = {
    "D3": ["生物蓄积性", "毒性", "持久性"],
    "D4": ["生物蓄积性", "毒性", "持久性", "迁移性", "内分泌干扰作用", "生殖系统影响"],
    "D5": ["毒性", "持久性", "迁移性", "内分泌干扰作用", "生殖系统影响"],
    "D6": ["毒性", "持久性", "内分泌干扰作用", "生殖系统影响"],
    "D7": ["内分泌干扰作用", "生殖系统影响"]
}

# 创建图谱对象
G = nx.Graph()

# 添加边（污染物—毒性维度）
for compound, effects in toxicity_data.items():
    for effect in effects:
        G.add_edge(compound, effect)

# 绘图
plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=0.5, seed=42)  # 使用 spring_layout 使图谱美观
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=2000)
nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")

# 设置标题
plt.title("D3–D7 毒性维度对比图谱（正向 + 高频）", fontsize=16)
plt.axis('off')  # 不显示坐标轴
plt.tight_layout()
plt.show()
plt.savefig("D3–D7 毒性维度对比图谱.png", dpi=300)
