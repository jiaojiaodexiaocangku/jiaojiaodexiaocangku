#print函数
#输出数字
print(520)

#输出字符串
print("helloworld")
print('helloworld')

#输出含运算符的表达式
print(3+1)

#数据输出到文件中;注意：1，所指定的盘符存在，2，使用file=fp
fp=open('E:/text.txt','a+')#a+如果文件不存在就创建，存在就在文件内容的后面继续追加。
print('helloworld',file=fp)
fp.close()

#不进行换行输出
print('hello','world','python')

#转义字符
print('hello\nworld')#\+转义功能的首字母  n——>newline的首字母表示换行
print('hello\tworld')
print('helloooo\tworld')#\t——>水平制表符，4位为一个制表位
print('hello\rworld')#r-->return的首字母表示回车，world将hello覆盖了
print('hello\bworld')#\b是退一个格
print('http:\\\\www.baidu.com')
print('老师说:\'大家好\'')

#原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或者R
#注意事项：最后一个字符不能是反斜杠，但是可以是双斜杠
#print(r'hello\nworld\')
print(r'hello\nworld')
print(r'hello\nworld\\')
input()