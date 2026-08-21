# The 6th Chinese Abstract Meaning Representation Parsing Evaluation (SIGHAN Beta v1.0)

## Important Dates

- Evaluation task registration
- Training and development data release
- Test data release and system submission
- Technical report submission and evaluation workshop

## Evaluation Corpus Licensing

- Corpus application and license agreement
- Data usage restrictions
- Copyright information

## Organizers

### Organizers

- Nianwen Xue, Brandeis University
- Jin Zhao, Brandeis University
- Bin Li, Nanjing Normal University
- Zhixing Xu, Nanjing Normal University

### Staff

- TBD

### Contact

- TBD

------

# 1. Overview

Chinese Abstract Meaning Representation (CAMR) provides a structured semantic representation of Chinese sentences by representing concepts and their semantic relations as graphs. Previous CAMR parsing evaluations have primarily focused on sentence-level semantic parsing, while recent evaluations have begun to extend CAMR beyond individual sentences toward discourse-level semantic representation.

Natural discourse, however, cannot be fully understood by analyzing sentences independently. Semantic information is connected across sentence boundaries through phenomena such as **coreference** and **discourse relations**. Entities and events may be repeatedly mentioned, reformulated, omitted, or referred to by different expressions across sentences, while individual sentences and discourse units are connected through semantic relations such as coordination, causation, contrast, and elaboration. Modeling these phenomena is therefore an important step toward extending structured semantic parsing from the sentence level to the discourse level.

The 6th Chinese Abstract Meaning Representation Parsing Evaluation (CAMRP 2026) focuses on **discourse-level semantic parsing based on CAMR**. This evaluation introduces two complementary tasks:

- **Task 1: Discourse Coreference Resolution**, which requires systems to identify coreferential mentions across sentences and predict their fine-grained coreference relations.
- **Task 2: Discourse Relation Parsing**, which requires systems to identify semantic relations among sentences or discourse units and construct the corresponding discourse-level relation structure.

Together, the two tasks evaluate the ability of systems to model both **semantic continuity across sentences** and **semantic organization among discourse units**, extending CAMR from sentence-level semantic graphs toward structured discourse-level semantic representations.

------

# 2. Task 1: Discourse Coreference Resolution

## 2.1 Task Definition

CAMR provides structured semantic representations within individual sentences, including concepts and their semantic relations. However, discourse-level understanding additionally requires modeling how entities and events introduced in one sentence are referred to, continued, or transformed in subsequent sentences.

Based on the sentence-level CAMR annotation framework, we construct a **discourse coreference annotation framework** that extends coreference relations across sentence boundaries. Rather than representing coreference only as identity relations among textual mentions, the framework distinguishes fine-grained semantic variations between an antecedent and its subsequent mentions.

Given a discourse consisting of multiple tokenized Chinese sentences, participating systems are required to identify the coreference chains in the discourse and predict the corresponding **coreference relation, sentence index, and coreferential mention** for each member of a chain.

## 2.2 Annotation Scheme

The discourse coreference annotation framework defines **nine fine-grained coreference relation types**:

| No.  | Label     | Description                                                  |
| ---- | --------- | ------------------------------------------------------------ |
| 1    | `:root`   | The antecedent of a coreference chain, normally its first mention. |
| 2    | `:homo`   | The coreferential mention has the same expression as the antecedent. |
| 3    | `:add`    | The coreferential mention adds information to the antecedent. |
| 4    | `:reduce` | The coreferential mention is a reduced form of the antecedent. |
| 5    | `:alias`  | The coreferential mention refers to the antecedent using an alternative expression. |
| 6    | `:zero`   | The antecedent is referred to through zero anaphora without an explicit surface mention. |
| 7    | `:pro`    | The antecedent is referred to using a pronoun.               |
| 8    | `:illus`  | The coreferential mention elaborates on the antecedent by providing additional information or context. |
| 9    | `:encap`  | The coreferential mention summarizes or encapsulates the antecedent using a general term, phrase, or clause. |

The framework explicitly represents different forms of semantic continuity and variation across sentences. In particular, relations such as `:zero`, `:reduce`, and `:alias` capture discourse-level referential phenomena that are especially relevant to Chinese.

## 2.3 Task Input and Output

### Task Input

The input is a discourse consisting of multiple tokenized Chinese sentences. Each sentence is assigned a unique sentence identifier.

Example:

```text
s1: 中国 十四 个 边境 开放 城市 经济 建设 成就 显著 。

s2: 中国 十四 个 边境 对 外 开放 城市 一九九五年 经济 建设 取得 可喜 成果 。

s3: 据 统计 ， 这些 城市 去年 完成 国内 生产 总值 一百九十多亿 元 ， ……

s4: 三 年 来 ， 这些 城市 累计 完成 固定 资产 投资 一百二十亿 元 ， 昔日 边境 城市 的 ……
```

### Task Output

Participating systems are required to identify all coreference chains in the discourse. Each chain begins with a `:root` relation representing its antecedent, followed by subsequent coreferential mentions and their corresponding fine-grained relation types.

Example:

```text
:root   s1_x6 / 城市
:add    s2_x8 / 城市
:alias  s3_x5 / 城市
:alias  s4_x7 / 城市
:reduce s4_x17 / 城市
```

## 2.4 Evaluation Metrics

**TBD**

## 2.5 Evaluation Script

**TBD**

------

# 3. Task 2: Discourse Relation Parsing

## 3.1 Task Definition

In addition to coreference, discourse-level semantic understanding requires modeling the semantic relations that connect sentences and larger discourse units. Individual sentences in a discourse do not occur independently, but form coherent structures through relations such as expansion, causation, and coordination.

Based on the same discourse documents used in Task 1, we annotate **discourse relation structures** over multiple sentences. The annotation follows an AMR-like representation, in which sentences are identified by sentence IDs (`s1`, `s2`, ...), while discourse relations are represented as relation nodes (`d1`, `d2`, ...). A discourse relation may connect individual sentences or larger discourse units, allowing hierarchical and nested discourse structures to be represented.

Given a discourse consisting of multiple tokenized Chinese sentences, participating systems are required to identify the relations among sentences or discourse units and generate the corresponding discourse relation structure.

## 3.2 Annotation Scheme

- **Sentence nodes (`sX`)** represent individual sentences in the source discourse.
- **Discourse relation nodes (`dX / relation`)** represent semantic relations between sentences or discourse units, such as `expansion` and `causation`.
- Relations may take sentences or other discourse relation nodes as their arguments, enabling nested structures; coordination relations such as `and` may connect multiple discourse units through operands such as `:op1`, `:op2`, and `:op3`.

The complete discourse relation inventory and detailed annotation guidelines will be provided with the evaluation data.

## 3.3 Discourse Representation

Discourse relations are represented in an AMR-like notation. For example:

```text
d1 / expansion
    :arg1 s3
    :arg2 d2 / and
        :op1 s4
        :op2 d3 / expansion
            :arg1 s5
            :arg2 d4 / causation
                :arg1 d5 / and
                    :op1 s6
                    :op2 s7
                :arg2 s8
        :op3 d6 / expansion
            :arg1 s9
            :arg2 d7 / and
                :arg1 s10
                :arg2 s11
                :arg3 s12
```

In this example, `s3`–`s12` correspond to sentences in the source discourse, while `d1`–`d7` represent discourse relation nodes. The representation captures both the semantic relations between discourse units and their hierarchical organization.

## 3.4 Task Input and Output

### Task Input

The input is a discourse consisting of multiple tokenized Chinese sentences. Each sentence is assigned a unique sentence identifier (`s1`, `s2`, ...), following the same discourse documents used in Task 1.

### Task Output

Participating systems are required to generate the discourse relation structure corresponding to the input discourse. The output should identify:

- the discourse relation types;
- the sentences or discourse units participating in each relation;
- the hierarchical and nested organization of these relations.

The detailed output format and additional examples will be provided with the evaluation data.

## 3.5 Evaluation Metrics

**TBD**

## 3.6 Evaluation Script

**TBD**

------

# 4. Evaluation Data

## 4.1 Corpus

- The evaluation corpus is based on CAMR discourse documents with sentence-level semantic annotations.
- The same discourse documents are used for discourse coreference and discourse relation annotation.
- Corpus size, document length, domain distribution, and other statistics will be provided with the data release.

## 4.2 Data Splits

- **Training Set:** discourse documents with gold annotations for the evaluation tasks.
- **Development Set:** discourse documents for system development and validation.
- **Test Set:** discourse documents used for the official evaluation.

## 4.3 Data Format and Release

- Each discourse contains multiple tokenized sentences with unique sentence identifiers.
- Task 1 provides discourse coreference annotations, while Task 2 provides discourse relation structures over the corresponding sentences.
- Detailed file formats, naming conventions, and the data release schedule will be announced before the evaluation.

------

# 5. Evaluation Protocol

## 5.1 Closed Track

- Systems must use the specified evaluation corpus and permitted pretrained models.
- The use of external training data and resources is restricted.
- Detailed restrictions and permitted resources will be specified in the final evaluation guidelines.

## 5.2 Open Track

- Systems may use external corpora, pretrained models, and other external resources.
- Large language models may be used in accordance with the evaluation guidelines.
- Participating teams must describe the external resources used in their technical reports.

## 5.3 General Rules

- Manual correction of system-generated test outputs is prohibited.
- Participating systems must not use gold annotations of the test set during system development or inference.
- Additional rules concerning reproducibility and test-set usage will be provided in the final guidelines.

------

# 6. Submission

## 6.1 Submission Format

- Task 1 submissions should contain the predicted discourse coreference structures for all test documents.
- Task 2 submissions should contain the predicted discourse relation structures for all test documents.
- Detailed output formats and file naming conventions will be provided with the test data.

## 6.2 Submission Runs

- Each participating team may submit a limited number of runs for each task.
- Runs should indicate whether they belong to the open or closed track.
- The maximum number of submissions will be specified in the final evaluation guidelines.

## 6.3 Submission Procedure

- Submission files should be packaged according to the specified directory structure.
- The submission platform or email address will be announced before the evaluation.
- Submitted results will be checked for format validity before official evaluation.

------

# 7. Ranking

## 7.1 Task-wise Ranking

- Task 1 and Task 2 will be evaluated and ranked separately.
- Open and closed tracks will be ranked separately where applicable.
- Official ranking metrics will be announced with the evaluation scripts.

## 7.2 Overall Ranking

- An overall ranking combining the two discourse-level tasks may be provided.
- **TBD**.

------

# 8. Technical Report Writing

## 8.1 Paper Requirements

- Technical reports may be written in Chinese or English.
- The official paper template and page limit will be announced separately.
- Reports should follow the submission requirements of the evaluation workshop.

## 8.2 Required Contents

- Description of the submitted system and model architecture.
- Training data, pretrained models, and external resources used.
- Evaluation results, analysis, and discussion for the participated task(s).

## 8.3 Submission and Publication

- Participating teams should submit their technical reports according to the announced schedule.
- Accepted reports will proceed to camera-ready submission.
- Publication and workshop presentation information will be announced separately.

------

# 9. Awards

- Awards will be provided separately for Task 1 and Task 2.
- Track-specific awards may be provided where applicable.
- Detailed prize information will be announced separately.

------

# 10. Frequently Asked Questions

- Questions concerning task definitions and annotation formats.
- Questions concerning open/closed tracks and permitted resources.
- Questions concerning submission, evaluation, and ranking.

------

# 11. References

- Chinese Abstract Meaning Representation (CAMR)
- Previous CAMRP evaluations
- Related work on discourse coreference and discourse relation parsing