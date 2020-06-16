# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:44:25 2018

@author: shrey
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

r=open('SuperComputers.txt','w')
country_list=[]
for i in range(1,6): 
    url = "https://www.top500.org/list/2018/06/?page={}".format(i)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    for e in soup.findAll('br'):
        country_list.append(e.next_sibling)
        e.extract()
        
    th=soup.findAll("th");
    cols=[x.text.strip() for x in th]
    l=soup.findAll("td");
    p=list(l[1].children)
    country=p[1]
    cols=[x.text.strip() for x in l]
    str=""
    n=0
    i=0
    country_list=[v for v in country_list if v is not None]    
    for k in cols:
        if (n<6):
            r.write(k+"|")
            n+=1
        else:
            r.write(k+"|"+country_list[i]+"\n")
            i=i+1
            n=0
r.close()

SuperComputers = pd.read_excel('C:/Users/shrey/Desktop/George Mason University/Sem 1/AIT 580/Completed Assignments/SuperComputers.xlsx')

#Summary Statistics
#1. Cores
#Summary Statistics
print("************************************************************************")
print(SuperComputers.Cores.describe())

#2. Rmax
#Summary Statistics
print("************************************************************************")
print(SuperComputers.Rmax.describe())

#3. Rpeak
#Summary Statistics
print("************************************************************************")
print(SuperComputers.Rpeak.describe())

#4. Power
#Summary Statistics
print("************************************************************************")
print(SuperComputers.Power.describe())

#Relationship between -
#1. Cores and Rpeak
print("************************************************************************")
plt.scatter(SuperComputers.Cores,SuperComputers.Rpeak)
plt.title("Scatter Plot between Cores and Rpeak")
plt.xlabel("Cores")
plt.ylabel("Rpeak")
plt.show()
print("************************************************************************")
SuperComputers['Cores'].corr(SuperComputers['Rpeak'])

#2. Cores and Power
print("************************************************************************")
plt.scatter(SuperComputers.Cores,SuperComputers.Power)
plt.title("Scatter Plot between Cores and Power")
plt.xlabel("Cores")
plt.ylabel("Power")
plt.show()
print("************************************************************************")
SuperComputers['Cores'].corr(SuperComputers['Power'])

#Summary Statistics & Visualization of Country Data
#Summary Statistics
print("************************************************************************")
print(SuperComputers.Country.describe())
#Visualization
print("************************************************************************")
SuperComputers.groupby('Country')
plt.style.use('ggplot')
SuperComputers.groupby(['Country']).Country.count().plot.bar(legend=True)
plt.show()