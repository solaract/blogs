import sys

# #bisect
# import bisect
# def grade(score,breakpoints=[60,70,80,90],grades='FDCBA'):
#     i = bisect.bisect(breakpoints,score)
#     return grades[i]
# grades = [grade(score) for score in [33,99,77,70,89,90,100]]
# for x in grades:
#     print(x)

# #insort
# import bisect
# import random
# SIZE = 7
# random.seed(1729)
# my_list = []
# for i in range(SIZE):
#     new_item = random.randrange(SIZE*2)
#     bisect.insort(my_list,new_item)
#     print('%2d ->' % new_item,my_list)

# #array
# from array import array
# from random import random
# floats = array('d',(random() for i in range(10**7)))
# print(floats[-1])
# fp = open('floats.bin','wb')
# floats.tofile(fp)
# fp.close()
# floats2 = array('d')
# fp = open('floats.bin','rb')
# floats2.fromfile(fp,10**7)
# fp.close()
# print(floats2[-1])
# print(floats == floats2)

# #内存视图
# import array
# numbers = array.array('h',[-2,-1,0,1,2])
# memv = memoryview(numbers)
# print(len(memv))
# print(memv[0])
# memv_oct = memv.cast('B')
# print(memv_oct.tolist())
# memv_oct[5] = 4
# print(numbers)

# tt = (1,2,(30,40))
# print(hash(tt))
# tf = (1,2,frozenset([30,40]))
# print(hash(tf))
# tl = (1,2,[30,40])
# print(hash(tl))

DIAL_CODES = [
    (86,'China'),
    (91,'India'),
    (1,'United States'),
    (62,'Indonesia'),
    (55,'Brazil'),
    (92,'Pakistan'),
    (880,'Bangladesh'),
    (234,'Nigeria'),
    (7,'Russia'),
    (81,'Japan'),
]
country_code = {country: code for code,country in DIAL_CODES}
print(country_code)
print({code:country.upper() for country,code in country_code.items() if code < 66})
