<div align="center">
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/logo.png" width="200">
</div>

# <p align="center">Chinese Abstract Meaning Representation Parsing 2022</p>

**Entry Form:**
<a href="https://docs.google.com/forms/d/e/1FAIpQLSfCwkl_wQl64VxpIE4tJU9jtHTZpwas-PvPmJb_BCKYIe0qqw/viewform?usp=pp_url">CLICK ME</a>

**Chinese Version**: <a href="https://github.com/GoThereGit/Chinese-AMR/blob/main/README.md">README.md</a>

* Orgnizers:
  * **Bin Li** (Nanjing Normal University, Nanjing, China) (E-mail: <libin.njnu@gmail.com>)
  * **Weiguang Qu** (Nanjing Normal University, Nanjing, China)
  * **Junsheng Zhou** (Nanjing Normal University, Nanjing, China)
  * **Nianwen Xue** (Brandeis University, Waltham, US)
 
* Student Members:
  * **Zhixing Xu** (Nanjing Normal University, Nanjing, China)
  * **Liming Xiao** (Nanjing Normal University, Nanjing, China)
  * **Jingya Lu** (Nanjing Normal University, Nanjing, China)
  * **Jin Chen** (Nanjing Normal University, Nanjing, China)
  * **Yuanyuan Xie** (Nanjing Normal University, Nanjing, China)
  * **Yiguo Yuan** (Nanjing Normal University, Nanjing, China)

# 1 Introduction
With the growing maturity of morphological analysis and syntactic analysis techniques, 
natural language processing in general has advanced to the level of semantic analysis. More specifically, 
sentence-level meaning parsing has already occupied the core position of semantic analysis research. 
To address the lack of whole-sentence semantic representation and the domain-dependent problem of sentence semantic annotation, 
Banarescu et al. (2013) proposed a domain-independent whole-sentence semantic representation method called Abstract Meaning Representation (AMR) that can abstract the meaning of a sentence with a single-rooted, acyclic and directed graph and predicts the semantic structure of the targeted sentence. 
There have been large-scaled corpora constructed for AMR and two international conferences held for AMR semantic parsing evaluation tasks. 
And similar to AMR, the corpus of Chinese AMR (CAMR) has also begun to take shape and played an important role in the stage of CoNLL 2020. 


Our evaluation task is to parse input sentences and output AMR graphs of the targeted sentences with data from CAMR corpus. 
It is noteworthy that the alignment of concept and relation are added in CAMR and some extra semantic role labels as well to better distinguish characteristics in Chinese. 
The evaluation task in CoNLL 2020, however, failed to leverage the alignment of concept and relation and therefore in our CAMP 2022 evaluation task, 
we aim to better evaluate the performance of automatic parsing via the newly-designed metric named Align-smatch, 
which contains the alignment of concept and relation.

## 1.1 AMR
AMR is to abstract the meaning of a sentence into a single-rooted, directed and acyclic graph. 
Specifically, words are abstracted as concept nodes and relations between words as directed arcs with semantic role labels. 
This abstract semantic representation way enables AMR not only to describe the situation like argument sharing when there is one single noun allocated by several predicates, 
but also to add, delete and modify concepts nodes in order to complement the implicit concept annotation.

AMR aroused the attentions of professions and researchers as soon as it come out, 
and has prevailed the world with its great power of sentence-level semantic representation. 
Related work of automatic parsing with AMR has been widely applied into downstream tasks in NLP such as question answering systems and text summarization, 
and yielded good returns. In the cross-framework task of Meaning Representation Parsing (MRP) held by <a href="http://mrp.nlpl.eu/2020/index.php">CoNLL 2020</a>, Hitachi (Hiroaki O. et al., 2020) 
and ÚFAL (Samuel D. et al., 2020) among five teams achieved 0.80 and 0.78 F-score in the track of Chinese AMR parsing evaluation, respectively, 
and were awarded first prize and second prize accordingly. 
In fact, their performances in Chinese AMR parsing were fairly close to that of in English AMR (which is 0.82).

English AMR has no alignment of concept and relation, which presents problems for data training and automatic parsing. 
Although the alignment of concept and relation are added into Chinese AMR, it was a no-show in CoNLL 2020 in order to be consistent in formatting with English AMR. 
Additionally, most of experiments and evaluations including CoNLL use Smatch metric, which was originally designed based on English AMR. 
Inevitably, Smatch is not quite compatible with Chinese AMR considering the different characteristics between the two languages, 
for example, it has no way processing the alignment of concept and relation in Chinese AMR. 
Therefore, in order to fill the gap of alignment information in Chinese AMR and to provide a brand-new standard for Chinese AMR parsing, 
Xiao et al. (2022) come up with a new evaluation metric named Align-smatch with concept alignment metric and relation alignment metric added based on Smatch.

## 1.2 Alignment in Chinese AMR
English AMR normally annotates the index of concept nodes with the initial letter of the words or assigns the number index simply by the sequence of nodes. 
It leads to the inability of computers to directly trace concepts back to their sources and to restore the order of sentences from AMR, 
and brings great difficulties to AMR parsing. To solve this problem, 
Li et al. (2016) proposed an efficient framework incorporating concept-to-word alignment to achieve concept alignment for Chinese AMR. 
By assigning a number to each word in the original sentence after word separation according to the principle of linear ordering, 
each concept node is also assigned a corresponding number. The numbering takes the form of “x” plus a number. As shown in Figure 1, 
the Chinese word “惨痛” is the third word in original sentence and therefore assigned with the number “x3”, 
indicating the alignment with the concept node “x3/惨痛-01”, namely the **concept alignment**.

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/figure_1.png">
 <p>Figure 1: CAMR text representation of the sample sentence "希望我惨痛的经历给大家一个教训呀"</p>
</div>

In addition to concept alignment, AMR also omits function words such as prepositions and articles that are less meaningful, 
assuming they do not contribute much to the semantic. However, function words in Chinese, as a matter of fact, 
are quite useful for connecting contexts and contain rich semantic information. Hence, Chinese AMR chooses to retain function words for annoation. 
Specifically, function words indicating aspect meaning and mood meaning of the sentence are treated as concept nodes while function words 
indicating the relations between content word are regarded as mappings of semantic relations and labeled on arcs together with semantic role labels (Dai et al., 2020). 
Function words on arcs are numbered as well, which would achieve relation alignment by completing the alignment of semantic relations with the words in sentences. 
As shown in Figure 2, 
the function word “的” has been annotated on the directed arc with semantic role label “arg0-of” together and numbered “x4” 
for it is the forth word in original sentence. Finally, we could say the function word “x4/的” is aligned with the semantic relation “arg0-of”, 
namely the **relation alignment**.

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/figure_2.png" >
 <p>Figure 2: CAMR graph of the sample sentence "希望我惨痛的经历给大家一个教训呀"</p>
</div>

## 1.3 Summary
In a nutshell, to better promote and advance the development of Chinese AMR parsing, 
we Nanjing Normal University hereby present this evaluation task of CAMRP 2022. 
Unlike the cross-framework/cross-lingual task of MRP held by CoNLL 2020, 
we aim to evaluate Chinese AMR parsing **only**, and of course with Align-smatch metric. 

# 2 Data
## 2.1 Data Sample
Figure 3 is a copy of CAMR data sample from training set, detailed with sentence ID, word tokens, 
word ID, alignment of concept and relation, and the text representation of CAMR. 
All files are encoded in UTF-8. 

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/figure_3.png">
 <p>Figure 3: Data sample of CAMR</p>
</div>

## 2.2 Data Set
Chinese Abstract Meaning Representation Corpus was constructed and cooperated by Nanjing Normal University and Bradeis University from 2015. 
Specifically, the data offered in this CAMRP 2022 is the <a href="https://catalog.ldc.upenn.edu/LDC2021T13">CAMR v2.0</a> released via Linguisitc Data Consortium (LDC),
of which the original data was from Chinese Tree Bank 8.0 including 20,000 Chinese sentences in total. 
The data sets as usual include training set, validation set and test set, and have been proven with high quality in the evaluation task in CoNLL 2020. 
We hereby use the exact same data sets in order to see whether there is any progression of Chinese AMR parsing in recent two years. 
Blind set (Test B) including 2000 sentences is also provided to measure the generalization performance of parsers.
The data in blind test is not released yet. Table 1 shows the distribution of each data set:

<table align="center">
<p align="center">Table 1: Data sets</p>
<thead>
  <tr>
    <th style="text-align:center">Data Sets</th>
    <th style="text-align:center">Sentences</th>
    <th style="text-align:center">Word Tokens</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>Training Set</td>
    <td align='center'>16576</td>
    <td align='center'>386234</td>
  </tr>
  <tr>
    <td align='center'>Validation Set</td>
    <td align='center'>1789</td>
    <td align='center'>41822</td>
  </tr>
  <tr>
    <td align='center'>Test A</td>
    <td align='center'>1713</td>
    <td align='center'>39228</td>
  </tr>
  <tr>
    <td align='center'>Test B</td>
    <td align='center'>about 2000</td>
    <td align='center'>about 40,000</td>
  </tr>
</tbody>
</table>

# 3 Tentative Schedule
* **June 10, 2022**
  * Initial Public Call for Participation
  * Release of Training Set and Validation Set
  * Availability of Evaluation Software (Align-smatch)
* **August 8, 2022**
  * Enrolment Deadline
* **August 10, 2022**
  * Release of Test Set (Test A) and Blind Set (Test B)
* **August 20, 2022**
  * Submission of annotated data
* **August 26, 2022**
  * Release of Gold Data of Test Set (Test A) and Blind Set (Test B)
* **September 5, 2022**
  * Submission of Technical Report
  * Reviewer Feedback Available
* **September 30, 2022**
  * Final Submission of Camera-Ready Technical Report
* **October 14-16, 2022**
  * Evaluation Period 
  * Release of Final Rankings Online
  * Workshop for Technical Evaluation Tasks of <a href="http://www.cips-cl.org/static/CCL2022/en/cclEval/taskCollection/index.html">CCL 2022</a>

**Entry Form:**
<a href="https://docs.google.com/forms/d/e/1FAIpQLSfCwkl_wQl64VxpIE4tJU9jtHTZpwas-PvPmJb_BCKYIe0qqw/viewform?usp=pp_url">CLICK ME</a>

# 4 Task Requirements
# 4.1 Two Modalities
The evaluation task includes **Open Modality** and **Closed Modality**:
1.	Once chosen Closed Modality, the participants must use the training data, test data and pre-trained model which are all designated in advance. No alternative is allowed. We also offer dependency analysis results of training set for each team under Closed Modality. HIT_Roberta from Harbin Institue of Technology (Cui et al., 2021) as pre-trained model is highly recommended. 
2.	Once chosen Open Modality, the participants are allowed to use pre-trained model and external resources such as named entities and dependency analysis results with no limits. Note that all kinds of resources that participants employ should be mentioned and written in detail in the final technical report. Manual correction is forbidden in both modalities.

<table align="center">
<p align="center">Table 2: Limitations on two modalities</p>
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
    <td align='center'>No Limits</td>
    <td align='center'>No Limits</td>
  </tr>
  <tr>
    <td align='center'>Pre-trained Model</td>
    <td align='center'>HIT_Roberta, Dependency Tree</td>
    <td align='center'>No Limits</td>
  </tr>
  <tr>
    <td align='center'>Data Set</td>
    <td align='center'>Training Set, Validation Set</td>
    <td align='center'>No Limits</td>
  </tr>
  <tr>
    <td align='center'>Manual Correction</td>
    <td align='center'>Not Allowed</td>
    <td align='center'>Not Allowed</td>
  </tr>
</tbody>
</table>

## 4.2 Writing the Technical Report
1.	Technical report can be written in both **Chinese** and **English**.
2.	Technical report should be formatted according to <a href="http://cips-cl.org/static/CCL2022/downloads/ccl2022_template.zip">CCL 2022 template</a>.
3.	The maximum length should be 4 pages (excluding references).
4.	Technical report should include at least the following sections: **introduction**, **evaluation results**, **result analysis** and **references**.

## 4.3 Awards
Awards include **First Prize**, **Second Prize** and **Third Prize**, 
and each team will be awarded with a unique certificate presented by **Chinese Information Processing Society of China** (CIPS).

