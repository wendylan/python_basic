"""
写入JSON文件
"""

import json;

teacher_dict = {'name': '魏桂花', 'age': 20, 'title': '讲师'};
json_str = json.dumps(teacher_dict);
print(json_str);
print(type(json_str));
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya'];
json_str = json.dumps(fruits_list);
print(json_str);
print(type(json_str));