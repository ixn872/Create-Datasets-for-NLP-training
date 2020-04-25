import csv
import pandas as pd
import codecs

f=open('train.txt','a')
f2=open('target.txt','a')


with codecs.open('train.csv', mode='r', encoding='UTF-8', errors='strict', buffering=1) as csv_file:

    data = pd.read_csv(csv_file,header=0,encoding='UTF-8')
    for index, row in data.iterrows():
        if row['is_duplicate']==1:
           row['question1']=row['question1'].encode('ascii','ignore').decode('UTF-8','ignore')
           row['question2']=row['question2'].encode('ascii','ignore').decode('UTF-8','ignore')
           f.write(row['question1']+'\n')
           f2.write(row['question2']+'\n')
    f.close()
    f2.close()
