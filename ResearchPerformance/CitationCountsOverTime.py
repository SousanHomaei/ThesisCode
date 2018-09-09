
import pickle

pkl_file = open('APSJournals/APSJournals-net/data/da.pkl', 'rb')
dates = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('APSJournals/APSJournals-net/data/deg.pkl', 'rb')
deg = pickle.load(pkl_file)
pkl_file.close()

from collections import defaultdict

degovertime = defaultdict(dict)

for i in dates.keys():
    d=dates.get(i)
    if d[0]<="1970-00-00":
           degovertime['1970'][i]=(deg.get(i))
    if "1970-00-00"<d[0]<="1975-00-00":
           degovertime['1975'][i]=(deg.get(i))
    if "1975-00-00"<d[0]<="1980-00-00":
           degovertime['1980'][i]=(deg.get(i))
    if "1980-00-00"<d[0]<="1985-00-00":
           degovertime['1985'][i]=(deg.get(i))
    if "1985-00-00"<d[0]<="1990-00-00":
           degovertime['1990'][i]=(deg.get(i)) 
    if "1990-00-00"<d[0]<="1995-00-00":
           degovertime['1995'][i]=(deg.get(i)) 
    if "1995-00-00"<d[0]<="2000-00-00":
           degovertime['2000'][i]=(deg.get(i)) 
    if "2000-00-00"<d[0]<="2005-00-00":
           degovertime['2005'][i]=(deg.get(i))
    if "2005-00-00"<d[0]<="2010-00-00":
           degovertime['2010'][i]=(deg.get(i))
    if "2010-00-00"<d[0]:
           degovertime['2016'][i]=(deg.get(i))
            
output = open('APSJournals/APSJournals-net/data/degovertime.pkl', 'wb')
pickle.dump(degovertime, output)
output.close()

