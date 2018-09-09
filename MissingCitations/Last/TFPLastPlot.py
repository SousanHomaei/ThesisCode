
import networkx as nx
import pickle
with open("aps-dataset-citations.csv" , 'rb') as inf:
        next(inf, '')  
        G= nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), encoding="utf-8")

pkl_file = open('APSJournals/APSJournals-net/data/ToFemaleLast.pkl', 'rb')
ToFemale = pickle.load(pkl_file)
pkl_file.close()

Th = []
Th.append(0.01)
Th.append(0.001)
Th.append(0.0001)
Th.append(0.00001)
Th.append(0.000001)
Th.append(0.0000001)
Th.append(0.00000001)
Th.append(0.000000001)
Th.append(0.0000000001)
Th.append(0.00000000001)
Th.append(0.000000000001)
Th.append(0.0000000000001)
Th.append(0.00000000000001)
Th.append(0.000000000000001)
Th.append(0.0000000000000001)
Th.append(0.00000000000000001)


def fun(Threshold):
    ValidPairs=[]
    for j in ToFemale:
            if j[2]<Threshold :
                    ValidPairs.append(tuple([j[0],j[1]])) 
                    ValidPairs=set(ValidPairs)
                    ValidPairs=list(ValidPairs)

    l=len(ValidPairs)
    j=0
    for i in ValidPairs:
        if i[0] in G.predecessors(i[1]):
            j=j+1
    if l!=0:
        return (j/l)
    else:
        return 0
        
from multiprocessing import Pool
with Pool(3) as p:
        n=p.map(fun,Th) 

output = open('APSJournals/APSJournals-net/data/TFPLastPlot.pkl', 'wb')
pickle.dump(n, output)
output.close()
