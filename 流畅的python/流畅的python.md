# 字典（dict）和集合（set）
@import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false}

<!-- code_chunk_output -->

- [字典推导（python 2.7）](#字典推导python-27)

<!-- /code_chunk_output -->



- 标准库里的所有映射类型都是利用dict来实现的，因此它们有个共同的限制，即只有可散列的数据类型才能用作这些映射的键。
- 可散列对象：
    >如果一个对象是可散列的，那么在这个对象的生命周期中，它的散列值是不变的，而且这个对象需要实现_hash_()方法。另外可散列对象还要有_eq_()方法，这样才能跟其他键作比较。如果两个可散列对象是相等的，那么它们的散列值一定是一样的
    - 原子不可变数据类型：str、bytes和数值类型
    - frozenset
    - 所有元素都是可散列类型的元组
        ```py {.line-numbers}
        tt = (1,2,(30,40))
        print(hash(tt))
        #-3907003130834322577
        tf = (1,2,frozenset([30,40]))
        print(hash(tf))
        #5149391500123939311
        tl = (1,2,[30,40])
        print(hash(tl))
        #TypeError: unhashable type: 'list'
        ```
    - 用户自定义的类型的对象散列值就是id()函数的返回值
## 字典推导（python 2.7）
```py {.line-numbers}
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
#{'China': 86, 'India': 91, 'United States': 1, 'Indonesia': 62, 'Brazil': 55, 'Pakistan': 92, 'Bangladesh': 880, 'Nigeria': 234, 'Russia': 7, 'Japan': 81}
print({code:country.upper() for country,code in country_code.items() if code < 66})
#{1: 'UNITED STATES', 62: 'INDONESIA', 55: 'BRAZIL', 7: 'RUSSIA'}
```
