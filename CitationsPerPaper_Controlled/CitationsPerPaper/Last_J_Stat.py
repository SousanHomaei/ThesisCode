import networkx as nx
import pickle
import json

with open("aps-dataset-citations.csv" , 'rb') as inf:
        next(inf, '')  
        G= nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), encoding="utf-8")

pkl_file = open('APSJournals/APSJournals-net/data/LastAllJournals.pkl', 'rb')
firstpairs = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/data/genderdict.pkl', 'rb')
genderdict = pickle.load(pkl_file)
pkl_file.close()

def funname(i):
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
                if 'firstname' in s[0]:
                    fi=s[0].get('firstname')
                    su=s[0].get('surname')
            return(genderdict.get(fi+'+'+su))
    except:
            return('')

cicoF=[]
citerFF=0
citerMF=0
cicoM=[]
citerMM=0
citerFM=0

for i in firstpairs:
    g=funname(i[0])
    if g=='female':
        cicoF.append(G.in_degree(i[0]))
        for j in G.predecessors(i[0]):
            ge=funname(j)
            if ge=='female':
                citerFF=citerFF+1
            elif ge =='male':
                citerMF=citerMF+1
    elif g=='male':
        cicoM.append(G.in_degree(i[0]))
        for j in G.predecessors(i[0]):
            ge=funname(j)
            if ge=='female':
                citerFM=citerFM+1
            elif ge =='male': 
                citerMM=citerMM+1

        
    g=funname(i[1])
    if g=='female':
        cicoF.append(G.in_degree(i[1]))
        for j in G.predecessors(i[1]):
            ge=funname(j)
            if ge=='female':
                citerFF=citerFF+1
            elif ge =='male':
                citerMF=citerMF+1
    elif g=='male':
        cicoM.append(G.in_degree(i[1]))
        for j in G.predecessors(i[1]):
            ge=funname(j)
            if ge=='female':
                citerFM=citerFM+1
            elif ge =='male': 
                citerMM=citerMM+1

citer = []    
citer.append(citerFF)
citer.append(citerMF)
citer.append(citerMM)
citer.append(citerFM)


output = open('APSJournals/APSJournals-net/data/cicoFAJLast.pkl', 'wb')
pickle.dump(cicoF, output)
output.close()

output = open('APSJournals/APSJournals-net/data/cicoMAJLast.pkl', 'wb')
pickle.dump(cicoM, output)
output.close()

output = open('APSJournals/APSJournals-net/data/citerAJLast.pkl', 'wb')
pickle.dump(citer, output)
output.close()





