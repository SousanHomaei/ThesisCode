
import pickle

pkl_file = open('APSJournals/APSJournals-net/data/dates.pkl', 'rb')
dates = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('APSJournals/APSJournals-net/data/degrees.pkl', 'rb')
degrees = pickle.load(pkl_file)
pkl_file.close()

from collections import defaultdict

da = defaultdict(list)
deg={}
num={}
pp={}

for i in dates.keys():
    d=dates.get(i)
    num[i]=len(d)
    da[i].append(min(d))
    da[i].append(max(d))    
    
for i in degrees.keys():
    s=0
    for j in degrees.get(i):
        if type(j)==int:
            s=s+j
    deg[i]=s
    
for i in degrees.keys():
    pp[i]=deg.get(i)/num.get(i)

output = open('APSJournals/APSJournals-net/data/da.pkl', 'wb')
pickle.dump(da, output)
output.close()

output = open('APSJournals/APSJournals-net/data/deg.pkl', 'wb')
pickle.dump(deg, output)
output.close()

output = open('APSJournals/APSJournals-net/data/num.pkl', 'wb')
pickle.dump(num, output)
output.close()

output = open('APSJournals/APSJournals-net/data/pp.pkl', 'wb')
pickle.dump(pp, output)
output.close()

