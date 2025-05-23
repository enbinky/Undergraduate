import pandas as pd
import re
from collections import Counter

# 读取原始文本内容
with open("data.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

# 提取所有国家名称（优先考虑中文或英文地名中的国家关键词）
# 构建常见国家关键词列表（可根据需要扩展）
country_keywords = [
    # 东亚
    "中国", "中国台湾", "中国香港", "中国澳门", "日本", "韩国", "朝鲜", "蒙古",

    # 东南亚
    "新加坡", "马来西亚", "印尼", "菲律宾", "泰国", "越南", "缅甸", "柬埔寨", "老挝", "文莱", "东帝汶",

    # 南亚
    "印度", "巴基斯坦", "孟加拉国", "尼泊尔", "不丹", "马尔代夫", "斯里兰卡",

    # 中亚
    "哈萨克斯坦", "乌兹别克斯坦", "土库曼斯坦", "吉尔吉斯斯坦", "塔吉克斯坦",

    # 西亚（中东）
    "土耳其", "伊朗", "伊拉克", "叙利亚", "黎巴嫩", "以色列", "巴勒斯坦", "约旦", "沙特阿拉伯",
    "阿联酋", "阿曼", "也门", "卡塔尔", "巴林", "科威特",

    # 欧洲（西欧+北欧+南欧+东欧）
    "英国", "爱尔兰", "法国", "德国", "意大利", "西班牙", "葡萄牙", "比利时", "荷兰", "卢森堡",
    "挪威", "瑞典", "芬兰", "丹麦", "冰岛",
    "瑞士", "奥地利", "希腊", "捷克", "匈牙利", "波兰", "斯洛伐克", "斯洛文尼亚", "克罗地亚",
    "保加利亚", "罗马尼亚", "爱沙尼亚", "拉脱维亚", "立陶宛", "塞尔维亚", "黑山", "马其顿", "阿尔巴尼亚",
    "波斯尼亚和黑塞哥维那", "摩尔多瓦", "乌克兰", "白俄罗斯", "俄罗斯",

    # 北美洲
    "美国", "加拿大", "墨西哥",

    # 中美洲与加勒比海
    "危地马拉", "洪都拉斯", "尼加拉瓜", "哥斯达黎加", "巴拿马", "古巴", "牙买加", "多米尼加共和国",
    "海地", "巴哈马", "特立尼达和多巴哥", "波多黎各",

    # 南美洲
    "巴西", "阿根廷", "智利", "乌拉圭", "巴拉圭", "玻利维亚", "秘鲁", "厄瓜多尔", "哥伦比亚", "委内瑞拉", "苏里南", "圭亚那",

    # 大洋洲
    "澳大利亚", "新西兰", "斐济", "巴布亚新几内亚", "所罗门群岛", "汤加", "萨摩亚", "瓦努阿图", "密克罗尼西亚", "马绍尔群岛", "帕劳",

    # 非洲
    "埃及", "南非", "尼日利亚", "阿尔及利亚", "摩洛哥", "突尼斯", "苏丹", "利比亚", "埃塞俄比亚", "索马里",
    "肯尼亚", "乌干达", "坦桑尼亚", "卢旺达", "布隆迪", "莫桑比克", "马达加斯加", "赞比亚", "津巴布韦",
    "博茨瓦纳", "纳米比亚", "安哥拉", "刚果（金）", "刚果（布）", "加蓬", "赤道几内亚", "中非", "乍得",
    "尼日尔", "马里", "布基纳法索", "塞内加尔", "冈比亚", "几内亚", "几内亚比绍", "利比里亚", "塞拉利昂",
    "贝宁", "多哥", "加纳", "科特迪瓦", "毛里塔尼亚", "马拉维", "莱索托", "斯威士兰", "佛得角", "科摩罗",
    "吉布提", "厄立特里亚", "圣多美和普林西比", "毛里求斯", "塞舌尔",

    # 其他/特殊地区
    "梵蒂冈", "摩纳哥", "圣马力诺", "安道尔", "列支敦士登", "库拉索", "法属圭亚那", "法属波利尼西亚",
    "新喀里多尼亚", "格陵兰", "关岛", "美属萨摩亚", "英属维尔京群岛", "美属维尔京群岛"
]

# 使用正则提取每一行中的国家词汇（严格匹配）
matched_countries = []
for line in raw_text.splitlines():
    for country in country_keywords:
        if country in line:
            matched_countries.append(country)
            break  # 一行最多记录一个国家，避免重复

# 统计频次
country_counts = Counter(matched_countries)

# 创建DataFrame
df_country_count = pd.DataFrame(country_counts.items(), columns=["国家", "数量"]).sort_values(by="数量",
                                                                                              ascending=False)
df_country_count.reset_index(drop=True, inplace=True)

# 保存为Excel
output_path = "采样国家统计_from_txt.xlsx"
df_country_count.to_excel(output_path, index=False)
