import math
import pandas as pd
from pandas.core.arrays.integer import safe_cast
import statistics as st

data = pd.read_csv("DummyData.csv")

print(data)
data1 = data["RowA"].tolist()


def MeanOfData(data):
    n = len(data)
    total = 0

    for x in data:
        total = total + int(x)
    
    print(n)
    print(total)

    mean = total/n
    return mean

mean = MeanOfData(data1)
n = len(data1)

print(mean)

sqauredList = []
for x in data1:
    temp = int(x) - mean
    temp = temp**2
    sqauredList.append(temp)

sum = 0

for x in sqauredList:
    sum = sum + int(x)

print(sqauredList)

StandardDiviation = math.sqrt(sum/n-1)

print("Standard diviation of the data is: "+ str(StandardDiviation))

print(st.stdev(data1))