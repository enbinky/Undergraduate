import os
import re
import pandas as pd


def main():
    # excel 表头标题，且包含顺序
    columns = excel_col('Paper_Conclusion.xlsx')
    '''
    '基础判断', 
    '污染物种类','文章名称', '文献类型', '文献所属领域', '样本采样年份', '样本类型', 
    '污染物来源行业及生产地', '采样地点', 
    '模式生物', '暴露浓度', '实验步骤简述', 
    '数据类型', '持久性', '生物蓄积性', '毒性', '迁移性', 
    '生殖系统影响', '内分泌干扰作用','体内代谢特征', '致畸性', '致癌性', '致突变性', 
    '总结或备注', '判定']
    '''
    # txt内部固定标题，可能会有其他字符串,且包含顺序
    txt_headers = ['基础判断',
                   '污染物种类', '文章名称', '文献类型', '文献所属领域', '样本采样年份', '样本类型',
                   '污染物来源行业及生产地', '采样地点',
                   '模式生物', '暴露浓度', '实验步骤简述',
                   '数据类型', '持久性', '生物蓄积性', '毒性', '迁移性',
                   '生殖系统影响', '内分泌干扰作用', '体内代谢特征', '致畸性', '致癌性', '致突变性']

    Inp = 'paper_answer_library'
    row = 0
    for txt in os.listdir(Inp):
        txtPath = os.path.join(Inp, txt)
        with open(txtPath, 'r', encoding='utf-8') as f:
            ans = f.read()
            current_pos = 0
            # 柳暗花明疑无路，暴力代码亦可为
            for i in range(len(txt_headers) - 1):
                start = ans.find(txt_headers[i], current_pos)
                start_index = start + len(txt_headers[i])
                end = ans.find(txt_headers[i + 1], start_index)

                # 截取当前元素之后、下一个元素之前的内容
                content = ans[start_index:end]
                current_pos = end
                content = wash(content)
                content = nan(content)

                if i == 0:
                    # 优先判断是否包含 "第二步关键信息"，删除首次出现及之后内容
                    pattern_chinese_section = r'(第二步)'
                    match_chinese = re.search(pattern_chinese_section, content)
                    if match_chinese:
                        content = content[:match_chinese.start()].strip()

                excel(content, txt_headers[i], row)

            # 提取最后一个元素之后的内容
            last_elem = txt_headers[-1]
            last_pos = ans.find(last_elem)
            start_index = last_pos + len(last_elem)
            newline_index = ans.find('\n', start_index)
            tail_content = ans[start_index:newline_index]
            tail_content = wash(tail_content)
            tail_content = nan(tail_content)
            excel(tail_content, txt_headers[-1], row)

            last_cot = ans[newline_index:]
            last_cot = wash(last_cot)
            excel(last_cot, '总结或备注', row)

        print(f'{txt}文件已经处理完成')
        row += 1

    print('所有任务已经完成')


def excel_col(excel_path):
    df_excel = pd.read_excel(excel_path)
    column = df_excel.columns.tolist()
    return column


# 分单元格写入excel
def excel(text, col, row):
    df = pd.read_excel('Paper_Conclusion.xlsx')
    df[col] = df[col].astype(str)  # 将整列转为 str 类型
    if col in df.columns:
        df.at[row, col] = text
        df.to_excel('Paper_Conclusion.xlsx', index=False)
    else:
        print(f'{col}不存在excel表格中')


# 用于清洗大语言模型生成的内容中用于表示逻辑的‘-’‘#’空格等字符
def wash(string):
    # 去除 *, -, 空格, 换行符
    cleaned_text = re.sub(r'[*：\r\n# ]', '', string)
    # 优先判断是否包含 "一、" ~ "四、"，删除首次出现及之后内容
    pattern_chinese_section = r'(一、|二、|三、|四、)'
    match_chinese = re.search(pattern_chinese_section, cleaned_text)
    if match_chinese:
        cleaned_text = cleaned_text[:match_chinese.start()].strip()
    # 查找所有“单个数字 + 点”的组合，删除最后一个及其之后内容
    pattern_number_dot = r'\b\d\.'
    matches = list(re.finditer(pattern_number_dot, cleaned_text))
    if matches:
        last_match = matches[-1]
        cleaned_text = cleaned_text[:last_match.start()].strip()
    if len(cleaned_text) > 0:
        if cleaned_text[-1] == '.':
            cleaned_text = cleaned_text[:-2]

    return cleaned_text.strip()  # 没有匹配项则返回原文


def nan(string):
    if 'NA' in string or string == '':
        return 'No Answer'
    else:
        return string

if __name__ == '__main__':
    main()
