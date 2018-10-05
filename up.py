import tkinter

root = tkinter.Tk()
root.maxsize(280, 500)
root.title('**的计算器')

# 1.界面布局
# 显示面板
result = tkinter.StringVar()
result.set(0)  # 显示面板1，用于显示默认结果0
result2 = tkinter.StringVar()
result2.set('')  # 显示面板2，用于显示计算结果
# 显示板
label = tkinter.Label(root, font=('微软雅黑', 20), bg='#EEE9E9', bd='9', fg='#828282',
                      anchor='se', textvariable=result2)
label.place(width=280, height=170)
label2 = tkinter.Label(root, font=('微软雅黑', 30), bg='#EEE9E9', bd='9', fg='black', anchor='se', textvariable=result)
label2.place(y=170, width=280, height=60)

# 数字按钮

btn7 = tkinter.Button(root, text='7', font=('微软雅黑', 20), fg=('#4F4F4F'), bd=0.5, command=lambda: pressNum('7'))
btn7.place(x=0, y=285, width=70, height=55)
btn8 = tkinter.Button(root, text='8', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('8'))
btn8.place(x=70, y=285, width=70, height=55)
btn9 = tkinter.Button(root, text='9', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('9'))
btn9.place(x=140, y=285, width=70, height=55)
btn4 = tkinter.Button(root, text='4', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('4'))
btn4.place(x=0, y=340, width=70, height=55)
btn5 = tkinter.Button(root, text='5', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('5'))
btn5.place(x=70, y=340, width=70, height=55)
btn6 = tkinter.Button(root, text='6', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('6'))
btn6.place(x=140, y=340, width=70, height=55)
btn1 = tkinter.Button(root, text='1', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('1'))
btn1.place(x=0, y=395, width=70, height=55)
btn2 = tkinter.Button(root, text='2', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('2'))
btn2.place(x=70, y=395, width=70, height=55)
btn3 = tkinter.Button(root, text='3', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('3'))
btn3.place(x=140, y=395, width=70, height=55)
btn0 = tkinter.Button(root, text='0', font=('微软雅黑', 20), fg='#4F4F4F', bd=0.5, command=lambda: pressNum('0'))
btn0.place(x=70, y=450, width=70, height=55)

# 运算符按钮
btnac = tkinter.Button(root, text='AC', bd=0.5, font=('黑体', 20), fg='orange', command=lambda: pressCompute('AC'))
btnac.place(x=0, y=230, width=70, height=55)
btnback = tkinter.Button(root, text='<--', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressCompute('b'))
btnback.place(x=70, y=230, width=70, height=55)
btndivi = tkinter.Button(root, text='÷', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressCompute('/'))
btndivi.place(x=140, y=230, width=70, height=55)
btnmult = tkinter.Button(root, text='×', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressCompute('*'))
btnmult.place(x=210, y=230, width=70, height=55)
btnsub = tkinter.Button(root, text='-', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressCompute('-'))
btnsub.place(x=210, y=285, width=70, height=55)
btnadd = tkinter.Button(root, text='+', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressCompute('+'))
btnadd.place(x=210, y=340, width=70, height=55)
btnequal = tkinter.Button(root, text='=', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressEqual())
btnequal.place(x=210, y=395, width=70, height=110)
btnper = tkinter.Button(root, text='%', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressCompute('%'))
btnper.place(x=0, y=450, width=70, height=55)
btnpoint = tkinter.Button(root, text='.', bd=0.5, font=('微软雅黑', 20), fg='#4F4F4F', command=lambda: pressCompute('.'))
btnpoint.place(x=140, y=450, width=70, height=55)

# 操作函数
lists = []  # 设置一个变量，保存运算数字和符号的列表
isPressSign = False  # 添加一个判断是否按下运算符号的标志，假设默认没有按下按钮


# 假设没有按下数字

# 数字函数
def pressNum(num):
    # 全局化变量
    global lists
    global isPressSign
    # 判断result是不是运算符
    if isPressSign == False:
        pass
    else:
        result.set(0)
        isPressSign = False
    # 将当前result写入lists
    oldNum = result.get()
    if result.get() == '0':
        result.set(num)
    else:
        newNum = oldNum + num
        result.set(newNum)


# 运算符函数
def pressCompute(sign):
    global lists
    global isPressSign
    # 将数字写入lists
    a = result.get()
    lists.append(a)
    lists.append(sign)
    # isPressSign变为True
    isPressSign = True

    if sign == 'AC':
        lists.clear()
        result.set(0)  # 当前数字变为0
    if sign == 'b':
        newA = a[0:-1]
        lists.clear()
        result.set(newA)  # 当前数字变为第一个到倒数第二个


# 结果函数
def pressEqual():
    global lists
    global isPressSign
    curnum = result.get()  # 得到当前屏幕数字
    lists.append(curnum)  # 将数字添加到列表
    strLists = ''.join(lists)  # 将列表字符组成字符串
    result_strLists = eval(strLists)  # 计算字符串的结果
    result.set(result_strLists)
    result2.set(strLists)


root.mainloop()
