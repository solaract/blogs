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

# # 遍历键值对
# # 遍历字典时，键—值对的返回顺序也与存储顺序不同
# user_0 = { 
#  'username': 'efermi', 
#  'first': 'enrico', 
#  'last': 'fermi', 
#  } 
# for key, value in user_0.items(): 
#     print("\nKey: " + key) 
#     print("Value: " + value)

# # 遍历所有键
# favorite_languages = { 
#  'jen': 'python', 
#  'sarah': 'c', 
#  'edward': 'ruby', 
#  'phil': 'python', 
#  }
# for name in favorite_languages.keys(): 
#  print(name.title())
# # 遍历字典时，会默认遍历所有的键
# # 因此等同于
# for name in favorite_languages: 
#  print(name.title())

# favorite_languages = { 
#  'jen': 'python', 
#  'sarah': 'c', 
#  'edward': 'ruby', 
#  'phil': 'python', 
#  } 
# if 'erin' not in favorite_languages.keys():
#  print("Erin, please take our poll!") 

# # 遍历所有值
#  favorite_languages = { 
#  'jen': 'python', 
#  'sarah': 'c', 
#  'edward': 'ruby', 
#  'phil': 'python', 
#  } 
# print("The following languages have been mentioned:") 
# for language in favorite_languages.values(): 
#  print(language.title()) 

# # 剔除重复项
#  favorite_languages = { 
#  'jen': 'python', 
#  'sarah': 'c', 
#  'edward': 'ruby', 
#  'phil': 'python', 
#  } 
# print("The following languages have been mentioned:") 
# for language in set(favorite_languages.values()): 
#  print(language.title())

# # 输入
# message = input("Tell me something, and I will repeat it back to you: ") 
# print(message) 

# height = input("How tall are you, in inches? ") 
# height = int(height) 
# if height >= 36: 
#  print("\nYou're tall enough to ride!") 
# else:
#  print("\nYou'll be able to ride when you're a little older.") 

# # 函数
# # 指定形参默认值
# def describe_pet(pet_name, animal_type='dog'): 
#  """显示宠物的信息""" 
#  print("\nI have a " + animal_type + ".") 
#  print("My " + animal_type + "'s name is " + pet_name.title() + ".") 

# # 一条名为Willie的小狗
# # 省略默认值
# describe_pet('willie') 
# describe_pet(pet_name='willie') 

# # 一只名为Harry的仓鼠
# # 位置实参
# describe_pet('harry', 'hamster') 
# # 关键字实参
# describe_pet(pet_name='harry', animal_type='hamster') 
# describe_pet(animal_type='hamster', pet_name='harry') 

# def make_pizza(*toppings): 
#  """概述要制作的比萨""" 
#  print("\nMaking a pizza with the following toppings:") 
#  for topping in toppings: 
#     print("- " + topping) 
 
# make_pizza('pepperoni') 
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(size, *toppings): 
#  """概述要制作的比萨""" 
#  print("\nMaking a " + str(size) + 
#  "-inch pizza with the following toppings:") 
#  for topping in toppings: 
#     print("- " + topping) 
 
# make_pizza(16, 'pepperoni') 
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 

# def build_profile(first, last, **user_info): 
#     """创建一个字典，其中包含我们知道的有关用户的一切""" 
#     profile = {} 
#     profile['first_name'] = first 
#     profile['last_name'] = last 
#     for key, value in user_info.items():
#         profile[key] = value 
#     return profile 
# user_profile = build_profile('albert', 'einstein', 
#     location='princeton', 
#     field='physics') 
# print(user_profile) 


# # 类
# # class Dog(): 
# #     """一次模拟小狗的简单尝试""" 

# #     def __init__(self, name, age): 
# #         """初始化属性name和age""" 
# #         self.name = name 
# #         self.age = age 

# #     def sit(self): 
# #         """模拟小狗被命令时蹲下""" 
# #         print(self.name.title() + " is now sitting.") 
# #     def roll_over(self): 
# #         """模拟小狗被命令时打滚""" 
# #         print(self.name.title() + " rolled over!") 

# # my_dog = Dog('willie', 6) 
# # your_dog = Dog('lucy', 3) 
# # print("My dog's name is " + my_dog.name.title() + ".") 
# # print("My dog is " + str(my_dog.age) + " years old.") 
# # my_dog.sit() 
# # print("\nYour dog's name is " + your_dog.name.title() + ".") 
# # print("Your dog is " + str(your_dog.age) + " years old.") 
# # your_dog.sit()

# class Car(): 
#     """一次模拟汽车的简单尝试""" 
#     def __init__(self, make, model, year): 
#         """初始化描述汽车的属性""" 
#         self.make = make 
#         self.model = model 
#         self.year = year 
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self): 
#         """返回整洁的描述性信息""" 
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
#         return long_name.title() 
#     def read_odometer(self): 
#         """打印一条指出汽车里程的消息""" 
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#     def update_odometer(self, mileage): 
#         """ 
#         将里程表读数设置为指定的值
#         禁止将里程表读数往回调
#         """ 
#         if mileage >= self.odometer_reading: 
#             self.odometer_reading = mileage 
#         else: 
#             print("You can't roll back an odometer!") 
#     def increment_odometer(self, miles): 
#         """将里程表读数增加指定的量""" 
#         self.odometer_reading += miles


# # my_new_car = Car('audi', 'a4', 2016) 
# # print(my_new_car.get_descriptive_name()) 
# # my_new_car.odometer_reading = 23
# # my_new_car.read_odometer() 
# # my_new_car.update_odometer(23500) 
# # my_new_car.read_odometer() 
# # my_new_car.increment_odometer(100) 
# # my_new_car.read_odometer() 

# class Battery(): 
#     """一次模拟电动汽车电瓶的简单尝试""" 
    
#     def __init__(self, battery_size=70): 
#         """初始化电瓶的属性""" 
#         self.battery_size = battery_size 
#     def describe_battery(self): 
#         """打印一条描述电瓶容量的消息""" 
#         print("This car has a " + str(self.battery_size) + "-kWh battery.") 

# class ElectricCar(Car): 
#     """电动汽车的独特之处""" 
#     def __init__(self, make, model, year): 
#         """初始化父类的属性""" 
#         super().__init__(make, model, year) 
#         # self.battery_size = 70
#         self.battery = Battery()
#     def describe_battery(self): 
#         """打印一条描述电瓶容量的消息""" 
#         print("This car has a " + str(self.battery_size) + "-kWh battery.") 
    

# my_tesla = ElectricCar('tesla', 'model s', 2016) 
# print(my_tesla.get_descriptive_name()) 
# # my_tesla.describe_battery() 
# my_tesla.battery.describe_battery()

# 文件和异常
# with open('pi_digits.txt') as file_object: 
#     contents = file_object.read() 
#     # print(contents)
#     print(contents.rstrip())

# filename = 'pi_digits.txt' 
# with open(filename) as file_object: 
#     for line in file_object: 
#         # print(line)
#         print(line.rstrip()) 

# filename = 'pi_digits.txt' 
# with open(filename) as file_object: 
#     lines = file_object.readlines() 
# for line in lines: 
#     print(line.rstrip()) 

# filename = 'programming.txt' 
# with open(filename, 'w') as file_object: 
#     file_object.write("I love programming.\n") 
#     file_object.write("I love creating new games.\n")
# with open(filename, 'a') as file_object: 
#     file_object.write("I also love finding meaning in large datasets.\n") 
#     file_object.write("I love creating apps that can run in a browser.\n") 

print("Give me two numbers, and I'll divide them.") 
print("Enter 'q' to quit.") 
while True: 
    first_number = input("\nFirst number: ") 
    if first_number == 'q': 
        break 
    second_number = input("Second number: ") 
    try: 
        answer = int(first_number) / int(second_number) 
    except ZeroDivisionError: 
        print("You can't divide by 0!") 
    else: 
        print(answer)