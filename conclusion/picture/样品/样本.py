import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# 原始数据（你也可以从 Excel 中读取）
raw_data = [
    "大鼠", "No Answer", "银鸥", "灰尘", "No Answer", "环境监测", "材料吸附", "No Answer", "材料研究", "No Answer",
    "化学体系", "No Answer", "污泥微生物", "No Answer", "细菌+反应器", "No Answer", "No Answer", "No Answer",
    "化学模拟", "No Answer", "人类", "空气采样", "室内空气", "室内空气", "No Answer", "No Answer", "环境采样",
    "化学工程", "口腔细菌", "环境基质", "小球藻", "No Answer", "工艺研究", "化学分析", "水蚤+斑马鱼+鼠",
    "微生物群落", "No Answer", "化学分析", "空气采样", "人类样本", "污泥微生物", "鸡胚", "No Answer", "No Answer",
    "环境水样", "室内空气", "材料研究", "No Answer", "SD+F344大鼠", "No Answer", "F344大鼠和SD大鼠", "No Answer",
    "污水污泥微生物", "No Answer", "No Answer", "鱼类+水蚤+藻类", "固体氧化物燃料电池", "未涉及", "燃料电池材料",
    "物理吸附", "非生物吸附", "大肠杆菌", "厌氧污泥+铜绿假单胞菌", "No Answer", "No Answer", "活性污泥",
    "No Answer", "No Answer", "No Answer", "No Answer", "No Answer", "A549细胞", "斑马鱼", "BEAS-2B细胞",
    "斑马鱼", "No Answer", "吸附材料", "大鼠+MCF-7细胞", "A549细胞", "人类志愿者", "斑马鱼", "A549",
    "大鼠+人类志愿者", "微生物群落", "BEAS-2B", "化学分析", "斑马鱼+大型溞", "斑马鱼+大鼠", "No Answer",
    "斑马鱼", "BEAS-2B", "A549", "F344+CrlBr+人类皮肤", "No Answer", "斑马鱼", "斑马鱼", "No Answer",
    "斑马鱼", "褐菖鲉", "BEAS-2B", "斑马鱼", "活性炭", "斑马鱼", "人类暴露", "No Answer", "细菌群落",
    "污泥细菌群落", "人类尸体皮肤", "No Answer", "大气", "空气样本", "环境介质", "离体皮肤", "工程学生",
    "ZnO催化", "斑马鱼+大型溞+鲷", "斑马鱼+大型溞+摇蚊+蚯蚓", "SD+F344+人类皮肤", "No Answer", "鲫鱼+鳊鱼+黑鲈",
    "废水处理", "材料吸附", "人类+大鼠+猪皮+尸体皮肤", "No Answer", "化学分析", "底栖生态风险", "引用虹鳟等",
    "厌氧污泥微生物", "鲤鱼+浮游生物+蛤+虾", "鲫鱼", "No Answer", "物理吸附", "污泥细菌", "斑马鱼胚胎",
    "No Answer", "河蚬", "贻贝", "鳕鱼", "斑马鱼", "No Answer", "化学降解", "仪器分析", "A549", "气溶胶",
    "人类志愿者", "斑马鱼", "家用燃气器具", "非生物", "No Answer"
]

# 字体设置
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
matplotlib.rcParams['axes.unicode_minus'] = False

# 样本分类规则
categories = {
    "空气": ["空气", "气溶胶", "室内空气", "灰尘", "家用燃气器具", "大气"],
    "水": ["水", "藻", "水样", "污水", "污泥", "浮游", "沼气", "水蚤", "鱼", "斑马鱼", "蛤", "虾", "湖", "饮用水"],
    "土壤": ["土壤", "沉积", "底栖", "泥"],
    "生物样本": ["大鼠", "小鼠", "人类", "皮肤", "细胞", "微生物", "菌", "胚", "尸体", "肺", "志愿者"]
}

# 分类函数
def classify_sample(text):
    for key, keywords in categories.items():
        if any(kw in text for kw in keywords):
            return key
    return "其他/不明"

# 应用分类
classified = [classify_sample(t) for t in raw_data]

# 构建数据表并去除“其他/不明”
df_summary = pd.Series(classified).value_counts().reset_index()
df_summary.columns = ["样本类别", "数量"]
df_summary = df_summary[df_summary["样本类别"] != "其他/不明"]

# --- 饼状图 ---
plt.figure(figsize=(6, 6))
plt.pie(df_summary["数量"], labels=df_summary["样本类别"], autopct="%1.1f%%", startangle=120)
plt.title("样本类型分布")
plt.axis("equal")
plt.savefig("样本饼状图.png", dpi=300)
plt.show()

# --- 柱状图 ---
plt.figure(figsize=(8, 5))
plt.bar(df_summary["样本类别"], df_summary["数量"], color="seagreen", edgecolor="black")
plt.ylabel("数量")
plt.xlabel("样本类别")
plt.title("样本类型分布")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("样本柱状图.png", dpi=300)
plt.show()
