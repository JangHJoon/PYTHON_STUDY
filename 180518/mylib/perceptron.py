import numpy as np

class Perceptron():

	def __init__(self,thresholds=0.0,eta=0.01,n_iter=10):
	# �Ӱ谪, learing rate, �н�Ƚ��
		self.thresholds=thresholds
		self.eta=eta
		self.n_iter=n_iter
	
	def fit(self,X,y):
	# Ʈ���̴� ������ X�� �ű⿡ ���� ���� ����� y
		
		self.w_=np.zeros(1+X.shape[1])
		# X = np.array([[0,0],[0,1],[1,0],[1,1]])
		# ����ġ�� �ϳ� �� �߰�, ����ġ �迭�� 0���� �ʱ�ȭ 
		# X.shape[0]�� �迭�� �� => 4���� Ʈ���̴� ������
		# X.shape[1]�� �迭�� �� => �� Ʈ���̴� �������� x����
		
		self.errors_=[]
		# �� �ݺ����� �������� ����������� ���̸� ����

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
			# �� �ݺ����� ����ġ �� ���
		return self

	def net_input(self,X):
	# ���Է��Լ�
		return np.dot(X,self.w_[1:])+self.w_[0]
		# x0 = 1
	
	def predict(self, X):
	# �Ҽ��Լ�
		return np.where(self.net_input(X)>self.thresholds,1,-1)