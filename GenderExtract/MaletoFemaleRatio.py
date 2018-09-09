import os
import json
from collections import defaultdict
import networkx as nx
import pickle

pkl_file = open('name/data/genderdict.pkl', 'rb')
namedict = pickle.load(pkl_file)
pkl_file.close()

def funcol(J):
    S = defaultdict(list)
    for root, dirs, files in os.walk('aps-dataset-metadata-2016/'+J):
         for name in files:
            try:
                 if name.endswith((".json")):
                    with open(os.path.join(root,name), 'r') as f:
                        data = json.load(f)
                        date=data.get('date')
                        if 'authors'in data:
                            s=data.get('authors')
                            firstlist=[]
                            lastlist=[]
                            fulllist=[]
                            for i in range(0,len(s)):
                                if 'firstname' in s[i]:
                                    fi=s[i].get('firstname')
                                    if fi.isspace() or fi=='':
                                            firstlist.append('NNN')
                                    else:
                                        firstlist.append(fi)
                                else: 
                                    firstlist.append('NNN')
                                if 'surname' in s[i]:
                                    su=s[i].get('surname')
                                    if su:
                                        lastlist.append(su)
                                    else:
                                        lastlist.append('NNN')
                                else: 
                                    lastlist.append('NNN')
                            for w in range(0,len(lastlist)):
                                fulllist.append(firstlist[w]+'+'+lastlist[w])
                            
                            if date<="1975-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1975].append((fulllist[h],fulllist[l]))

                            if date<="1980-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1980].append((fulllist[h],fulllist[l]))

                            if date<="1985-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1985].append((fulllist[h],fulllist[l]))

                            if date<="1990-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1990].append((fulllist[h],fulllist[l]))
                                            
                            if date<="1995-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[1995].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2000-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2000].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2005-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2005].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2010-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2010].append((fulllist[h],fulllist[l]))
                                            
                            if date<="2017-00-00":
                                for h in range (0,len(fulllist)):
                                    for l in range (h+1,len(fulllist)):
                                            S[2016].append((fulllist[h],fulllist[l]))
            except :
                continue
    return S

collaborationlist=defaultdict(list)
from multiprocessing import Pool
with Pool(8) as p:
        n=p.map(funcol,['PRAB','PRAPPLIED','PRFLUIDS','PRI','PRPER','PRSTAB','PRSTPER','PRX','RMP','PRA','PRB','PRC','PRD','PRE','PRL','PR'])   

for i in n:
        for j in [1975,1980,1985,1990,1995,2000,2005,2010,2016]:
            if j in i.keys():
                collaborationlist[j]=collaborationlist[j]+i.get(j)
        
def per5year(year):
    G=nx.Graph()
    G.add_edges_from(collaborationlist[year])

    for i in G.nodes():
        G.node[i]['gender']=namedict.get(i)

    NumF=0
    NumM=0
    unknown=0
    for i in G.nodes():
        if  G.node[i]['gender']=='female':
            NumF=NumF+1
        elif  G.node[i]['gender']=='male':
            NumM=NumM+1
        else:
            unknown=unknown+1

    return (year,G.number_of_nodes(),unknown,NumF,NumM,NumM/NumF)

MaleToFemaleRatio=[]
for i in collaborationlist.keys():
    MaleToFemaleRatio.append(per5year(i))

output = open('CollaborationProject/data/MaleToFemaleRatio.pkl', 'wb')
pickle.dump(MaleToFemaleRatio, output)
output.close()
