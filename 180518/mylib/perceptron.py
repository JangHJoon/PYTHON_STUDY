import numpy as np

class Perceptron():

	def __init__(self,thresholds=0.0,eta=0.01,n_iter=10):
	# 임계값, learing rate, 학습횟수
		self.thresholds=thresholds
		self.eta=eta
		self.n_iter=n_iter
	
	def fit(self,X,y):
	# 트레이닝 데이터 X와 거기에 대한 실제 결과값 y
		
		self.w_=np.zeros(1+X.shape[1])
		# X = np.array([[0,0],[0,1],[1,0],[1,1]])
		# 가중치를 하나 더 추가, 가중치 배열을 0으로 초기화 
		# X.shape[0]은 배열의 행 => 4개의 트레이닝 데이터
		# X.shape[1]은 배열의 행 => 각 트레이닝 데이터의 x개수
		
		self.errors_=[]
		# 매 반복마다 예측값과 실제결과값과 차이를 저장

		for _ in range(self.n_iter):

			errors=0

			for xi,target in zip(X,y):
			# [0,0],0
				update=self.eta*(target-self.predict(xi))
				# n(y-y^)
				self.w_[1:]+=update*xi
				# wi + n(y-y^)xi
				self.w_[0]+=update
				# x0 = 1
				# w0 + n(y-y^)x0
				

				errors+=int(update!=0.0)

			self.errors_.append(errors)

			print(self.w_)
			# 매 반복마다 가중치 값 출력
		return self

	def net_input(self,X):
	# 순입력함수
		return np.dot(X,self.w_[1:])+self.w_[0]
		# x0 = 1
	
	def predict(self, X):
	# 할성함수
		return np.where(self.net_input(X)>self.thresholds,1,-1)