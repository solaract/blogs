# Python编程从入门到实践
@import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false}

<!-- code_chunk_output -->

- [列表](#列表)
  - [修改列表元素](#修改列表元素)
  - [组织列表](#组织列表)
  - [数值列表](#数值列表)
  - [切片](#切片)
- [元组](#元组)
- [if语句](#if语句)
- [字典](#字典)
  - [遍历字典](#遍历字典)
- [用户输入](#用户输入)

<!-- /code_chunk_output -->


## 列表
> 列表由一系列按特定顺序排列的元素组成
```py {.line-numbers}
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
# 输出最后一个元素
print(bicycles[-1])
print(bicycles[-2])
```

### 修改列表元素
```py {.line-numbers}
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
```

- append()
  末尾添加新元素
  ```py {.line-numbers}
    motorcycles.append('ducati')
  ```
- insert()
  任意位置添加新元素
  ```py {.line-numbers}
    motorcycles.insert(0, 'ducati')
  ```
- del
  删除元素
  ```py {.line-numbers}
    del motorcycles[0]
  ```
- pop()
  弹出元素
  ```py {.line-numbers}
    # 弹出列表末尾元素
    popped_motorcycle = motorcycles.pop()
    # 弹出任意位置元素
    first_owned = motorcycles.pop(0)
  ```
- remove()
  根据值删除元素
  ```py {.line-numbers}
    motorcycles.remove('suzuki')
  ```
  > 方法remove()只删除第一个指定的值

### 组织列表
- sort()
  对列表按字母顺序排序
  ```py {.line-numbers}
    # 按字母顺序排序
    cars = ['bmw', 'audi', 'toyota', 'subaru']
    cars.sort()
    # 按字母顺序相反的顺序排序
    cars.sort(reverse=True)
  ```
- sorted()
  返回列表按字母顺序排序后的列表，不改变原列表的排列顺序。也可向函数sorted()传递参数reverse=True
  ```py {.line-numbers}
    # 不改变原列表排列顺序
    print(sorted(cars)) 
    print(cars) 
  ```
- reverse()
  反转列表排列顺序
  ```py {.line-numbers}
    cars.reverse()
  ```
- len()
  返回列表长度
  ```py {.line-numbers}
    len(cars)
  ```

### 数值列表
- range()
  生成一系列数字
  ```py {.line-numbers}
    # 打印数字1-4
    for value in range(1,5):
        print(value) 
    # 创建数字列表
    numbers = list(range(1,6))
    # 指定步长
    even_numbers = list(range(2,11,2))
  ```
- 计算最大值、最小值和总和
  ```py {.line-numbers}
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    min(digits)
    max(digits)
    sum(digits)
  ```
- 列表解析
  ```py {.line-numbers}
    # 创建1-10的平方数列
    squares = [value**2 for value in range(1,11)]
  ```

### 切片
```py {.line-numbers}
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
```

## 元组
不可变的列表
```py {.line-numbers}
dimensions = (200, 50) 
print(dimensions[0]) 
print(dimensions[1])
for dimension in dimensions: 
 print(dimension)
```

## if语句
```py {.line-numbers}
# 检查特定值是否包含在列表中
requested_toppings = ['mushrooms', 'onions', 'pineapple'] 
if 'mushrooms' in requested_toppings:
    print('mushrooms')
if 'pepperoni' in requested_toppings:
    print('pepperoni')
    
# 检查特定值是否不包含在列表中
banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie' 
if user not in banned_users: 
 print(user.title() + ", you can post a response if you wish.") 
```

## 字典
一系列键值对
```py {.line-numbers}
alien_0 = {'color': 'green', 'points': 5} 
new_points = alien_0['points'] 
print("You just earned " + str(new_points) + " points!")

# 添加键值对
print(alien_0) 
alien_0['x_position'] = 0 
alien_0['y_position'] = 25 
print(alien_0) 

# 修改键值对
alien_0 = {'color': 'green'} 
print("The alien is " + alien_0['color'] + ".") 
alien_0['color'] = 'yellow' 
print("The alien is now " + alien_0['color'] + ".")

# 删除键值对
alien_0 = {'color': 'green', 'points': 5} 
print(alien_0) 
del alien_0['points'] 
print(alien_0) 
```

### 遍历字典
- items()
  返回一个键值对列表

  遍历字典时，键值对的返回顺序也与存储顺序不同
  ```py {.line-numbers}
  # 遍历键值对
  user_0 = { 
  'username': 'efermi', 
  'first': 'enrico', 
  'last': 'fermi', 
  } 
  for key, value in user_0.items(): 
      print("\nKey: " + key) 
      print("Value: " + value)
  ```
- keys()
  返回一个键列表

  遍历字典时，会默认遍历所有的键
  ```py {.line-numbers}
  # 遍历所有键
  favorite_languages = { 
  'jen': 'python', 
  'sarah': 'c', 
  'edward': 'ruby', 
  'phil': 'python', 
  }
  for name in favorite_languages.keys(): 
  print(name.title())
  # 等同于
  for name in favorite_languages: 
  print(name.title())
  ```
  方法keys()并非只能用于遍历；实际上，它返回一个列表，其中包含字典中的所有键
  ```py {.line-numbers}
  favorite_languages = { 
  'jen': 'python', 
  'sarah': 'c', 
  'edward': 'ruby', 
  'phil': 'python', 
  } 
  if 'erin' not in favorite_languages.keys():
  print("Erin, please take our poll!") 
  ```
- values()
  返回一个值列表
  ```py {.line-numbers}
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
  ```
  创建集合set剔除重复元素
  ```py {.line-numbers}
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
  ```

## 用户输入
- input()
让程序暂停运行，等待用户输入一些文本  