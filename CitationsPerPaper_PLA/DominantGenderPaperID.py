import pickle
pkl_file = open('name/data/genderdict.pkl', 'rb')
genderdict = pickle.load(pkl_file)
pkl_file.close()

import os
import json

def FLD(J):
    
    dominated={}

    for root, dirs, files in os.walk('aps-dataset-metadata-2016/'+J):
        for name in files:
                if name.endswith((".json")):
                        try:
                            with open(os.path.join(root,name), 'r') as f:
                                    data = json.load(f)
                                    authorname=''
                                    s=data.get('authors')
                                
                                    NumFemale=0
                                    NumMale=0
                                    for i in s:
                                        fi=i.get('firstname')
                                        authorname=authorname+fi
                                        su=i.get('surname')
                                        authorname=authorname+'+'+su
                                        if genderdict.get(authorname)=='female':
                                            NumFemale=NumFemale+1
                                        elif genderdict.get(authorname)=='male':
                                            NumMale=NumMale+1
                                        if (NumMale+NumFemale) == len(s):
                                            if (NumFemale/len(s))> 0.5:
                                                dominated[data.get('id')] = 'f'
                                            else:
                                                dominated[data.get('id')] = 'm'
                                
                        except:
                                continue
    return (dominated)                         

from multiprocessing import Pool
with Pool(8) as p:
        n=p.map(FLD,['PRAB','PRAPPLIED','PRFLUIDS','PRI','PRPER','PRSTAB','PRSTPER','PRX','RMP','PRA','PRB','PRC','PRD','PRE','PRL','PR'])                               
dominated={}

for i in n:
    dominated.update(i)

output = open('CitationPerPaper/Data/dominatedpaper.pkl', 'wb')
pickle.dump(dominated, output)
output.close()                            
