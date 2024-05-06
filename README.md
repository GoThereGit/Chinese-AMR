<div align="center">
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/camrp2024.png" width=200>
</div>



# <p align="center">Chinese Abstract Meaning Representation Parsing 2024</p>

# <p align="center"><font size=50><strong>第四届中文抽象语义表示解析评测任务</strong></font></p>

# 最新消息：
|时间|消息|
|:---:|:---:|
|3月1日|评测任务报名|
|3月10日|评测报名推迟至3月31日|
|5月1日|测试集发布|



![What's new?](https://img.shields.io/badge/CAMRP_2024-NEW-red.svg "English Version")

**今年亮点**：新增2000句古代汉语语料，增强解析系统迁移学习和古汉语自动分析能力！

往届成绩排名请见：<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202023">**CAMRP 2023**</a> & <a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202022">**CAMRP 2022**</a>

[![Eng](https://img.shields.io/badge/README-English-yellow.svg "English Version")](./README_En.md)

**English Version:** <a href="https://github.com/GoThereGit/Chinese-AMR/blob/main/README_En.md">README_En.md</a>

[![signup](https://img.shields.io/badge/CAMRP_2024-日程-blue.svg "sign up")](https://forms.office.com/r/GS7ze5GcY7)

- [X] 2024年3月1日：<a href="https://forms.office.com/r/GS7ze5GcY7">**评测任务报名**</a>开始，提供<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202022/tools">**Align-smatch**</a>评测软件下载地址。

- [X] 2024年3月1日：LDC发布训练集以及验证集给参赛队。

- [X] ~2024年3月15日：评测任务报名截止。~

- [X] 2024年3月31日：评测任务报名截止。

- [X] 2024年5月1日：**本站**发布<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/data">**测试集**</a>（包含Test A、Test B和新的Test C）给参赛队。

- [ ] 2024年5月8日：参赛队提交自动标注的数据（提交格式详见<a href="#anchor2.2">2.2 任务说明</a>）。

- [ ] 2024年5月14日：**本站**发布测试集（包含Test A、Test B和新的Test C）黄金标准答案给参赛队。

- [ ] 2024年5月21日：参赛队提交中文抽象语义表示评测任务技术报告，用于审稿。

- [ ] 2024年5月25日：参赛队提交技术报告最终版。

- [ ] 2024年7月1日：评测论文录用通知，参赛队Camera-Ready版论文提交ACL/CCL Anthology收录。

- [ ] 2024年7月25日-28日：CCL 2024评测研讨会。

[![agreement](https://img.shields.io/badge/CAMRP_评测语料许可协议-LDC-red.svg "PDF")](./docs/LDC_Evaluation_License_Agreement_CCL2024.pdf)

**参赛队伍需自行向LDC申请CAMRP 2024评测语料使用权，并签署保密协议：**
1.	每支参赛队伍需指派一名联系负责人。
2.	参赛队伍联系负责人需填写[LDC评测语料许可协议](./docs/LDC_Evaluation_License_Agreement_CCL2024.pdf)，扫描后通过E-mail发送给LDC（<ldc@ldc.upenn.edu>）。
3.	申请通过后，LDC将返回CAMRP v2.0E版本语料库给参赛队伍联系负责人，以供参赛队伍使用。该语料数据只可用于本次CAMRP 2024评测任务，不可有其他任何用途。
4.	本次评测语料数据集的版权归<a href="https://www.ldc.upenn.edu/">LDC</a>所有。

![nnu](https://img.shields.io/badge/CAMRP_2024-NNU-green.svg "sign up")

* 组织者：
  * 李斌（南京师范大学）[![Email](https://img.shields.io/badge/Email-%F0%9F%93%A7-blue)](mailto:libin.njnu@gmail.com)
  * 曲维光（南京师范大学）
  * 周俊生（南京师范大学）
 
* 工作人员（研究生）：
  * 许智星（南京师范大学）[![Email](https://img.shields.io/badge/Email-%F0%9F%93%A7-blue)](mailto:xzx0828@live.com) 
  * 张艺璇（南京师范大学）
  * 芦靖雅（南京师范大学）

    

# 1 评测内容	
随着词法、句法分析技术的日益成熟，自然语言处理（Natural Language Processing，NLP）已整体推进到了语义分析层面
<sup>
 <a href="http://jcip.cipsc.org.cn/CN/article/downloadArticleFile.do?attachType=PDF&id=60">
  [1]
 </a>
</sup>
。句子语义作为重点和难点，更是占据了语义分析的核心地位。针对整句语义形式化表示的缺失，以及句子语义标注存在的领域相关性的问题，Banarescu et al.
<sup>
 <a href="https://aclanthology.org/W13-2322.pdf">
  [2]
 </a>
</sup>
提出了一种与领域无关的、通用的整句语义表示方法——抽象语义表示（Abstract Meaning Representation，AMR）。该方法使用单根有向无环图，来表示一个句子的语义结构，并且建设了规模较大的语料库，进行了两次国际AMR语义解析评测。与此同时，中文抽象语义表示（Chinese AMR，CAMR）语料库的构建已初具规模
<sup>
 <a href="https://aclanthology.org/W16-1702.pdf">
  [3]
 </a>
</sup>，在国际比赛CoNLL 2020上进行了语义解析评测，并连续两次进行了国内语义解析任务CAMRP 2022和CAMRP 2023的评测。

本次第四届中文抽象语义表示解析评测任务的重点和创新，在于自动解析出古汉语句子的AMR图结构。古籍处理自动化是当下研究的热点，如何有效地对古汉语中特殊的语言现象进行自动化分析，是目前的一大难点。相比英文AMR，中文AMR新增了概念对齐和关系对齐信息
<sup>
 <a href="https://journals.colorado.edu/index.php/lilt/article/view/1429/1271">
  [4]
 </a>
</sup>
，并针对中文特点增加了一些语义标签，能够更加精准地表达中文句子的语义结构。CAMRP 2022与CAMRP 2023包含了中文AMR特有的概念与关系对齐信息，弥补了CoNLL 2020上中文AMR评测的不足，取得了更好更真实的成绩，证明了中文AMR语料的质量。因此，本次评测将继续沿用前两届的语料与评测指标，对古汉语AMR自动解析性能进行评估。
## 1.1 AMR介绍
  AMR可以将一个句子的语义抽象为一个单根有向无环图，其中词抽象为概念节点（Node），词之间的语义关系抽象为带有语义角色标签的有向弧（Arc）。这种表示方法不仅可以描写一个名词由多个谓词支配所形成的论元共享（Argument Sharing）现象，还允许增加、删除、修改概念节点以补充隐含语义，进而更加完整地表达句子语义。
  
  
  整句的语义表示能力，使得AMR一经问世便引起了关注，成为了国际的热点。AMR自动解析等相关的技术也被广泛用于机器问答和文本摘要等自然语言处理下游任务中，并取得了优异的成果。在<a href="http://mrp.nlpl.eu/2020/index.php">CoNLL 2020</a>举办的跨语言跨框架语义表示解析（Meaning Representation Parsing，MRP） 评测比赛中， Hitachi
  <sup>
 <a href="https://aclanthology.org/2020.conll-shared.4.pdf">
  [5]
 </a>
</sup>
  和ÚFAL
  <sup>
 <a href="https://arxiv.org/pdf/2011.00758.pdf">
  [6]
 </a>
</sup>
  两支队伍在中文AMR解析评测任务中分别以为0.80和0.78的分数拿到了第一和第二的成绩（ÚFAL赛后补交了优化后的模型，以0.81的分数刷新了第一名的成绩）。这两支队伍实现的CAMR的解析精度接近了英文AMR的解析精度（0.82）
  <sup>
 <a href="https://aclanthology.org/2020.conll-shared.4.pdf">
  [5]
 </a>
</sup>
  。
  
  
  然而，英文AMR的缺点在于不包含概念和关系对齐信息，这给语料的训练与自动解析都带来了困扰。CAMR增加了概念关系对齐的机制，但为了和英文AMR保持格式相融，没有能在CoNLL 2020的评测中使用对齐信息。目前包括CoNLL在内的所有实验和评测所使用的指标都是基于英文AMR设计的，并不能很好地针对CAMR的特点进行兼容。评测所使用的Smatch评测指标无法对CAMR的概念和关系对齐信息进行解析和评测。因此，为了弥补CAMR解析评测在对齐信息上的空缺，为CAMR自动解析工作的提供新的标准，肖力铭等
  <sup>
 <a href="https://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2022&filename=MESS202201003&uniplatform=NZKPT&v=adniY_3P-0OTOYRAeX1Vw4Lg3POhq_Z3RIyf5-C0dU37LDFuc1MRtK17sV_Wjtkk">
  [7]
 </a>
</sup>
  在Smatch评测指标的基础上，加入了概念对齐指标和关系对齐指标——Align-smatch。CAMRP2022的评测引入了这种新的评测指标，在CoNLL2020的语料（Test A）上取得了0.8的F值，在新的语料Test B上也取得了较好的成绩。CAMRP 2022和CAMRP 2023的评测引入了这种新的评测指标，在CoNLL2020的语料上取得了最高0.81的$F_1$值，在盲测集上也取得了较好的成绩。详情请参考往届评测主页[CAMRP 2023](https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202023)。
  
## 1.2 古汉语AMR介绍
现代汉语相比古代汉语，在语音、词汇、语法方面均有变化。因此，古汉语AMR的标注在中文AMR标注框架的基础之上，增删了部分语义标签，修改了部分谓词的论元结构，并规定了特殊句式的标注方法。古汉语AMR整体上与中文AMR标注形式保持一致，同样包含了概念与关系对齐信息。如图1所示，节点“二百”被编号为x5，完成了概念对齐；虚词“以”被编号为x7，同时与语义“:arg2”一同被标注在由节点“x3/帅”指向节点“x8/伐”的有向弧上，完成了关系对齐。

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/figure1.jpg" width=500>
 <p>图1 例句“命子封帅车二百乘以伐京”古汉语AMR文本表示</p>
</div>

为了更好地描写古汉语的语义结构，古汉AMR在CAMR体系上新增了两个表示使用与意动用法的概念，分为是“make”和“consider”。如表1所示，“而速之”表达的意思为“而**使**之速”，“小人耻失其君”则意为“小人**以**失其君为耻”。


<table align="center">
<p align="center">表1 古汉AMR新增的概念标签及例子说明</p>
<thead>
  <tr>
    <th>新增概念标签</th>
    <th>节选例句</th>
    <th>对应标注</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>make-01</td>
    <td>“...而速之...”</td>
    <td>...<br>:arg2(x10/而) (x29 / make-01<br>      :arg1() (x11 / 速<br>...</td>
  </tr>
  <tr>
    <td>consider-01</td>
    <td>”...小人耻失其君...“</td>
    <td>...<br>:op1() (x48 / consider-01<br>      :arg0() (x8 / 小人<br>...</td>
  </tr>
</tbody>
</table>


词类活用是古代汉语中常见的语言现象。古汉语AMR根据这一特点，主要新增了名词作动词和名词作状语的标注规则。如图2所示，“皆肘之”中的“肘”，在实际标注中需将胳膊击打的动作补充出来，即将“击-01”作为句子的根节点，从而还原真实的语义表达。

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/figure2.png" width=300>
 <p>图2 古汉语AMR中名词作动词标注样例</p>
</div>


# 2 评测数据

## 2.1 数据样例
本次评测任务提供两种数据，包括**CAMR文本表示**及**CAMR多元组表示**。例句“命子封帅车二百乘以伐京”选自本次评测任务的测试集，以下为对应的两种表示样例：

[![sample](https://img.shields.io/badge/sample-CAMR_text-red.svg "CAMR_text")](https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/samples/CAMR_text.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/figure3.jpg" width=500>
 <p>图3 例句古汉语AMR文本表示样例</p>
</div>

图3为例句的古汉语AMR文本表示样例，具体包括句子ID、词序列、词编号（x）、概念对齐信息、关系对齐信息和CAMR文本表示；语料编码格式为UTF-8。

[![sample](https://img.shields.io/badge/sample-CAMR_tuple-blue.svg "CAMR_tuple")](https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/samples/CAMR_tuple.txt)


<table align=center>
<p align=center>表2 例句古汉语AMR多元组表示样例</p>
<thead>
  <tr>
    <th>句子编号</th>
    <th>节点编号1</th>
    <th>概念1</th>
    <th>关系</th>
    <th>关系编号</th>
    <th>关系对齐词</th>
    <th>节点编号2</th>
    <th>概念2</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>37</td>
    <td>x0</td>
    <td>root</td>
    <td>:top</td>
    <td>-</td>
    <td>-</td>
    <td>x1</td>
    <td>命</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x1</td>
    <td>命</td>
    <td>:arg1</td>
    <td>-</td>
    <td>-</td>
    <td>x14</td>
    <td>person</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x1</td>
    <td>命</td>
    <td>:arg2</td>
    <td>-</td>
    <td>-</td>
    <td>x3</td>
    <td>帅</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x14</td>
    <td>person</td>
    <td>:name</td>
    <td>-</td>
    <td>-</td>
    <td>x2</td>
    <td>子封</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x3</td>
    <td>帅</td>
    <td>:arg0</td>
    <td>-</td>
    <td>-</td>
    <td>x14</td>
    <td>person</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x3</td>
    <td>帅</td>
    <td>:arg1</td>
    <td>-</td>
    <td>-</td>
    <td>x4</td>
    <td>车</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x3</td>
    <td>帅</td>
    <td>:arg2</td>
    <td>x7</td>
    <td>以</td>
    <td>x8</td>
    <td>伐</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x4</td>
    <td>车</td>
    <td>:quant</td>
    <td>-</td>
    <td>-</td>
    <td>x5</td>
    <td>二百</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x4</td>
    <td>车</td>
    <td>:cunit</td>
    <td>-</td>
    <td>-</td>
    <td>x6</td>
    <td>乘</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x8</td>
    <td>伐</td>
    <td>:arg0</td>
    <td>-</td>
    <td>-</td>
    <td>x14</td>
    <td>person</td>
  </tr>
  <tr>
    <td>37</td>
    <td>x8</td>
    <td>伐</td>
    <td>:arg1</td>
    <td>-</td>
    <td>-</td>
    <td>x9</td>
    <td>京</td>
  </tr>
</tbody>
</table>

​	表2为例句的古汉语AMR多元组表示样例，具体包括句子编号1、节点编号1、概念1、同指节点1、关系、关系编号、关系对齐词、节点编号2、概念2和同指节点2。参赛队最终返回的自动标注数据也应为古汉语AMR多元组表示格式。


<a name="anchor2.2"></a>
## 2.2 任务说明

**输入：**
（分词后的句子）

``
命 子封 帅 车 二百 乘 以 伐 京
``

**输出：**
（CAMR多元组；<a href = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/tools/camr_to_tuples.py">转换脚本</a>由本站提供。）

``
见表2
``

**评测指标：**

``
Align-smatch
``

**自动标注结果提交格式：**

每个分项最多提交两个结果，每个结果命名格式如下：

``
<team>_<modality>_<test>_<run>.txt
``

参考样例：

- PKU_open_testA_1.txt
- PKU_open_testA_2.txt
- PKU_open_testB_1.txt
- PKU_open_testB_2.txt
- PKU_open_testC_1.txt
- PKU_open_testC_2.txt

所有结果需打包在一个文件夹内并压缩后发送至邮箱<xzx0828@live.com>，邮件名称为“CAMRP2024+参赛队名+submitdata”。

## 2.3 数据集
中文抽象语义表示语料库（Chinese Abstract Meaning Representation Corpus）于2015年开始，由南京师范大学和美国布兰迪斯大学合作构建
<sup>
 <a href="https://aclanthology.org/W16-1702.pdf">
  [3]
 </a>
</sup>。语料库为在LDC（Linguistic Data Consortium）发布的<a href="https://catalog.ldc.upenn.edu/LDC2021T13">CAMR v2.0</a>，约含2万中文句子，原始语料选自于宾州中文树库（Chinese Tree Bank 8.0，CTB 8.0），分为训练集、验证集和测试集。该语料和测试集B已在CoNLL 2020、CAMRP 2022和CAMRP 2023进行过评测。本次评测任务将继续沿用该语料库，以比较两年来中文AMR语义解析的进展。

​	本次评测任务新增了约2500句古代汉语语料，语料选自南京师范大学文学院经分词处理后的《左传》文本。同时，在标注过程中选取了杨伯峻版的《春秋左传注》注本作为参考。其中，500句为验证集B，2000句为测试集C，以重点考察解析系统在古汉语上的性能表现。

​	提供的各项数据具体如表3所示：


<table align="center">
<p align="center">表3 评测数据集详情</p>
<thead>
  <tr>
    <th>数据集（Data Sets）</th>
    <th>句子数（Sentences）</th>
    <th>词例数（Word Tokens）</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>训练集（现汉）</td>
    <td>16576</td>
    <td>386234</td>
  </tr>
  <tr>
    <td>验证集A（现汉）</td>
    <td>1789</td>
    <td>41822</td>
  </tr>
  <tr>
    <td><b>新增</b>验证集B（古汉）</td>
    <td>约500句</td>
    <td>约5000词</td>
  </tr>
  <tr>
    <td>测试集A（现汉）</td>
    <td>1713</td>
    <td>39228</td>
  </tr>
  <tr>
    <td>测试集B（现汉）</td>
    <td>1999</td>
    <td>36940</td>
  </tr>
  <tr>
    <td><b>新增</b>测试集C（古汉）</td>
    <td>约2000句</td>
    <td>约2万词</td>
  </tr>
</tbody>
</table>


# 3 评价标准与模态
## 3.1 作为主要标准的Align-smatch评测指标
本次评测沿用Align-smatch作为主要评测指标。Align-smatch与Smatch两种指标的区别在过去两届评测任务中已有相关介绍，详见[CAMRP 2023](https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202023)。


<a name="anchor3.3"></a>
## 3.2 模态选择
本次评测任务包含开放测试（Open Modality）和封闭测试（Closed Modality）：
1. 若参赛队选择封闭测试，则必须使用指定的训练集、测试集和预训练语言模型，不可自行替换为别的资源。在封闭测试中，主办方提供训练集的依存分析结果，并推荐使用哈工大的HIT_Roberta<sup><a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9599397">[12]</a></sup>预训练模型。
2. 若参赛队选择开放测试，预训练语言模型可自由选择（**包含ChatGPT等**），允许使用外部资源，如专名识别、依存句法分析结果等。开放测试中，参赛队使用的所有资源需要在最终提交的技术报告中给予详细说明。但无论哪种模态，均不可使用人工修正自动解析结果的方式。

<table align="center">
<p align="center">表4 两种模态的评测要求</p>
<thead>
  <tr>
    <th align='center'>可用资源</th>
    <th style="text-align:center">封闭测试</th>
    <th align='center'>开放测试</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>算法</td>
    <td align='center'>无限制</td>
    <td align='center'>无限制</td>
  </tr>
  <tr>
    <td align='center'>预训练模型</td>
    <td align='center'>HIT_Roberta</td>
    <td align='center'>无限制</td>
  </tr>
   <tr>
    <td align='center'>外部资源</td>
    <td align='center'>依存句法分析结果</td>
    <td align='center'>无限制</td>
  </tr>
  <tr>
    <td align='center'>语料</td>
    <td align='center'>指定训练集和测试集</td>
    <td align='center'>无限制</td>
  </tr>
  <tr>
    <td align='center'>人工修正</td>
    <td align='center'>禁止</td>
    <td align='center'>禁止</td>
  </tr>
</tbody>
</table>

为了更加完整、精确地解析古汉AMR，本次评测任务采用Align-smatch评测标准。各参赛队最终生成的AMR结果中需包含概念对齐信息和关系对齐信息，最终成绩评分按照Align-smatch评测标准，取**测试集C**下的$F_1$值进行排名。其中，Smatch评分仅用于和其他语言的AMR解析进行对比，不计入最终排名。



# 4 撰写技术报告
1.  报告可由中文或英文撰写。
2.  报告统一使用CCL 2024的<a href="http://cips-cl.org/static/CCL2024/downloads/ccl2024_template.rar">论文模板</a>。
3.  报告正文不得超过4页，参考文献页数不限。
4.  报告应至少包含以下四个部分：模型介绍、评测结果、结果分析与讨论和参考文献。


# 5 奖项设置
* 本届评测将设置一、二、三等奖，提供总额为**7000元**的奖金。
* 中国中文信息学会为本次评测获奖队伍提供荣誉证书。

# 6 参考文献
1. 孙茂松, et al. "语言计算的重要国际前沿." 中文信息学报 28.1 (2014): 1-8.
2. Banarescu, Laura, et al. "Abstract meaning representation for sembanking." Proceedings of the 7th linguistic annotation workshop and interoperability with discourse. 2013.
3. Li, Bin, et al. "Annotating the little prince with chinese amrs." Proceedings of the 10th linguistic annotation workshop held in conjunction with ACL 2016 (LAW-X 2016). 2016.
4. Li, Bin, et al. "Building a Chinese AMR bank with concept and relation alignments." Linguistic Issues in Language Technology 18 (2019).
5. Ozaki, Hiroaki, et al. "Hitachi at MRP 2020: Text-to-graph-notation transducer." Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing. 2020.
6. Samuel, David, and Milan Straka. "UFAL at MRP 2020: Permutation-invariant Semantic Parsing in PERIN." arXiv preprint arXiv:2011.00758 (2020).
7. 肖力铭, et al. "基于概念关系对齐的中文抽象语义表示解析评测方法." 中文信息学报 36.1 (2022): 21-30.
8. 戴玉玲, et al. "基于关系对齐的汉语虚词抽象语义表示与分析." 中文信息学报 34.4 (2020): 21-29.
9. Abzianidze, L., et al. "MRP 2020: The second shared task on cross-framework and cross-lingual meaning representation parsing." Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing (2020): 1-22.
10. Cai, Shu, and Kevin Knight. "Smatch: an evaluation metric for semantic feature structures." Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2013.
11. Song, Linfeng, and Daniel Gildea. "SemBleu: A robust metric for AMR parsing evaluation." arXiv preprint arXiv:1905.10726 (2019).
12. Cui, Yiming, et al. "Pre-training with whole word masking for chinese bert." IEEE/ACM Transactions on Audio, Speech, and Language Processing 29 (2021): 3504-3514.
13. Xu, Zhixing, et al. "[Overview of CCL23-Eval Task 2: The Third Chinese Abstract Meaning Representation Parsing Evaluation.](https://aclanthology.org/2023.ccl-3.7.pdf)" Proceedings of the 22nd Chinese National Conference on Computational Linguistics (Volume 3: Evaluations). 2023.
