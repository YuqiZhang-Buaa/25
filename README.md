# A Scalable Multiple Instance Learning Framework for Computational Pathology
Continuous updating.
## A. Additional Method Detail
### Figure 1. A lightweight feature fusion block.
<img src="fig/1.png" alt="A lightweight feature fusion block." style="height: 300px;">

## B. Dataset Descript
The details of all datasets are shown in Table 1. Each dataset contains WSIs of different sizes.
### Table 1. Details of all datasets.
|| BRACS |TCGA-NSCLC |CAMELYON-16|LUAD|LUSC|
| --- | --- | --- | --- | --- | --- |
|Sample| 537|1053 | 395 |541|512|
|Min Image Size|17135 $\times$ 11733| 10000 $\times$ 4617 |45056 $\times$ 35840|10000 $\times$ 4617|7995 $\times$ 7522|
|Max Image Size|181272 $\times$ 88334|191352 $\times$ 97078 |217088 $\times$ 111104|191352 $\times$ 97078|193223 $\times$ 90994|
|Min Bag Size|46| 35 |40 |35|41|
|Max Bag Size|7728 | 11747 |11221 |11747|11133|
### Cancer Diagnosis and Sub-typing Datasets
#### 1. BRACS
BRACS is a WSI dataset for breast cancer sub-typing that contains a total of 537 WSIs. It has seven subtypes, specifically: 40 normal (glandular tissue samples without lesions) WSIs, 145 pathologically benign (PB) WSIs, 70 ordinary ductal hyperplasia (UDH) WSIs, 41 flat epithelial atypical hyperplasia (FEA) WSIs, 48 atypical ductal hyperplasia (ADH) WSIs, 61 ductal carcinoma in situ (DCIS) WSIs, and 132 invasive carcinoma (IC) WSIs.
#### 2. TCGA-NSCLC
TCGA-NSCLC derived from The Cancer Genome Atlas Program (TCGA) is a WSI dataset for lung cancer sub-typing. It includes two subtypes: 512 lung squamous cell carcinoma (LUSC) WSIs and 541 lung adenocarcinoma (LUAD) WSIs.
#### 3. CAMELYON-16
CAMELYON-16 is a WSI dataset for the diagnosis of breast cancer metastasis. A total of 395 WSIs are included. It contains 236 normal WSIs and 159 tumor WSIs.
### Survival Prediction Datasets
#### 1. TCGA-LUAD
TCGA-LUAD derived from the TCGA, is a WSI dataset for cancer survival prediction. It included 541 cases of LUAD WSIs, and survival time and censoring indicator corresponding to each WSI.
#### 2. TCGA-LUSC
TCGA-LUSC derived from the TCGA, is a WSI dataset for cancer survival prediction. It included 512 cases of LUSC WSIs, and survival time and censoring indicator corresponding to each WSI.
## C. Cancer diagnosis results of CAMELYON-16
### Table 2. Cancer diagnosis results of CAMELYON-16.
| Method       | AUC          | ACC          | F1 Score     |
|--------------|--------------|--------------|--------------|
| Max Pooling  | 0.7748±0.103 | 0.7375±0.103 | 0.6450±0.104 |
| Mean Pooling | 0.7437±0.037 | 0.7042±0.027 | 0.5604±0.045 |
| ABMIL        | 0.8073±0.047 | 0.7564±0.052 | 0.6624±0.063 |
| CLAM         | 0.8097±0.045 | 0.7470±0.027 | 0.6592±0.054 |
| TransMIL     | <u>0.8159±0.092<u> | 0.7631±0.062 | 0.6641±0.125 |
| S4MIL        | 0.8053±0.069 | 0.7511±0.050 | 0.6467±0.095 |
| MambaMIL     | 0.7309±0.111 | 0.6923±0.151 | 0.5834±0.136 |
| RRTMIL       | 0.8104±0.047 | 0.7621±0.044 | 0.6635±0.045 |
| LongMIL      | 0.7562±0.106 | 0.4105±0.126 | 0.3168±0.185 |
| Our Model    | **0.8196±0.038** | **0.7668±0.024** | **0.6703±0.041** |


