import pickle
import json
def fundate(i):
        try :
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
            date=''
            with open("aps-dataset-metadata-2016/"+Jornal+"/"+str(n1)+"/"+n2+".json") as json_file:
                    json_data1 = json.load(json_file)
                    date=json_data1.get('date')
        except:
            date='N'
        return date

def fungender(i):
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
                    if fi.isspace() or fi=='':
                        authorname=authorname+'NON'
                    else:
                        authorname=authorname+fi
                else:
                    authorname=authorname+'NON'
                if 'surname' in s[0]:
                    su=s[0].get('surname')
                    authorname=authorname+'+'+su
                else:
                    authorname=authorname+'+'+'NON'
            return(finalfullnamedict.get(authorname))
        except:
            return 'N'

            
pkl_file = open('APSJournals/APSJournals-net/data/UniqueIndgrees.pkl', 'rb')
UniqueIndgrees = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/data/genderdict.pkl', 'rb')
finalfullnamedict = pickle.load(pkl_file)
pkl_file.close()

U=list(UniqueIndgrees)
ToMale=[]

from multiprocessing import Pool

def funtm(i):
        TM=[]
        pkl_file = open('APSJournals/APSJournals-net/data/qij'+str(i)+'.pkl', 'rb')
        qij = pickle.load(pkl_file)
        pkl_file.close()
        for j in qij:
            date0=fundate(j[0])
            date1=fundate(j[1])
            if date0!='N' and date1!='N':
                if date0 < date1: 
                    g=fungender(j[0])
                    if g=='male':
                        TM.append((j[1],j[0],j[2]))
                else:
                    g=fungender(j[1])
                    if g=='male':
                        TM.append((j[0],j[1],j[2]))
        return TM
    
with Pool(8) as p:
        n=p.map(funtm,U)    
for i in n:
    ToMale=ToMale+i

output = open('APSJournals/APSJournals-net/data/ToMale.pkl', 'wb')
pickle.dump(ToMale, output)
output.close()
    
