import csv
import pandas as pd

vocabulary=open("train_vocabulary.txt","a")
f=open("train_source.txt","r")
f2=open("train_target.txt","a")

with open('quora_questions_train.csv') as csv_file:
    data = pd.read_csv(csv_file,header=0)
    for index, row in data.iterrows():
        if row['is_duplicate']==1:
           f.write(row['question1']+'\n')     
           f2.write(row['question2']+'\n')

    file=f.read()
    word_list = file.split()
    unique_words = set(word_list)
    for word in unique_words:
        vocabulary.write(str(word) + "\n")


f.close()
f2.close()
