<div align="center">
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/logo.png" width="200">
</div>

# <p align="center">Chinese Abstract Meaning Representation Parsing 2022</p>

# News and Updates
* **June 10, 2022**
  * Initial Public Call for <a href="#anchor1">Participation</a>
  * Release of Train Set and Dev Set via <a href="#anchor2">LDC</a>
* ~~**June 15, 2022**~~
  * ~~Release of Evaluation Tool Align-smatch (original date: June 10)~~
* **June 20, 2022**
  * Update Align-smatch tool (<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/tools">the LATEST version</a>)  
* **June 23, 2022**
  * Update <a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/data">data</a> folder


[![Zh](https://img.shields.io/badge/README-Chinese-yellow.svg "Zh")](./README.md)

**Chinese Version**: [README.md](./README.md)

<a name="anchor1"></a>
[![signup](https://img.shields.io/badge/CAMRP_2022-Google_Form-blue.svg "sign up")](https://docs.google.com/forms/d/e/1FAIpQLSfCwkl_wQl64VxpIE4tJU9jtHTZpwas-PvPmJb_BCKYIe0qqw/viewform?usp=pp_url)

**Entry Form:** 
<a href="https://docs.google.com/forms/d/e/1FAIpQLSfCwkl_wQl64VxpIE4tJU9jtHTZpwas-PvPmJb_BCKYIe0qqw/viewform?usp=pp_url">CLICK ME</a>

<a name="anchor2"></a>

[![agreement](https://img.shields.io/badge/CAMRP_2022-LDC-red.svg "PDF")](./docs/LDC_Evaluation_License_Agreement_CCL2022.pdf)

**Participants must sign the LDC Evaluation License Agreement for the data/corpora used in the CAMRP 2022 Evaluation Task will be authorized via <a href="https://www.ldc.upenn.edu/">LDC</a> only:**
1.	Each team should designate a member as the data contact person.
2.	Each data contact person must fill in the [LDC Evaluation License Agreement](./docs/LDC_Evaluation_License_Agreement_CCL2022.pdf) and send a signed copy of the agreement to LDC (<ldc@ldc.upenn.edu>).
3.	Participants must use the received data/corpora from LDC in the CAMRP 2022 Evaluation Task only.
4.	For details, please refer to the [LDC Evaluation License Agreement](./docs/LDC_Evaluation_License_Agreement_CCL2022.pdf).


[![body](https://img.shields.io/badge/CAMRP_2022-Nanjing_Normal_University-green.svg "CAMRP 2022")](https://github.com/GoThereGit/Chinese-AMR/blob/main/README.md)

* Organizers:
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
<a href="https://aclanthology.org/W13-2322.pdf">Banarescu et al. (2013)</a> proposed a domain-independent whole-sentence semantic representation method called Abstract Meaning Representation (AMR) that can abstract the meaning of a sentence with a single-rooted, acyclic and directed graph and predicts the semantic structure of the targeted sentence. 
There have been large-scaled corpora constructed for AMR and two international conferences held for AMR semantic parsing evaluation tasks. 
And similar to AMR, the corpus of Chinese AMR (CAMR) <a href="https://aclanthology.org/W16-1702.pdf">(Li et al., 2016)</a> has also begun to take shape and played an important role in the stage of CoNLL 2020. 


Our evaluation task is to parse input sentences and output AMR graphs of the targeted sentences with data from CAMR corpus. 
It is noteworthy that the alignment of concept and relation are added in CAMR and some extra semantic role labels as well to better distinguish characteristics in Chinese. 
The evaluation task in CoNLL 2020, however, failed to leverage the alignment of concept and relation and therefore in our CAMP 2022 evaluation task, 
we aim to better evaluate the performance of automatic parsing via the newly-designed metric named Align-smatch, 
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

## 1.2 New Alignments in Chinese AMR
English AMR normally annotates the index of concept nodes with the initial letter of the words or assigns the number index simply by the sequence of nodes. 
It leads to the inability of computers to directly trace concepts back to their sources and to restore the order of sentences from AMR, 
and brings great difficulties to AMR parsing. To solve this problem, 
<a href="https://journals.colorado.edu/index.php/lilt/article/view/1429/1271">Li et al. (2019)</a> proposed an efficient framework incorporating concept-to-word alignment to achieve concept alignment for Chinese AMR. 
By assigning a number to each word in the original sentence after word separation according to the principle of linear ordering, 
each concept node is also assigned a corresponding number. The numbering takes the form of “x” plus a number. As shown in Figure 1, 
the Chinese word “惨痛” is the third word in original sentence and therefore assigned with the number “x3”, 
indicating the alignment with the concept node “x3/惨痛-01”, namely the **concept alignment**.

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/Figure_1_En.png">
 <p>Figure 1: CAMR text representation of the sample sentence "希望我惨痛的经历给大家一个教训呀"</p>
</div>

In addition to concept alignment, AMR also omits function words such as prepositions and articles that are less meaningful, 
assuming they do not contribute much to the semantic. However, function words in Chinese, as a matter of fact, 
are quite useful for connecting contexts and contain rich semantic information. Hence, Chinese AMR chooses to retain function words for annoation. 
Specifically, function words indicating aspect meaning and mood meaning of the sentence are treated as concept nodes while function words 
indicating the relations between content word are regarded as mappings of semantic relations and labeled on arcs together with semantic role labels <a href="https://journals.colorado.edu/index.php/lilt/article/view/1429/1271">(Li et al., 2019)</a>. 
Function words on arcs are numbered as well, which would achieve relation alignment by completing the alignment of semantic relations with the words in sentences. 
As shown in Figure 2, 
the function word “的” has been annotated on the directed arc with semantic role label “arg0-of” together and numbered “x4” 
for it is the fourth word in original sentence. Finally, we could say the function word “x4/的” is aligned with the semantic relation “arg0-of”, 
namely the **relation alignment**.

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/figure_2.png" width=800>
 <p>Figure 2: CAMR graph of the sample sentence "希望我惨痛的经历给大家一个教训呀"</p>
</div>

## 1.3 Summary
In a nutshell, to better promote and advance the development of Chinese AMR parsing, 
we Nanjing Normal University hereby present this evaluation task of CAMRP 2022. 
Unlike the cross-framework/cross-lingual task of MRP held by CoNLL 2020, 
we aim to evaluate Chinese AMR parsing **only**, and of course with Align-smatch metric. 

# 2 Important Dates
* **June 10, 2022**
  * - [x] Initial Public Call for Participation
  * - [x] Release of the Train Set and Dev Set
  * - [x] Availability of Evaluation Software (Align-smatch)
* **August 8, 2022**
  * - [ ] Enrolment Deadline
* **August 10, 2022**
  * - [ ] Release of the Test Set (Test A and Test B)
* **August 20, 2022**
  * - [ ] Submission of Annotated Data
* **August 26, 2022**
  * - [ ] Release of Gold Data of the Test Set (Test A and Test B)
* **September 5, 2022**
  * - [ ] Submission of Technical Report
* **September 30, 2022**
  * - [ ] Final Submission of Camera-Ready Technical Report
  * - [ ] Evaluation Period
* **October 14-16, 2022** 
  * - [ ] Release of Final Rankings Online
  * - [ ] Workshop for Technical Evaluation Tasks of <a href="http://www.cips-cl.org/static/CCL2022/en/cclEval/taskCollection/index.html">CCL 2022</a>

**Entry Form:**
<a href="https://docs.google.com/forms/d/e/1FAIpQLSfCwkl_wQl64VxpIE4tJU9jtHTZpwas-PvPmJb_BCKYIe0qqw/viewform?usp=pp_url">CLICK ME</a>

# 3 Data
## 3.1 Data Sample
We offer three kinds of data sets including: **CAMR text**, **dependency analysis result** and **CAMR tuple**. 

[![sample](https://img.shields.io/badge/sample-CAMR_text-red.svg "CAMR_text")](./docs/samples/CAMR_text.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/Figure_3.png">
 <p>Figure 3: Data sample of CAMR text representation</p>
</div>

Figure 3 is a copy of CAMR text data sample from training set, detailed with sentence ID, word tokens, 
word ID, alignment of concept and relation, and the text representation of CAMR. 
All files are encoded in UTF-8. 

[![sample](https://img.shields.io/badge/sample-CAMR_dep-green.svg "CAMR_dep")](./docs/samples/CAMR_dep.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/Figure_4.png" width=700>
 <p>Figure 4: Data sample of dependency analysis result</p>
</div>

Figure 4 is a copy of dependency analysis result. Note that in the closed modality, participants are allowed to use dependency analysis results as the external resource for training (more info please refer to <a href="#anchor4.3">4.3 Two Modalities</a>).

[![sample](https://img.shields.io/badge/sample-CAMR_tuple-blue.svg "CAMR_tuple")](./docs/samples/CAMR_tuple.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/figure_5.PNG">
 <p>Figure 5: Data sample of CAMR tuple representation</p>
</div>

Figure 5 is a copy of CAMR tuple representation including sentence ID (sid), node_1 ID (nid1), concept_1 (concept1), co-reference node_1 (coref1), relation (rel), relation ID (rid), relation alignment word (ralign), node_2 ID (nid2), concept_2 (concept2) and co-reference node_2 (coref2).

## 3.2 Data Set
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
    <td align='center'>Train Set</td>
    <td align='center'>16576</td>
    <td align='center'>386234</td>
  </tr>
  <tr>
    <td align='center'>Dev Set</td>
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
    <td align='center'>2000 (approx.)</td>
    <td align='center'>40,000 (approx.)</td>
  </tr>
</tbody>
</table>


# 4 Evaluation Metrics and Modalities
## 4.1 Smatch 

As the most widely-used evaluation metric, smatch focuses on the overlapping of two AMR graphs. For two AMR graphs to be matched, smatch first renames the nodes of AMR graphs and transforms each AMR graph into a set of triples <a href="https://aclanthology.org/P13-2131.pdf">(S. Cai et al., 2013)</a>. There are three categories of triples as following:

1.	**Node triple: instance(node_index, concept).**

“instance” represents the concept nodes. “node_index” is the index of nodes in AMR graph and denoted as “$a_i$”. Without loss of generality, we have $i∈${$0, 1, …, n$}. “concept” is abstracted from the word accordingly. As shown in Table 2, for example, the triple “instance($a_0$, 希望-01)” indicates the instantiation of the word “希望” including its index “$a_0$” and the abstracted concept “希望-01”.

2.	**Arc triple: relation(node_index1, node_index2).**

“node_index1” and “node_index2” are indexs of two different concept nodes, and their mappings are “$a_i$” and “$a_j$”, respectively. As always, $j∈${$0,1,…,n$}. Note that the assignments of indexs can be without order and totally random. For the sake of simplicity, we follow the easiest way to assign each node with sequential index in Figure 6. “relation” is the semantic relation between the index “$a_i$” and “$a_j$”. As shown in Figure 2, the arc triple “arg1($a_1$, $a_4$)” means that the semantic relation between the mapping words of the index “$a_1$” and “$a_4$” is “arg1 (Object)”.

3.	**Node property triple: property(node_index, value).**

As shown in Table 2, the property triple “root($a_0$, top)” indicates that the property of the index “$a_0$” is “root”, in which “value” equals “top”, meaning that it is the root node in the graph.


<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/figures/figure_6.png" width=800>
 <p>Figure 6: CAMR graph of the sample sentence "希望我惨痛的经历给大家一个教训呀" (with indices)</p>
</div>


After the transformation from AMR graphs to triples, smatch performs the Hill-climbing search to obtain the maximum number of the matching triples between Gold AMR and Generated AMR, and returns **Precision**, **Recall** and **F-score**:
$$ P = {{count(Matching\enspace Triples)} \over {count(Generated\enspace Triples)}} $$
$$ R = {{count(Matching\enspace Triples)} \over {count(Gold\enspace Triples)}} $$
$$ F_β=(1+β^2)\*\frac{(P\*R)}{(β^2\*P)+R} $$

Specifically, **Precision** is the ratio of the maximum number of the matching triples between Gold AMR and Generated AMR, and the total number of Generated AMR triples. **Recall** is the ratio of the maximum number of the matching triples between Gold AMR and Generated AMR, and the total number of Gold AMR triples. **F-score** is the harmonic mean of **Precision** and **Recall**.

<table width='500' align="center">
<p align="center">Table 2: Smatch triples representation of the sample sentence</p>
<thead>
  <tr>
    <th style="text-align:center">Category</th>
    <th style="text-align:center">Triples</th>
    <th style="text-align:center">Quantity</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>Nodes</td>
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
    <td align='center'>Arcs</td>
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
    <td style="text-align:center">Property</td>
    <td align='center'>root(a0, top)</td>
    <td align='center'>1</td>
  </tr>
</tbody>
</table>

Although smatch has been prevailing since it came up, it has some flaws. When searching arc triples to be matched, smatch only considers whether the relations are the same but does not examine the concept nodes. It sometimes leads to such situation that two sentence with completely different semantics yet get oddly high matching scores <a href="https://arxiv.org/pdf/1905.10726.pdf">(Song et al., 2019)</a>.

## 4.2 Main metric: Align-smatch
With two types of information added, including concept alignment and relation alignment, Align-smatch now transforms Chinese AMR graph into tuples <a href="http://www.lrec-conf.org/proceedings/lrec2022/pdf/2022.lrec-1.638.pdf">(Xiao et al., 2022)</a>. 

1.	**The new triple for concept alignment: anchor(node_index, token_num).**

We name it concept alignment triple and add it into the same category with node property triple. “anchor” stands for it node property. “node_index” remains the same as in smatch. “token_num” means the number of the word in original sentence (as we mentioned earlier). As shown in Table 3, for example, the property triple “anchor($a_7$, x3)” indicates that the mapping concept node “惨痛-01” of the index “$a_7$” is aligned with the mapping word “惨痛” of the token number “x3”.

2.	**The new tuple for relation alignment: (Word_on_Arc, token_num, node_index1, node_index2).**

Likewise, we name it relation alignment tuple and add it into the same category with arc triple (tuple). “Word_on_Arc” represents the function word on arc for it actually matters a lot and conveys relations between content words in Chinese. As shown in Table 3, the arc tuple “(的, x4, $a_3$, $a_7$)” indicates that the function word “的” is on the arc from the index “$a_3$” to “$a_7$”, and assigned with the token number “x4” for it is the fourth word in the original sentence (after word segmentation).

3.	**The new arc triple: relation(node_index1, node_index2).**
	
When processing the word on the root node, we now replace the original property triple with the new arc triple. As shown in Table 2, the root node triple under smatch metric was “root($a_0$, top)”, and has been changed into “root($a_0$, $a_0$)” as we can see in Table 3.  


<table width='500' align="center">
 <p align="center">Table 3: Align-smatch tuples representation of the sample sentence</p>
<thead>
  <tr>
    <th style="text-align:center">Category</th>
    <th style="text-align:center">Tuples</th>
    <th style="text-align:center">Quantity</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>Nodes</td>
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
    <td align="center">Arcs</td>
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
    <td style="text-align:center">Property</td>
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


Similar to smatch, **Precision** in align-smatch is the ratio of the maximum number of the matching tuples between Gold AMR and Generated AMR, and the total number of Generated AMR tuples. **Recall** in align-smatch is the ratio of the maximum number of the matching tuples between Gold AMR and Generated AMR, and the total number of Gold AMR tuples.
$$ P = {{count(Matching\enspace Tuples)} \over {count(Generated\enspace Tuples)}} $$
$$ R = {{count(Matching\enspace Tuples)} \over {count(Gold\enspace Tuples)}} $$
$$ F_β=(1+β^2)\*\frac{(P\*R)}{(β^2\*P)+R} $$

<a name="anchor4.3"></a>

## 4.3 Two Modalities
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


To better parse and evaluate Chinese AMR, our evaluation task use Align-smatch as the main metric. The CAMR parsing results each team generates should contain the alignment information of concept and relation. Table 5 is a full example of evaluation scores output includes two metrics, two modalities and two different test sets, which are, therefore, eight tests in total. Note that Smatch scores are optional for we rank participants referring to the F-scores under **Align-smatch metric only**.


<table align="center">
<p align="center">Table 5: Example of evaluation scores</p>
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
    <td rowspan="4" align="center">Smatch (FYI)</td>
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
    <td rowspan="4">Align-smatch (Main)</td>
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

# 5 Writing the Technical Report
1.	Technical report can be written in both **Chinese** or **English**.
2.	Technical report should be formatted according to <a href="http://cips-cl.org/static/CCL2022/downloads/ccl2022_template.zip">CCL 2022 template</a>.
3.	The maximum length should be 4 pages (excluding references).
4.	Technical report should include at least the following sections: **introduction**, **evaluation results**, **result analysis** and **references**.

# 6 Awards
Awards include **First Prize**, **Second Prize** and **Third Prize**, 
and each team will be awarded with a unique certificate presented by **Chinese Information Processing Society of China** (CIPS).

# 7 References
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
