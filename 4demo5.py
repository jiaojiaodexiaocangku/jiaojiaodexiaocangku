'''条件表达式：if……else简写
x if 判断条件 else y
若判断条件的布尔值为True，条件表达式的返回值为x，否则条件返回值为y'''
'''从键盘录入两个整数，比较两个整数的大小'''
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
#比较大小
'''if num_a>=num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a,'小于',num_b)
 '''
print('使用条件表达式进入比较')
print(str(num_a)+'大于等于'+str(num_b)  if num_a>=num_b else  str(num_a)+'小于'+str(num_b))

'''Pass语句:什么都不做，只是一个占位符
何时用：先搭建语法结构，还没想好代码怎么写的时候
和哪些语句一起使用：if语句的条件执行体
                   for_in语句的循环体
                   定义语句时的函数体
'''
answer=input('您是会员吗？y/n')
if answer=='y':
    pass
else:
    pass
age=int(input('请输入您的年龄：'))
if age:
    print(age)
else:
    print('年龄为：',age)
