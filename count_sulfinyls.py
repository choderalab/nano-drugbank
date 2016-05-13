from __future__ import print_function

__author__ = 'isikm'

import pandas as pd
from openeye import oechem, oedepict

df_drugbank_smiles=pd.DataFrame.from_csv('df_drugbank_smiles.csv', encoding='utf-8')

# Count number of sulfinyl groups in each row using SMARTS matching
for i, row in enumerate(df_drugbank_smiles.iterrows()):
    smiles = df_drugbank_smiles.loc[i,"smiles"]
    mol = oechem.OEGraphMol()
    oechem.OESmilesToMol(mol, str(smiles))

    # create a substructure search object
    queried_substructure="[SX3](=O)(*)*"
    ss = oechem.OESubSearch(queried_substructure)
    oechem.OEPrepareSearch(mol, ss)

    # loop over matches to count
    matched_ss_list=[]
    count=0
    for index, match in enumerate(ss.Match(mol)):
        if ss.SingleMatch(mol) == True:
            matched_ss_list.append((index, match))
            count = len(matched_ss_list)
            # print(count, match)

    # add number of matches to dataframe
    df_drugbank_smiles.loc[i,"sulfinyl"] = count

#write to csv
df_drugbank_smiles.to_csv("df_drugbank_smiles.csv", encoding='utf-8')

print("Done.")