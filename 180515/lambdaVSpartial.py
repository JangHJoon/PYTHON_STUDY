funcs = []

for i in range(5):
    funcs.append(lambda : print(i))

# 람다는 부를때 비로소 코드가 생성됨
for f in funcs:
    f()


from functools import partial

funcs = []
for i in range(5):
    funcs.append(partial(print,i))
 
# 파셜은 생성될때 바로 코드가 생성됨
for f in funcs:
    f()