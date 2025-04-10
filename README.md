<div align="center">
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/camrp2025.png" width=200>
</div>



# <p align="center">Chinese Abstract Meaning Representation Parsing Evaluation 2025</p>

# <p align="center"><font size=50><strong>第五届中文抽象语义表示解析评测任务</strong></font></p>




![What's new?](https://img.shields.io/badge/CAMRP_2025-NEW-red.svg "English Version")

**本届亮点**：新增6000+句篇章语料，关注**篇章指代消解**，考察模型对于篇章共指的解析能力！

**往届评测论文**现已收录至**ACL Anthology**：<a href="https://aclanthology.org/volumes/2023.ccl-3/">CCL23-Eval</a>，<a href="https://aclanthology.org/volumes/2024.ccl-3/">CCL24-Eval</a>

[![Eng](https://img.shields.io/badge/README-English-yellow.svg "English Version")](./README_En.md)

**English Version:** <a href="https://github.com/GoThereGit/Chinese-AMR/blob/main/README_En.md">README_En.md</a> 

[![signup](https://img.shields.io/badge/CAMRP_2025-日程-blue.svg "sign up")](https://forms.office.com/r/wwU0NgZdJz)

- [X] 2025年3月1日：<a href="https://forms.office.com/r/wwU0NgZdJz">**评测任务报名**</a>开始。

- [x] 2025年3月20日：**LDC**发布训练集以及验证集给参赛队（详见<a href="#ldc">评测语料授权</a>）。

- [ ] 2025年4月15日：评测任务报名截止。

- [ ] 2025年5月1日：**本站**发布**测试集**给参赛队。

- [ ] 2025年5月8日：参赛队提交自动标注的数据（提交格式详见<a href="#anchor2.2">2.3 任务说明</a>）。

- [ ] 2025年5月14日：**本站**发布测试集黄金标准答案给参赛队。

- [ ] 2025年5月21日：参赛队提交中文抽象语义表示评测任务技术报告，用于审稿。

- [ ] 2025年5月25日：参赛队提交技术报告最终版。

- [ ] 2025年7月1日：评测论文录用通知，参赛队Camera-Ready版论文提交ACL/CCL Anthology收录。

- [ ] 2025年8月11日-14日：CCL 2025评测研讨会。


<a name="ldc"></a>
[![agreement](https://img.shields.io/badge/CAMRP_评测语料授权-LDC-red.svg "PDF")](./docs/LDC_Evaluation_License_Agreement_CCL2025.pdf)

**参赛队伍需自行向<a href="https://www.ldc.upenn.edu/">LDC</a>（Linguistic Data Consortium，语言数据联盟）申请CAMRP 2025评测语料使用权，并签署保密协议：**
1.	每支参赛队伍需指派一名联系负责人。
2.	参赛队伍联系负责人需填写[LDC评测语料许可协议](./docs/LDC_Evaluation_License_Agreement_CCL2025.pdf)，扫描后通过E-mail发送给LDC（<ldc@ldc.upenn.edu>）。
3.	申请通过后，**LDC**将返回**CAMRP v2.0E**版本语料（训练集和验证集）给参赛队伍联系负责人，以供参赛队伍使用。该语料数据只可用于本次CAMRP 2025评测任务，不可有其他任何用途。
4.	本次评测语料数据集的版权归**LDC**所有。


![nnu](https://img.shields.io/badge/CAMRP_2025-NNU-green.svg "sign up")

* 组织者：
  * 李斌（南京师范大学）[![Email](https://img.shields.io/badge/Email-%F0%9F%93%A7-blue)](mailto:libin.njnu@gmail.com)
  * 曲维光（南京师范大学）
  * 周俊生（南京师范大学）

* 工作人员（研究生）：
  * 许智星（南京师范大学）[![Email](https://img.shields.io/badge/Email-%F0%9F%93%A7-blue)](mailto:xzx0828@live.com) 
  * 张艺璇（南京师范大学）
  * 徐静（南京师范大学）

# 1. 任务内容
本次第五届中文抽象语义表示解析评测任务（CAMRP 2025）的重点和创新，在于自动解析中文篇章的共指链，将句子级AMR解析进一步拓展至篇章级AMR解析。
## 1.1 基于中文AMR的篇章共指语料标注
CAMR作为句子级标注语料，本身提供了包含共指关系在内的语义结构关系。因此，我们在句子级CAMR的标注体系基础之上，构建了篇章共指标注体系，进一步标注了不同句子之间概念同指的关系。CAMR篇章共指标注体系根据先行词和共指词的不同，共设计了9个共指关系类型标签，如表1所示。

​									表1 9种共指关系类型标签

| 编号 | 标签    | 含义                             | 示例                                             |
| ---- | ------- | -------------------------------- | ------------------------------------------------ |
| 1    | :root   | 该词为先行词                     | $[这个善良的女孩]_1$很开心                       |
| 2    | :homo   | 共指词与先行词相同               | $[这个善良的女孩]_1$很开心                       |
| 3    | :add    | 共指词在先行词基础上添加某些成分 | $[这个美丽善良的女孩]_1$很开心                   |
| 4    | :reduce | 共指词在先行词基础上减少某些成分 | $[这个女孩]_1$很开心                             |
| 5    | :alias  | 共指词在先行词基础上改换其他表达 | $[这个快乐的女孩]_1$很开心                       |
| 6    | :zero   | 共指词为零形式                   | $&#8709;_1$很开心                                     |
| 7    | :pro    | 共指词为代词                     | $[她]_1$很开心                                   |
| 8    | :illus  | 阐述共指，对短语或小句进行阐述   | $[张三和李四]_1$很开心，$[两个人]_1$很开心       |
| 9    | :encap  | 概述共指，对短语或小句进行概述   | $[这个善良的女孩很开心]_1$，$[这一幕]_1$非常感人 |

其中，“:homo”（同形指代）“:zero”（零指代）出现的频次较高（以500篇语料为样本进行统计），符合汉语的语言学特点。为了更好地形成CAMR篇章共指语义图的统一框架，我们在标注过程中保留了CAMR体系中的语义角色关系标签，将先行词/共指词的句内语义角色关系与共指关系相互连结，如下文2.2数据样例所示。

因此，本届CAMRP评测共包含以下两个子任务：


- **CAMR解析**：给定分词后的句子，输出句子对应的CAMR图结构，要求包含概念对齐与关系对齐信息。
- **篇章共指解析**：给定包含若干分词后的句子的篇章，输出该篇章中的所有共指链，要求包含共指关系、句子编号与共指词。

# 2. 评测数据
## 2.1 数据集
中文抽象语义表示语料库（Chinese Abstract Meaning Representation Corpus）于2015年开始，由南京师范大学和美国布兰迪斯大学合作构建。语料库为在LDC（Linguistic Data Consortium）发布的[CAMR v2.0](https://catalog.ldc.upenn.edu/LDC2021T13)，约含2万中文句子，原始语料选自于宾州中文树库（Chinese Tree Bank 8.0，CTB 8.0），分为训练集、验证集和测试集。该语料已在CoNLL 2020和CAMRP 2022-2024进行过评测。本次评测任务将继续沿用该语料库，以比较两年来中文AMR语义解析的进展。

本次评测任务新增了500篇篇章语料，语料源自宾州中文树库语料库中编号chtb0001-chtb0659中的6237句文本，涵盖经济、体育及生活等多种体裁。其中，300篇为验证集，200篇为测试集C，用以考察解析系统在篇章共指上的性能表现。

评测数据集详情具体如表2所示。相比前几届CAMRP评测任务，本次评测首次引入篇章级解析，为后续CAMR自动分析提供了新的方向与思路。



​									表2 评测数据集详情

| 数据集                | 句子数    | 词例数     |
| --------------------- | --------- | ---------- |
| 训练集（句子级）      | 16,576    | 386,234    |
| 验证集（句子级）     | 1,789     | 41,822     |
| 新增验证集（篇章级） | 约3,800句 | 约96,000词 |
| 测试集A（句子级）     | 1,713     | 39,228     |
| 测试集B（句子级）     | 1,999     | 36,940     |
| 新增测试集C（篇章级） | 约2,400句 | 约64,000词 |

## 2.2 数据样例

本次评测共提供三种类型的数据，分别为CAMR文本表示、CAMR多元组表示及篇章共指AMR图。其中，CAMR文本表示与CAMR多元组表示已在CAMRP 2022-2024三届评测任务中有过介绍，详见我们的[GitHub主页](https://github.com/GoThereGit/Chinese-AMR/)。

**篇章样例：**

> 中国 十四 个 边境 开放 城市 经济 建设 成就 显著
> 新华社 北京 二月 十二日 电
> 中国 十四 个 边境 对 外 开放 城市 一九九五年 经济 建设 取得 可喜 成果 。
> 据 统计 ， 这些 城市 去年 完成 国内 生产 总值 一百九十多亿 元 ， 比 开放 前 的 一九九一年 增长 九成多 。
> 国务院 于 一九九二年 先后 批准 了 黑河 、 凭祥 、 珲春 、 伊宁 、 瑞丽 等 十四 个 边境 城市 为 对 外 开放 城市 ， 同时 还 批准 这些 城市 设立 十四 个 边境 经济 合作区 。
> 三 年 多 来 ， 这些 城市 社会 经济 发展 迅速 ， 地方 经济 实力 明显 增强 ； 经济 年平均 增长 百分之十七 ， 高于 全 国 年平均 增长 速度 。
> 据 介绍 ， 这 十四 个 城市 的 城市 建设 和 合作区 开发 建设 步伐 加快 。
> 三 年 来 ， 这些 城市 累计 完成 固定 资产 投资 一百二十亿 元 ， 昔日 边境 城市 的 “ 楼 不 高 ， 路 不 平 、 灯 不 明 、 水 不 清 、 通讯 不 畅 ” 的 状况 已 得到 了 改变 。
> 经济 合作区 内 已 开发 二十二点六 平方公里 ， 引进 “ 三 资 ” 企业 二百八十七 家 ， 实际 利用 外资 八点九亿 美元 。
> 此外 ， 还 有 内联 企业 五千一百 家 ， 已 投产 工业 项目 一百七十五 个 。

**篇章共指AMR图样例：**

> p0003_r1_entity
> 	:root()  s1_:arg0_x6 / 城市（中国十四个边境开放城市）
> 	:add()  s3_:arg0_x8 / 城市（中国十四个边境对外开放城市）
> 	:alias()  s4_:arg0_x5 / 城市（这些城市）
> 	:alias()  s5_:arg1_x20 / 城市（黑河、凭祥、珲春、伊宁、瑞丽等十四个边境城市）
> 	:zero()  s5_:arg0_x80 / x20
> 	:alias()  s5_:arg1_x31 / x20（这些城市）
> 	:zero()  s5_:arg0_x82 / x20
> 	:alias()  s5_:arg1_x25 / 城市（这些城市）
> 	:alias()  s6_:arg0_x7 / 城市（这些城市）
> 	:zero()  s6_:arg0_x51 / x7
> 	:alias()  s7_:mod_x7 / 城市（这十四个城市）
> 	:alias()  s8_:arg0_x6 / 城市（这些城市）
> 	:zero()  s8_:arg0_x65 / x6
> 	:reduce()  s8_:poss_x17 / x6（边境城市）
>
> p0003_r2_entity
> 	:root()  s5_:arg1_x37 / 合作区（14个边境经济合作区）
> 	:reduce()  s7_:arg1_x12 / 合作区
> 	:zero()  s7_:arg1_x36 / x12
> 	:reduce()  s9_:range_x2 / 合作区（经济合作区）
>
> p0003_r3_entity
> 	:root()  s3_:direction_x6 / 外
> 	:homo()  s5_:direction_x23 / 外
>
> p0003_r4_event
> 	:root()  s7_:op1_x10 / 建设-01（这14个城市的城市建设）
> 	:encap_of_alias()  s8_x48 / causation
>
> p0003_r5_event
> 	:root()  s7_:op2_x31 / and（合作区开发建设）
> 	:encap_of_alias()  s9_x25 / and
>
> p0003_r6_entity
> 	:root()  s4_:arg1_x10 / 总值
> 	:zero()  s4_:arg0_x43 / x10
> 	:zero()  s4_:dcopy_x44 / x10

上文为篇章样例及对应的篇章共指AMR图示例。其中，该篇章的共指链共有6个，分别为①“城市”②“合作区”③“外”④“建设”⑤“合作区开发建设”⑥“总值”。标注具体信息包含：

- “p0003”表示为语料中第3个篇章
- “r1”代表该篇章中第1条共指链
- “entity”意为该共指链类型为“事件”
- “s1”代表篇章中的第1个句子
- “:arg0”为该先行词/共指词在句内的语义角色关系
- “x6”为先行词/共指词编号
- “城市”为先行词/共指词

<a name="anchor2.2"></a>
#### 2.3 任务说明

**任务输入**：（若干句子组成的篇章）

> 中国 十四 个 边境 开放 **<u>城市</u>** 经济 建设 成就 显著 。
>
> 中国 十四 个 边境 对 外 开放 **<u>城市</u>** 一九九五年 经济 建设 取得 可喜 成果 。
>
> 据 统计 ， 这些 **<u>城市</u>** 去年 完成 国内 生产 总值 一百九十多亿 元 ，...
>
> 三 年 来 ， 这些 **<u>城市</u>** 累计 完成 固定 资产 投资 一百二十亿 元 ， 昔日 边境 **<u>城市</u>** 的 “ 楼 不 高 ， 路 不 平 、 ...
>
> ...

**任务输出**：（该篇章中存在的共指链，此处以“城市”共指链为例）

> p001_r1_entity:
>
> ​	:root() s1_:arg0() x6 / 城市
>
> ​	:add() s2_:arg0() x8 / 城市
>
> ​	:alias() s3_:arg1() x5 / 城市
>
> ​	:reduce() s4_:poss() x17 / 城市

为了更加高效地完成篇章共指解析评测，在本届评测任务中，我们暂不对篇章编号（p001）、共指链编号（r1）、共指链类型（entity）和共指词语义角色关系（:arg0）等对篇章共指解析精度无关的信息进行统计，仅保留共指关系、句子编号和共指词，形成共指三元组：***relation(index, coref)***，如下表所示。

| 共指关系 | 句子编号 | 共指词                             |
| -------- | -------- | ---------------------------------- |
| :root    | s1       | 城市（中国十四个边境开放城市）     |
| :add     | s2       | 城市（中国十四个边境对外开放城市） |
| :alias   | s3       | 城市（这些城市）                   |
| :alias   | s4       | 城市（这些城市）                   |
| :reduce  | s4       | 城市（边境城市）                   |
| ...      | ...      | ...                                |

**评测指标**：

`Align-smatch（包含篇章共指解析）`

**自动标注结果提交格式**：

- 每个分项最多提交两个结果，每个结果命名格式如下：

​	`<team>_<modality>_<test>_<run>.txt`

- 参考样例：
  - PKU_open_testA_1.txt
  - PKU_open_testA_2.txt
  - PKU_closed_testB_1.txt
  - PKU_closed_testB_2.txt
  - PKU_open_testC_1.txt
  - PKU_open_testC_2.txt
- 所有结果需打包在一个文件夹内并压缩后发送至邮箱xzx0828@live.com，邮件名称为“CAMRP2025+参赛队名+submitdata”。

# 3 评价标准与模态

## 3.1 作为主要标准的Align-smatch评测指标

本次评测沿用Align-smatch（包含篇章共指解析评测）作为主要评测指标。Align-smatch与Smatch两种指标的区别在过去两届评测任务中已有相关介绍，详见<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP 2023">CAMRP 2023</a>。 

## 3.2 模态选择

​	本次评测任务包含开放测试（Open Modality）和封闭测试（Closed Modality）：

- 若参赛队选择封闭测试，则必须使用指定的训练集、测试集和预训练语言模型，不可自行替换为别的资源。在封闭测试中，主办方提供训练集的依存分析结果，并推荐使用哈工大的HIT_Roberta预训练模型。
- 若参赛队选择开放测试，预训练语言模型可自由选择（**包含ChatGPT等**），允许使用外部资源，如专名识别、依存句法分析结果等。开放测试中，参赛队使用的所有资源需要在最终提交的技术报告中给予详细说明。但无论哪种模态，均不可使用人工修正自动解析结果的方式。

​									表3 两种模态的评测要求

|  可用资源  |      封闭测试      | 开放测试 |
| :--------: | :----------------: | :------: |
|    算法    |       无限制       |  无限制  |
| 预训练模型 |    HIT_Roberta     |  无限制  |
|  外部资源  |  依存句法分析结果  |  无限制  |
|    语料    | 指定训练集和验证集 |  无限制  |
|  人工修正  |        禁止        |   禁止   |

​	为了更加完整、精确地解析CAMR，本次评测任务采用Align-smatch评测标准。各参赛队最终生成的CAMR中需包含概念对齐信息和关系对齐信息，最终成绩评分按照Align-smatch评测标准，取**测试集A**、**测试集B**和**测试集C**下的$F_1$值进行综合排名。其中，Smatch评分仅用于和其他语言的AMR解析进行对比，不计入最终排名。

# 4 撰写技术报告

- 报告可由中文或英文撰写。
- 报告统一使用CCL 2025的<a href="http://cips-cl.org/static/CCL2025/downloads/ccl2025_template.zip">论文模板</a>。
- 报告正文一般不超过4页，参考文献页数不限。
- 报告应至少包含以下四个部分：模型介绍、评测结果、分析与讨论和参考文献。

# 5 奖项设置

- 本次评测将设置一、二、三等奖，由中国中文信息学会为本次评测获奖队伍提供荣誉证书。
- 主办方为获奖队伍提供奖金。

# 6 参考文献

   [1] 孙茂松等. "语言计算的重要国际前沿." *中文信息学报* 28.1 (2014): 1-8.

   [2] Banarescu, Laura, et al. "Abstract meaning representation for sembanking." *Proceedings of the 7th linguistic annotation workshop and interoperability with discourse*. 2013.

   [3] Li, Bin, et al. "Annotating the little prince with chinese amrs." *Proceedings of the 10th linguistic annotation workshop held in conjunction with ACL 2016*. 2016.

   [4] Li, Bin, et al. "Building a Chinese AMR bank with concept and relation alignments." *Linguistic Issues in Language Technology*. 2019.

   [5] 肖力铭等. "基于概念关系对齐的中文抽象语义表示解析评测方法." *中文信息学报* 36.1 (2022): 21-30.

   [6] 戴玉玲等. "基于关系对齐的汉语虚词抽象语义表示与分析." *中文信息学报* 34.4 (2020): 21-29.

   [7] Abzianidze, L., et al. "MRP 2020: The second shared task on cross-framework and cross-lingual meaning representation parsing." *Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing*. 2020.

   [8] Cai, Shu, and Kevin Knight. "Smatch: an evaluation metric for semantic feature structures." *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*. 2013.

   [9] Cui, Yiming, et al. "Pre-training with whole word masking for chinese bert." *IEEE/ACM Transactions on Audio, Speech, and Language Processing*. 2021.

   [10] Xiao, Liming, et al. "Align-smatch: A novel evaluation method for chinese abstract meaning representation parsing based on alignment of concept and relation." *Proceedings of the Thirteenth Language Resources and Evaluation Conference*. 2022.   

   [11] Xu, Zhixing, et al. "Overview of CCL23-Eval Task 2: The Third Chinese Abstract Meaning Representation Parsing Evaluation." *Proceedings of the 22nd Chinese National Conference on Computational Linguistics (Volume 3: Evaluations)*. 2023.

   [12] Xu, Zhixing, et al. "The Fourth Chinese Abstract Meaning Representation Parsing Evaluation." *Proceedings of the 23rd Chinese National Conference on Computational Linguistics (Volume 3: Evaluations)*. 2024.

   [13] 张艺璇等. "从句子图到篇章图——基于抽象语义表示的篇章级共指标注体系研究". *外语学刊* 2025(01):19-28.

