'''
from guoya2.demo_1 import Product
#实例化
phone1 = Product("土豪金")
#获取属性
print(phone1.color)
'''
import json
#json转字典
j = '{"name":"leiyh","sex":"男"}'
a = json.loads(j)
a["sex"] = "女"
print(a)
b = json.dumps(a,ensure_ascii=False)
print(b)

#获取随机数，
import random
a = random.randint(1,5)
print(a)
#获取随机字符串
b = random.choice("dsfhajfasd")
print(b)
#获取随机列表
c = random.choice([1,2,3,4])
print(c)
#获得随机元组
d = random.choice((1,2,3,4))
print(d)
#获取文件的绝对路径
import os
p = os.path.abspath("demo_1")
print(p)
#获取文件的文件夹路径
q = os.path.dirname(p)
print(q)
#获取文件名
f = os.path.basename(p)
print(f)
#拼接目录和文件
path = os.path.join(q,f)
print(path)

#定义模块;
def hello():
    print("hell")
#捕获异常
try:
    os.mkdir("_init_")#正常的操作
except FileExistsError:#发生异常，执行这块代码
    print("文件夹已存在")
print("adassda")





