import os
import shutil
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import GrobidParser

# 本地文件
paper_library = 'paper_pdf_library'
paper_text_library = 'paper_text_library'
grobid_log = 'grobid_log.txt'
grobid_fail = 'grobid_fail.txt'
paper_zero = 'zero'
paper_fail = 'fail'


def main():
    for pdf in os.listdir(paper_library):
        pdfPath = os.path.join(paper_library, pdf)
        txt = pdf[:-4] + '.txt'
        txtPath = os.path.join(paper_text_library, txt)
        with open(txtPath, "w") as f:
            f.write('')
        try:
            docs_pdf = Grobid(pdfPath)
            if docs_pdf:  # 确保docs列表非空
                with open(txtPath, 'a', encoding='utf-8') as f:
                    f.write(docs_pdf[0].metadata['paper_title'])
                    f.write('\n')
                    for doc in docs_pdf:
                        f.write(doc.metadata['text'])
                        f.write('\n')
                with open(grobid_log, 'a', encoding='utf-8') as log:
                    log.write(f'{str(pdf)} 的标题与文本已经成功写入同名txt文件')
                    log.write('\n')
                print(f'{str(pdf)} 的标题与文本已经成功写入同名txt文件')
            else:
                with open(grobid_fail, 'a', encoding='utf-8') as fail:
                    fail.write(f'{str(pdf)}文件的docs列表为空')
                    fail.write('\n')
                print(f'{str(pdf)}文件的docs列表为空')
                copy_file = os.path.join(paper_zero, pdf)
                shutil.copy2(pdfPath, copy_file)
        except Exception as e:
            with open(grobid_fail, 'a', encoding='utf-8') as fail:
                fail.write(f'{str(pdf)}文件处理出现错误：{str(e)}')
                fail.write('\n')
            print(f'{str(pdf)}文件处理出现错误')
            copy_file = os.path.join(paper_fail, pdf)
            shutil.copy2(pdfPath, copy_file)


def Grobid(pdfPath):
    # 设置文件系统路径和解释器
    loader = GenericLoader.from_filesystem(
        path=pdfPath,
        glob='*',
        suffixes=['.pdf'],
        parser=GrobidParser(segment_sentences=False),
    )
    docs = loader.load()
    return docs


if __name__ == '__main__':
    main()
