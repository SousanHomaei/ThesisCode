import pickle
pkl_file = open('name/data/genderdict.pkl', 'rb')
genderdict = pickle.load(pkl_file)
pkl_file.close()

import os
import json

def FLD(J):
    first={}

    for root, dirs, files in os.walk('aps-dataset-metadata-2016/'+J):
        for name in files:
                if name.endswith((".json")):
                        try:
                            with open(os.path.join(root,name), 'r') as f:
                                    data = json.load(f)
                                    authorname=''
                                    s=data.get('authors')
                                
                                    fi=s[0].get('firstname')
                                    authorname=authorname+fi
                                    su=s[0].get('surname')
                                    authorname=authorname+'+'+su
                                    if genderdict.get(authorname)=='female':
                                        first[data.get('id')] = 'f'
                                    elif genderdict.get(authorname)=='male':
                                        first[data.get('id')] = 'm'
                                    
                        except:
                                continue
    return (first)                         

from multiprocessing import Pool
with Pool(8) as p:
        n=p.map(FLD,['PRAB','PRAPPLIED','PRFLUIDS','PRI','PRPER','PRSTAB','PRSTPER','PRX','RMP','PRA','PRB','PRC','PRD','PRE','PRL','PR'])                               
first={}

for i in n:
    first.update(i)
        
output = open('CitationPerPaper/Data/firstgenderpaper.pkl', 'wb')
pickle.dump(first, output)
output.close()                            
