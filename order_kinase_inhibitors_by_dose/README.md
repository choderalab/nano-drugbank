## Analysis of the dose strength range of kinase inhibitors in DrugBank

We wanted to observe the range of single dose strength for kinase inhibitors listed in Drugbank.

#### Filtering criteria for drug enteries

- type: small molecule  
- group: approved   (Investigational drugs don't have dosage information.)  
- category: "Kinase Inhibitor" or "Protein Kinase Inhibitor"  

#### Analysis Instructions  
1. Download latest DrugBank Database v5.1.0 (released on 2018-04-02) in XML format from 
https://www.drugbank.ca/releases/5-1-0/downloads/all-full-database and rename the file as drugbank_20180402.xml

2. Run order_kinase_inhibitors_by_dose_strenght.ipynb  
 
