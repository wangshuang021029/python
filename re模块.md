# re模块

## 1.re.findall("①","②")

​    ①中填写所需要查找的正则表达式，②中需要查找的内容

​    

```python
import re

result = re.findall(r"\d","我今年19岁，我有10923块钱")
#为了防止出现转义字符，\d前面应＋r
print(result)
```

```python
import re

result = re.findall(r"\w","我今年19岁，我有32个同学",re.A)
#对于\w,python3.3后显示的不仅仅是字母、数字和下划线，而是整个Unicode集。如果想要仅得到字母、数字和下划线，可以在后面加上re.A
print(result)
```

## 2.re.finditer

```python
import re

result = re.finditer(r"\d","我今年19岁，我有32个同学")
print(result)
```

上面代码得到的结果，明显是一个迭代器（迭代器可以提高执行效率）![](C:\Users\26656\AppData\Roaming\Typora\typora-user-images\image-20240301083710742.png)

需要从迭代器里面提取到数据，采用的是for循环来提取。

```python
import re


result = re.finditer(r"\d+","我今年19岁，我有32个同学")
for item in result:#通过for循环来提取迭代器中的数据。
    print(item.group())#从匹配到的结果拿到数据
```

## 3.re.search("","")

search区别于finditer，最大的区别是：search只会查找第一项就停止,而finditer所有的都匹配，所以需要用到for循环。

```python
import re
result = re.search(r"\d+","我今年19岁，我有32个同学")
print(result.group())#group()拿数据，其中只有当迭代器中有数据的时候，group才可以使用
```

## 4.re.match()

  match是从字符串的开头进行匹配的，类似在正则前面加上了^。

也是找到一个数据就返回。

## 5.re.compile("正则表达式")

可以提前预加载，提前把正则表达式加载出来。

```python
import re
obj = re.compile(r"\d+")
for result in obj.findall("我今年19岁，我有32个同学"):
  print(result)
```

