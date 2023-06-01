## 本次CAMRP 2023评测任务共提供三个测试集，详情信息如下：

||testA|testB|testC|
|:---:|:---:|:---:|:---:|
|测试语料|√|√|√|
|token长度|√|√|√|
|依存句法结果|√|×|×|

- **token长度**（max_len.txt）为使用<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202022/tools">**Align-smatch**</a>评测得分时必须的文件，详见使用说明。
- 测试集testA额外提供对应的**依存句法分析结果**。
- **测试语料**格式为：```<原始句子编号> + tab + <分词后的句子>``` 
- **token长度**格式为：```<原始句子编号> + tab + <max length>``` 
- 如有任何疑问，请与我们联系：<xzx0828@live.com>
