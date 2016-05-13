from __future__ import print_function

__author__ = 'isikm'

import pandas as pd
import numpy as np
import os
from openeye import oechem, oedepict


df_drugbank_smiles=pd.DataFrame.from_csv('df_drugbank_smiles.csv', encoding='utf-8')

# Counting tertiarry amine groups in each row using SMARTS matching
for i, row in enumerate(df_drugbank_smiles.iterrows()):
    smiles = df_drugbank_smiles.loc[i,"smiles"]
    mol = oechem.OEGraphMol()
    oechem.OESmilesToMol(mol, str(smiles))

    #create a substructure search object - neutral tertiary amine
    queried_substructure="[NX3]([C,c])([C,c])[C,c]"
    ss = oechem.OESubSearch(queried_substructure)
    oechem.OEPrepareSearch(mol, ss)

    # loop over matches to count
    matched_ss_list=[]
    count=0
    for index, match in enumerate(ss.Match(mol, True)):
       if ss.SingleMatch(mol) == True:
           matched_ss_list.append((index, match))
           count = len(matched_ss_list)

    neutral_tertiary_amine_count=count

    # Count number of aromatic carbonyls in each row using SMARTS matching

    #create a substructure search object - protonated tertiary amine or quaternary amine
    queried_substructure="[NX4+1]([C,c])([C,c])([C,c])[C,c,H]"
    ss2 = oechem.OESubSearch(queried_substructure)
    oechem.OEPrepareSearch(mol, ss2)

    # loop over matches to count
    matched_ss2_list=[]
    count=0
    for index, match in enumerate(ss2.Match(mol, True)):
        if ss2.SingleMatch(mol) == True:
            matched_ss2_list.append((index, match))
            count = len(matched_ss2_list)

    quaternary_amine_count=count

    # Total number of tertiary amine
    total_tert_amine_count = neutral_tertiary_amine_count + quaternary_amine_count

    # add number of matches to dataframe
    df_drugbank_smiles.loc[i,"tert-amine"] = total_tert_amine_count

#write to csv
df_drugbank_smiles.to_csv("df_drugbank_smiles.csv", encoding='utf-8')

print("Worked!")
