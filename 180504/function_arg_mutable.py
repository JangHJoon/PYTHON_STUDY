def f(a, L=[]):
	L.append(a)
	return L

def f1(a, S=set()):
	S.add(a)
	return S;
	

def f2(a, I=1):
	I=a
	return I;

def f4(a, F=None):
	if F is None:
		F = []
	F.append(a)
	return F

print(f(1))
print(f(2))
print(f(3))

print(f1(1))
print(f1(2))
print(f1(3))

print(f2(1))
print(f2(2))
print(f2(3))

print(f4(1))
print(f4(2))
print(f4(3))
