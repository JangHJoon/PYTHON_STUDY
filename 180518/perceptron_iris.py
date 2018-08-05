import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
from mylib.perceptron import Perceptron
import numpy as np

# 단층 퍼셉트론은 바이너리 결과값이 나와서
# 2개 결과값에 대해서만 트레이닝 가능함

style.use('seaborn-talk')
# user\.matplotlib\font.json 파일
krfont = {'family' : 'New Gulim' , 'weight' : 'bold', 'size' : 10}
matplotlib.rc('font' , **krfont)
matplotlib.rcParams['axes.unicode_minus'] = False

if __name__ == "__main__":

	style.use('seaborn-talk')

	df = pd.read_csv('iris.csv', header = None)
	# 0:꽃받침길이, 1:꽃받침환비, 2:꽃잎길이, 3:꽃잎너비
	# pandas의 DataFrame객체로 변환
	#print(df)
	
	y = df.iloc[0:100,4].values
	y = np.where(y=='Iris-setosa',-1,1)
	# 실제 결과값 
	X = df.iloc[0:100, [0,2]].values
	# 트레이닝 데이터중 0열 2열(꽃받침길이, 꽃잎길이)

	#print(y)
	#print(X)

	plt.scatter(X[:50,0],X[:50,1],color='r',marker='o',label='setosa')
	plt.scatter(X[50:100,0],X[50:100,1], color='b',marker='x', label ='versicolor')
	plt.xlabel('꽃잎 길이(cm)')
	plt.ylabel('꽃받침 길이(cm)')

	plt.legend(loc=5) 
	# 참조
	plt.show()

	ppn1 = Perceptron(eta=0.1)
	ppn1.fit(X,y)
	print(ppn1.errors_)
	# [-0.4  -0.7   1.84]
	# -0.4 + -0.7*꽃받침길이 + 1.84*꽃잎길이
