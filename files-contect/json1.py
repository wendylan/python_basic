"""
读取JSON数据
"""

import json;
import csv2;

json_str = '{"name":"wendy", "age": 22, "title": "老师"}';
result = json.loads(json_str); 
print(result);
print(type(result));
print(result['name']);
print(result['age']);

# 把转换得到的字典作为关键字参数传入Teacher的构造器
teacher = csv2.Teacher(**result);
print(teacher);
print(teacher.name);
print(teacher.age);
print(teacher.title);