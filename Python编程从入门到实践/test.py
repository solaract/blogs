# -*- coding: utf-8 -*-

# print("Languages:\n\tPython\n\tC\n\tJavaScript") 

# 列表
# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)
# print(bicycles[0])
# print(bicycles[0].title())
# print(bicycles[-1])
# print(bicycles[-2])

# # 修改元素
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles[0] = 'ducati'
# # 末尾添加新元素
# motorcycles.append('ducati')
# print(motorcycles)
# # 任意位置添加新元素
# motorcycles.insert(0, 'ducati')
# print(motorcycles)
# # 删除元素
# del motorcycles[0]
# print(motorcycles)
# # 弹出列表末尾元素
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)
# # 弹出任意位置元素
# first_owned = motorcycles.pop(0)
# print(first_owned)
# # 根据值删除元素
# motorcycles.remove('suzuki')
# print(motorcycles)

# # 组织列表
# # 按字母顺序排序
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
# # 按字母顺序相反的顺序排序
# cars.sort(reverse=True)
# print(cars) 
# # 不改变原列表排列顺序
# print(sorted(cars)) 
# print(cars) 
# # 反转列表排列顺序
# cars.reverse()
# print(cars)

# # 数值列表
# for value in range(1,5):
#  print(value) 
# # 创建数字列表
# numbers = list(range(1,6))
# print(numbers)
# # 指定步长
# even_numbers = list(range(2,11,2))
# print(even_numbers)
# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# min(digits)
# max(digits)
# sum(digits)
# # 创建1-10的平方数列
# squares = [value**2 for value in range(1,11)]
# print(squares) 

# 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 前三个元素的子集
print(players[0:3])
# 第2-4个元素的子集
print(players[1:4])
# 第1-4个元素的子集
print(players[:4])
# 第3到末尾所有元素的子集
print(players[2:])
# 最后三个元素的子集
print(players[-3:])
# 复制一个新的列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream') 
print(my_foods)
print(friend_foods)