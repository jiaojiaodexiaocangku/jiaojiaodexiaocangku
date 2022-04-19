#数据类型
#整数类型——>int
#浮点数类型——>float
#布尔类型——>bool（true,false)
#字符串类型——>str(带引号）

#整数类型：整数可以表示为二进制，十进制（默认），八进制，十六进制
n1=90
n2=-76
n3=0
print(n1,type(n1))
print(n2,type(n2))
print(n3,type(n3))
print('十进制',118)
print('二进制',0b10101111)#二进制以0b开头
print('八进制',0o176)#八进制以0o开头
print('十六进制',0x1EAF)#十六进制以0o开头

#浮点类型
a=3.14159
print(a,type(a))
n1=1.1
n2=2.2
n3=2.1
print(n1+n2)
print(n1+n3)
#解决浮点数计算可能会出现小数位不确定的情况：导入模块Decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型：可以转为整数（True-->1，False-->0)
f1=True
f2=False
print(f1,type(f1))
print(f2,type(f2))
print(f1+1)
print(f2+1)

#字符串类型
str1='人生苦短，我用Python'
str2="人生苦短，我用Python"
#单引号，双引号只能在一行写，三引号可以写多行
str3="""人生苦短，
我用Python"""
str4='''人生苦短，
我用Python'''
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))

#数据类型转换
#str()转成字符串；int()转成整数；float()转成浮点型
name='张三'
age=20
print(type(name),type(age))#说明name和age的数据类型相同
#print('我叫'+name+'，今年'+str(age)+'岁')：数据类型不同不能直接连接，解决方法：数据类型转化
print('我叫'+name+'，今年'+str(age)+'岁')

print('--------str()将其他类型转成str类型--')
a=10
b=198.8
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('--------int()将其他类型转成int类型--')
s1='128'
f1=98.7
s2='76.77'
ff=True
s3='hello'
print(type(s1),type(f1),type(s2),type(ff),type(s3))
print(int(s1),type(int(s1)))  #将str转为int类型，字符串为数字串
print(int(f1),type(int(f1)))  #float转为int类型，截取整数部分，舍掉小数部分
#print(int(s2),type(int(s2)))  #将str转为int类型，报错，因为字符串为小数串
print(int(ff),type(int(ff)))
#print(int(s3),type(int(s3)))  #将str转为inte类型时，字符串必须为数字串（整数），非数字串是不允许转换

print('--------float()将其他类型转成float类型--')
x='128.98'
y='76'
m=True
z='hello'
i=98
print(type(x),type(y),type(m),type(z),type(i))
print(float(x),type(float(x)))
print(float(y),type(float(y)))
print(float(m),type(float(m)))
#print(float(z),type(float(z)))#字符串中的数据如果是非数字串，则不允许转换
print(float(i),type(float(i)))#整数转成浮点数，末尾为.0

