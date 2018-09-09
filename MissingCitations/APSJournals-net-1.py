import networkx as nx
from collections import defaultdict

with open("aps-dataset-citations.csv", 'rb') as inf:
    next(inf, '')
    G = nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), encoding="utf-8")

indgree=G.in_degree()
UniqueIndgrees = set(indgree.values())
UniqueIndgrees.remove(0)
UniqueIndgrees.remove(1)

SB = defaultdict(list)
for i in G.nodes():
    j=indgree.get(i)
    SB[j].append(i)

NB=dict.fromkeys(SB)
for i in SB.keys():
    NB[i]=len(SB[i])

SA = defaultdict(list)
links = defaultdict(list)
def SaALinks(k):
    for i in SB[k]:
        pre=G.predecessors(i)
        SA[k]=SA[k]+pre
        for j in pre:
            links[k].append((j,i))
    SA[k]=set(SA[k])
for k in UniqueIndgrees:
    SaALinks(k)

import pickle
output = open('APSJournals/APSJournals-net/data/UniqueIndgrees.pkl', 'wb')
pickle.dump(UniqueIndgrees, output)
output.close()

output = open('APSJournals/APSJournals-net/data/SB.pkl', 'wb')
pickle.dump(SB, output)
output.close()

output = open('APSJournals/APSJournals-net/data/NB.pkl', 'wb')
pickle.dump(NB, output)
output.close()

output = open('APSJournals/APSJournals-net/data/SA.pkl', 'wb')
pickle.dump(SA, output)
output.close()

output = open('APSJournals/APSJournals-net/data/links.pkl', 'wb')
pickle.dump(links, output)
output.close()

