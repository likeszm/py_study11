#学习记录11: 异常

"""
1.异常发生后会运行其中一个 except ,可以通过异常类型来增加更多的细节,也可以就纯写一个 except 来笼统的报错
2.通过打印异常对象，可以更加详细的了解异常细节
3.如果是没有异常的情况，建议使用 else
4.不论如何,  finally 后的语句都会运行
5.利用raise手动触发自定义类型的异常,只要记得继承自 Exception 类就行

例如用户输入数据的部分可以利用异常来告知用户输入类型有误
"""

#1.尝试从编译器内手动获取异常,从运行结果可以得到异常类型: ZeroDivisionError
"""
a = 100/0
"""

#2.然后就可以捕获异常
"""
try :
    a = 100 / 0
except ZeroDivisionError :
    print("捕获到除数为0的异常")
"""

#3.异常类型可以有多种
"""
try:
    if 1 :
        a = '0' / 1     #异常类型: TypeError
    else :
        a = 1 / 0       #异常类型: ZeroDivisionError
except TypeError:
    print("类型异常!")
except ZeroDivisionError :
    print("除0异常!")
"""

#4.意料之外的异常类型, 任何异常都是Exception的子类,所以用这个异常类型来捕获全部的异常
"""
try :
    a = 0 / 0           #异常类型: ZeroDivisionError
except TypeError :
    print("类型错误!")
except :                  #用于捕获没有写出来的类型的错误
    print("未知的错误类型!")
"""

"""
try :
    a = 0 / 0           #异常类型: ZeroDivisionError
except TypeError :
    print("类型错误!")
except Exception :       #用于捕获没有写出来的类型的错误
    print("未知的错误类型!")
"""

#5.else的使用
"""
try :
    a = 0 / 1           #异常类型: ZeroDivisionError
except TypeError :
    print("类型错误!")
except :                  #用于捕获没有写出来的类型的错误
    print("未知的错误类型!")
else :
    print("运行成功!!")
"""

#6.finally的使用
"""
try :
    a = 0 / 0             #异常类型: ZeroDivisionError
except TypeError :
    print("类型错误!")
except :                  #用于捕获没有写出来的类型的错误
    print("未知的错误类型!")
else :
    print("运行成功!!")
finally :
    print("不论正确与否，运行结束")
"""

#7.异常对象: py解释器报错就会打印出这个，我们也可以手动打印
"""
try:
    100/0
except ZeroDivisionError as e:
    print (f'异常对象信息:{e}')
"""

#8.获取异常的详细信息
"""
import traceback

try:
    100/0
except :
    print(traceback.format_exc())
"""

#9.主动抛出自定义类型的异常
"""
class MY_ERROR1(Exception) :
    pass

class MY_ERROR2(Exception) :
    pass

test = 1

if test == 1 :
    raise MY_ERROR1()
elif test == 2 :
    raise MY_ERROR2()
"""
