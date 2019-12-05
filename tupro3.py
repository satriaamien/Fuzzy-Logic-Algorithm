import pandas as pd
import numpy as np
# import matplotplib.pyplot as plt
def getfile():
	csv=[]
	file=pd.read_csv("influencers.csv",header=None)
	filepd=pd.DataFrame(file)
	getpd=filepd.to_numpy()
	data=np.delete(getpd,0,0)
	for x in range(len(data)):
		csv.append([int(data[x][0]),int(data[x][1]),float(data[x][2])])	
	return csv

#bagus cukup buruk
# followerCount
def flwjelek(x): 
	#8.000 - 16.000  
	if (x<=8000):
		return 1
	elif(x>8000 and x<20000):
		return float((20000-x)/(20000-8000)) 
	elif(x>=20000):
		return 0
def flwcukup(x):
	if (x>=50000) or (x<=8000):
		return 0
	elif(x>8000 and x<20000):
		return (x-8000)/(20000-8000)
	elif(x>=20000 and x<=35000):
		return 1
	elif(x>35000 and x<50000):
		return (50000-x)/(50000-35000)
def flwbagus(x):
	if (x<=35000):
		return 0
	elif(x>35000 and x<50000):
		(x-35000)/(50000-35000)
	elif(x>=50000):
		return 1

# engagementRate
def engjelek(x):
	if (x<=0.8):
		return 1
	elif(x>0.8 and x<1.6):
		return (0.8-x)/(1.6-0.8)
	else:
		return 0
def engcukup(x):
	if (x<=0.8) or (x>=3.4):
		return 0
	elif(x>0.8 and x<2.0):
		return (x-0.8)/(2.0-0.8)
	elif(x>=2.0 and x<=2.6):
		return 1
	elif(x>2.6 and x<3.4):
		return (3.4-x)/(3.4-2.6)
def engbagus(x):
	if (x<=2.6):
		return 0
	if (x>2.6 and x<3.4):
		return (x-2.6)/(3.4-2.6)
	else:
		return 1

#inferens
def inference(fb,fm,fg,eb,em,eg):
	acc,con,rej=[],[],[]
	acc.append(min(fg,eg))
	acc.append(min(fg,em))
	acc.append(min(fm,eg))

	con.append(min(fg,eb))
	con.append(min(fm,em))
	con.append(min(fb,eg))

	rej.append(min(fm,eb))
	rej.append(min(fb,em))
	rej.append(min(fb,eb))
	return [max(acc),max(con),max(rej)]

def sugeno(acc,con,rej):
	atas = (acc*100)+(con*50)+(rej*30)
	bawah = acc+con+rej+0.0000000000000000000000000000000001
	return atas/bawah

#main
csv=getfile()
getsugeno=[]
# print csv[2][2]
for x in range(len(csv)):
	flwbad= flwjelek(csv[x][1])
	flwmed= flwcukup(csv[x][1])
	flwgood= flwbagus(csv[x][1])
	engbad= engjelek(csv[x][2])
	engmed= engcukup(csv[x][2])
	enggood= engbagus(csv[x][2])
	getinf= inference(flwbad,flwmed,flwgood,engbad,engmed,enggood)
	acc,con,rej = getinf[0],getinf[1],getinf[2] 
	hasildef = sugeno(acc, con, rej)
	getsugeno.append([hasildef,x+1])
print("20 TOP TERBAIK")
data = sorted(getsugeno, key=lambda x: x[0], reverse=True)
sugeno=data[:20]
sugeno.insert(0,['top','id'])
getsugeno=pd.DataFrame(np.array(sugeno))
print getsugeno
getsugeno.to_csv('chosen.csv', sep=',', index=False, header= None)