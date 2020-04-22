import random
import pandas as pd


listOfWords = []

file = open("words.txt").read().splitlines()
for i in range(3):
    myline = random.choice(file)
    listOfWords.append(myline)


stringOfWords = listOfWords[0]+"_"+listOfWords[1]+"_"+listOfWords[2]


df=pd.DataFrame([stringOfWords])
df.to_clipboard(index=False,header=False)