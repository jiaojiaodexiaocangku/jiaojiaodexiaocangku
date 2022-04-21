present=input('大圣想要什么礼物呢？')#输入函数；返回值为str
print(present,type(present))
#从键盘录入两个整数，计算两个整数和
a=int(input('请输入一个加数：'))
#a=int(a)#将转换之后的结果存储到a中
b=int(input('请输入另一个一个加数：'))
#b=int(b)
print(type(a),type(b))
print(a+b)

#运算符
#算术运算符
print(1+1)#加法运算
print(1-1)#减法运算
print(2*4)#乘法运算
print(11/2)#除法运算
print(11//2)#整除运算
print(11%2)#取余运算
print(2**3)#表示的是2的3次方

print(9//4)#2
print(-9//-4)#2
#一正一负的整除公式，向下取整
print(9//-4)#-3
print(-9//4)#-3
#公式  余数=被除数-除数*商
print(9%-4)#-3   9-（-4）*（-3） 9-12——>-3
print(-9%4)#3    -9-4*（-3）   -9+12——>3

#赋值运算符
i=3+4
print(i)
a=b=c=20#链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))

print('--------支持参数赋值--------')
a=20
a+=30 #相当于a=a+30
print(a,type(a))
a-=10  #相当于a=a-10
print(a,type(a))
a*=2  #相当于a=a*2
print(a,type(a))
a/=3  #相当于a=a/3
print(a,type(a))
a//=2
print(a,type(a))
a%=2
print(a,type(a))

print('--------支持系列解包赋值--------')
a,b,c=20,30,40#左右变量个数和值的个数定义
print(a,b,c)
print('--------交换两个变量的值--------')
a,b=10,20
print('交换之前：',a,b)
#交换
a,b=b,a
print('交换之后：',a,b)

#比较运算符,结果为bool类型
a,b=10,20
print('a>b吗？',a>b) #False
print('a<b吗？',a<b) #True
print('a>=b吗？',a>=b)#False
print('a<=b吗？',a<=b)#True
print('a==b吗？',a==b)#False
print('a!=b吗？',a!=b)#True

'''一个 =称为赋值运算符 ,==称为比较运算符
一个变量由三部分组成，标识，类型，值
==比较的是值还是标识呐？比较的是值
比较对象的标识使用 is
'''
a=10
b=10
print(a==b)    #True 说明，a与b的value相等
print(a is b)  #True 说明，a与b的id标识相等

#以下代码没学过，后面会讲解
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)  #value ——>True
print(lst1 is lst2) #id ——>False
print(id(lst1))
print(id(lst2))
print(a is not b)#False a的id和b的id是不相等的
print(lst1 is not lst2)#True lst1的id和lst2的id是不相等的

#布尔运算符
a,b=1,2
print('-------------and 并且----------')
print(a==1 and b==2)#True    True and True——>True
print(a==1 and b<2)#False    True and False——>False
print(a!=1 and b==2)#False   False and True——>False
print(a!=1 and b!=2)#False   False and False——>False

print('-------------or 或者----------')
print(a==1 or b==2)#True    True or True——>True
print(a==1 or b<2)#True     True or False——>True
print(a!=1 or b==2)#True    False or True——>True
print(a!=1 or b!=2)#False   False or False——>False

print('-------------not 对bool类型的操作上取反----------')
f1=True
f2=False
print(not f1)
print(not f2)

print('-------------in 与 not in----------')
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s) #False
print('k' not in s) #True

#位运算符
print(4&8) #按位与 同为1时结果为1
print(4|8) #按位或 同为0时结果为0
print(4<<1)#向左移动1位（移动一个位置）相当于乘2
print(4<<2)#向左移动2位（移动一个位置）相当于乘4
print(4>>1)#向右移动1位（移动一个位置）相当于除以2
print(4>>2)#向右移动2位（移动一个位置）相当于除以4

#运算符的比较级：
#算术运算符：先算乘除，后算加减，有幂先算幂；
# 位运算；
# 比较运算符（结果为True或者False);
# 布尔运算；
# 赋值运算
#有括号先算括号