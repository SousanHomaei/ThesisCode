import pandas as pd
dff=pd.read_csv('name/data/firstname.csv',sep="\n",names=['firstname'])
dfl=pd.read_csv('name/data/lastname.csv',sep="\n",names=['lastname'])
firstlist=dff['firstname'].tolist()
lastlist=dfl['lastname'].tolist()
# making full name from first name and surename if there is first name
fullnamelist=[]
for i in range(0,len(firstlist)):
    if firstlist[i]!='NON':
        fullnamelist.append(firstlist[i]+'+'+lastlist[i])
# set of people (Uniqe full names)
setfullnamelist=set(fullnamelist)
import pickle
pkl_file = open('name/data/namedict.pkl', 'rb')
namedict = pickle.load(pkl_file)
pkl_file.close()

# fullnamedict : keys are fullnames and values are extracted genders (male,female) using genderize based on first names
# keys : fullnames, values:female or male for example  'James+Chen': 'male'

setfullnamelist=list(setfullnamelist)
fullnamedict = {}
# z is number of full names that their gender can't be extracted. Their first names can't be recognized because
# they are initials
z=0
NotInitial=[]
for i in range(0,len(setfullnamelist)):
    f=setfullnamelist[i].split('+')[0]
    b=[]
    fnsplit=f.split()
    for j in range(0,len(fnsplit)):
            if fnsplit[j].find('.')== -1 :
                b.append(fnsplit[j])
    for k in range(0,len(b)):
        if b[k].find('-') !=-1:
                fnsplit2=b[k].split('-')
                for h in range(0,len(fnsplit2)):
                            b.append(fnsplit2[h])
    if len(b)==0:
        z=z+1
    else:
        NotInitial.append(setfullnamelist[i])
    for n in range(0,len(b)):
        g=namedict.get(b[n])
        if g=='male':
            fullnamedict[setfullnamelist[i]] = g
            break
        if g=='female':
            fullnamedict[setfullnamelist[i]] = g
            break

# Fullnames whose genders aren't recognized by genderize
FacePP=list(set(NotInitial)-set(fullnamedict.keys()))
import pickle
output = open('name/data/fullnamedict.pkl', 'wb')
pickle.dump(fullnamedict, output)
output.close()
output = open('name/data/FacePP.pkl', 'wb')
pickle.dump(FacePP, output)
output.close()

print("Not initials:")
print("   Uniqe fullnames:"+str(len(setfullnamelist)-z))
print("   Uniqe fullnames whose genders are extracted using genderize:"+str(len(fullnamedict)))
print("   Percentage of uniqe fullnames whose genders are recognized using genderize:"+str(len(fullnamedict)/len(setfullnamelist)-z))
print("Not initials and initials:")
print("   Percentage of uniqe fullnames whose genders are recognized using genderize:"+str(len(fullnamedict)/len(setfullnamelist)))
