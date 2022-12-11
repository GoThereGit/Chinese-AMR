# <p align="center">Guidelines</p>

# Introduction

CAMRP 2022 uses Align-smatch as the main evaluation metric while Smatch is for reference only. Align-smatch returns an overall score between parsed CAMR and gold CAMR.

This is a guideline for how to use evaluation tool Align-smatch.

# Requirements and Installation

Python 3.5 or higher version is required.

You need to clone this repository to run Align-smatch.py (or Smatch.py).

# Usage

To run Smatch.py, you need following command with at least the [-f] option, which requires two filename arguments:

    python smatch.py -f parsed_amr.txt gold_amr.txt

To run Align-smatch.py, you need following command with at least the [-f] option and [-lf] option:

    python Align-smatch.py -f parsed_amr.txt gold_amr.txt -lf max_len.txt


### Input: 

* Two files which contain CAMR data. Each file may contain several CAMRs, and every two CAMRs are separated by a blank line.
* A file which contains the max length of each sentence in data sets. (**Align-smatch ONLY**)

### Input File Format: 

Please refer to "../docs/samples/<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/docs/samples/CAMR_tuple.txt">CAMR_tuple.txt</a>" and "./<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/tools/max_len.txt">max_len.txt</a>" (**Align-smatch ONLY**).

### Output: 

F-scores under Align-smatch (or Smatch) metric.

### Arguments:

* ***-h***: Help for more information.

* ***-f***: Two files of CAMR data. **Arguments required**.

* ***-lf***: A file including the max length of each sentence after tokenization. **Arguments required**. (**Align-smatch ONLY**)

* ***-r***: Restart number of the heuristic search during computation. This argument must be a positive integer. Note that Large restart number will reduce the chance of search error, but also increase the running time. Small restart number will reduce the running time as well as increase the chance of search error. The default value is by far the best trade-off. Participants can set a large number if the CAMR length is too long (with large search space) or not in need of a high speed of calculation. **Set to 4 by default**.

* ***-v***: Verbose output. The verbose information includes the tuples of each CAMR, the matching tuple number found for each iterations, and the optimal matching tuple number. It may help you better understand how the program works. **Set to FALSE by default**.

* ***--ms***: Output Align-smatch scores for every CAMR pair (for manual check). Align-smatch normally returns one single overall score based on all pairs of CAMRs, which are weighted according to their number of tuples. **Set to FALSE by default**.

* ***--pr***: Output Precision and Recall as well as the F-score. **Set to FALSE by default**.

# Citation
```
@InProceedings{xiao-EtAl:2022:LREC,
  author    = {Xiao, Liming  and  Li, Bin  and  Xu, Zhixing  and  Huo, Kairui  and  Feng, Minxuan  and  Zhou, Junsheng  and  Qu, Weiguang},
  title     = {Align-smatch: A Novel Evaluation Method for Chinese Abstract Meaning Representation Parsing based on Alignment of Concept and Relation},
  booktitle      = {Proceedings of the Language Resources and Evaluation Conference},
  month          = {June},
  year           = {2022},
  address        = {Marseille, France},
  publisher      = {European Language Resources Association},
  pages     = {5938--5945},
}
```
