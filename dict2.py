"""
字典的常用操作
"""

def main():
    stu = {'name': 'wendy','age': 18, 'gender': True};
    print(stu);
    print(stu.keys());
    print(stu.values());
    print(stu.items());

    for elem in stu.items():
        print(elem);
        print(elem[0], elem[1]);
    if 'age' in stu:
        stu['age'] = 20;
    print(stu);
    stu.setdefault('score', 10);
    print(stu);
    stu.setdefault('score', 100);
    print(stu);
    stu['score'] = 100;
    print(stu);

if __name__ == '__main__':
    main();