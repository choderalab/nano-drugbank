nano-drugbank
==============

Cheminformatic analysis of small molecule type drugs in DrugBank for their ability to form nanoparticles with indocyanine dyes. 

Related Publication
-------
Shamay, Y., Shah, J., Tschaharganeh, D. F., Roxbury, D., Budhathoki-Uprety, J., Işık, M., Mizrachi, A., Nawaly, K., Sugarman, J. L., Baut, E., Johnson, D. C., Sridharan, R., Neiman, M. R., Chu, K. L., Vinagolu, K. R., Chodera, J. D., Lowe, S. W., Heller, D. A. (2016) Quantitative Self-Assembly Prediction Yields Targeted Nanomedicines. Nature Methods. Manuscript submitted.

Author
-------
* Mehtap Işık | mehtap.isik@choderalab.org

Overview
-------
This repository contains analysis of small molecule drug entries in XML version of DrugBank Database Version 4.5.0 (released on 2016.04.20) to categorize predicted nanoparticle formation abilities according to the decision tree in publication above. SMILES, LogP, strongest acidic pKa and strongest basic pKa values were extracted from DrugBank DataBase. Number of High Intrinsic State Substructures (NHISS) is calculated as the total number of functional groups in a molecule with fluorine (-F) and double bonded oxygen (=O). Substructure search was performed for fluorine, carbonyl, nitro, nitroso, sulfinyl and sulfonyl functional groups on the SMILES strings of each DrugBank entry. Substructure search based on SMARTS was performed programmatically using OpenEYE OEChem Toolkit [45]. 

Steps of the analysis of drugs in DrugBank:

1. Downloading latest DrugBank Database (Released on Apr. 20th, 2016, XML format)  from http://www.drugbank.ca/releases/4-5-0/downloads/all-full-database and named drugbank_20160420.xml

2. Run IPython Notebook get_descriptors_from_drugbank_xml.ipynb

  Dependencies of this notebook:

* OpenEye OEChem library, version 2.0.5, OpenEye Scientific Software, Inc., Santa Fe, NM, USA, www.eyesopen.com, 2010.

* Python scripts: count_carbonyls.py, count_fluorines.py, count_sulfinyls.py, count_sulfonyls.py, count_nitroso.py, count_nitro.py

3. Run IPython Notebookdrugbank_decision_tree.ipynb

  Output: df_drugbank_decision_tree.csv (Group column represents which group of decision tree each small molecule drug is categorized to.)


