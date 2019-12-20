'''
f = open("C:\\softwareDate\\guoya_demo\\test.txt","w",encoding="utf-8")
f.write("你好，苗苗\n")
f.close()
#读取文件
f = open("test.txt","r",encoding="utf-8")
#读取全部内容
#c = f.read()
#print(c)
lines = f.readlines()
print(lines)
#with是一个上下文管理器，with内的代码块在执行结束或者执行出错的时候
#都会自动执行释放系统资源的操作
with open("test.txt","r",encoding="utf-8") as f:
    c = f.read()
    print(c)
#类相当于一个模板，没有实体
class Man():
    name = '雷阳洪'
    def xiedaima(self):
        print(self.name,'在写代码')

a = Man()
a.xiedaima()
'''

 #产品 手机
class Product():
    size="6寸"
    def __init__(self,color):
        self.color=color
    def call(self):
        print("hello")
    def send_message(self):
        print("你有一个快递")
#实例化
phone1 = Product("土豪金")
#获取属性
print(phone1.color)
print(phone1.color)
print(phone1.color)
print(phone1.color)
print(phone1.color)
print(phone1.color)







