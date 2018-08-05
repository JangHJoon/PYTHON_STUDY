

class A:
    def _single_method(self):
        pass

    def __double_method(self): # 맹글링을 위한 메서드
        pass

class B(A):
    def __double_method(self): # 맹글링을 위한 메서드
        pass


print(dir(A())) # ['_A_double_method', ..., '_single_method']
print(dir(B())) # ['_A_double_method', '_B_double_method', ..., '_single_method']


#a = A
#A.__double_method(a) #접근 불가 __classname__double_methode로 접근 해야함

class C:
    def _single_method(self):
        pass

    def double_method(self): 
        pass

class D(C):
    def double_method(self): 
        pass

print(dir(C()))
print(dir(D()))

c = C
C.double_method(c)
