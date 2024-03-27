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
- [函数](#函数)
  - [传递任意数量的实参](#传递任意数量的实参)
  - [导入函数模块](#导入函数模块)
  - [as指定别名](#as指定别名)
- [类](#类)
  - [修改实例属性值](#修改实例属性值)
  - [继承](#继承)
  - [导入类模块](#导入类模块)
  - [类编码风格](#类编码风格)
- [文件和异常](#文件和异常)
  - [读取文件](#读取文件)
  - [文件路径](#文件路径)
  - [逐行读取](#逐行读取)
  - [写入文件](#写入文件)
  - [异常](#异常)
  - [存储数据](#存储数据)
  - [重构](#重构)
- [测试代码](#测试代码)
  - [测试函数](#测试函数)
  - [测试类](#测试类)
- [项目](#项目)
  - [创建虚拟环境](#创建虚拟环境)

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
```py {.line-numbers}
height = input("How tall are you, in inches? ") 
height = int(height) 
if height >= 36: 
 print("\nYou're tall enough to ride!") 
else:
 print("\nYou'll be able to ride when you're a little older.") 
```

## 函数
```py {.line-numbers}
# 指定形参默认值
def describe_pet(pet_name, animal_type='dog'): 
 """显示宠物的信息""" 
 print("\nI have a " + animal_type + ".") 
 print("My " + animal_type + "'s name is " + pet_name.title() + ".") 

# 一条名为Willie的小狗
# 省略默认值
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠
# 位置实参
describe_pet('harry', 'hamster')
# 关键字实参
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 传入列表副本实参
# 切片表示法[:]创建列表的副本
# 函数中的修改不会影响列表list_name
unction_name(list_name[:])
```

### 传递任意数量的实参
形参名*toppings创建一个名为toppings的空元组，并将收到的所有值都封
装到这个元组中
```py {.line-numbers}
def make_pizza(*toppings): 
 """概述要制作的比萨""" 
 print("\nMaking a pizza with the following toppings:") 
 for topping in toppings: 
    print("- " + topping) 
 
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 结合位置实参
def make_pizza(size, *toppings): 
 """概述要制作的比萨""" 
 print("\nMaking a " + str(size) + 
 "-inch pizza with the following toppings:") 
 for topping in toppings: 
    print("- " + topping) 
 
make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
```

形参**user_info创建一个名为user_info的空字典，并将收到的所
有名称—值对都封装到这个字典中
```py {.line-numbers}
def build_profile(first, last, **user_info): 
    """创建一个字典，其中包含我们知道的有关用户的一切""" 
    profile = {} 
    profile['first_name'] = first 
    profile['last_name'] = last 
    for key, value in user_info.items():
        profile[key] = value 
    return profile 
user_profile = build_profile('albert', 'einstein', 
    location='princeton', 
    field='physics') 
print(user_profile) 
```

### 导入函数模块
模块pizza.py文件：
```py {.line-numbers}
def make_pizza(size, *toppings): 
  """概述要制作的比萨""" 
  print("\nMaking a " + str(size) + 
  "-inch pizza with the following toppings:") 
  for topping in toppings: 
  print("- " + topping) 
```
- 导入模块
  ```py {.line-numbers}
  import module_name
  ```
  ```py {.line-numbers}
  import pizza 
  pizza.make_pizza(16, 'pepperoni') 
  pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
  ```
- 导入模块特定函数
  ```py {.line-numbers}
  from module_name import function_0, function_1, function_2
  ```
  ```py {.line-numbers}
  from pizza import make_pizza 
  make_pizza(16, 'pepperoni') 
  make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
  ```
- 导入模块所有函数（不推荐）
  ```py {.line-numbers}
  from module_name import * 
  ```
  ```py {.line-numbers}
  from pizza import * 
  make_pizza(16, 'pepperoni') 
  make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
  ```

### as指定别名
- as指定函数别名
  如果要导入的函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名——函数的另一个名称
  ```py {.line-numbers}
  from module_name import function_name as fn
  ```
  ```py {.line-numbers}
  # 函数make_pizza()指定别名mp()
  from pizza import make_pizza as mp 
  mp(16, 'pepperoni') 
  mp(12, 'mushrooms', 'green peppers', 'extra cheese')
  ```

- as指定模块名
  给模块指定简短的别名
  ```py {.line-numbers}
  import module_name as mn
  ```
  ```py {.line-numbers}
  import pizza as p 
  p.make_pizza(16, 'pepperoni') 
  p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 
  ```

## 类
类中的函数称为方法，变量称为属性
```py {.line-numbers}
class Dog(): 
    """一次模拟小狗的简单尝试""" 

    def __init__(self, name, age): 
        """初始化属性name和age""" 
        self.name = name 
        self.age = age 

    def sit(self): 
        """模拟小狗被命令时蹲下""" 
        print(self.name.title() + " is now sitting.") 
    def roll_over(self): 
        """模拟小狗被命令时打滚""" 
        print(self.name.title() + " rolled over!") 

my_dog = Dog('willie', 6) 
your_dog = Dog('lucy', 3) 
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.") 
my_dog.sit() 
print("\nYour dog's name is " + your_dog.name.title() + ".") 
print("Your dog is " + str(your_dog.age) + " years old.") 
your_dog.sit()
```
- \_\_init__()
  \_\_init__()是一个特殊的方法，每次根据类创建新实例时，Python都会自动运行它
  方法\_\_init__()并未显式地包含return语句，但每次调用时Python自动返回一个新实例
- self
  每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
  每当我们根据Dog类创建实例时，都只需给最后两个形参（name和age）提供值

通常可以认为首字母大写的名称（如Dog）指的是类，而小写的名称（如my_dog）指的是根据类创建的实例

### 修改实例属性值
1. 指定属性默认值
   类中的每个属性都必须有初始值，哪怕这个值是0或空字符串
2. 直接修改属性值
3. 通过方法修改属性值
```py {.line-numbers}
class Car(): 
    """一次模拟汽车的简单尝试""" 
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
        # 指定属性默认值
        self.odometer_reading = 0
    
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title() 
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage): 
        """ 
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """ 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!") 
    def increment_odometer(self, miles): 
        """将里程表读数增加指定的量""" 
        self.odometer_reading += miles


my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 
# 直接修改属性值
my_new_car.odometer_reading = 23
my_new_car.read_odometer() 
# 通过方法修改属性值
my_new_car.update_odometer(23500) 
my_new_car.read_odometer() 
my_new_car.increment_odometer(100) 
my_new_car.read_odometer() 
```

### 继承
一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类称为**父类**，而新类称为**子类**。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。对不符合子类模拟的实物的方法可以进行重写，可在子类中定义一个这样的方法，即它与要重写的父类方法同名
> 创建子类时，父类必须包含在当前文件中，且位于子类前面。定义子类时，必须在括号内指定父类的名称
```py {.line-numbers}
class ElectricCar(Car): 
    """电动汽车的独特之处""" 
    def __init__(self, make, model, year): 
        """初始化父类的属性，再初始化电动汽车特有的属性""" 
        super().__init__(make, model, year) 
        self.battery_size = 70
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息""" 
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 
    
my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) 
```
- super()
super()是一个特殊函数，将父类和子类关联起来。这行代码让Python调用
ElectricCar的父类的方法__init__()，让ElectricCar实例包含父类的所有属性。父类也称为超类（superclass），名称super因此而得名

#### 将实例作为属性
可以要将类的一部分作为一个独立的类提取出来，将大型类拆分成多个协同工作的小类
```py {.line-numbers}
class Battery(): 
    """一次模拟电动汽车电瓶的简单尝试""" 
    
    def __init__(self, battery_size=70): 
        """初始化电瓶的属性""" 
        self.battery_size = battery_size 
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息""" 
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 

class ElectricCar(Car): 
    """电动汽车的独特之处""" 
    def __init__(self, make, model, year): 
        """初始化父类的属性""" 
        super().__init__(make, model, year) 
        # self.battery_size = 70
        self.battery = Battery()
    # def describe_battery(self): 
    #     """打印一条描述电瓶容量的消息""" 
    #     print("This car has a " + str(self.battery_size) + "-kWh battery.") 

my_tesla = ElectricCar('tesla', 'model s', 2016) 
print(my_tesla.get_descriptive_name()) 
# my_tesla.describe_battery() 
my_tesla.battery.describe_battery()
```

### 导入类模块
模块car.py文件：
```py {.line-numbers}
class Car(): 
    """一次模拟汽车的简单尝试""" 
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0
    
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title() 
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    def update_odometer(self, mileage): 
        """ 
        将里程表读数设置为指定的值
        禁止将里程表读数往回调
        """ 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!") 
    def increment_odometer(self, miles): 
        """将里程表读数增加指定的量""" 
        self.odometer_reading += miles

class Battery(): 
    """一次模拟电动汽车电瓶的简单尝试""" 
    
    def __init__(self, battery_size=70): 
        """初始化电瓶的属性""" 
        self.battery_size = battery_size 
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息""" 
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 

class ElectricCar(Car): 
    """电动汽车的独特之处""" 
    def __init__(self, make, model, year): 
        """初始化父类的属性""" 
        super().__init__(make, model, year) 
        # self.battery_size = 70
        self.battery = Battery()
    def describe_battery(self): 
        """打印一条描述电瓶容量的消息""" 
        print("This car has a " + str(self.battery_size) + "-kWh battery.") 
```

- 从模块导入多个类
  ```py {.line-numbers}
  from car import Car, ElectricCar 

  my_beetle = Car('volkswagen', 'beetle', 2016) 
  print(my_beetle.get_descriptive_name()) 

  my_tesla = ElectricCar('tesla', 'roadster', 2016) 
  print(my_tesla.get_descriptive_name())
  ```

- 导入整个模块
  ```py {.line-numbers}
  import car 

  my_beetle = car.Car('volkswagen', 'beetle', 2016) 
  print(my_beetle.get_descriptive_name()) 

  my_tesla = car.ElectricCar('tesla', 'roadster', 2016) 
  print(my_tesla.get_descriptive_name())
  ```

- 导入模块中所有类
  不推荐
  ```py {.line-numbers}
  from module_name import * 
  ```

- 模块依赖
  模块car.py文件：
  ```py {.line-numbers}
  class Car(): 
      """一次模拟汽车的简单尝试""" 
      def __init__(self, make, model, year): 
          """初始化描述汽车的属性""" 
          self.make = make 
          self.model = model 
          self.year = year 
          self.odometer_reading = 0
      
      def get_descriptive_name(self): 
          """返回整洁的描述性信息""" 
          long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
          return long_name.title() 
      def read_odometer(self): 
          """打印一条指出汽车里程的消息""" 
          print("This car has " + str(self.odometer_reading) + " miles on it.")
      def update_odometer(self, mileage): 
          """ 
          将里程表读数设置为指定的值
          禁止将里程表读数往回调
          """ 
          if mileage >= self.odometer_reading: 
              self.odometer_reading = mileage 
          else: 
              print("You can't roll back an odometer!") 
      def increment_odometer(self, miles): 
          """将里程表读数增加指定的量""" 
          self.odometer_reading += miles
  ```

  模块electric_car.py文件（.依赖car.py）：
  ```py {.line-numbers}
  from car import Car

  class Battery(): 
      """一次模拟电动汽车电瓶的简单尝试""" 
      
      def __init__(self, battery_size=70): 
          """初始化电瓶的属性""" 
          self.battery_size = battery_size 
      def describe_battery(self): 
          """打印一条描述电瓶容量的消息""" 
          print("This car has a " + str(self.battery_size) + "-kWh battery.") 

  class ElectricCar(Car): 
      """电动汽车的独特之处""" 
      def __init__(self, make, model, year): 
          """初始化父类的属性""" 
          super().__init__(make, model, year) 
          # self.battery_size = 70
          self.battery = Battery()
      def describe_battery(self): 
          """打印一条描述电瓶容量的消息""" 
          print("This car has a " + str(self.battery_size) + "-kWh battery.") 
  ```
  导入模块文件
  ```py {.line-numbers}
  from car import Car 
  from electric_car import ElectricCar 

  my_beetle = Car('volkswagen', 'beetle', 2016) 
  print(my_beetle.get_descriptive_name()) 

  my_tesla = ElectricCar('tesla', 'roadster', 2016) 
  print(my_tesla.get_descriptive_name()) 
  ```

### 类编码风格
类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。实例名和模块名都采用小写格式，并在单词之间加上下划线


## 文件和异常
### 读取文件
> 读取文本文件时，Python将其中的所有文本都解读为字符串。如果你读取的是数字，并要将其作为数值使用，就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数

pi_digits.txt文件：
```
3.1415926535 
 8979323846 
 2643383279 
```
打开并读取文件
```py {.line-numbers}
with open('pi_digits.txt') as file_object: 
    contents = file_object.read() 
    print(contents)
```
- open()
  函数open()接受一个参数：要打开的文件的名称，返回一个表示文件的对象。Python在当前执行的文件所在的目录中查找指定的文件

- with关键字
  关键字with在不再需要访问文件后将其关闭
  > 也可以调用open()和close()来打开和关闭文件，但这样做时，如果程序存在bug，导致close()语句未执行，文件将不会关闭，但未妥善地关闭文件可能会导致数据丢失或受损。如果在程序中过早地调用close()，你会发现需要使用文件时它已关闭（无法访问），这会导致更多的错误

- read()
  read()方法读取文件的全部内容，并返回一个字符串
  > read()到达文件末尾时返回一个空字符串

### 文件路径
> **在Windows系统中，在文件路径中使用反斜杠（\）而不是斜杠（/）**
- 相对文件路径
  相对于当前运行的程序所在目录的位置
- 绝对文件路径
  通过使用绝对路径，可读取系统任何地方的文件

### 逐行读取
```py {.line-numbers}
filename = 'pi_digits.txt' 
with open(filename) as file_object: 
    for line in file_object: 
        # print(line)
        # 删除多余空行
        print(line.rstrip()) 
```

- readlines()
  的方法readlines()从文件中读取每一行，并将其存储在一个列表中
  ```py {.line-numbers}
  filename = 'pi_digits.txt' 
  with open(filename) as file_object: 
      lines = file_object.readlines() 
  for line in lines: 
      print(line.rstrip()) 
  ```

### 写入文件
> Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式

> open()函数打开文件时，可指定**读取模式（'r'）**、**写入模式（'w'）**、**附加模式（'a'）**或**读取和写入文件的模式（'r+'）**。如果省略了模式实参，将以默认的只读模式打开文件

> 以写入（'w'）模式打开文件时，如果写入的文件不存在，函数open()将自动创建它。**如果指定的文件已经存在，Python将在返回文件对象前清空该文件**

> 以附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾。**如果指定的文件不存在，Python将为你创建一个空文件**

- write()
  方法write()将一个字符串写入文件，**函数write()不会在你写入的文本末尾添加换行符**
```py {.line-numbers}
filename = 'programming.txt' 
# open()第一个实参指定打开文件的名称，第二个实参'w'表示以写入模式打开文件
with open(filename, 'w') as file_object: 
    # 添加换行符'\n'
    file_object.write("I love programming.\n") 
    file_object.write("I love creating new games.\n")
with open(filename, 'a') as file_object: 
    file_object.write("I also love finding meaning in large datasets.\n") 
    file_object.write("I love creating apps that can run in a browser.\n") 
```

### 异常
> Python使用被称为异常的特殊对象来管理程序执行期间发生的错误。每当发生让Python不知所措的错误时，它都会创建一个异常对象。如果你编写了处理该异常的代码，程序将继续运行；如果你未对异常进行处理，程序将停止，并显示一个traceback，其中包含有关异常的报告

> 异常是使用try-except代码块处理的。try-except代码块让Python执行指定的操作，同时告诉Python发生异常时怎么办。使用了try-except代码块时，即便出现异常，程序也将继续运行：显示你编写的友好的错误消息，而不是令用户迷惑的traceback

#### ZeroDivisionError 异常
> **try代码块只包含可能导致错误的代码，except代码块捕获错误并处理，依赖于try代码块成功执行的代码都放在else代码块中**
```py {.line-numbers}
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
```

#### FileNotFoundError 异常
- 处理文件不存在异常
  ```py {.line-numbers}
  filename = 'alice.txt' 
  try: 
      with open(filename) as f_obj: 
          contents = f_obj.read() 
  except FileNotFoundError: 
      msg = "Sorry, the file " + filename + " does not exist." 
  print(msg) 
  ```
- 分析文本文件
  ```py {.line-numbers}
  filename = 'alice.txt' 
  try: 
      with open(filename) as f_obj: 
          contents = f_obj.read() 
  except FileNotFoundError: 
      msg = "Sorry, the file " + filename + " does not exist." 
      print(msg) 
  else: 
      # 计算文件大致包含多少个单词 
      words = contents.split() 
      num_words = len(words) 
      print("The file " + filename + " has about " + str(num_words) + " words.") 
  ```

> try-except代码块重要的优点:
> 1. 避免让用户看到traceback
> 2. **让程序能够继续分析能够找到的其他文件，不会因为预料中的错误停止运行**

- 分析多个文本文件（部分文件不存在）
  ```py {.line-numbers}
  def count_words(filename): 
      """计算一个文件大致包含多少个单词""" 
      try: 
          with open(filename) as f_obj: 
              contents = f_obj.read()  
      except FileNotFoundError: 
          msg = "Sorry, the file " + filename + " does not exist." 
          print(msg) 
      else: 
          # 计算文件大致包含多少个单词 
          words = contents.split() 
          num_words = len(words) 
          print("The file " + filename + " has about " + str(num_words) +  
              " words.") 
  
  filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] 
  for filename in filenames: 
      count_words(filename) 
  ```

- pass语句
  **什么都不做**
  ```py {.line-numbers}
  def count_words(filename): 
      """计算一个文件大致包含多少个单词""" 
      try: 
          with open(filename) as f_obj: 
              contents = f_obj.read()  
      except FileNotFoundError: 
          pass
          # msg = "Sorry, the file " + filename + " does not exist." 
          # print(msg) 
      else: 
          # 计算文件大致包含多少个单词 
          words = contents.split() 
          num_words = len(words) 
          print("The file " + filename + " has about " + str(num_words) +  
              " words.") 
  
  filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] 
  for filename in filenames: 
      count_words(filename) 
  ```

### 存储数据
存储数据的一种简单方式是使用模块json：
1. 将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件
中的数据
2. 可以使用json在Python程序之间分享数据，或与使用其他编程语言共享数据

- json.dump()
  保存json文件，函数json.dump()接受两个实参：要存储的数据以及可用于存储数据的文件对象
- json.load() 
  读取json文件

保存和读取用户生成的数据：
```py {.line-numbers}
import json
# 如果以前存储了用户名，就加载它 
# 否则，就提示用户输入用户名并存储它 
filename = 'username.json' 
try: 
    with open(filename) as f_obj: 
        username = json.load(f_obj) 
except FileNotFoundError: 
    username = input("What is your name? ") 
    with open(filename, 'w') as f_obj: 
        json.dump(username, f_obj) 
        print("We'll remember you when you come back, " + username + "!") 
else: 
    print("Welcome back, " + username + "!") 
```

### 重构
代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数，这样的过程被称为重构。重构让代码更清晰、更易于理解、更容易扩展

重构上一段代码：
1. 将所有代码都放到一个名为greet_user()的函数中：
  ```py {.line-numbers}
  import json 
  def greet_user(): 
      """问候用户，并指出其名字""" 
      filename = 'username.json' 
      try: 
          with open(filename) as f_obj: 
              username = json.load(f_obj) 
      except FileNotFoundError: 
          username = input("What is your name? ") 
          with open(filename, 'w') as f_obj: 
              json.dump(username, f_obj) 
              print("We'll remember you when you come back, " + username + "!") 
      else: 
          print("Welcome back, " + username + "!") 
  
  greet_user() 
  ```
2. 简化greet_user()部分功能，首先将获取存储的用户名的代码移到另一个函数中
  ```py {.line-numbers}
  import json 
  def get_stored_username(): 
      """如果存储了用户名，就获取它""" 
      filename = 'username.json' 
      try: 
          with open(filename) as f_obj: 
              username = json.load(f_obj) 
      except FileNotFoundError: 
          return None 
      else: 
          return username 
  def greet_user(): 
      """问候用户，并指出其名字""" 
      username = get_stored_username() 
      if username: 
          print("Welcome back, " + username + "!") 
      else: 
          username = input("What is your name? ") 
          filename = 'username.json' 
          with open(filename, 'w') as f_obj: 
              json.dump(username, f_obj) 
              print("We'll remember you when you come back, " + username + "!") 
  greet_user()
  ```
3. 进一步简化greet_user()，将没有存储用户名时提示用户输入的代码放在一个独立的函数中
  ```py {.line-numbers}
  import json 
  def get_stored_username(): 
      """如果存储了用户名，就获取它""" 
      filename = 'username.json' 
      try: 
          with open(filename) as f_obj: 
              username = json.load(f_obj) 
      except FileNotFoundError: 
          return None 
      else: 
          return username 
  def get_new_username(): 
      """提示用户输入用户名""" 
      username = input("What is your name? ") 
      filename = 'username.json' 
      with open(filename, 'w') as f_obj: 
          json.dump(username, f_obj) 
      return username 
  
  def greet_user(): 
      """问候用户，并指出其名字""" 
      username = get_stored_username() 
      if username: 
          print("Welcome back, " + username + "!") 
      else: 
          username = get_new_username() 
          print("We'll remember you when you come back, " + username + "!") 
  greet_user() 
  ```
最终每个函数都执行单一而清晰的任务

## 测试代码
### 测试函数
函数接受名和姓并返回整洁的姓名（name_function.py）：
```py {.line-numbers}
def get_formatted_name(first, last): 
    """Generate a neatly formatted full name.""" 
    full_name = first + ' ' + last 
    return full_name.title()
```

python标准库模块unittest提供了代码测试工具
- 单元测试：用于核实函数的某个方面没有问题
- 测试用例：一组单元测试，这些单元测试一起核实函数在各种情形下的行为都符合要求。良好的测试用例考虑到了函数可能收到的各种输入，包含针对所有这些情形的测试
- 全覆盖式测试：用例包含一整套单元测试，涵盖了各种可能的函数使用方式

```py {.line-numbers}
import unittest 
from name_function import get_formatted_name 
#继承unittest.TestCase类
class NamesTestCase(unittest.TestCase): 
    """测试name_function.py""" 
    #自动运行
    def test_first_last_name(self): 
        """能够正确地处理像Janis Joplin这样的姓名吗?"""            
        formatted_name = get_formatted_name('janis', 'joplin') 
        #断言方法
        self.assertEqual(formatted_name, 'Janis Joplin') 
#运行测试
unittest.main() 
```
> **运行测试代码时，所有以test_打头的方法都将自动运行**

- 断言方法
  断言方法用来核实得到的结果是否与期望的结果一致

  | 方法 | 用途 |
  |:-------:|:------:|
  | assertEqual(a, b)       | 核实a == b  |
  | assertNotEqual(a, b)    | 核实a != b  |
  | assertTrue(x)           | 核实x为True |
  | assertFalse(x)          | 核实x为False  |
  | assertIn(item, list)    | 核实item在list中 |
  | assertNotIn(item, list) | 核实item不在list中 |



测试成功结果：
```bash
#句点表示测试通过
.
----------------------------------------------------------------------
#运行了一个测试，消耗的时间不到0.001秒
Ran 1 test in 0.000s
#该测试用例中的所有单元测试都通过
OK
```

测试失败结果：
```bash
#测试结果的总结，表示有失败的测试
F
======================================================================
#失败的测试用例的名称，包括测试方法名称（test_first_last_name）和测试类名称（NamesTestCase）
FAIL: test_first_last_name (__main__.NamesTestCase)
#测试用例的描述
能够正确地处理像Janis Joplin这样的姓名吗?
----------------------------------------------------------------------
Traceback (most recent call last):
  File "d:\学习\blog\Python编程从入门到实践\test.py", line 528, in test_first_last_name
    self.assertEqual(formatted_name, 'Janis1 Joplin')
#断言失败的详细信息。它说明了预期的值和实际的值不相等。
AssertionError: 'Janis Joplin' != 'Janis1 Joplin'
- Janis Joplin
+ Janis1 Joplin
?      +


----------------------------------------------------------------------
Ran 1 test in 0.001s

#测试的总体结果，包括运行了多少个测试用例和是否有失败的测试
FAILED (failures=1)
```

### 测试类
匿名调查类（survey.py）：
```py {.line-numbers}
class AnonymousSurvey(): 
    """收集匿名调查问卷的答案""" 
     
    def __init__(self, question): 
        """存储一个问题，并为存储答案做准备""" 
        self.question = question 
        self.responses = [] 
         
    def show_question(self): 
        """显示调查问卷""" 
        print(self.question) 
         
    def store_response(self, new_response): 
        """存储单份调查答卷""" 
        self.responses.append(new_response) 
         
    def show_results(self): 
        """显示收集到的所有答卷""" 
        print("Survey results:") 
        for response in self.responses: 
            print('- ' + response) 
```

使用用例：
```py {.line-numbers}
from survey import AnonymousSurvey 
 
#定义一个问题，并创建一个表示调查的AnonymousSurvey对象 
question = "What language did you first learn to speak?" 
my_survey = AnonymousSurvey(question) 
 
#显示问题并存储答案 
my_survey.show_question() 
print("Enter 'q' at any time to quit.\n") 
while True: 
    response = input("Language: ") 
    if response == 'q': 
        break 
    my_survey.store_response(response) 
# 显示调查结果 
print("\nThank you to everyone who participated in the survey!") 
my_survey.show_results() 
```

测试用例：
```py {.line-numbers}
import unittest 
from survey import AnonymousSurvey 
 
class TestAnonymousSurvey(unittest.TestCase): 
    """针对AnonymousSurvey类的测试""" 
     
    def test_store_single_response(self): 
        """测试单个答案会被妥善地存储""" 
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 
        my_survey.store_response('English') 
         
        self.assertIn('English', my_survey.responses) 
         
    def test_store_three_responses(self): 
        """测试三个答案会被妥善地存储""" 
        question = "What language did you first learn to speak?" 
        my_survey = AnonymousSurvey(question) 
        responses = ['English', 'Spanish', 'Mandarin'] 
        for response in responses: 
            my_survey.store_response(response) 
             
        for response in responses: 
            self.assertIn(response, my_survey.responses) 
 
unittest.main() 
```

- setUp()
  如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。这样，在你编写的每个测试方法中都可使用在方法setUp()中创建的对象了。**可在setUp()方法中创建一系列实例并设置它们的属性，再在测试方法中直接使用这些实例**

改进的测试用例：
```py {.line-numbers}
import unittest 
from survey import AnonymousSurvey 
 
class TestAnonymousSurvey(unittest.TestCase): 
    """针对AnonymousSurvey类的测试""" 
    
    def setUp(self):
        """ 
        创建一个调查对象和一组答案，供使用的测试方法使用 
        """ 
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self): 
        """测试单个答案会被妥善地存储""" 
        self.my_survey.store_response(self.responses[0]) 
        self.assertIn(self.responses[0], self.my_survey.responses) 
         
    def test_store_three_responses(self): 
        """测试三个答案会被妥善地存储""" 
        for response in self.responses: 
            self.my_survey.store_response(response) 
        for response in self.responses: 
            self.assertIn(response, self.my_survey.responses) 
 
unittest.main() 
```

测试结果：
```bash
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
> 运行测试用例时，每完成一个单元测试，Python都打印一个字符：测试通过时打印一个句点；测试引发错误时打印一个E；测试导致断言失败时打印一个F

## 项目
### 创建虚拟环境
1. 创建虚拟环境
  ```bash
  python -m venv venv
  ```
  > 将在项目下新建文件夹'venv'
2. 激活虚拟环境
  ```bash
  .\venv\Scripts\activate
  ```
  > 报错“**此系统上禁止运行脚本**”时，以管理员身份运行powershell并执行：
  ```bash
  Set-ExecutionPolicy RemoteSigned
  ```
3. 切换编辑器的解释器环境为虚拟环境中的\venv\Scripts\python.exe
4. 退出虚拟环境
  ```bash
  deactivate
  ```