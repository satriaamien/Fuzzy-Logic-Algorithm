import numpy as np
import pandas as pd

file=pd.read_csv("influencers.csv",header=None)
filepd=pd.DataFrame(file)
getpd=filepd.to_numpy()
data=np.delete(getpd,0,0)
# print(data)

# def data():
# 	file=pd.read_csv("influencers.csv",header=None)
# 	filepd=pd.DataFrame(file)
# 	getpd=filepd.to_numpy()
# 	data=np.delete(getpd,0,0)

# 	return data
print data
csv=[]
for x in range(len(data)):
	csv.append([int(data[x][0]),int(data[x][1]),float(data[x][2])])
print csv


data = sorted(getsugeno, key=lambda x: x[0], reverse=True)
print("----20 TOP TERBAIK----")
topsugeno=data[:20]	
for x in range(len(topsugeno)):
# print("SCORE FUZZY : ", data[:20])
	get=topsugeno[x]
	for y in range(1):
		print
print("INDEX DATA  : " data[:20])