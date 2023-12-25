# -*- coding: utf-8 -*-

# print("Languages:\n\tPython\n\tC\n\tJavaScript") 

# 列表
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[-1])
# print(bicycles[-2])

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
# 末尾添加新元素
motorcycles.append('ducati')
print(motorcycles)
# 任意位置添加新元素
motorcycles.insert(0, 'ducati')
print(motorcycles)
# 删除元素
del motorcycles[0]
print(motorcycles)
# 弹出列表末尾元素
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
# 弹出任意位置元素
first_owned = motorcycles.pop(0)
print(first_owned)