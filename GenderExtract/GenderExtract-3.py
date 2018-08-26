import pickle
pkl_file = open('name/data/FacePP.pkl', 'rb')
FacePP = pickle.load(pkl_file)
pkl_file.close()

from bs4 import BeautifulSoup
import requests
import re
import os
import json
import pandas as pd
from datetime import datetime
import sys
from multiprocessing import Pool
def get_soup(url,header):
    resp = requests.get(url,headers=header)
    return BeautifulSoup(resp.content,'html.parser')
def get_url_list(soup, num):
    actual_images=[]
    for a in soup.find_all("div",{"class":"rg_meta"})[:num]:
        link = json.loads(a.text)["ou"]
        actual_images.append((link))
    return actual_images
def load_list(path,col,typ="csv"):
    if typ == "csv":
        df = pd.read_csv(path)
        return df[col].unique()
    if typ == "json":
        df = pd.read_json(path)
        return df[col].unique()
    return []
def get_query(name):
    return "https://www.google.co.in/search?q="+name+"&source=lnms&tbm=isch"
def return_url_df(path, path_save):
    names = path
    print(str(len(names))+" names loaded!")
    header={
        'User-Agent':
        "Mozilla/5.0 (Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko)Chrome/43.0.2357.134 Safari/537.36"
    }
    url1, url2, url3, url4, url5 = [],[],[],[],[]
    num = 1
    name2=[]
    for name in names:
            try:
                url = get_query(name)
                soup = get_soup(url, header)
                link1, link2, link3, link4, link5 = get_url_list(soup,5)
                url1.append(link1)
                url2.append(link2)
                url3.append(link3)
                url4.append(link4)
                url5.append(link5)
                print("{} - {} - {}".format(num, str(datetime.now()), name))
                num = num + 1
                name2.append(name)
            except:
                continue
    df = pd.DataFrame({
        'name': name2,
        'url1':url1,
        'url2':url2,
        'url3':url3,
        'url4':url4,
        'url5':url5
    })
    df.to_csv(path_save, header=False, index=False, encoding="utf-8")
    print("Dataframe saved at: "+path_save)
if __name__ == '__main__':
    with Pool(8) as p:
        p.starmap(return_url_df, [(FacePP[0:4000],'name/data/FacePP1.csv'), (FacePP[4000:8000],'name/data/FacePP2.csv'), 
                                  (FacePP[8000:12000],'name/data/FacePP3.csv'),(FacePP[12000:16000],'name/data/FacePP4.csv'),
                                  (FacePP[16000:20000],'name/data/FacePP5.csv'), (FacePP[20000:24000],'name/data/FacePP6.csv'), 
                                  (FacePP[24000:28000],'name/data/FacePP7.csv'),(FacePP[28000:33054],'name/data/FacePP8.csv')])
