import pickle
import json

pkl_file = open('name/data/genderdict.pkl', 'rb')
finalfullnamedict = pickle.load(pkl_file)
pkl_file.close()

def func(i):
    authors=[]
    try:
            n1=int(i.split('.')[2])
            n2=i.split('/')[1]  
            Jornal=''
            if i.find('AccelBeams') != -1:
                Jornal='PRAB'
            elif i.find('Applied') != -1:
                Jornal='PRAPPLIED'
            elif i.find('Fluids') != -1:
                Jornal='PRFLUIDS'
            elif i.find('Series') != -1:
                Jornal='PRI'
            elif i.find('EducRes') != -1:
                Jornal='PRPER'
            elif i.find('STAB') != -1:
                Jornal='PRSTAB'
            elif i.find('STPER') != -1:
                Jornal='PRSTPER'
            elif i.find('RevX') != -1:
                Jornal='PRX'
            elif i.find('Mod') != -1:
                Jornal='RMP'
            elif i.find('RevA') != -1:
                Jornal='PRA'
            elif i.find('RevB') != -1:
                Jornal='PRB'
            elif i.find('RevC') != -1:
                Jornal='PRC'
            elif i.find('RevD') != -1:
                Jornal='PRD'
            elif i.find('RevE') != -1:
                Jornal='PRE'
            elif i.find('Lett') != -1:  
                Jornal='PRL'
            else:
                Jornal='PR'
            with open("aps-dataset-metadata-2016/"+Jornal+"/"+str(n1)+"/"+n2+".json") as json_file:
                json_data1 = json.load(json_file)
            authorname=''
            if 'authors'in json_data1:
                s=json_data1.get('authors')
                for l in s:
                    if 'firstname' in l:
                        fi=l.get('firstname')
                        if fi.isspace() or fi=='':
                            authorname=authorname+'NON'
                        else:
                            authorname=authorname+fi
                    else:
                        authorname=authorname+'NON'
                    if 'surname' in l:
                        su=l.get('surname')
                        authorname=authorname+'+'+su
                    else:
                        authorname=authorname+'+'+'NON'
                    authors.append(authorname)

    except:
        pass
    return (authors)

import networkx as nx
with open("aps-dataset-citations.csv" , 'rb') as inf:
        next(inf, '')  
        G= nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), encoding="utf-8")

authors1=0   
authors2=0
manselfcite=0
womanselfcite=0
for j in G.edges():
    authors1=func(j[0])
    authors2=func(j[1])
    intersection=set(authors1).intersection(set(authors2))
    for i in list(intersection):
        gen=finalfullnamedict.get(i)
        if gen=='female':
            womanselfcite=womanselfcite+1
        elif gen=='male':
            manselfcite=manselfcite+1

print(manselfcite)
print(womanselfcite)  
print('kkk')  
