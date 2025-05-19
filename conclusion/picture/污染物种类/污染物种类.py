import matplotlib.pyplot as plt
import matplotlib

# 数据
# D2D3	D4	D5	D6	D7	D8	D9	D10	D11	D12	D13	D14	D15	D16	D17	D18	D19	D20	D21 # 共20个污染物
labels = ['D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18',
          'D19', 'D20', 'D21']
out_labels = ['', 'D3', 'D4', 'D5', 'D6', 'D7', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
numbers = [1, 41, 135, 113, 61, 9, 4, 4, 0, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1]

# 饼状图中各部分的颜色
colors = ['#F5FFFA', '#00FF7F', '#3CB371', '#2E8B57', '#F0FFF0', '#90EE90', '#98FB98', '#8FBC8F', '#32CD32', '#00FF00',
          '#228B22', '#008000', '#006400', '#7FFF00', '#7CFC00', '#ADFF2F', '#556B2F', '#6B8E23', '#FAFAD2', '#FFFFF0']
# 设置字体，中文使用楷体，数字和英文使用 Times New Roman，字号放大
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
matplotlib.rcParams['axes.unicode_minus'] = False

# 自定义 autopct：仅为有标签的部分显示数字
def custom_autopct(pct, allvals):
    index = custom_autopct.index
    label = out_labels[index]
    custom_autopct.index += 1
    return f'{pct:.1f}%' if label != '' else ''


custom_autopct.index = 0  # 添加属性用于跟踪索引

# 绘制饼状图

plt.figure(figsize=(9, 9))
plt.pie(numbers,
        labels=out_labels,
        colors=colors,
        startangle=90,
        labeldistance=1.1,
        autopct=lambda pct: custom_autopct(pct, numbers))
plt.legend(labels,
           title='污染物种类')
plt.tight_layout()
plt.show()
