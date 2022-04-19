print(chr(0b100111001011000))#ob表示二进制
print(ord('乘'))#ord表示十进制
import keyword
print(keyword.kwlist)#查找保留字（给任何对象起名字都不能用）
name='马丽亚'
print(name)
print('标识',id(name))#表示对象所存储的内存地址
print('类型',type(name))
print('值',name)
name='马丽亚'
name='楚溜冰'#多次赋值之后，变量名会指向新的空间
print(name)
input()



