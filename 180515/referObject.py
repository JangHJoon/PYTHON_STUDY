# https://wikidocs.net/13969
import sys
import gc

class A:
    pass

class B:
    def __init__(self, obj):
        self.obj = obj


a = A()
b = B(a)
c = b


gc.collect()

# 객체의 현재 참조 수(객체 생성시 기본 2개)
print(sys.getrefcount(c))

# 객체가 현재 참조 하고 있는 목록
# 현재 객체와, 맴버변수는 dic으로 표현 
# [{'obj': <__main__.A object at 0x02111110>}, <class '__main__.B'>]
print(gc.get_referents(c))
