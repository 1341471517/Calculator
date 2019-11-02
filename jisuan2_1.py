import tkinter as tk
import tkinter.messagebox as mesgbox
from decimal import Decimal 
import cmath


def remove_exponent(num):
    return num.to_integral() if num == num.to_integral() else num.normalize()
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
        result=Decimal(eval(result1.get()))
        # 输出结果由小数计算后是整数会多出小数点，想办法去掉
        # 最多保留九位小数，可以后续开发出选择保留几位小数的选项
        result=remove_exponent(round(result,9))  #去除保留小数后的多余零
        result1.set(str(result))   

    except:
        mesgbox.showerror("错误","请输入正确的计算公式")

form1=tk.Tk()
form1.minsize(350,420)
form1.title('计算器')
form1.geometry("350x420+200+100")


result1 = tk.StringVar()
result1.set('')                           #result1显示面板显示结果以及输入
result2 = tk.StringVar()                  #result2显示面板用于显示计算过程
result2.set('')

#显示版
label = tk.Label(form1,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = result2)
label.place(width = 350,height = 70)
label2 = tk.Label(form1,font = ('微软雅黑',30),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result1)
label2.place(y=70,width = 350,height = 60)

#第二部分
#创建frame框架
f1=tk.Frame(form1)
f1.grid(sticky=tk.EW)
f1.place(y=130)

#开始创建按钮
#按钮文本的流标
#现在只考虑最基础的计算器，并不考虑科学计算器等工能
fh=["AC","Mod","←","/",7,8,9,"*",4,5,6,"-",1,2,3,"+",0,"00","."]
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

form1.mainloop()