
import pickle
import json
import datetime

pkl_file = open('APSJournals/APSJournals-net/data/ToMaleLast.pkl', 'rb')
ToFemale = pickle.load(pkl_file)
pkl_file.close()

pkl_file = open('name/data/genderdict.pkl', 'rb')
genderdict = pickle.load(pkl_file)
pkl_file.close()

def timediff(d1,d2):
    try:
        format_str = '%Y-%m-%d' # The format
        t1 = datetime.datetime.strptime(d1, format_str)
        t2 = datetime.datetime.strptime(d2, format_str)
        if (t2 - t1).days<356:
            return('y')
    except:
        return('n')

def fundate(i):
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
                return(json_data1.get('date'))
                
    except:
            return('')
    

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
                fi=s[-1].get('firstname')
                su=s[-1].get('surname')
            return(genderdict.get(fi+'+'+su))
    except:
            return('')
    
            
               
lastprl=[]
for j in ToFemale:
     if j[2]<0.01 :
              if j[0].find('Mod') != -1 and j[1].find('Mod') != -1: 
                       if funname(j[0])=='female':
                            d1=fundate(j[0])
                            d2=fundate(j[1])
                            if timediff(d1,d2)=='y':
                                    lastprl.append((j[0],j[1]))


pkl_file = open('APSJournals/APSJournals-net/data/ToFemaleLast.pkl', 'rb')
ToFemale = pickle.load(pkl_file)
pkl_file.close()

for j in ToFemale:
     if j[2]<0.01 :
              if j[0].find('Mod') != -1 and j[1].find('Mod') != -1: 
                       if funname(j[0])=='male':
                            d1=fundate(j[0])
                            d2=fundate(j[1])
                            if timediff(d1,d2)=='y':
                                    lastprl.append((j[0],j[1]))
                                    
                                                                
output = open('APSJournals/APSJournals-net/data/Last-Mod.pkl', 'wb')
pickle.dump(lastprl, output)
output.close()
