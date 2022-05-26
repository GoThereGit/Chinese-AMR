# CAMRP 2022
**Chinese Abstract Meaning Representation Parsing 2022**
# 中文抽象语义表示解析评测任务
* 组织者：
  * 李斌（南京师范大学）  
  * 曲维光（南京师范大学）
  * 周俊生（南京师范大学）
  * 薛念文（布兰迪斯大学）
 
* 工作人员：
  * 许智星（南京师范大学）
  * 肖力铭（南京师范大学）
  * 芦靖雅（南京师范大学）
  * 陈瑾（南京师范大学）
  * 谢媛媛（南京师范大学）
  * 袁义国（南京师范大学）

# 1 评测内容	
随着词法、句法分析技术的日益成熟，自然语言处理（Natural Language Processing，NLP）已整体推进到了语义分析层面（孙茂松等，2014）。句子语义作为重点和难点，更是占据了语义分析的核心地位。针对整句语义形式化表示的缺失，以及句子语义标注存在的领域相关性的问题，Banarescu et al.（2013）提出了一种与领域无关的、通用的整句语义表示方法——抽象语义表示（Abstract Meaning Representation，AMR）。该方法使用单根有向无环图，来表示一个句子的语义结构，并且建设了规模较大的语料库，进行了两次国际AMR语义解析评测。中文抽象语义表示（Chinese AMR，简称CAMR）语料库的构建已初具规模，也在CoNLL2020上进行了语义解析评测。


本次评测任务是在中文抽象语义语料库上，自动解析出句子的AMR图。与英文AMR不同的是，中文AMR增加了概念关系对齐信息，并针对中文特点增加了一些语义标签。概念关系对齐信息并没有用于CoNLL2020的评测。因此，本次评测重新设计了包含了概念关系对齐的信息的新评测指标Align-smatch，能够更好地评估自动解析的性能。
## 1.1 AMR介绍
  AMR可以将一个句子的语义抽象为一个单根有向无环图，其中词抽象为概念节点（Node），词之间的语义关系抽象为带有语义角色标签的有向弧（Arc）。这种表示方法不仅可以描写一个名词由多个谓词支配所形成的论元共享（Argument Sharing）现象，还允许增加、删除、修改概念节点以补充隐含语义，进而更加完整地表达句子语义。
  
  
  整句的语义表示能力，使得AMR一经问世便引起了关注，成为了国际的热点。AMR自动解析等相关的技术也被广泛用于机器问答和文本摘要等自然语言处理下游任务中，并取得了优异的成果。在CoNLL 2020举办的跨语言跨框架语义表示解析（Meaning Representation Parsing，MRP） 评测比赛中， Hitachi和ÚFAL两支队伍在中文AMR解析评测任务中分别以为0.80和0.78的分数拿到了第一和第二的成绩（ÚFAL赛后补交了优化后的模型，以0.81的分数刷新了第一名的成绩）（Hiroaki O. et al.，2020）（Samuel D. et al.，2020）。这两支队伍实现的CAMR的解析精度接近了英文AMR的解析精度（0.82）（Hiroaki O. et al.，2020）。
  
  
  然而，英文AMR的缺点在于不包含概念和关系对齐信息，这给语料的训练与自动解析都带来了困扰。CAMR增加了概念关系对齐的机制，但为了和英文AMR保持格式相融，没有能在CoNLL2020的评测中使用对齐信息。目前包括CoNLL在内的所有实验和评测所使用的指标都是基于英文AMR设计的，并不能很好地针对CAMR的特点进行兼容。评测所使用的Smatch评测指标无法对CAMR的概念和关系对齐信息进行解析和评测。因此，为了弥补CAMR解析评测在对齐信息上的空缺，为CAMR自动解析工作的提供新的标准，肖力铭等（2022）在Smatch评测指标的基础上，加入了概念对齐指标和关系对齐指标——Align-smatch。以下将详细介绍CAMR的特点和Align-smatch评测指标。
## 1.2 中文AMR介绍
在英文AMR的标注中，一般使用词语的首字母作为概念节点的编号，或者按照节点的出现顺序来直接分配编号，这导致计算机处理时无法对概念溯源，一定程度上影响了解析的精度。为了解决这一问题，Li et al.（2019）根据汉语的特点对AMR进行了改进，在保留了AMR较强语义表示能力的同时，在CAMR中增加了“词与概念”的对齐信息和“词与关系”的对齐信息。通过对分词后对原始句子按照线性排序的原则，采用“x+数字”的形式，依次给每个词赋予不同的编号，而对应的概念节点也获得相同的编号。如图1中，“惨痛”为句子中的第3个词，因而被赋予了“x3”的编号，同时与概念节点“x3/惨痛-01”完成了对齐。


除了编号方案的处理不同，CAMR对虚词的处理也不一样。英文AMR一般直接忽略了句子中如介词、冠词等对句子语义没有贡献的虚词。而考虑到语言的不同特点，CAMR选择保留虚词并对其进行标注，将表示句子体意义和语气意义的虚词处理为概念节点，将表示实词间关系意义的虚词看作语义关系的映射，并将其与语义角色标签一同标注在有向弧上（戴玉玲等，2020）。最后，沿用概念对齐中编号的方案，有向弧上的虚词同样被赋予了顺序的编号，以实现关系对齐。如图2所示，虚词“的”和语义角色标签“arg0-of”一起被标注在了有向弧上，又由于它是第4个词，因而被编号为“x4”，以上两个步骤完成了语义关系“arg0-of”和虚词“x4/的”的对齐。
## 1.3 小结
因此，为了更好地推进中文抽象语义表示解析工作的展开，南京师范大学提出了本次中文抽象语义表示评测任务。不同于CoNLL 2020举办的MRP跨语言/跨语义框架评测，本次评测任务是对中文AMR解析评测，评测标准选用更加细致的Align-smatch评测标准，包括了概念对齐信息和关系对齐信息（详见下文3.2）。
# 2 评测数据
## 2.1 数据样例
图3为评测语料的CAMR数据样例，具体包括句子ID、词序列、词编号（x）、概念对齐信息、关系对齐信息和CAMR文本表示；语料编码格式为UTF-8。
## 2.2 数据集
中文抽象语义表示语料库（Chinese Abstract Meaning Representation Corpus）于2015年开始，由南京师范大学和美国布兰迪斯大学合作构建。语料库为在LDC发布的CAMR v2.0 ，约含2万中文句子，原始语料选自于宾州中文树库（Chinese Tree Bank 8.0，CTB 8.0），分为训练集、验证集和测试集，该语料已经在CoNLL2020进行评测。本次评测任务中，继续沿用该语料库，以比较两年来中文AMR语义解析的进展。为了防止参赛队将测试集用于训练，本次评测设置了盲测集，约含2000句语料。该部分语料没有公开，亦可观察各个系统在盲测数据集上，可用来评测解析模型处理不同语体风格的文本数据时的泛化能力。提供的各项数据分布如表1所示：
<table style="margin:0 auto;">
<caption>表1 评测数据集</caption>
<thead>
  <tr>
    <th style="text-align:center">数据集（Data Sets）</th>
    <th style="text-align:center">句子数（Sentences）</th>
    <th style="text-align:center">词例数（Word Tokens）</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>训练集（Training Set）</td>
    <td align='center'>16576</td>
    <td align='center'>386234</td>
  </tr>
  <tr>
    <td align='center'>验证集（Validation Set）</td>
    <td align='center'>1789</td>
    <td align='center'>41822</td>
  </tr>
  <tr>
    <td align='center'>测试集（Test A）</td>
    <td align='center'>1713</td>
    <td align='center'>39228</td>
  </tr>
  <tr>
    <td align='center'>盲测集（Test B）</td>
    <td align='center'>约2000句</td>
    <td align='center'>约4万句</td>
  </tr>
</tbody>
</table>
# 3 评价标准
## 3.1 作为参考标准的Smatch评测指标
作为目前最主要的AMR评测指标，Smatch主要考虑的是两个AMR图之间的重叠程度。对于两个需要进行匹配的AMR图，Smatch首先将每个AMR图转化为三元组（Triple）的集合（S. Cai，2013），每个集合一般包含三种数据类型的三元组：
1.  **表示节点的三元组：instance(node_index, concept)。**
其中，instance表示对概念节点的实例化；node_index为节点索引，记作$a_i$，$i∈${$0,1,…,n$}；concept为由词抽象出的概念。如表2所示，在例句“希望我惨痛的经历给大家一个教训呀”对应的AMR三元组中，节点三元组包含了所有节点的实例、节点索引和对应的概念。如三元组“instance($a_0$, 希望-01)”表示“希望”一词的实例化，该词的节点索引为$a_0$，AMR抽象出的概念为“希望-01”。
2.  **表示有向弧的三元组：relation(node_index1, node_index2)。**
node_index1和node_index2表示为两个不同概念节点的索引，分别对应$a_i$和$a_j$，同理，$j∈${$0,1,…,n$}，节点索引的分配可以是完全随机的，如图5所示（本文选用完全二叉树的顺序存储方式对节点索引进行编号，仅供参考）；relation为$a_i$、$a_j$节点对应的两个词之间的语义关系。如表2所示，有向弧三元组“arg1($a_1$,$a_4$)”表示$a_1$索引和$a_4$索引所对应的词“给”和“大家”之间的语义关系为“arg1（受事）”。
3.  **表示节点属性的三元组：property(node_index, value)。**
如表2所示，节点属性三元组root($a_0$, top)表示$a_0$节点的属性为根节点，其中，value=top。
完成了AMR三元组的转化之后，Smatch使用爬山算法（Hill-climbing Method）进行贪婪搜索以获取黄金AMR（Gold AMR）三元组集合和解析生成的AMR（Generated AMR）三元组集合之间的最大匹配个数，最终返回准确率（P）、召回率（R）和F值（F-score）：
$$ P = \frac{\#Matching\enspace Triples}{\#Generated\enspace Triples} $$
$$ R = \frac{\#Matching\enspace Triples}{\#Gold\enspace Triples} $$
$$ F_β=(1+β^2)*\frac{(P*R)}{(β^2*P)+R} $$

其中，Smatch里的准确率P为黄金AMR的三元组集合和解析生成的AMR三元组集合间的最大匹配个数与解析生成的AMR的三元组总个数之比；召回率R为黄金AMR三元组集合和解析生成的AMR三元组集合间的最大匹配个数与黄金AMR的三元组总个数之比；F值为准确率和召回率的调和平均值（Harmonic Mean），$β∈R^+$，表示为影响权重：当$β>1$时，召回率比准确率更重要；反之，当$β<1$时，准确率比召回率更重要；当$β=1$时，召回率和确准率同样重要（即$F_β=F_1$）。
<table width='500' style="margin:0 auto;">
<caption>表2 Smatch三元组表示</caption>
<thead>
  <tr>
    <th style="text-align:center">类型</th>
    <th style="text-align:center">三元组</th>
    <th style="text-align:center">数量</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>节点</td>
    <td align='center'>instance(a0, 希望-01)<br>
    instance(a1, 给-01)<br>
    instance(a2, expressive)<br>
    instance(a3, 经历)<br>
    instance(a4, 大家)<br>
    instance(a5, 教训)<br>
    instance(a6, 我)<br>
    instance(a7, 惨痛-01)<br>
    instance(a8, 1)<br>
    instance(a9, 个)
    </td>
    <td align='center'>10</td>
  </tr>
  <tr>
    <td style="text-align:center">有向弧</td>
    <td align='center'>mode(a0, a2)<br>
    arg1(a0, a1)<br>
    arg0(a1, a3)<br>
    arg2(a1, a4)<br>
    arg1(a1, a5)<br>
    arg0-of(a3, a7)<br>
    poss(a3, a6)
    </td>
    <td align='center'>7</td>
  </tr>
  <tr>
    <td style="text-align:center">节点属性</td>
    <td align='center'>root(a0, top)</td>
    <td align='center'>1</td>
  </tr>
</tbody>
</table>

Smatch自提出以来被广泛使用于AMR解析评测，但其仍然存在一些弊端：在比较有向弧的三元组时，Smatch只考虑语义角色标签是否相同，而忽视了概念节点是否一致，这容易导致两个语义不同的句子反而出现匹配程度较高的情况（肖力铭等，2022）。
## 3.2 作为主要标准的Align-smatch评测指标
Align-smatch在Smatch的基础上增添了两种新的数据：概念对齐信息和关系对齐信息。不同于Smatch的三元组，Align-smatch将中文AMR转化为一个多元组（Tuple）集合，每个多元组包含三个或者四个元素。Align-smatch对多元组的数据类型作了以下修改：

1. **在原节点属性三元组中新增了表示概念对齐的三元组：anchor(node_index, token_num)。**
其中，anchor表示该节点的属性为“对齐”，node_index为节点索引，token_num为词编号。如表3所示，节点属性三元组anchor($a_7$, x3 )表示$a_7$索引对应的概念节点“惨痛-01”与词编号x3对应的词“惨痛”完成了概念对齐。
2. **在原有向弧三元组中新增了表示关系对齐的四元组：(Word_on_Arc, token_num, node_index1, node_index2)。**
其中，Word_on_Arc为有向弧上的虚词，传递实词之间的关系意义。如表3所示，有向弧四元组(的, x4, $a_3$, $a_7$)表示虚词“的”位于$a_3$索引和$a_7$索引分别对应的两个节点所连成的有向弧上，同时“的”被赋予词编号$x_4$，完成了关系对齐。
3. **使用有向弧多元组来表示位于根节点的词，而不再使用节点属性三元组表示：property(node_index, value) → relation(node_index1, node_index2)。**
如表2所示，在Smatch指标下，例句中的根节点的三元组表示为：root($a_0$, top)。如表3所示，Align-smatch中该节点的表示则修改为：root($a_0$, $a_0$)。
Align-smatch评测公式如下：
$$ P = \frac{\#Matching\enspace Tuples}{\#Generated\enspace Tuples} $$
$$ R = \frac{\#Matching\enspace Tuples}{\#Gold\enspace Tuples} $$
$$ F_β=(1+β^2)*\frac{(P*R)}{(β^2*P)+R} $$

同样的，Align-smatch中的准确率P为黄金AMR的多元组集合和解析生成的AMR多元组集合间的最大匹配个数与解析生成的AMR多元组总个数之比；召回率R为黄金AMR的多元组集合和解析生成的AMR多元组集合之间的最大匹配个数与黄金AMR的多元组总个数之比；F值同上。
<table width='500' style="margin:0 auto;">
<caption>表3 Align-smatch多元组表示</caption>
<thead>
  <tr>
    <th style="text-align:center">类型</th>
    <th style="text-align:center">多元组</th>
    <th style="text-align:center">数量</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>节点</td>
    <td align='center'>instance(a0, 希望-01)<br>
    instance(a1, 给-01)<br>
    instance(a2, expressive)<br>
    instance(a3, 经历)<br>
    instance(a4, 大家)<br>
    instance(a5, 教训)<br>
    instance(a6, 我)<br>
    instance(a7, 惨痛-01)<br>
    instance(a8, 1)<br>
    instance(a9, 个)
    </td>
    <td align='center'>10</td>
  </tr>
  <tr>
    <td style="text-align:center">有向弧</td>
    <td align='center'>
    root(a0, a0)<br>
    mode(a0, a2)<br>
    arg1(a0, a1)<br>
    arg0(a1, a3)<br>
    arg2(a1, a4)<br>
    arg1(a1, a5)<br>
    arg0-of(a3, a7)<br>
    (的, x4, a3, a7)<br>
    poss(a3, a6)
    </td>
    <td align='center'>9</td>
  </tr>
  <tr>
    <td style="text-align:center">节点属性</td>
    <td align='center'>
    anchor(a0, x1)<br>
    anchor(a1, x6)<br>
    anchor(a2, x11)<br>
    anchor(a3, x5)<br>
    anchor(a4, x7)<br>
    anchor(a5, x10)<br>
    anchor(a6, x2)<br>
    anchor(a7, x3)<br>
    anchor(a8, x8)<br>
    anchor(a9, x9)<br>
    </td>
    <td align='center'>10</td>
  </tr>
</tbody>
</table>

## 3.3 总结
为了更加完整、精确地解析CAMR，本次评测任务采用Align-smatch评测标准。各参赛队最终生成的CAMR中需包含概念对齐信息和关系对齐信息，最终成绩评分按照Align-smatch评测标准，取F值进行排名。表4为完整的评分样例，一共八个实验测试，分别包含两种评测指标和两种模态（详见下文4.1）。其中，Smatch评分仅用于和其他语言的AMR解析进行对比，不计入最终排名。
<table style="margin:0 auto;">
<caption>表4 评分样例</caption>
<thead>
  <tr>
    <th>Metrics</th>
    <th colspan="2">Modalities</th>
    <th>Precision</th>
    <th>Recall</th>
    <th>F1-score</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="4" >Smatch</td>
    <td rowspan="2">Closed Modality</td>
    <td>Test A</td>
    <td align='center'>0.68</td>
    <td align='center'>0.71</td>
    <td align='center'>0.70</td>
  </tr>
  <tr>
    <td>Test B</td>
    <td align='center'>0.74</td>
    <td align='center'>0.66</td>
    <td align='center'>0.70</td>
  </tr>
  <tr>
    <td rowspan="2">Open Modality</td>
    <td>Test A</td>
    <td align='center'>0.74</td>
    <td align='center'>0.74</td>
    <td align='center'>0.74</td>
  </tr>
  <tr>
    <td>Test B</td>
    <td align='center'>0.82</td>
    <td align='center'>0.79</td>
    <td align='center'>0.80</td>
  </tr>
  <tr>
    <td rowspan="4">Align-smatch</td>
    <td rowspan="2">Closed Modality</td>
    <td>Test A</td>
    <td align='center'>0.75</td>
    <td align='center'>0.81</td>
    <td align='center'>0.78</td>
  </tr>
  <tr>
    <td>Test B</td>
    <td align='center'>0.68</td>
    <td align='center'>0.69</td>
    <td align='center'>0.68</td>
  </tr>
  <tr>
    <td rowspan="2">Open Modality</td>
    <td>Test A</td>
    <td align='center'>0.78</td>
    <td align='center'>0.78</td>
    <td align='center'>0.78</td>
  </tr>
  <tr>
    <td>Test B</td>
    <td align='center'>0.82</td>
    <td align='center'>0.50</td>
    <td align='center'>0.62</td>
  </tr>
</tbody>
</table>

# 4 评测赛程
## 4.1 模态选择
本次评测任务包含开放测试（Open Modality）和封闭测试（Closed Modality）：
<table style="margin:0 auto;">
<caption>表5 两种模态的评测要求</caption>
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
    <td align='center'>HIT_Roberta、依存句法分析结果</td>
    <td align='center'>无限制</td>
  </tr>
  <tr>
    <td align='center'>语料</td>
    <td align='center'>仅训练、测试集</td>
    <td align='center'>无限制</td>
  </tr>
  <tr>
    <td align='center'>人工修正</td>
    <td align='center'>禁止</td>
    <td align='center'>禁止</td>
  </tr>
</tbody>
</table>

## 4.2 赛程
2022年6月1日：评测报名开始，参赛队发邮件至<libin.njnu@gmail.com>统一报名；发布训练集以及验证集给参赛队；提供Align-smatch评测软件下载地址。

2022年8月8日：报名截止。

2022年8月10日：发布测试集（Test A）和盲测（Test B）数据集给参赛队。

2022年8月20日：参赛队提交自动标注的数据。

2022年8月26日：发布测试集（Test A）和盲测（Test B）的黄金标准答案给参赛队。

2022年9月5日：参赛队提交中文抽象语义表示评测任务技术报告。

2022年9月30日：参赛队提交技术报告。

2022年10月14日-16日：CCL 2022评测研讨会，线上公布最终排名，评测结束。

## 4.3 报告格式
1.  报告可由中文或英文撰写。
2.  报告统一使用CCL 2022 的论文模版。
3.  报告正文不得超过4页，参考文献页数不限。
4.  报告应至少包含以下四个部分：模型介绍、评测结果、结果分析与讨论和参考文献。

**参考文献**
