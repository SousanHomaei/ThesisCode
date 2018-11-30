import pickle
pkl_file = open('name/data/genderdict.pkl', 'rb')
genderdict = pickle.load(pkl_file)
pkl_file.close()

import os
import json

def FLD(J):
    last={}
    for root, dirs, files in os.walk('aps-dataset-metadata-2016/'+J):
        for name in files:
                if name.endswith((".json")):
                        try:
                            with open(os.path.join(root,name), 'r') as f:
                                    data = json.load(f)
                                    authorname=''
                                    s=data.get('authors')
                                    
                                    fi=s[-1].get('firstname')
                                    authorname=authorname+fi
                                    su=s[-1].get('surname')
                                    authorname=authorname+'+'+su
                                    if genderdict.get(authorname)=='female':
                                        last[data.get('id')] = 'f'
                                    elif genderdict.get(authorname)=='male':
                                        last[data.get('id')] = 'm'
                                    
                        except:
                                continue
    return (last)                         

from multiprocessing import Pool
with Pool(8) as p:
        n=p.map(FLD,['PRAB','PRAPPLIED','PRFLUIDS','PRI','PRPER','PRSTAB','PRSTPER','PRX','RMP','PRA','PRB','PRC','PRD','PRE','PRL','PR'])                               
last={}

for i in n:
    last.update(i)

output = open('CitationPerPaper/Data/lastgenderpaper.pkl', 'wb')
pickle.dump(last, output)
output.close()                            
