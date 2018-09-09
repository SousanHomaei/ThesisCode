import pickle
pkl_file = open('APSJournals/APSJournals-net/data/UniqueIndgrees.pkl', 'rb')
UniqueIndgrees = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('APSJournals/APSJournals-net/data/SB.pkl', 'rb')
SB = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('APSJournals/APSJournals-net/data/NB.pkl', 'rb')
NB = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('APSJournals/APSJournals-net/data/SA.pkl', 'rb')
SA = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('APSJournals/APSJournals-net/data/links.pkl', 'rb')
links = pickle.load(pkl_file)
pkl_file.close()

import networkx as nx
from collections import defaultdict
import math

def combination(n,x):
    return (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))

def PX(DI,X,NB,DJ):
    return (combination(DI,X)*combination(NB-DI,DJ-X))/(combination(NB,DJ))

def buildnet(k):
    M = []
    qs = []
    H = nx.DiGraph()
    H.add_edges_from(links[k])
    lenSA = len(SA[k])
    SAL=list(SA[k])
    for i in range(0, lenSA):
        for j in range(i + 1, lenSA):
            SAI = SAL[i]
            SAJ = SAL[j]
            NIJ = len(set(H.successors(SAI)).intersection(set(H.successors(SAJ))))
            if NIJ != 0:
                DI = H.out_degree(SAI)
                DJ = H.out_degree(SAJ)
                sum_ = 0
                for x in range(0, NIJ):
                    if (NB[k] - DI - DJ + x) > 0:
                        sum_ = sum_ + PX(DI, x, NB[k], DJ)
                if sum_ != 0:
                    q = 1 - (sum_)
                    M.append(tuple([SAI, SAJ, q]))
                    qs.append(q)
    # M[I,J] is qij(k)
    output = open('APSJournals/APSJournals-net/data/qij' + str(k) + '.pkl', 'wb')
    pickle.dump(M, output)
    output.close()

    # qs is the list of P-values of tests(qij(k))
    output = open('APSJournals/APSJournals-net/data/q' + str(k) + '.pkl', 'wb')
    pickle.dump(qs, output)
    output.close()
    print(k)

from multiprocessing import Pool

U=list(UniqueIndgrees)
if __name__ == '__main__':
    with Pool(8) as p:
        p.map(buildnet, U[:50])
    with Pool(8) as p:
        p.map(buildnet, U[50:])
