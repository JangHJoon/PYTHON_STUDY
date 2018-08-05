my_nums = [x*x for x in [1, 2, 3, 4, 5]]

print(my_nums)

for num in my_nums:
    print(num)





my_nums = (x*x for x in [1, 2, 3, 4, 5])  #제네레이터 생성

print(my_nums)

for num in my_nums:
    print(num)




my_nums2 = [yield x*x for x in [1, 2, 3, 4, 5]]

print(my_nums2)

for num in my_nums2:
    print(num)

