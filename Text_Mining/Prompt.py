from openai import OpenAI
import os


def main():
    Inp = 'paper_text_library'
    Out = 'paper_answer_library'

    for txt in os.listdir(Inp):
        TxtPath = os.path.join(Inp, txt)
        with open(TxtPath, 'r', encoding='utf-8') as f:
            text = f.read()
            a = DeepSeek_API(text).choices[0].message.content
        # 写入输出文件夹中同名文件
        filename = txt
        output_path = os.path.join(Out, filename)
        with open(output_path, 'w', encoding='utf-8') as f_out:
            f_out.write(a)

        print(f'{txt}txt文件解析完成并写入同名文件')

    print('所有任务已经完成')


def DeepSeek_API(file_path):
    client = OpenAI(
        api_key="自己买",
        base_url="https://api.deepseek.com",
    )
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role": "system",
                "content": """
                
                            您是一个环境毒理学领域的专家，专注于分析环状挥发性甲基硅氧烷（cVMS）污染物，特别是 D3–D15。
                            请对提供的 .txt 文献文件进行解析，并按以下格式提取关键信息。
                            
                            第一步：基础判断
                            读取文件内容并判断：是否包含有效的科技文献正文内容？
                                若内容为空、乱码、或仅为参考文献目录、杂志投稿须知等，请输出 无有效正文内容。
                                若内容结构清晰，包括摘要、引言、方法、结果、讨论等，则继续下一步提取。
                            
                            第二步：请按下列顺序逐项提取或搜索推测内容，若未在文献中找到，请填写“NA”。
                            
                            一、基本信息
                            污染物种类：如 D3、D4、D5…等；若仅提及“cVMS”，请据实写出；无具体信息则写“NA”。
                            文章名称（请严格分为两行输出）：
                                第一行：英文标题
                                第二行：中文翻译标题（若文献无翻译，请基于文意自行翻译）
                            文献类型（如实验研究、综述、建模模拟等）                            
                            文献所属领域（根据 D3–D15 类 cVMS 科技文献的分类，细化为以下子领域之一：环境毒理学、环境化学、分析化学、环境工程、公共健康、生态毒理学、其他（请注明））
                            样本采样年份（如1999年）
                            样本类型（如空气样、水样、土壤样、生物组织等）
                            污染物来源行业及生产地（具体到国家下一级行政区）：如“化妆品行业，美国加州”
                            采样地点（具体到国家下一级行政区）：如“中国广东省广州市”。
                            
                            二、实验设定与条件
                            模式生物（如斑马鱼、大鼠、Daphnia magna、人类细胞系等）
                            暴露浓度（请附单位，如 µg/L, mg/kg 等）
                            实验步骤简述（一句话概括实验流程；如无写 NA）
                            
                            三、cVMS 毒理特征提取（请提供简短的文字阐述）
                            数据类型：实测（Observed）或预测（Predicted）
                            持久性（Persistence）：如半衰期、环境中稳定性等
                            生物蓄积性（Bioaccumulation）：如 BCF/BAF 值、蓄积证据等
                            毒性（Toxicity）：急性/慢性毒性，行为、代谢、发育等方面
                            迁移性（Movement）：是否描述其在空气、水、食物链等介质中的扩散与转移能力
                            
                            四、cVMS 相关健康与生态风险（请提供简短的文字阐述，若未提及，请写“NA”）
                            生殖系统影响：是否干扰精子、卵母细胞、性腺等。
                            内分泌干扰作用：是否被归为 EDC，是否影响激素水平。
                            体内代谢特征：代谢部位、代谢产物、排泄方式等。
                            三致性质（按子项分列）：
                                致畸性（Teratogenicity）
                                致癌性（Carcinogenicity）
                                致突变性（Mutagenicity）
                            
                            """
            },
            {
                "role": "user",
                "content": file_path
            },
        ],
        max_tokens=1024,
        temperature=0.7,
        stream=False)

    return response


if __name__ == '__main__':
    main()
