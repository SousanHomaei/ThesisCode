import os
import json
import pickle

pkl_file = open('name/data/genderdict.pkl', 'rb')
genderdict = pickle.load(pkl_file)
pkl_file.close()

from collections import defaultdict

import networkx as nx
with open("aps-dataset-citations.csv" , 'rb') as inf:
        next(inf, '')  
        G= nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), encoding="utf-8")

def DegDate():
    dates = defaultdict(list)
    degrees=defaultdict(list)
    for root, dirs, files in os.walk('aps-dataset-metadata-2016'):
         for name in files:
            try:
                 if name.endswith((".json")):
                    with open(os.path.join(root,name), 'r') as f:
                        data = json.load(f)
                        s=data.get('authors')
                        for i in range(0,len(s)):
                                try:
                                    fi=s[i].get('firstname')
                                    su=s[i].get('surname')
                                
                                    f=fi+'+'+su
                                    if f in genderdict.keys():  
                                        dates[f].append(data.get('date'))
                                        degrees[f].append(G.in_degree(data.get('id')))
                                except:
                                    continue
                                            
            except :
                continue
    return (dates,degrees)

dates,degrees=DegDate()   

output = open('APSJournals/APSJournals-net/data/dates.pkl', 'wb')
pickle.dump(dates, output)
output.close()

output = open('APSJournals/APSJournals-net/data/degrees.pkl', 'wb')
pickle.dump(degrees, output)
output.close()
