# extracting first names and last names of authors.

import os
import json
import csv

firstname = "name/data/firstname.csv"
lastname = "name/data/lastname.csv"

with open(firstname, "w") as outputfirst:
    with open(lastname, "w") as outputlast:
        for root, dirs, files in os.walk('aps-dataset-metadata-2016'):
            for name in files:
                 if name.endswith((".json")):
                    with open(os.path.join(root,name), 'r') as f:
                        data = json.load(f)
                        if 'authors'in data:
                            s=data.get('authors')
                            for i in range(0,len(s)):
                                if 'firstname' in s[i]:
                                    fi=s[i].get('firstname')
                                    if fi.isspace() or fi=='':
                                            outputfirst.write('NON' + '\n')
                                    else:
                                            outputfirst.write(fi + '\n')
                                else:
                                    outputfirst.write('NON' + '\n')
                                if 'surname' in s[i]:
                                    su=s[i].get('surname')
                                    outputlast.write(su + '\n')
                                else:
                                    outputlast.write('NON' + '\n')

import pandas as pd
dff=pd.read_csv('name/data/firstname.csv',sep="\n")
dfl=pd.read_csv('name/data/lastname.csv',sep="\n")

firstlist=dff['firstname'].tolist()

firstlist2=[]
for i in range(0,len(firstlist)):
    if firstlist[i]!='NON':
        firstlist2.append(firstlist[i])

setfirstlist2=set(firstlist2)

firstlist=list(setfirstlist2)
GenderizeInput=[]
for i in range(0,len(firstlist)):
    f=firstlist[i].split('+')[0]
    fnsplit=f.split()
    for j in range(0,len(fnsplit)):
            if fnsplit[j].find('.')== -1 :
                if fnsplit[j].find('-')== -1 :
                        GenderizeInput.append(fnsplit[j])
                else:
                        fnsplit2=fnsplit[j].split('-')
                        for h in range(0,len(fnsplit2)):
                            GenderizeInput.append(fnsplit2[h])

import pandas as pd
import sys
from genderize import Genderize
import time


# Genderize client can be downloaded from:
# https://pypi.python.org/pypi/Genderize

# TIPS:
# 1. Remove all names that are just initials
# 2. Remove first names containing two words like "John Wiliam"

def get_genderize(api_key):
    """ Returns genderize object, useful when using this script as a module
    """
    genderize = Genderize(
        user_agent='GenderizeDocs/0.0',
        api_key=api_key)
    return genderize


def fetch_gender(name_list, genderize_obj):
    """Return a list of dictionaries, a dictionary for each name in the passed list
    name_list.
    """
    # name_list = df.cleaned_name.unique()
    gender_list = []
    for i in range(0, len(name_list), 10):

        # sometimes helps to be polite
        if i % 5 == 0:
            time.sleep(2)
        try:
            resp = genderize_obj.get(name_list[i:i + 10])
        except Exception as e:
            print(e)
            print(name_list[i:i + 10])
            time.sleep(120)
            resp = genderize_obj.get(name_list[i:i + 10])
            print("Had a 2 minute break")
        # print(x)
        if i % 50 == 0:
            print(str(i + 50) + " names fetched!")
        gender_list.append(resp)
    # gender_list[0]
    gender_list_flat = [item for sublist in gender_list for item in sublist]
    return gender_list_flat


def male_female(dic, thres):
    if dic == None:
        return dic
    if dic["gender"] == 'male' and dic["probability"] > thres:
        dic['gender'] = 'male'
    elif dic["gender"] == 'female' and dic["probability"] > thres:
        dic['gender'] = 'female'
    else:
        dic['gender'] = 'unknown'
    return dic


def get_dataframe_thres(flat_list, thres):
    """ Returns pandas dataframe, where every row is a dictionary from the flat list.
        In this case it takes into account the confidence and also assigns unknown gender
    """
    lst = []
    for i in flat_list:
        new_dic = male_female(i, thres)
        lst.append(new_dic)
    df = pd.DataFrame(lst)
    return df


def get_dataframe(flat_list):
    """ Returns pandas dataframe, where every row is a dictionary from the flat list
    """
    return pd.DataFrame(flat_list)


def get_stats(df, col):
    """ Returns a dictionary with number absolute and relative frequency
    """
    total = len(df)
    dic = df[col].value_counts().to_dict()
    for k, v in dic.items():
        dic[k] = [v, round(v / total, 2)]
    return dic


def load_file(path, col, typ="json"):
    """ Returns list of unique names from a specified file, and column
    """
    if typ == "csv":
        df = pd.read_csv(path)
    else:
        df = pd.read_json(path)
    print("Loading: {}".format(path))
    name_list = df[col].unique()
    print("Loaded {} unique names".format(len(name_list)))
    return name_list


def save_file(df, path, typ="json"):
    """Saves dataframe as file in specified format:
       JSON or CSV
    """
    if typ == "csv":
        df.to_csv(path, encoding="utf8")
    else:
        df.to_json(path)
    print("File saved at: " + path)


if __name__ == "__main__":
    # command line arguments for input and output file paths
    # input_path "input.csv"
    # output_path "output.csv"

    genderize = get_genderize('886cbf0996d6aa757c44f708b4faafee')  # Add your API key

    # example

    name_list = GenderizeInput[1:10]

    print("Fetching gender...")

    flat_list = fetch_gender(name_list, genderize)

    df_no_thres = get_dataframe(flat_list)
    df = get_dataframe_thres(flat_list, 0.8)
import pickle
di={}
for i in range(0,len(df)):
        di[df.iloc[i][2]]=df.iloc[i][1]
output = open('name/data/namedict.pkl', 'wb')
pickle.dump(di, output)
output.close()
