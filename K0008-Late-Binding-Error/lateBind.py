def multipliers():
    return [lambda x : i*x for i in range(4)]


i = 0
print(lambda x = 2 : i*x for i in range(4))
print(i)


what = [lambda x : i*x for i in range(4)]
print(what)
print("what[0](2) = " + str(what[0](2)))
print("what[1](2) = " + str(what[1](2)))

for m in multipliers():
    print(m)
    print(m(2))


"""
def 這塊突然看的懂了

把lambda x 看成 func(x) 但是沒有給它名稱 ， x 是之後 用的時侯會給 的值，

所 以後的不一定要給 ，  但這裡有另一個變數就要先給 了，

range(4) 會跑出0 1 2 3 ，所以 這裡是要建立一個func list

[f(0*x), f(1*x), f(2*x), f(3*x)]

確實也有被建出來， 但之後 引用的時侯,  i變數又重新跑了一次。


被建出來的樣子，不是上面的樣子，

應該 是這樣

[f(i*x), f(i*x), f(i*x), f(i*x)]

"""

"""  還是不懂，但就 貼上來吧
在这里我们做了以下几个动作：
1、 创建了包含了4个函数的列表
2、 这些函数是什么呢？-- fun(x): return i*x
3、 在这个阶段Python并不关心i和x的值
4、 但是在循环结束之后i 的值就成了3



现在在调用这些函数：

喔 ，  下面的這段 code沒錯，只不過，它是用python2.x 。
for f in fun_list:
        print f(2)


        5、 调用f(2)，它会返回i*x
        6、 这里x等于2，i等于3，所以调用f(2)会返回6

Reference:
    https://python.freelycode.com/contribution/detail/127
"""

