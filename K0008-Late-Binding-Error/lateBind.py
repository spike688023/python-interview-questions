def multipliers():
    return [lambda x : i*x for i in range(4)]

for m in multipliers():
    print m(2)

"""  還是不懂，但就 貼上來吧
在这里我们做了以下几个动作：
1、 创建了包含了4个函数的列表
2、 这些函数是什么呢？-- fun(x): return i*x
3、 在这个阶段Python并不关心i和x的值
4、 但是在循环结束之后i 的值就成了3



现在在调用这些函数：

for f in fun_list:
        print f(2)


        5、 调用f(2)，它会返回i*x
        6、 这里x等于2，i等于3，所以调用f(2)会返回6

Reference:
    https://python.freelycode.com/contribution/detail/127
"""

