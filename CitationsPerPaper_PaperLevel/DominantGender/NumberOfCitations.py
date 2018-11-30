import networkx as nx
with open("aps-dataset-citations.csv" , 'rb') as inf:
        next(inf, '')  
        G= nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), encoding="utf-8")         

degree={}        
for i in G.nodes():
    ind=G.in_degree(i)
    if type(ind) == int:    
        degree[i] = ind

import pickle        
output = open('CitationPerPaper/Data/degree.pkl', 'wb')
pickle.dump(degree, output)
output.close()        
        
       
