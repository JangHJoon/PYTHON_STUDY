# 타입힌팅-> annotation

def greeting(name: str) -> str: 
	return 'Hello ' + name


print(greeting.__annotations__)