import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import pycountry
import matplotlib

# 字体设置
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
matplotlib.rcParams['axes.unicode_minus'] = False

# === 第一步：读取国家统计数据（仅有“国家”和“数量”列）===
df = pd.read_excel("采样国家统计_from_txt.xlsx")  # 替换为你的实际文件路径

# 中文国家名映射为英文
country_name_map = {
    '中国': 'China',
    '美国': 'United States',
    '德国': 'Germany',
    '意大利': 'Italy',
    '英国': 'United Kingdom',
    '瑞士': 'Switzerland',
    '奥地利': 'Austria',
    '瑞典': 'Sweden',
    '芬兰': 'Finland',
    '挪威': 'Norway',
    '韩国': 'South Korea',
    '日本': 'Japan',
    '加拿大': 'Canada',
    '西班牙': 'Spain',
    '葡萄牙': 'Portugal',
    '荷兰': 'Netherlands',
    '波兰': 'Poland',
    '希腊': 'Greece',
    '巴西': 'Brazil',
    '智利': 'Chile',
    '法国': 'France',
    '比利时': 'Belgium'
}
df["country_en"] = df["国家"].map(country_name_map)


# 获取 ISO A3 编码
def get_iso_a3(name):
    try:
        return pycountry.countries.lookup(name).alpha_3
    except:
        return None


df["iso_a3"] = df["country_en"].apply(get_iso_a3)

# === 第二步：读取本地地图数据（Shapefile）===
world = gpd.read_file("map/ne_110m_admin_0_countries.shp")  # 替换为你的本地路径

# === 第三步：合并国家统计数据 ===
world = world.merge(df, left_on="ADM0_A3", right_on="iso_a3", how="left")
print(world.columns)

# === 第四步：绘制地图 ===
fig, ax = plt.subplots(figsize=(16, 9))
world.boundary.plot(ax=ax, linewidth=0.5, color='gray')
world.plot(column="数量", cmap="Blues", linewidth=0.8, ax=ax, edgecolor='0.8', legend=True,
           missing_kwds={"color": "lightgrey", "label": "No data"})

# === 标注：国家名称（仅Top 10，防止重叠） ===
top_countries = world.dropna(subset=["数量"]).sort_values(by="数量", ascending=False).head(10)
for idx, row in top_countries.iterrows():
    rep_point = row["geometry"].representative_point()
    ax.text(rep_point.x, rep_point.y,
            row["country_en"],
            fontsize=9, ha="center", color="black",
            bbox=dict(facecolor='white', edgecolor='none', alpha=0.6))

# 美化与保存
ax.set_title("采样国家分布图", fontsize=16)
ax.axis("off")
plt.tight_layout()
plt.savefig("采样国家分布图.png", dpi=300)
plt.show()
