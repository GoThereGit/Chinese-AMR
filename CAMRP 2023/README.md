<div align="center">
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/img/2023logo.png" width=200>
</div>



# <p align="center">Chinese Abstract Meaning Representation Parsing 2023</p>

# <p align="center"><font size=50><strong>中文抽象语义表示解析评测任务</strong></font></p>

# 最新消息：
|时间|消息|
|:---:|:---:|
|3月1日|评测任务报名|
|4月1日|LDC发布训练集以及验证集|
|5月1日|报名截止日期推迟至5月25日|
|6月1日|<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/data">**测试集**</a>发布|
|6月7日|自动标注结果提交截止时间推迟至**6月8日23:59 PM**|
|6月12日|测试集黄金标准答案发布时间推迟至**6月14日**|
|6月15日|获奖排名将在参赛队提交技术报告后公布|
|7月13日|公布评测结果|

# 评测排名：

🥇**SUDA**

🥈**WestlakeNLP**

🥉**SJTU**

CAMRP 2023评测论文现已被收录进<a href='https://aclanthology.org/events/ccl-2023/'>ACL Anthology</a>

<table align='center'>
 <p align='center'>Table 1: Closed Test A</p>
<thead>
  <tr>
    <th rowspan="2">Team</th>
    <th rowspan="2">Run</th>
    <th colspan="3">Align-smatch</th>
    <th colspan="3">Smatch</th>
    <th colspan="3">MRP</th>
  </tr>
  <tr>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">BUPT</td>
    <td>1</td>  
    <td>0.7774</td>
    <td>0.7682</td>
    <td>0.7728</td>
    <td>0.7598</td>
    <td>0.7539</td>
    <td>0.7569</td>
    <td>0.8086</td>
    <td>0.8057</td>
    <td>0.8071</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.7840</td>
    <td>0.7644</td>
    <td>0.7741</td>
    <td>0.7529</td>
    <td>0.7350</td>
    <td>0.7438</td>
    <td>0.8035</td>
    <td>0.7947</td>
    <td>0.7991</td>
  </tr>
  <tr>
    <td rowspan="2">GDUFE</td>
    <td>1</td>
    <td>0.8080</td>
    <td>0.7287</td>
    <td>0.7663</td>
    <td>0.7905</td>
    <td>0.7121</td>
    <td>0.7492</td>
    <td>0.8308</td>
    <td>0.7631</td>
    <td>0.7955</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SUDA</td>
    <td>1</td>
    <td>0.8183</td>
    <td>0.7824</td>
    <td>0.8000</td>
    <td>0.8104</td>
    <td>0.7696</td>
    <td>0.7895</td>
    <td>0.8463</td>
    <td>0.8142</td>
    <td>0.8299</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.8185</td>
    <td>0.7654</td>
    <td>0.7911</td>
    <td>0.8104</td>
    <td>0.7515</td>
    <td>0.7798</td>
    <td>0.8460</td>
    <td>0.7963</td>
    <td>0.8204</td>
  </tr>
  <tr>
    <td rowspan="2">WHU</td>
    <td>1</td>
    <td>0.7894</td>
    <td>0.7490</td>
    <td>0.7687</td>
    <td>0.7528</td>
    <td>0.7326</td>
    <td>0.7426</td>
    <td>0.8036</td>
    <td>0.7941</td>
    <td>0.7988</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</tbody>
</table>

<table align='center'>
 <p align='center'>Table 2: Closed Test B</p>
<thead>
  <tr>
    <th rowspan="2">Team</th>
    <th rowspan="2">Run</th>
    <th colspan="3">Align-smatch</th>
    <th colspan="3">Smatch</th>
    <th colspan="3">MRP</th>
  </tr>
  <tr>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">BUPT</td>
    <td>1</td>
    <td>0.6959</td>
    <td>0.7103</td>
    <td>0.7030</td>
    <td>0.6999</td>
    <td>0.7045</td>
    <td>0.7022</td>
    <td>0.7564</td>
    <td>0.7527</td>
    <td>0.7545</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.7209</td>
    <td>0.6968</td>
    <td>0.7087</td>
    <td>0.7041</td>
    <td>0.6872</td>
    <td>0.6956</td>
    <td>0.7484</td>
    <td>0.7509</td>
    <td>0.7497</td>
  </tr>
  <tr>
    <td rowspan="2">GDUFE</td>
    <td>1</td>
    <td>0.7575</td>
    <td>0.6118</td>
    <td>0.6769</td>
    <td>0.7515</td>
    <td>0.6111</td>
    <td>0.6741</td>
    <td>0.7921</td>
    <td>0.6617</td>
    <td>0.7210</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SUDA</td>
    <td>1</td>
    <td>0.7516</td>
    <td>0.7028</td>
    <td>0.7264</td>
    <td>0.7569</td>
    <td>0.7119</td>
    <td>0.7337</td>
    <td>0.7964</td>
    <td>0.7529</td>
    <td>0.7740</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.7535</td>
    <td>0.6968</td>
    <td>0.7240</td>
    <td>0.7622</td>
    <td>0.7058</td>
    <td>0.7329</td>
    <td>0.8008</td>
    <td>0.7452</td>
    <td>0.7720</td>
  </tr>
  <tr>
    <td rowspan="2">WHU</td>
    <td>1</td>
    <td>0.7241</td>
    <td>0.6783</td>
    <td>0.7004</td>
    <td>0.7028</td>
    <td>0.6823</td>
    <td>0.6924</td>
    <td>0.7489</td>
    <td>0.7488</td>
    <td>0.7488</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</tbody>
</table>

<table align='center'>
 <p align='center'>Table 3: Closed Test C</p>
<thead>
  <tr>
    <th rowspan="2">Team</th>
    <th rowspan="2">Run</th>
    <th colspan="3">Align-smatch</th>
    <th colspan="3">Smatch</th>
    <th colspan="3">MRP</th>
  </tr>
  <tr>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">BUPT</td>
    <td>1</td>
    <td>0.8096</td>
    <td>0.7862</td>
    <td>0.7977</td>
    <td>0.7925</td>
    <td>0.7980</td>
    <td>0.7952</td>
    <td>0.8354</td>
    <td>0.8386</td>
    <td>0.8370</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.8060</td>
    <td>0.7777</td>
    <td>0.7916</td>
    <td>0.7780</td>
    <td>0.7562</td>
    <td>0.7669</td>
    <td>0.8300</td>
    <td>0.8072</td>
    <td>0.8185</td>
  </tr>
  <tr>
    <td rowspan="2">GDUFE</td>
    <td>1</td>
    <td>0.8238</td>
    <td>0.7308</td>
    <td>0.7745</td>
    <td>0.8048</td>
    <td>0.7161</td>
    <td>0.7578</td>
    <td>0.8489</td>
    <td>0.7653</td>
    <td>0.8049</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SUDA</td>
    <td>1</td>
    <td>0.8331</td>
    <td>0.7951</td>
    <td>0.8137</td>
    <td>0.8265</td>
    <td>0.7870</td>
    <td>0.8063</td>
    <td>0.8652</td>
    <td>0.8282</td>
    <td>0.8463</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.8111</td>
    <td>0.8050</td>
    <td>0.8081</td>
    <td>0.8126</td>
    <td>0.8102</td>
    <td>0.8114</td>
    <td>0.8563</td>
    <td>0.8445</td>
    <td>0.8504</td>
  </tr>
  <tr>
    <td rowspan="2">WHU</td>
    <td>1</td>
    <td>0.8098</td>
    <td>0.7635</td>
    <td>0.7859</td>
    <td>0.7798</td>
    <td>0.7548</td>
    <td>0.7671</td>
    <td>0.8313</td>
    <td>0.8069</td>
    <td>0.8189</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</tbody>
</table>

<table align='center'>
 <p align='center'>Table 4: Open Test A</p>
<thead>
  <tr>
    <th rowspan="2">Team</th>
    <th rowspan="2">Run</th>
    <th colspan="3">Align-smatch</th>
    <th colspan="3">Smatch</th>
    <th colspan="3">MRP</th>
  </tr>
  <tr>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">GDUFE</td>
    <td>1</td>
    <td>0.7553</td>
    <td>0.7560</td>
    <td>0.7556</td>
    <td>0.7333</td>
    <td>0.7403</td>
    <td>0.7368</td>
    <td>0.7832</td>
    <td>0.7944</td>
    <td>0.7887</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SJTU</td>
    <td>1</td>
    <td>0.4741</td>
    <td>0.4645</td>
    <td>0.4692</td>
    <td>0.6173</td>
    <td>0.6094</td>
    <td>0.6133</td>
    <td>0.5131</td>
    <td>0.5022</td>
    <td>0.5076</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SUDA</td>
    <td>1</td>
    <td>0.8081</td>
    <td>0.8174</td>
    <td>0.8128</td>
    <td>0.7960</td>
    <td>0.8060</td>
    <td>0.8010</td>
    <td>0.8375</td>
    <td>0.8456</td>
    <td>0.8415</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.8082</td>
    <td>0.8179</td>
    <td>0.8130</td>
    <td>0.7955</td>
    <td>0.8054</td>
    <td>0.8004</td>
    <td>0.8376</td>
    <td>0.8457</td>
    <td>0.8416</td>
  </tr>
  <tr>
    <td rowspan="2">WestlakeNLP</td>
    <td>1</td>
    <td>0.7440</td>
    <td>0.7024</td>
    <td>0.7226</td>
    <td>0.7300</td>
    <td>0.6936</td>
    <td>0.7114</td>
    <td>0.7816</td>
    <td>0.7322</td>
    <td>0.7561</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</tbody>
</table>

<table align='center'>
 <p align='center'>Table 5: Open Test B</p>
<thead>
  <tr>
    <th rowspan="2">Team</th>
    <th rowspan="2">Run</th>
    <th colspan="3">Align-smatch</th>
    <th colspan="3">Smatch</th>
    <th colspan="3">MRP</th>
  </tr>
  <tr>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">GDUFE</td>
    <td>1</td>
    <td>0.6971</td>
    <td>0.6733</td>
    <td>0.6850</td>
    <td>0.6882</td>
    <td>0.6778</td>
    <td>0.6830</td>
    <td>0.7394</td>
    <td>0.7306</td>
    <td>0.7350</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SJTU</td>
    <td>1</td>
    <td>0.4644</td>
    <td>0.4568</td>
    <td>0.4606</td>
    <td>0.6037</td>
    <td>0.6001</td>
    <td>0.6019</td>
    <td>0.5137</td>
    <td>0.5099</td>
    <td>0.5118</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SUDA</td>
    <td>1</td>
    <td>0.7433</td>
    <td>0.7485</td>
    <td>0.7459</td>
    <td>0.7505</td>
    <td>0.7635</td>
    <td>0.7570</td>
    <td>0.7899</td>
    <td>0.7963</td>
    <td>0.7931</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.7439</td>
    <td>0.7503</td>
    <td>0.7471</td>
    <td>0.7521</td>
    <td>0.7669</td>
    <td>0.7595</td>
    <td>0.7916</td>
    <td>0.7975</td>
    <td>0.7945</td>
  </tr>
  <tr>
    <td rowspan="2">WestlakeNLP</td>
    <td>1</td>
    <td>0.7042</td>
    <td>0.6863</td>
    <td>0.6952</td>
    <td>0.7021</td>
    <td>0.6930</td>
    <td>0.6975</td>
    <td>0.7501</td>
    <td>0.7301</td>
    <td>0.7400</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</tbody>
</table>

<table align='center'>
 <p align='center'>Table 6: Open Test C</p>
<thead>
  <tr>
    <th rowspan="2">Team</th>
    <th rowspan="2">Run</th>
    <th colspan="3">Align-smatch</th>
    <th colspan="3">Smatch</th>
    <th colspan="3">MRP</th>
  </tr>
  <tr>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
    <th>P</th>
    <th>R</th>
    <th>F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2">GDUFE</td>
    <td>1</td>
    <td>0.7730</td>
    <td>0.7814</td>
    <td>0.7772</td>
    <td>0.7521</td>
    <td>0.7691</td>
    <td>0.7605</td>
    <td>0.8020</td>
    <td>0.8181</td>
    <td>0.8100</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SJTU</td>
    <td>1</td>
    <td>0.6282</td>
    <td>0.5839</td>
    <td>0.6052</td>
    <td>0.7262</td>
    <td>0.6840</td>
    <td>0.7045</td>
    <td>0.6697</td>
    <td>0.6228</td>
    <td>0.6454</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td rowspan="2">SUDA</td>
    <td>1</td>
    <td>0.8206</td>
    <td>0.8212</td>
    <td>0.8209</td>
    <td>0.8164</td>
    <td>0.8195</td>
    <td>0.8179</td>
    <td>0.8575</td>
    <td>0.8566</td>
    <td>0.8571</td>
  </tr>
  <tr>
    <td>2</td>
    <td>0.8211</td>
    <td>0.8213</td>
    <td>0.8212</td>
    <td>0.8163</td>
    <td>0.8186</td>
    <td>0.8175</td>
    <td>0.8576</td>
    <td>0.8563</td>
    <td>0.8569</td>
  </tr>
  <tr>
    <td rowspan="2">WestlakeNLP</td>
    <td>1</td>
    <td>0.8273</td>
    <td>0.8249</td>
    <td>0.8261</td>
    <td>0.8143</td>
    <td>0.8118</td>
    <td>0.8130</td>
    <td>0.8561</td>
    <td>0.8549</td>
    <td>0.8555</td>
  </tr>
  <tr>
    <td>2</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
</tbody>
</table>

![What's new?](https://img.shields.io/badge/CAMRP_2023-NEW-red.svg "English Version")

今年亮点：新增2000句问句语料，增强汉语的问句焦点和一句多问的分析能力！

[![Eng](https://img.shields.io/badge/README-English-yellow.svg "English Version")](./README_En.md)

**English Version:** <a href="https://github.com/GoThereGit/Chinese-AMR/blob/main/README_En.md">README_En.md</a>

[![signup](https://img.shields.io/badge/CAMRP_2023-报名-blue.svg "sign up")](https://forms.office.com/r/67EyjvBFm2)

- [X] 2023年3月1日：<a href="https://forms.office.com/r/67EyjvBFm2">**评测报名**</a>开始，提供<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/CAMRP%202022/tools">Align-smatch</a>评测软件下载地址。

- [X] 2023年4月1日：LDC发布训练集以及验证集给参赛队。

- [X] 2023年5月25日：报名截止。

- [X] 2023年6月1日：**本站**发布<a href="https://github.com/GoThereGit/Chinese-AMR/tree/main/data">**测试集**</a>（包含Test A、Test B和新的Test C）给参赛队。

- [X] 2023年6月8日：参赛队提交自动标注的数据（提交格式详见<a href="#anchor2.2">2.2 任务说明</a>）。

- [X] 2023年6月14日：**本站**发布测试集（包含Test A、Test B和新的Test C）黄金标准答案给参赛队。

- [X] 2023年6月21日：参赛队提交中文抽象语义表示评测任务技术报告，用于审稿。

- [X] 2023年6月25日：参赛队提交技术报告最终版。

- [X] 2023年8月3日-5日：<a href="http://cips-cl.org/static/CCL2023/cclEval/taskCollection/index.html">CCL 2023</a>评测研讨会。

[![agreement](https://img.shields.io/badge/CAMRP_评测语料许可协议-LDC-red.svg "PDF")](./docs/LDC_Evaluation_License_Agreement_CCL2022.pdf)

**参赛队伍需自行向LDC申请CAMRP 2022评测语料使用权，并签署保密协议：**
1.	每支参赛队伍需指派一名联系负责人。
2.	参赛队伍联系负责人需填写[LDC评测语料许可协议](./docs/LDC_Evaluation_License_Agreement_CCL2023.pdf)，扫描后通过E-mail发送给LDC（<ldc@ldc.upenn.edu>）。
3.	申请通过后，LDC将返回CAMRP v2.0E版本语料库给参赛队伍联系负责人，以供参赛队伍使用。该语料数据只可用于本次CAMRP 2023评测任务，不可有其他任何用途。
4.	本次评测语料数据集的版权归<a href="https://www.ldc.upenn.edu/">LDC</a>所有。

![nnu](https://img.shields.io/badge/CAMRP_2023-NNU-green.svg "sign up")

* 组织者：
  * 李斌（南京师范大学）（联系邮箱：<libin.njnu@gmail.com>）
  * 曲维光（南京师范大学）
  * 周俊生（南京师范大学）
  * 薛念文（布兰迪斯大学）
 
* 工作人员（研究生）：
  * 许智星（南京师范大学）
  * 肖力铭（南京师范大学）
  * 芦靖雅（南京师范大学）
  * 陈瑾（南京师范大学）
  * 谢媛媛（南京师范大学）
  * 张艺璇（南京师范大学）
  

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
提出了一种与领域无关的、通用的整句语义表示方法——抽象语义表示（Abstract Meaning Representation，AMR）。该方法使用单根有向无环图，来表示一个句子的语义结构，并且建设了规模较大的语料库，进行了两次国际AMR语义解析评测。中文抽象语义表示（Chinese AMR，CAMR）语料库的构建已初具规模
<sup>
 <a href="https://aclanthology.org/W16-1702.pdf">
  [3]
 </a>
</sup>，也在CoNLL 2020上进行了语义解析评测。

本次评测任务是在中文抽象语义语料库上，自动解析出句子的AMR图。与英文AMR不同的是，中文AMR增加了概念关系对齐信息
<sup>
 <a href="https://journals.colorado.edu/index.php/lilt/article/view/1429/1271">
  [4]
 </a>
</sup>
，并针对中文特点增加了一些语义标签。概念关系对齐信息并没有用于CoNLL 2020的评测。因此，本次评测重新设计了包含了概念关系对齐的信息的新评测指标Align-smatch，能够更好地评估自动解析的性能。
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
  在Smatch评测指标的基础上，加入了概念对齐指标和关系对齐指标——Align-smatch。CAMRP2022的评测引入了这种新的评测指标，在CoNLL2020的语料（Test A）上取得了0.8的F值，在新的语料Test B上也取得了较好的成绩。今年CAMRP2023将使用和CAMRP2022相同的训练和测试语料，另外新增2000句问句语料，以便增强汉语的问句焦点和一句多问的自动分析能力。以下将详细介绍CAMR的特点和Align-smatch评测指标。
  
## 1.2 中文AMR介绍
在英文AMR的标注中，一般使用词语的首字母作为概念节点的编号，或者按照节点的出现顺序来直接分配编号，这导致计算机处理时无法对概念溯源，一定程度上影响了解析的精度。为了解决这一问题，Li et al.
<sup>
 <a href="https://journals.colorado.edu/index.php/lilt/article/view/1429/1271">
  [4]
 </a>
</sup>
根据汉语的特点对AMR进行了改进，在保留了AMR较强语义表示能力的同时，在CAMR中增加了“词与概念”的对齐信息和“词与关系”的对齐信息。通过对分词后对原始句子按照线性排序的原则，采用“x+数字”的形式，依次给每个词赋予不同的编号，而对应的概念节点也获得相同的编号。如图1中，“惨痛”为句子中的第3个词，因而被赋予了“x3”的编号，同时与概念节点“x3/惨痛-01”完成了对齐。

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/figures/figure_1.png">
 <p>图1 例句“希望我惨痛的经历给大家一个教训呀”CAMR文本表示</p>
</div>

除了编号方案的处理不同，CAMR对虚词的处理也不一样。英文AMR一般直接忽略了句子中如介词、冠词等对句子语义没有贡献的虚词。而考虑到语言的不同特点，CAMR选择保留虚词并对其进行标注，将表示句子体意义和语气意义的虚词处理为概念节点，将表示实词间关系意义的虚词看作语义关系的映射，并将其与语义角色标签一同标注在有向弧上
<sup>
 <a href="https://www.researchgate.net/profile/Bin-Li-238/publication/342919422_Representation_and_Analysis_of_Abstract_Meaning_of_Chinese_Function_Words_Based_on_Relation_Alignmentjiyuguanxiduiqidehanyuxucichouxiangyuyibiaoshiyufenxi/links/5f0d9865a6fdcce8ae96f65d/Representation-and-Analysis-of-Abstract-Meaning-of-Chinese-Function-Words-Based-on-Relation-Alignmentjiyuguanxiduiqidehanyuxucichouxiangyuyibiaoshiyufenxi.pdf">
  [8]
 </a>
</sup>
。最后，沿用概念对齐中编号的方案，有向弧上的虚词同样被赋予了顺序的编号，以实现关系对齐。如图2所示，虚词“的”和语义角色标签“arg0-of”一起被标注在了有向弧上，又由于它是第4个词，因而被编号为“x4”，以上两个步骤完成了语义关系“arg0-of”和虚词“x4/的”的对齐。

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/figures/figure_2.png" width=800>
 <p>图2 例句“希望我惨痛的经历给大家一个教训呀”的CAMR图示</p>
</div>

## 1.3 小结
因此，为了更好地推进中文抽象语义表示解析工作的展开，南京师范大学提出了本次中文抽象语义表示评测任务。不同于CoNLL 2020举办的MRP跨语言/跨语义框架评测
<sup>
 <a href="https://dspace.library.uu.nl/bitstream/handle/1874/414809/2020.conll_shared.1.pdf?sequence=1&isAllowed=y">
  [9]
 </a>
</sup>，本次评测任务是对中文AMR解析评测，评测标准选用更加细致的Align-smatch评测标准，包括了概念对齐信息和关系对齐信息（详见<a href="#anchor3.2">3.2 作为主要标准的Align-smatch评测指标</a>）。

# 2 评测数据

## 2.1 数据样例
本次评测任务提供三种数据，包括**CAMR文本表示**、**依存句法分析结果**及**CAMR多元组表示**。例句“这几天关于中俄战略合作伙伴关系成了大热点。”选自本次评测任务的训练集，以下为对应的三种表示样例：

[![sample](https://img.shields.io/badge/sample-CAMR_text-red.svg "CAMR_text")](https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/samples/CAMR_text.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/figures/figure_3.png">
 <p>图3 CAMR文本表示样例</p>
</div>

图3为例句的CAMR文本表示样例，具体包括句子ID、词序列、词编号（x）、概念对齐信息、关系对齐信息和CAMR文本表示；语料编码格式为UTF-8。


[![sample](https://img.shields.io/badge/sample-CAMR_dep-green.svg "CAMR_dep")](https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/samples/CAMR_dep.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/figures/Figure_4.png" width=800>
 <p>图4 依存句法分析结果样例</p>
</div>

图4为例句的依存句法分析结果样例。在封闭测试中，该依存句法分析结果可作外部资源供参赛队使用（详见<a href="#anchor3.3">3.3 模态选择</a>）。

[![sample](https://img.shields.io/badge/sample-CAMR_tuple-blue.svg "CAMR_tuple")](https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/samples/CAMR_tuple.txt)

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/figures/figure_5.PNG" >
 <p>图5 CAMR多元组表示样例</p>
</div>

图5为例句的CAMR多元组表示样例，具体包括句子编号1、节点编号1、概念1、同指节点1、关系、关系编号、关系对齐词、节点编号2、概念2和同指节点2。参赛队最终返回的自动标注数据也应为CAMR多元组表示格式（详见<a href="#anchor2.2">2.2 任务说明</a>）。

<a name="anchor2.2"></a>
## 2.2 任务说明

**输入：**
（分词后的句子）

``
希望 我 惨痛 的 经历 给 大家 一 个 教训 呀
``

**输出：**
（CAMR多元组；<a href = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/tools/camr_to_tuples.py">转换脚本</a>由本站提供。）

|句子编号|节点编号1|概念1|同指节点1|关系|关系编号|关系对齐词|节点编号2|概念2|同指节点2|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|1617|x0|root|-|:top|-|-|x1|希望-01|-|
|1617|x1|希望-01|-|:arg1|-|-|x6|给-01|-|
|1617|x1|希望-01|-|:mode|-|-|x11|expressive|-|
|1617|x6|给-01|-|:arg0|-|-|x5|经历|-|
|1617|x6|给-01|-|:arg2|-|-|x7|大家|-|
|1617|x6|给-01|-|:arg1|-|-|x10|教训|-|
|1617|x5|经历|-|:poss|-|-|x2|我|-|
|1617|x5|经历|-|:arg0-of|x4|的|x3|惨痛-01|-|
|1617|x10|教训|-|:quant|-|-|x8|1|-|
|1617|x10|教训|-|:cunit|-|-|x9|个|-|

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

所有结果需打包在一个文件夹内并压缩后发送至邮箱<libin.njnu@gmail.com>，邮件名称为“CAMRP2023+参赛队名+submitdata”。

## 2.3 数据集
中文抽象语义表示语料库（Chinese Abstract Meaning Representation Corpus）于2015年开始，由南京师范大学和美国布兰迪斯大学合作构建
<sup>
 <a href="https://aclanthology.org/W16-1702.pdf">
  [3]
 </a>
</sup>。语料库为在LDC（Linguistic Data Consortium）发布的<a href="https://catalog.ldc.upenn.edu/LDC2021T13">CAMR v2.0</a>，约含2万中文句子，原始语料选自于宾州中文树库（Chinese Tree Bank 8.0，CTB 8.0），分为训练集、验证集和测试集。该语料已在CoNLL 2020进行过评测。本次评测任务将继续沿用该语料库，以比较两年来中文AMR语义解析的进展。为了防止参赛队将测试集用于训练，本次评测设置了盲测集，约含3000句语料。该部分语料没有公开，亦可观察各个系统在盲测数据集上的表现，可用来评测解析模型处理不同语体风格的文本数据时的泛化能力。提供的各项数据分布如表1所示：


<table align="center">
<p align="center">表1 评测数据集</p>
<thead>
  <tr>
    <th style="text-align:center">数据集（Data Sets）</th>
    <th style="text-align:center">句子数（Sentences）</th>
    <th style="text-align:center">词例数（Word Tokens）</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align='center'>训练集（Train Set）</td>
    <td align='center'>16576</td>
    <td align='center'>386234</td>
  </tr>
  <tr>
    <td align='center'>验证集（Dev Set）</td>
    <td align='center'>1789</td>
    <td align='center'>41822</td>
  </tr>
  <tr>
    <td align='center'>测试集（Test A）</td>
    <td align='center'>1713</td>
    <td align='center'>39228</td>
  </tr>
  <tr>
    <td align='center'>测试集（Test B）</td>
    <td align='center'>约2000句</td>
    <td align='center'>约4万词</td>
  </tr>
    <tr>
    <td align='center'>盲测集（Test C）</td>
    <td align='center'>约2000句</td>
    <td align='center'>约3万词</td>
  </tr>
</tbody>
</table>


# 3 评价标准与模态
## 3.1 作为参考标准的Smatch评测指标
作为目前最主要的AMR评测指标，Smatch主要考虑的是两个AMR图之间的重叠程度。对于两个需要进行匹配的AMR图，Smatch首先将每个AMR图转化为三元组（Triple）的集合
<sup>
 <a href="https://aclanthology.org/P13-2131.pdf">
  [10]
 </a>
</sup>
，每个集合一般包含三种数据类型的三元组：
1.  **表示节点的三元组：instance(node_index, concept)。**

其中，instance表示对概念节点的实例化；node_index为节点索引，记作a**i**，**i**$\in$\{0,1,…,n\}；concept为由词抽象出的概念。如表2所示，在例句“希望我惨痛的经历给大家一个教训呀”对应的AMR三元组中，节点三元组包含了所有节点的实例、节点索引和对应的概念。如三元组“instance(a0, 希望-01)”表示“希望”一词的实例化，该词的节点索引为a0，AMR抽象出的概念为“希望-01”。

2.  **表示有向弧的三元组：relation(node_index1, node_index2)。**

node_index1和node_index2表示为两个不同概念节点的索引，分别对应a**i**和a**j**，同理，**j**$\in$\{0,1,…,n\}，节点索引的分配可以是完全随机的，如图6所示（本文选用完全二叉树的顺序存储方式对节点索引进行编号，仅供参考）；relation为a**i**、a**j**节点对应的两个词之间的语义关系。如表2所示，有向弧三元组“arg1(a1,a4)”表示a1索引和a4索引所对应的词“给”和“大家”之间的语义关系为“arg1（受事）”。

3.  **表示节点属性的三元组：property(node_index, value)。**

如表2所示，节点属性三元组root(a0, top)表示a0节点的属性为根节点，其中，value=top。

<div align=center>
<img src = "https://github.com/GoThereGit/Chinese-AMR/blob/main/CAMRP%202022/docs/figures/figure_6.png" width=800>
 <p>图6 例句“希望我惨痛的经历给大家一个教训呀”的CAMR图示（带有节点索引）</p>
</div>

完成了AMR三元组的转化之后，Smatch使用爬山算法（Hill-climbing Method）进行贪婪搜索以获取黄金AMR（Gold AMR）三元组集合和解析生成的AMR（Generated AMR）三元组集合之间的最大匹配个数，最终返回准确率（P）、召回率（R）和F值（F-score）：
$$P = {{count(Matching\enspace Triples)} \over {count(Generated\enspace Triples)}}$$
$$R = {{count(Matching\enspace Triples)} \over {count(Gold\enspace Triples)}}$$
$$F_β=(1+β^2)\*\frac{P\*R}{(β^2\*P)+R}$$

其中，Smatch里的准确率P为黄金AMR的三元组集合和解析生成的AMR三元组集合间的最大匹配个数与解析生成的AMR的三元组总个数之比；召回率R为黄金AMR三元组集合和解析生成的AMR三元组集合间的最大匹配个数与黄金AMR的三元组总个数之比；F值为准确率和召回率的调和平均值（Harmonic Mean），β$\in{R^+}$，表示为影响权重：当β>1时，召回率比准确率更重要；反之，当β<1时，准确率比召回率更重要；当β=1时，召回率和确准率同样重要（即$F_β=F_1$）。

<table width='500' align="center">
<p align="center">表2 Smatch三元组表示</p>
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


Smatch自提出以来被广泛使用于AMR解析评测，但其仍然存在一些弊端：在比较有向弧的三元组时，Smatch只考虑语义角色标签是否相同，而忽视了概念节点是否一致，这容易导致两个语义不同的句子反而出现匹配程度较高的情况
<sup>
 <a href="https://arxiv.org/pdf/1905.10726.pdf">
  [11]
 </a>
</sup>
。

<a name="anchor3.2"></a>
## 3.2 作为主要标准的Align-smatch评测指标
Align-smatch在Smatch的基础上增添了两种新的数据：概念对齐信息和关系对齐信息
<sup>
 <a href="http://124.16.136.79/CN/article/downloadArticleFile.do?attachType=PDF&id=3243">
  [7]
 </a>
</sup>
。不同于Smatch的三元组，Align-smatch将中文AMR转化为一个多元组（Tuple）集合，每个多元组包含三个或者四个元素。Align-smatch对多元组的数据类型作了以下修改：

1. **在原节点属性三元组中新增了表示概念对齐的三元组：anchor(node_index, token_num)。**

其中，anchor表示该节点的属性为“对齐”，node_index为节点索引，token_num为词编号。如表3所示，节点属性三元组anchor(a7, x3 )表示a7索引对应的概念节点“惨痛-01”与词编号x3对应的词“惨痛”完成了概念对齐。

2. **在原有向弧三元组中新增了表示关系对齐的四元组：(Word_on_Arc, token_num, node_index1, node_index2)。**

其中，Word_on_Arc为有向弧上的虚词，传递实词之间的关系意义。如表3所示，有向弧四元组(的, x4, a3, a7)表示虚词“的”位于a3索引和a7索引分别对应的两个节点所连成的有向弧上，同时“的”被赋予词编号x4，完成了关系对齐。

3. **使用有向弧多元组来表示位于根节点的词，而不再使用节点属性三元组表示：property(node_index, value) → relation(node_index1, node_index2)。**

如表2所示，在Smatch指标下，例句中的根节点的三元组表示为：root(a0, top)。如表3所示，Align-smatch中该节点的表示则修改为：root(a0, a0)。
Align-smatch评测公式如下：
$$P = {{count(Matching\enspace Tuples)} \over {count(Generated\enspace Tuples)}}$$
$$R = {{count(Matching\enspace Tuples)} \over {count(Gold\enspace Tuples)}}$$
$$F_β=(1+β^2)\*\frac{P\*R}{(β^2\*P)+R}$$

同样的，Align-smatch中的准确率P为黄金AMR的多元组集合和解析生成的AMR多元组集合间的最大匹配个数与解析生成的AMR多元组总个数之比；召回率R为黄金AMR的多元组集合和解析生成的AMR多元组集合之间的最大匹配个数与黄金AMR的多元组总个数之比；F值同上。

<table width='500' align="center">
 <p align="center">表3 Align-smatch多元组表示</p>
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
    <td align="center">有向弧</td>
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

<a name="anchor3.3"></a>
## 3.3 模态选择
本次评测任务包含开放测试（Open Modality）和封闭测试（Closed Modality）：
1. 若参赛队选择封闭测试，则必须使用指定的训练集、测试集和预训练语言模型，不可自行替换为别的资源。在封闭测试中，主办方提供训练集的依存分析结果，并推荐使用哈工大的HIT_Roberta<sup><a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9599397">[12]</a></sup>预训练模型。
2. 若参赛队也选择开放测试，预训练语言模型可自由选择，允许使用外部资源，如专名识别、依存句法分析结果等。开放测试中，参赛队使用的所有资源需要在最终提交的技术报告中给予详细说明。但无论哪种模态，均不可使用人工修正自动解析结果的方式。

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

为了更加完整、精确地解析CAMR，本次评测任务采用Align-smatch评测标准。各参赛队最终生成的CAMR中需包含概念对齐信息和关系对齐信息，最终成绩评分按照Align-smatch评测标准，取F值进行排名。表5为包含Test A和Test B的评分样例。其中，Smatch评分仅用于和其他语言的AMR解析进行对比，不计入最终排名。

<table align="center">
<p align="center">表5 评分样例</p>
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
    <td rowspan="4" align="center">Smatch (仅供参考)</td>
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
    <td rowspan="4">Align-smatch (主要指标)</td>
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


# 4 撰写技术报告
1.  报告可由中文或英文撰写。
2.  报告统一使用CCL 2023的<a href="http://cips-cl.org/static/CCL2023/downloads/ccl2023_template.zip">论文模板</a>。
3.  报告正文不得超过4页，参考文献页数不限。
4.  报告应至少包含以下四个部分：模型介绍、评测结果、结果分析与讨论和参考文献。


# 5 奖项设置
* 本次评测将设置一、二、三等奖，由中国中文信息学会为本次评测获奖队伍提供荣誉证书。
* 小牛公司为本次获奖队伍提供总价值1万元的奖金。

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
