import pickle
    
pkl_file = open('CitationPerPaper/Data/firstgenderpaper.pkl', 'rb')
first = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('CitationPerPaper/Data/lastgenderpaper.pkl', 'rb')
last = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('CitationPerPaper/Data/dominatedpaper.pkl', 'rb')
dominated = pickle.load(pkl_file)
pkl_file.close()

import networkx as nx
with open("aps-dataset-citations.csv" , 'rb') as inf:
        next(inf, '')  
        G= nx.read_edgelist(inf, delimiter=',', create_using=nx.DiGraph(), encoding="utf-8")         
        

degreefemalefirst=[]
degreemalefirst=[]

for i,v in first.items():
    if type(G.in_degree(i)) == int:    
        if first.get(i)=='f':
            degreefemalefirst.append(G.in_degree(i))
        elif first.get(i)=='m':
            degreemalefirst.append(G.in_degree(i))
        
output = open('CitationPerPaper/Data/degreefemalefirst.pkl', 'wb')
pickle.dump(degreefemalefirst, output)
output.close()

output = open('CitationPerPaper/Data/degreemalefirst.pkl', 'wb')
pickle.dump(degreemalefirst, output)
output.close()
        
        
degreefemalelast=[]
degreemalelast=[]

for i,v in last.items():
    if type(G.in_degree(i)) == int:    
        if last.get(i)=='f':
            degreefemalelast.append(G.in_degree(i))
        elif last.get(i)=='m':
            degreemalelast.append(G.in_degree(i))

output = open('CitationPerPaper/Data/degreefemalelast.pkl', 'wb')
pickle.dump(degreefemalelast, output)
output.close() 

output = open('CitationPerPaper/Data/degreemalelast.pkl', 'wb')
pickle.dump(degreemalelast, output)
output.close() 

degreefemaledominated=[]
degreemaledominated=[]

for i,v in dominated.items():
     if type(G.in_degree(i)) == int:    
        if dominated.get(i)=='f':
            degreefemaledominated.append(G.in_degree(i))
        elif dominated.get(i)=='m':
            degreemaledominated.append(G.in_degree(i))

output = open('CitationPerPaper/Data/degreefemaledominated.pkl', 'wb')
pickle.dump(degreefemaledominated, output)
output.close()

output = open('CitationPerPaper/Data/degreemaledominated.pkl', 'wb')
pickle.dump(degreemaledominated, output)
output.close()
        
