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

# # 切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# # 前三个元素的子集
# print(players[0:3])
# # 第2-4个元素的子集
# print(players[1:4])
# # 第1-4个元素的子集
# print(players[:4])
# # 第3到末尾所有元素的子集
# print(players[2:])
# # 最后三个元素的子集
# print(players[-3:])
# # 复制一个新的列表
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# my_foods.append('cannoli')
# friend_foods.append('ice cream') 
# print(my_foods)
# print(friend_foods)

# # 元组
# dimensions = (200, 50) 
# print(dimensions[0]) 
# print(dimensions[1])
# for dimension in dimensions: 
#  print(dimension)

# # if语句
# # 检查特定值是否包含在列表中
# requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
# if 'mushrooms' in requested_toppings:
#     print('mushrooms')
# if 'pepperoni' in requested_toppings:
#     print('pepperoni')

# # 检查特定值是否不包含在列表中
# banned_users = ['andrew', 'carolina', 'david'] 
# user = 'marie' 
# if user not in banned_users: 
#  print(user.title() + ", you can post a response if you wish.") 


# 字典
# alien_0 = {'color': 'green', 'points': 5} 
# new_points = alien_0['points'] 
# print("You just earned " + str(new_points) + " points!")

# # 添加键值对
# print(alien_0) 
# alien_0['x_position'] = 0 
# alien_0['y_position'] = 25 
# print(alien_0) 

# # 修改键值对
# alien_0 = {'color': 'green'} 
# print("The alien is " + alien_0['color'] + ".") 
# alien_0['color'] = 'yellow' 
# print("The alien is now " + alien_0['color'] + ".")

# # 删除键值对
# alien_0 = {'color': 'green', 'points': 5} 
# print(alien_0) 
# del alien_0['points'] 
# print(alien_0) 

# 遍历键值对
# 遍历字典时，键—值对的返回顺序也与存储顺序不同
user_0 = { 
 'username': 'efermi', 
 'first': 'enrico', 
 'last': 'fermi', 
 } 
for key, value in user_0.items(): 
    print("\nKey: " + key) 
    print("Value: " + value)

# 遍历所有键
favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 }
for name in favorite_languages.keys(): 
 print(name.title())
# 遍历字典时，会默认遍历所有的键
# 因此等同于
for name in favorite_languages: 
 print(name.title())

favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 
if 'erin' not in favorite_languages.keys():
 print("Erin, please take our poll!") 

# 遍历所有值
 favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 
print("The following languages have been mentioned:") 
for language in favorite_languages.values(): 
 print(language.title()) 

# 剔除重复项
 favorite_languages = { 
 'jen': 'python', 
 'sarah': 'c', 
 'edward': 'ruby', 
 'phil': 'python', 
 } 
print("The following languages have been mentioned:") 
for language in set(favorite_languages.values()): 
 print(language.title())