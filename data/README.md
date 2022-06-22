All the data participants need in CAMRP 2022 evaluation task should include three sets:
- **train set**
- **dev set** 
- **test set**


and  with four forms: 

- **CAMR**
- **CAMR tuples**
- **dependency tree** (external resource)
- **max length** (additional information)

Note that this repo doesn't offer data sets of training and validation (excluding max length files). Participants should contact [LDC](https://github.com/GoThereGit/Chinese-AMR/blob/main/docs/LDC_Evaluation_License_Agreement_CCL2022.pdf) to acquire the **train set** and **dev set** used in evaluation task.

Max length is required for evaluation tool Align-smatch. Please refer to [./tools/GUIDELINE.md](https://github.com/GoThereGit/Chinese-AMR/blob/main/tools/GUIDELINE.md) for more details.

**Test set** and **max length files** of all three data sets will be released via this repo.

Therefore, each team, for example, should recieve training data with a complete list of:

- **camr_train.txt** (via LDC)
- **tuples_train.txt** (via LDC)
- **camr_train.txt.out.conllu** (via LDC)
- **max_len_train.txt** (via this repo)

Follow us for the latest update! 
