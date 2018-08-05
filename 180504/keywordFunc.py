def kF(kind, *args, **kwgs):
	"""
	args 남은 인수 
	kwgs 키워드를 설정한 인수들
	"""
	print(kind)
	print("-"*30)
	for arg in args:
		print(arg)
	print("-"*30)

	for kw in kwgs:
		print(kw,":",kwgs[kw])


kF(1, 2, k=3)
kF(1,2,3,4, k=4, g=5)
kF((1,2),(1,2),(3,2),[1,2],{'k':2})