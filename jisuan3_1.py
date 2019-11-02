import tkinter as tk
from decimal import Decimal 
import math

def remove_exponent(num):#去零
    if (num == int(num)):
        return int(num)
    else:
        return str('{0:.9g}'.format(float(num)))

#右侧小键盘
def calcu(e):
    txt=str(e.widget.configure('text')[-1])
    if(txt=="AC"):
        result1.set("")
    elif(txt=="←"):
        result1.set(result1.get()[0:len(result1.get())-1])
    elif(txt=="Mod"):
        result1.set(result1.get()+"%")
    else:   
        result1.set(result1.get()+txt)
def btnEqual_Click():
    try:
        result2.set(result1.get())
        result=eval(result1.get())
        result=remove_exponent(round(result,9))
        result1.set(str(result))   
    except:
        result1.set("错误,请输入正确的计算公式") 

def func(key):#左侧小键盘
    txt=str(key.widget.configure('text')[-1])
    try:
        if(txt=='rad'):
            temp=result1.get()#得到当前输入框中的字符串
            result1.set(remove_exponent(math.radians(eval(temp))))
            result2.set("rad("+temp+")")

        elif(txt=='deg'):
            temp=result1.get()
            result1.set(remove_exponent(math.degrees(eval(temp))))
            result2.set("deg("+temp+")")
        elif(txt=='('):
            result1.set(result1.get()+txt)
        elif(txt==')'):
            result1.set(result1.get()+txt)
        elif(txt=='!'):
            temp=result1.get()
            if(eval(temp)>200):
                result1.set("溢出")
                result2.set("("+temp+")!")
            else:
                result1.set(round(float(math.factorial(eval(temp))),9))
                result2.set("("+temp+")!")
        elif(txt=='^2'):
            temp=result1.get()
            result1.set(remove_exponent(round(float(math.pow(eval(temp),2)),9)))
            result2.set("("+temp+")^2")
        elif(txt=='1/x'):
            temp=result1.get()
            result1.set(remove_exponent(round(1.0/int(temp),9)))
            result2.set("1/("+temp+")")      
        elif(txt=="√"):
            result2.set("√("+result1.get()+")")
            result=math.sqrt(eval(result1.get()))
            result=remove_exponent(round(result,9))
            result1.set(result)
        elif(txt=='sin'):
            temp=result1.get()
            result1.set(remove_exponent(round(math.sin(eval(temp)),9)))
            result2.set("sin("+temp+")")
        elif(txt=='cos'):
            temp=result1.get()
            result1.set(remove_exponent(round(math.cos(eval(temp)),9)))
            result2.set("cos("+temp+")")
        elif(txt=='tan'):
            temp=result1.get()
            result1.set(remove_exponent(round(math.tan(eval(temp)),9)))
            result2.set("tan("+temp+")")
        elif(txt=='lg'):
            temp=result1.get()
            result1.set(remove_exponent(round(math.log(eval(temp),10),9)))
            result2.set("lg("+temp+")")
        elif(txt=='ln'):
            temp=result1.get()
            result1.set(remove_exponent(round(math.log(eval(temp)),9)))
            result2.set("ln("+temp+")")
        elif(txt=='π'):
            result1.set(result1.get()+str(math.pi))
        elif(txt=='e'):
            result1.set(result1.get()+str(math.e))
    except:
        result1.set("错误,计算不符合规格")
        
form1=tk.Tk()
form1.minsize(615,385)
form1.title('计算器3.1')
form1.geometry("615x385+200+100")
form1.iconbitmap("jisuanqi/123.ico")

result1 = tk.StringVar()
result1.set('')                           #result1显示面板显示结果以及输入
result2 = tk.StringVar()                  #result2显示面板用于显示计算过程
result2.set('')

label = tk.Entry(form1,font = ('微软雅黑',20),insertwidth="0",justify="right",bg = '#EEE9E9',bd ='0',fg = '#828282',textvariable = result2)
label.grid(row=0,columnspan=2,sticky=tk.EW)
label2 = tk.Entry(form1,font = ('微软雅黑',30),insertwidth="0",justify="right",bg = '#EEE9E9',bd ='0',fg = 'black',textvariable = result1)
label2.grid(row=1,columnspan=2,sticky=tk.EW)


f1=tk.Frame(form1)
f1.grid(row=2,column=1,sticky=tk.EW)
f2=tk.Frame(form1)
f2.grid(row=2,column=0,sticky=tk.EW)
fh=["AC","Mod","←","/",7,8,9,"*",4,5,6,"-",1,2,3,"+","00",0,"."]
#行
ri=0 
#列
ci=0 
#通过循环遍历出按钮
for v in fh:
    if(ci!=0 and ci%4==0):
        ri+=1  #换行
        ci=0   #咧重新赋值
    btn1=tk.Button(f1,text=v,font=('微软雅黑',20),bd = 0.5,width = 5)
    btn1.bind("<Button-1>",calcu)
    btn1.grid(row=ri,column=ci)
    ci+=1
btnEqual=tk.Button(f1,text="=",font=('微软雅黑',20),bd = 0.5,width = 5,command=btnEqual_Click)
btnEqual.grid(row=4,column=3)
fh2=["sin","cos","tan","ln","lg","!","π","e","^2","(",")","√","1/x","rad","deg"]
ri2=0
ci2=0
for v in fh2:
    if(ci2!=0 and ci2%3==0):
        ri2+=1  #换行
        ci2=0   #咧重新赋值
    btn1=tk.Button(f2,text=v,font=('微软雅黑',20),bd = 0.5,width = 5)
    btn1.bind("<Button-1>",func)
    btn1.grid(row=ri2,column=ci2)
    ci2+=1

form1.mainloop()