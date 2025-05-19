# Text_Mining——文本挖掘

主要用于介绍代码功能与文档逻辑



## 前处理

### 1.WOS(web of science)提取DOI信息

从 Web Of Sciencea中提取文献的基础信息，下载至excel文件中，主要是使用文档中的DOI信息。

由于WOS最多一次性下载1000篇文献信息，所以需要学会合并excel文件。

为避免法律风险，请手动下载文献！！！

### 2.Grobid

确保电脑上已经安装Grobid，推荐使用docker镜像。

使用前，需要在本地run grobid，使用流程：

先启动docker

再在本地启动docker，指令：

```
docker pull lfoppiano/grobid:0.7.2

docker run -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2
```

在浏览器访问 http://localhost:8070 确认是否运行成功。

PS：偶尔可能会出一些问题，可以挂梯子调整一下。



## 文件逻辑

### paper_pdf_library

源文件pdf所在文件夹

### paper_text_library

pdf提取文本后的同名txt文件

### paper_answer_library

AI回答txt文件文件



## 代码与文档介绍

### Extract.py

功能：利用开源grobid对科技文献的标题与正文进行文本提取，并写入paper_text_library/同名.txt中。

### Prompt.py

功能：人工智能筛选

### clean.py

功能：数据清洗

### Information.py

功能：数据提取



## 文档介绍

功能：记录grobid.py成功和失败的日志

### grobid_fail.txt

功能：输出grobid.py提取失败的文献（文献名称）
