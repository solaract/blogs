# Python编程从入门到实践
@import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false}

<!-- code_chunk_output -->

- [列表](#列表)
  - [修改列表元素](#修改列表元素)
  - [组织列表](#组织列表)
  - [数值列表](#数值列表)
  - [切片](#切片)

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