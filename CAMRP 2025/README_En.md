
<div align="center">
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/camrp2025.png" width=200>
</div>


# <p align="center"><font size=50><strong>The 5th Chinese Abstract Meaning Representation Parsing Evaluation</strong></font></p>

![What's new?](https://img.shields.io/badge/CAMRP_2025-NEW-red.svg "English Version")

**Highlights of this year**: Over 6000 new sentences in the corpus, focusing on **discourse coreference resolution**, testing the model's ability to parse discourse coreference!

**Previous evaluation papers** are now included in the **ACL Anthology**: <a href="https://aclanthology.org/volumes/2023.ccl-3/">CCL23-Eval</a>, <a href="https://aclanthology.org/volumes/2024.ccl-3/">CCL24-Eval</a>

[![Eng](https://img.shields.io/badge/README-English-yellow.svg "English Version")](./README_En.md)

**Chinese Version:** <a href="https://github.com/GoThereGit/Chinese-AMR/blob/main/README.md">README.md</a>

[![signup](https://img.shields.io/badge/CAMRP_2025-Schedule-blue.svg "sign up")](https://forms.office.com/r/wwU0NgZdJz)

- [X] March 1, 2025: <a href="https://forms.office.com/r/wwU0NgZdJz">**Evaluation task registration**</a> starts.
- [X] March 20, 2025: **LDC** releases the training and validation sets to the participating teams (see <a href="#ldc">Evaluation Corpus Licensing</a>).
- [ ] April 15, 2025: Registration for evaluation tasks ends.
- [ ] May 1, 2025: **This site** releases the **test set** to participating teams.
- [ ] May 8, 2025: Teams submit automatic annotation results (submission format detailed in <a href="#anchor2.2">2.3 Task Description</a>).
- [ ] May 14, 2025: **This site** releases the gold standard data to participating teams.
- [ ] May 21, 2025: Teams submit the technical report for the Chinese Abstract Meaning Representation Parsing Evaluation task for review.
- [ ] May 25, 2025: Teams submit the final version of the technical report.
- [ ] July 1, 2025: Notification of acceptance of evaluation papers, and submission of Camera-Ready papers for inclusion in the ACL/CCL Anthology.
- [ ] August 11-14, 2025: CCL 2025 Evaluation Workshop.

<a name="ldc"></a>
[![agreement](https://img.shields.io/badge/CAMRP_Licensing-LDC-red.svg "PDF")](./docs/LDC_Evaluation_License_Agreement_CCL2025.pdf)

**Participating teams must apply for the CAMRP 2025 evaluation corpus from the <a href="https://www.ldc.upenn.edu/">LDC</a> (Linguistic Data Consortium) and sign a non-disclosure agreement:**
1. Each team must designate a contact person.
2. The contact person must fill out the [LDC Evaluation Corpus License Agreement](./docs/LDC_Evaluation_License_Agreement_CCL2025.pdf), scan it, and send it to LDC via email (<ldc@ldc.upenn.edu>).
3. After the application is approved, **LDC** will return the **CAMRP v2.0E** version of the corpus (train and dev sets) to the contact person for team use. The corpus data can only be used for the CAMRP 2025 evaluation task and cannot be used for any other purposes.
4. The copyright of the evaluation corpus dataset belongs to **LDC**.

![nnu](https://img.shields.io/badge/CAMRP_2025-NNU-green.svg "sign up")

*Organizers:*
  * Bin Li (Nanjing Normal University) [![Email](https://img.shields.io/badge/Email-%F0%9F%93%A7-blue)](mailto:libin.njnu@gmail.com)
  * Weiguang Qu (Nanjing Normal University)
  * Junsheng Zhou (Nanjing Normal University)

*Staff (Graduate Students):*
  * Zhixing Xu (Nanjing Normal University) [![Email](https://img.shields.io/badge/Email-%F0%9F%93%A7-blue)](mailto:xzx0828@live.com)
  * Yixuan Zhang (Nanjing Normal University)
  * Jing Xu (Nanjing Normal University)

# 1. Task Content
The main focus and innovation of the 5th Chinese Abstract Meaning Representation Parsing Evaluation (CAMRP 2025) lies in the automatic parsing of discourse coreference chains in Chinese, expanding sentence-level AMR parsing to discourse-level AMR parsing.

## 1.1 Discourse Coreference Annotation Based on Chinese AMR
CAMR, as a sentence-level annotated corpus, itself provides semantic relations, including coreference relations. Therefore, based on the sentence-level CAMR annotation system, we have constructed a discourse coreference annotation system, which further annotates the coreference relations between concepts across sentences. The discourse coreference annotation system in CAMR is designed with 9 coreference relation types, as shown in Table 1.

| No.  | Label  | Meaning                                 | Example                                       |
| ---- | ------ | --------------------------------------- | --------------------------------------------- |
| 1    | :root  | The word is the antecedent.             | **_This kind-hearted girl_** is happy.       |
| 2    | :homo  | Coreferent and antecedent are the same. | **_This kind-hearted girl_** is happy.       |
| 3    | :add   | Coreferent adds some elements to antecedent. | **_This beautiful and kind girl_** is happy. |
| 4    | :reduce| Coreferent reduces some elements from antecedent. | **_This girl_** is happy.                  |
| 5    | :alias | Coreferent changes the expression of the antecedent. | **_This happy girl_** is happy.            |
| 6    | :zero  | Coreferent is in zero form.            | $&#8709;_1$ is happy.                        |
| 7    | :pro   | Coreferent is a pronoun.               | **_She_** is happy.                          |
| 8    | :illus | Coreference provides further clarification. | **_Zhang San and Li Si_** are happy, **_Both_** are happy. |
| 9    | :encap | Coreference gives a summary or encapsulates. | **_This kind-hearted girl_** is happy, **_This scene_** is very touching. |

Among these, “:homo” (homophoric) and “:zero” (zero coreference) occur more frequently, in line with the linguistic characteristics of Chinese. In order to form a unified framework for the CAMR discourse coreference graph, we retained the semantic role relation labels in the CAMR system, linking the in-sentence semantic role relations of antecedents/coreferents to coreference relations, as shown in the data example in section 2.2.

Thus, this year's CAMRP evaluation includes two sub-tasks:

- **CAMR Parsing**: Given tokenized sentences, output the corresponding CAMR graph structure, which should include concept alignment and relation alignment information.
- **Discourse Coreference Parsing**: Given a discourse consisting of several tokenized sentences, output all coreference chains in the discourse, including coreference relations, sentence numbers, and coreferent words.

# 2. Evaluation Data
## 2.1 Dataset
The Chinese Abstract Meaning Representation Corpus (CAMR) was initiated in 2015, a collaborative project between Nanjing Normal University and Brandeis University. The corpus is based on the LDC-released [CAMR v2.0](https://catalog.ldc.upenn.edu/LDC2021T13) and contains about 20,000 Chinese sentences. The original data was selected from the Chinese Tree Bank 8.0 (CTB 8.0), divided into training, validation, and test sets. This corpus has been used in evaluations such as CoNLL 2020 and CAMRP 2022-2024. This year's evaluation will continue using this corpus to compare the progress in Chinese AMR semantic parsing over the past two years.

This year's evaluation task introduces 500 new chapters, sourced from 6237 sentences in the Chinese Tree Bank, covering various genres such as economy, sports, and daily life. Among these, 200 chapters are for Validation Set B, and 300 chapters are for Test Set C, testing the model's performance in discourse coreference.

## 2.2 Sample Data

This year, we provide three types of data: CAMR text representation, CAMR tuple representation, and discourse coreference AMR graphs. Details can be found in our [GitHub page](https://github.com/GoThereGit/Chinese-AMR/).

**Discourse Example:**

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

**Discourse Coreference AMR Graph Example:**

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

## 2.3 Task Description
- **Task Input**: (A discourse composed of several sentences)

> 中国 十四 个 边境 开放 **<u>城市</u>** 经济 建设 成就 显著 。
>
> 中国 十四 个 边境 对 外 开放 **<u>城市</u>** 一九九五年 经济 建设 取得 可喜 成果 。
>
> 据 统计 ， 这些 **<u>城市</u>** 去年 完成 国内 生产 总值 一百九十多亿 元 ，...
>
> 三 年 来 ， 这些 **<u>城市</u>** 累计 完成 固定 资产 投资 一百二十亿 元 ， 昔日 边境 **<u>城市</u>** 的 “ 楼 不 高 ， 路 不 平 、 ...
>
> ...


- **Task Output**: (The coreference chain in this discourse, using the "城市(city)" coreference chain as an example)

> p001_r1_entity:
>
> ​	:root() s1_:arg0() x6 / 城市
>
> ​	:add() s2_:arg0() x8 / 城市
>
> ​	:alias() s3_:arg1() x5 / 城市
>
> ​	:reduce() s4_:poss() x17 / 城市

To more efficiently complete the discourse coreference parsing evaluation, we will not record irrelevant information such as discourse IDs (_p001_), coreference chain IDs (_r1_), 
coreference chain types (_entity_), and the semantic role relation of coreferent words (e.g., _:arg0_) in this evaluation task. 
Instead, we will only keep the coreference relations, sentence IDs, and coreferent words, forming coreference triples: **_relation(index, coref)_**, as shown in the table below.


| Coreference Relation | Sentence ID | Coreferent |                 
| -------- | -------- | ---------------------------------- |
| :root    | s1       | 城市（中国十四个边境开放城市）     |
| :add     | s2       | 城市（中国十四个边境对外开放城市） |
| :alias   | s3       | 城市（这些城市）                   |
| :alias   | s4       | 城市（这些城市）                   |
| :reduce  | s4       | 城市（边境城市）                   |
| ...      | ...      | ...                                |

- **Evaluation Metric**:

Align-smatch (including discourse coreference resolution)

- **Submission Format for Automatic Annotation Results**:

Each subtask can submit up to two results, with each result named in the following format:
​	`<team>_<modality>_<test>_<run>.txt`

- **Example**:
  - PKU_open_testA_1.txt
  - PKU_open_testA_2.txt
  - PKU_closed_testB_1.txt
  - PKU_closed_testB_2.txt
  - PKU_open_testC_1.txt
  - PKU_open_testC_2.txt

All results must be packaged in a folder, compressed, and sent to the email xzx0828@live.com. The email subject should be `CAMRP2025+Team Name+submitdata`.


# 3. Evaluation Criteria & Modalities

## 3.1 Align-smatch Evaluation Metric

The primary evaluation metric for this year is Align-smatch, which incorporates discourse coreference parsing. This metric has been introduced in previous evaluations, such as in <a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP 2023">CAMRP 2023</a>.

## 3.2 Modalities

This year, the evaluation will include both open and closed modalities:

- **Closed modality**: Teams must use the specified training and test sets and pre-trained language models.
- **Open modality**: Teams are free to choose their own pre-trained models, such as ChatGPT, and may use external resources.


| Available Resources | Closed Test | Open Test |
| :----------------: | :---------: | :-------: |
| Algorithm          | No restriction | No restriction |
| Pre-trained Model  | HIT_Roberta  | No restriction |
| External Resources | Dependency parsing results | No restriction |
| Corpus             | Specified training and test sets | No restriction |
| Manual Correction  | Forbidden   | Forbidden |



# 4. Technical Report Writing

- The report can be written in either Chinese or English. See <a href="http://cips-cl.org/static/CCL2025/downloads/ccl2025_template.zip">CCL 2025 template</a>.
- The report should not exceed 4 pages, with no limit on references.
- The report should contain at least the following four parts: model description, evaluation results, analysis and discussion, and references.

# 5. Awards

- Prizes for first, second, and third place will be awarded by the Chinese Information Processing Society of China (CIPSC).
- Monetary rewards will be provided to the winners.

# 6. References
   [1] 孙茂松等. "语言计算的重要国际前沿." 中文信息学报 28.1 (2014): 1-8.

   [2] 肖力铭等. "基于概念关系对齐的中文抽象语义表示解析评测方法." 中文信息学报 36.1 (2022): 21-30.

   [3] 戴玉玲等. "基于关系对齐的汉语虚词抽象语义表示与分析." 中文信息学报 34.4 (2020): 21-29.

   [4] Banarescu, Laura, et al. "Abstract meaning representation for sembanking." *Proceedings of the 7th linguistic annotation workshop and interoperability with discourse*. 2013.

   [5] Li, Bin, et al. "Annotating the little prince with chinese amrs." *Proceedings of the 10th linguistic annotation workshop held in conjunction with ACL 2016*. 2016.

   [6] Li, Bin, et al. "Building a Chinese AMR bank with concept and relation alignments." *Linguistic Issues in Language Technology*. 2019.

   [7] Ozaki, Hiroaki, et al. "Hitachi at MRP 2020: Text-to-graph-notation transducer." *Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing*. 2020.

   [8] Samuel, David, and Milan Straka. "ÚFAL at MRP 2020: Permutation-invariant Semantic Parsing in PERIN." *Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing*. 2020.

   [9] Oepen, Stephan, et al. "MRP 2020: The second shared task on cross-framework and cross-lingual meaning representation parsing." *Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing*. 2020.

   [10] Cai, Shu, and Kevin Knight. "Smatch: an evaluation metric for semantic feature structures." *Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers)*. 2013.

   [11] Cui, Yiming, et al. "Pre-training with whole word masking for chinese bert." *IEEE/ACM Transactions on Audio, Speech, and Language Processing*. 2021.

   [12] Xiao, Liming, et al. "Align-smatch: A novel evaluation method for chinese abstract meaning representation parsing based on alignment of concept and relation." *Proceedings of the Thirteenth Language Resources and Evaluation Conference*. 2022.
