<div align="center">
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/camrp2024.png" width=200>
</div>



# <p align="center">Chinese Abstract Meaning Representation Parsing 2024</p>

# Important Dates
* **March 1, 2024**
  * - [X] Initial Public Call for Participation
  * - [X] Release of Training & Development Set
  * - [X] Availability of Evaluation Software <a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202022/tools">Align-smatch</a>
* **May 15, 2024**
  * - [X] Enrolment Deadline
* **May 1, 2024**
  * - [X] Release of Test Set
* **May 8, 2024**
  * - [X] Submission of Auto-annotated Data
* **May 14, 2024**
  * - [X] Release of Gold-Standard Chinese AMR
* **May 21, 2024**
  * - [X] Submission of Technical Report
  * - [X] Preliminary Evaluation Results
* **May 25, 2024**
  * - [X] Submission of Technical Report
  * - [X] Evaluation Period
* **July 1, 2024**
  * - [X] Camera-Ready Technical Report
* **July 25-28, 2024**
  * - [X] Release of Final Rankings Online
  * - [X] Workshop for Technical Evaluation Tasks of CCL 2024


[![Zh](https://img.shields.io/badge/README-Chinese-yellow.svg "Zh")](./README.md)

- **Chinese Version**: [README.md](./README.md)

- The brand-new CAMR homepage is on the way: <a href="https://www.camrp.tech">Welcome to CAMR!</a>

<a name="anchor1"></a>
[![signup](https://img.shields.io/badge/CAMRP_2024-Microsoft_Form-blue.svg "sign up")](https://forms.office.com/r/GS7ze5GcY7)

**Entry Form:** 
<a href="https://forms.office.com/r/GS7ze5GcY7">CLICK ME</a>


<a name="anchor2"></a>

[![agreement](https://img.shields.io/badge/CAMRP_2024-LDC-red.svg "PDF")](./docs/LDC_Evaluation_License_Agreement_CCL2024.pdf)

**Participants must sign the LDC Evaluation License Agreement for the data/corpora used in the CAMRP 2024 Evaluation Task will be authorized via <a href="https://www.ldc.upenn.edu/">LDC</a> only:**
1.	Each team should designate a member as the data contact person.
2.	Each data contact person must fill in the [LDC Evaluation License Agreement](./docs/LDC_Evaluation_License_Agreement_CCL2024.pdf) and send a signed copy of the agreement to LDC (<ldc@ldc.upenn.edu>).
3.	Participants must use the received data/corpora from LDC in the CAMRP 2024 Evaluation Task only.
4.	For details, please refer to the [LDC Evaluation License Agreement](./docs/LDC_Evaluation_License_Agreement_CCL2024.pdf).


[![body](https://img.shields.io/badge/CAMRP_2024-Nanjing_Normal_University-green.svg "CAMRP 2024")](https://github.com/GoThereGit/Chinese-AMR/blob/main/README.md)

* Organizers:
  * **Bin Li** (Nanjing Normal University, Nanjing, China) (E-mail: <libin.njnu@gmail.com>)
  * **Weiguang Qu** (Nanjing Normal University, Nanjing, China)
  * **Junsheng Zhou** (Nanjing Normal University, Nanjing, China)
  
* Student Members:
  * **Zhixing Xu** (Nanjing Normal University, Nanjing, China)
  * **Yixuan Zhang** (Nanjing Normal University, Nanjing, China)
  * **Jingya Lu** (Nanjing Normal University, Nanjing, China)

# 1 Introduction
With the growing maturity of morphological analysis and syntactic analysis techniques, 
natural language processing in general has advanced to the level of semantic analysis. More specifically, 
sentence-level meaning parsing has already occupied the core position of semantic analysis research. 
To address the lack of whole-sentence semantic representation and the domain-dependent problem of sentence semantic annotation, 
<a href="https://aclanthology.org/W13-2322.pdf">Banarescu et al. (2013)</a> proposed a domain-independent whole-sentence semantic representation method called Abstract Meaning Representation (AMR) that can abstract the meaning of a sentence with a single-rooted, acyclic and directed graph and predicts the semantic structure of the targeted sentence. 
There have been large-scaled corpora constructed for AMR and two international conferences held for AMR semantic parsing evaluation tasks. 
And similar to AMR, the corpus of Chinese AMR (CAMR) <a href="https://aclanthology.org/W16-1702.pdf">(Li et al., 2016)</a> has also begun to take shape and played an important role in the stage of CoNLL 2020. 


Our evaluation task is to parse input sentences and output AMR graphs of the targeted sentences with data from CAMR corpus. 
It is noteworthy that the alignment of concept and relation are added in CAMR and some extra semantic role labels as well to better distinguish characteristics in Chinese. 
The evaluation task in CoNLL 2020, however, failed to leverage the alignment of concept and relation and therefore in our former CAMP 2022 & CAMRP 2023 evaluation task, 
we aimed to better evaluate the performance of automatic parsing via the newly-designed metric named Align-smatch, 
which contains the alignment of concept and relation.

## 1.1 AMR
AMR is to abstract the meaning of a sentence into a single-rooted, directed and acyclic graph. 
Specifically, words are abstracted as concept nodes and relations between words as directed arcs with semantic role labels. 
This abstract representation way enables AMR not only to describe the situation like argument sharing when there is one single noun allocated by several predicates, 
but also to add, delete and modify concept nodes in order to complement the implicit concept annotation.

AMR aroused the attentions of professions and researchers as soon as it came out, 
and has prevailed the world with its great power of sentence-level semantic representation. 
Related work of automatic parsing with AMR has been widely applied into downstream tasks in NLP such as question answering systems and text summarization, 
and yielded good returns. In the cross-framework task of Meaning Representation Parsing (MRP) held by <a href="http://mrp.nlpl.eu/2020/index.php">CoNLL 2020</a>, Hitachi <a href="https://aclanthology.org/2020.conll-shared.4.pdf">(Hiroaki O. et al., 2020)</a> 
and ÚFAL <a href="https://arxiv.org/pdf/2011.00758.pdf">(Samuel D. et al., 2020)</a> among five teams achieved 0.80 and 0.78 F-score in the track of Chinese AMR parsing evaluation, respectively, 
and were awarded first prize and second prize accordingly. 
In fact, their performances in Chinese AMR parsing were fairly close to that of in English AMR (which is 0.82).

English AMR, however, has no alignment of concept and relation, which presents problems for data training and automatic parsing. 
Although the alignment of concept and relation are added into Chinese AMR, it was a no-show in CoNLL 2020 in order to be consistent in formatting with English AMR. 
Additionally, most of experiments and evaluations including CoNLL use Smatch metric, which was originally designed based on English AMR. 
Inevitably, Smatch is not quite compatible with Chinese AMR considering the different characteristics between the two languages, 
for example, it has no way processing the alignment of concept and relation in Chinese AMR. 
Therefore, in order to fill the gap of alignment information in Chinese AMR and to provide a brand-new standard for Chinese AMR parsing, 
<a href="http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.638.pdf">Xiao et al. (2022)</a> came up with a new evaluation metric named Align-smatch with concept alignment metric and relation alignment metric added based on Smatch.
The best results in CAMRP 2022 & CAMRP 2023 are beyond 0.81.
For more details, please refer to our <a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202023">former introduction</a>.

## 1.2 Ancient Chinese AMR

In modern Chinese, compared to ancient Chinese, there have been changes in phonetics, vocabulary, and grammar. Therefore, the annotation of Ancient Chinese AMR is based on the Chinese AMR framework, with some semantic labels added or deleted, some predicate argument structures modified, and specific sentence patterns defined for annotation. Ancient Chinese AMR overall maintains consistency with the Chinese AMR annotation format, including concept and relation alignment information. As shown in Figure 1, the node "二百" (two hundred) is labeled as x5, completing concept alignment; the function word "以" (with) is labeled as x7 and simultaneously annotated with the semantic relation ":arg2" on the directed arc from the node "x3/帅" (to lead) to the node "x8/伐" (attack), completing relation alignment.

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/figure1.jpg" width=500>
 <p>Figure 1 Sample sentence “命子封帅车二百乘以伐京” in Ancient Chinese AMR text</p>
</div>


To better describe the semantic structure of Ancient Chinese, Ancient Chinese AMR introduces two new concepts in the CAMR system to represent the usage of causative and considerative constructions, namely "make" and "consider". As shown in Table 1, the expression "而速之" (and make it quick) conveys the meaning of "and make it quick", while "小人耻失其君" (a petty person is ashamed to lose their lord) implies "a petty person is ashamed to lose their lord".

<table align="center">
<p align="center">Table 1 New concepts in Ancient Chinese AMR</p>
<thead>
  <tr>
    <th>New concept</th>
    <th>Sample sentence</th>
    <th>Annotation</th>
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

One word can own mutiple tags of Part-of-Speech, which is quiet common in Ancient Chinese. In Ancient Chinese AMR, based on this characteristic, additional annotation rules have been primarily introduced for nouns functioning as verbs and nouns acting as adverbials. As shown in Figure 2, in the phrase "皆肘之" (all hit it with elbows), the "肘" (elbow) requires the action of hitting the arm to be supplemented in the actual annotation, namely, taking "击-01" (hit-01) as the root node of the sentence, thus restoring the true semantic expression.

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/figure2.png" width=300>
 <p>Figure 2 Sample of nouns as verbs in Ancient Chinese AMR</p>
</div>

# 2 Data
## 2.1 Data Sample
We offer two kinds of data sets including: **CAMR text** and **CAMR tuple**. 

[![sample](https://img.shields.io/badge/sample-CAMR_text-red.svg "CAMR_text")](./docs/samples/CAMR_text.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/figure3.jpg" width=500>
 <p>Figure 3 Data sample of CAMR (Ancient) text representation</p>
</div>

Figure 3 is a copy of CAMR text data sample from training set, detailed with sentence ID, word tokens, 
word ID, alignment of concept and relation, and the text representation of CAMR. 
All files are encoded in UTF-8. 


[![sample](https://img.shields.io/badge/sample-CAMR_tuple-blue.svg "CAMR_tuple")](./docs/samples/CAMR_tuple.txt)

<table align=center>
<p align=center>Table 2 Data sample of CAMR (Ancient) tuples representation</p>
<thead>
  <tr>
    <th>sid</th>
    <th>nid1</th>
    <th>concept1</th>
    <th>rel</th>
    <th>rid</th>
    <th>ralign</th>
    <th>nid2</th>
    <th>concept2</th>
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

Table 2 is a copy of CAMR tuple representation including sentence ID (sid), node_1 ID (nid1), concept_1 (concept1), relation (rel), relation ID (rid), relation alignment word (ralign), node_2 ID (nid2) and concept_2 (concept2).

## 2.2 Task Introduction
**Input:**
(Sentence with word segmentation)

``
命 子封 帅 车 二百 乘 以 伐 京
``

**Output:**
（CAMR tuples）

``
As shown in Figure 2
``

**Evaluation Metric:**

``
Align-smatch
``

**Submission:**

Each track can submit up to two results. The naming format for each result is as below:

``
<team>_<modality>_<test>_<run>.txt
``

For instance：

- PKU_open_testA_1.txt
- PKU_open_testA_2.txt
- PKU_open_testB_1.txt
- PKU_open_testB_2.txt
- PKU_open_testC_1.txt
- PKU_open_testC_2.txt

## 2.3 Data Set
Chinese Abstract Meaning Representation Corpus was constructed and cooperated by Nanjing Normal University and Bradeis University from 2015. 
Specifically, the data offered in CAMRP 2023 was the <a href="https://catalog.ldc.upenn.edu/LDC2021T13">CAMR v2.0E</a> released via Linguisitc Data Consortium (LDC),
of which the original data was from Chinese Tree Bank 8.0 including 20,000 Chinese sentences in total. 
The data sets as usual include training set, dev set and test set, and have been proven with high quality in the evaluation task in CoNLL 2020, CAMRP 2022 and CAMRP 2023. 


In this evaluation task, approximately 2500 sentences of Ancient Chinese corpus were added, selected from the segmented text of "Zuo Zhuan" from the School of Chinese Language and Literature at Nanjing Normal University. Among these, 500 sentences form Dev set B, and 2000 sentences form Test set C, focusing on evaluating the performance of parsing systems on Ancient Chinese.Table 3 shows the distribution of each data set:

<table align="center">
<p align="center">Table 3 Evaluation data set details</p>
<thead>
  <tr>
    <th>Data Sets</th>
    <th>Sentences</th>
    <th>Word Tokens</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Training Set (Chinese Mandarin)</td>
    <td>16576</td>
    <td>386234</td>
  </tr>
  <tr>
    <td>Dev Set A (Chinese Mandarin)</td>
    <td>1789</td>
    <td>41822</td>
  </tr>
  <tr>
    <td><b>New</b>Dev Set B (Ancient Chinese)</td>
    <td>500 (approx.)</td>
    <td>5000 (approx.)</td>
  </tr>
  <tr>
    <td>Test Set A (Chinese Mandarin)</td>
    <td>1713</td>
    <td>39228</td>
  </tr>
  <tr>
    <td>Test Set B (Chinese Mandarin)</td>
    <td>1999</td>
    <td>36940</td>
  </tr>
  <tr>
    <td><b>New</b>Test Set C (Ancient Chinese)</td>
    <td>2000 (approx.)</td>
    <td>20,000 (approx.)</td>
  </tr>
</tbody>
</table>


# 3 Evaluation Metrics and Modalities
## 3.1 Main metric: Align-smatch
CAMRP 2024 uses Align-smatch as the main metric. Difference between Smatch and Align-smatch please kindly refer to [CAMRP 2023](https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202023).

<a name="anchor3.3"></a>

## 3.2 Two Modalities
The evaluation task includes **Open Modality** and **Closed Modality**:
1.	Once chosen Closed Modality, the participants must use the training data, test data and pre-trained model which are all designated in advance. No alternative is allowed. We also offer dependency analysis results of the train set for each team under Closed Modality. HIT_Roberta from Harbin Institue of Technology <a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9599397">(Cui et al., 2021)</a> as pre-trained model is highly recommended. 
2.	Once chosen Open Modality, the participants are allowed to use pre-trained model and external resources such as named entities and dependency analysis results with no limits. Note that all kinds of resources that participants employ should be mentioned and written in detail in the final technical report. Manual correction is forbidden in both modalities.

<table align="center">
<p align="center">Table 4: Limitations on two modalities</p>
<thead>
  <tr>
    <th align='center'>Resources</th>
    <th style="text-align:center">Closed Modality</th>
    <th align='center'>Open Modality</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>Algorithm</td>
    <td align='center'>No Limit</td>
    <td align='center'>No Limit</td>
  </tr>
  <tr>
    <td align='center'>Pre-trained Model</td>
    <td align='center'>HIT_Roberta</td>
    <td align='center'>No Limit</td>
  </tr>	
   <tr>
    <td align='center'>External Resource</td>
    <td align='center'>Dependency Tree</td>
    <td align='center'>No Limit</td>
  </tr>	
  <tr>
    <td align='center'>Data Set</td>
    <td align='center'>Train Set, Dev Set</td>
    <td align='center'>No Limit</td>
  </tr>
  <tr>
    <td align='center'>Manual Correction</td>
    <td align='center'>Not Allowed</td>
    <td align='center'>Not Allowed</td>
  </tr>
</tbody>
</table>


To better parse and evaluate Chinese AMR, our evaluation task use Align-smatch as the main metric. The CAMR parsing results each team generates should contain the alignment information of concept and relation. Note that Smatch scores are optional for we rank participants referring to the F-scores on **Test Set C only**.



# 4 Writing the Technical Report
1.	Technical report can be written in either **Chinese** or **English**.
2.	Technical report should be formatted according to <a href="http://cips-cl.org/static/CCL2023/downloads/ccl2023_template.zip">CCL 2023 template</a>.
3.	The maximum length should be 4 pages (excluding references).
4.	Technical report should include at least the following sections: **introduction**, **evaluation results**, **result analysis** and **references**.

# 5 Awards
1. Awards include **First Prize**, **Second Prize** and **Third Prize**, 
and each team will be awarded with a unique certificate presented by **Chinese Information Processing Society of China** (CIPS).


# 6 References
1. Banarescu, Laura, et al. "Abstract meaning representation for sembanking." Proceedings of the 7th linguistic annotation workshop and interoperability with discourse. 2013.
2. Li, Bin, et al. "Building a Chinese AMR bank with concept and relation alignments." Linguistic Issues in Language Technology 18 (2019).
3. Cai, Shu, and Kevin Knight. "Smatch: an evaluation metric for semantic feature structures." Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2013.
4. Cui, Yiming, et al. "Pre-training with whole word masking for chinese bert." IEEE/ACM Transactions on Audio, Speech, and Language Processing 29 (2021): 3504-3514.
5. Ozaki, Hiroaki, et al. "Hitachi at MRP 2020: Text-to-graph-notation transducer." Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing. 2020.
6. Li, Bin, et al. "Annotating the little prince with chinese amrs." Proceedings of the 10th linguistic annotation workshop held in conjunction with ACL 2016 (LAW-X 2016). 2016.
7. Abzianidze, L., et al. "MRP 2020: The second shared task on cross-framework and cross-lingual meaning representation parsing." Proceedings of the CoNLL 2020 Shared Task: Cross-Framework Meaning Representation Parsing (2020): 1-22.
8. Samuel, David, and Milan Straka. "UFAL at MRP 2020: Permutation-invariant Semantic Parsing in PERIN." arXiv preprint arXiv:2011.00758 (2020).
9. Song, Linfeng, and Daniel Gildea. "SemBleu: A robust metric for AMR parsing evaluation." arXiv preprint arXiv:1905.10726 (2019).
10. Xiao, Liming, et al. "Align-smatch: A Novel Evaluation Method for Chinese Abstract Meaning Representation Parsing based on Alignment of Concept and Relation." Proceedings of the Language Resources and Evaluation Conference. 2022.
11. Xu, Zhixing, et al. "[Overview of CCL23-Eval Task 2: The Third Chinese Abstract Meaning Representation Parsing Evaluation.](https://aclanthology.org/2023.ccl-3.7.pdf)" Proceedings of the 22nd Chinese National Conference on Computational Linguistics (Volume 3: Evaluations). 2023.
