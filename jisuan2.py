import tkinter as tk
import tkinter.messagebox as mesgbox


def calcu(e):
    txt=str(e.widget.configure('text')[-1])
    # if("="in varEntry1.get()):         #计算结束继续输入时清空
    #     varEntry1.set(txt)
    #     if(txt=="AC"):
    #         varEntry1.set("")
    #     elif(txt=="←"):
    #         varEntry1.set(varEntry1.get()[0:len(varEntry1.get())-1])   
    #     else:      
    #         varEntry1.set(varEntry1.get()+txt)
    if(txt=="AC"):
        varEntry1.set("")
    elif(txt=="←"):
        varEntry1.set(varEntry1.get()[0:len(varEntry1.get())-1])
    else:   
        varEntry1.set(varEntry1.get()+txt)
def btnEqual_Click():
    try:
        result=eval(varEntry1.get())
        varEntry1.set(str(result))
    except:
        mesgbox.showerror("错误","请输入正确的计算公式")
    pass




form1=tk.Tk()
form1.minsize(350,445)
form1.title('计算器')
form1.geometry("350x445")
# form1.iconbitmap("")    #左上角图标




#第一部分
#声明变量绑定entry控件
varEntry1=tk.StringVar()
entry1=tk.Entry(form1,fg="black",bg="white",textvariable=varEntry1)
entry1.grid(row=0,column=0,sticky=tk.EW,)


# #1.界面布局
# #显示面板
# result = tk.StringVar()
# result.set(0)                           #显示面板显示结果1，用于显示默认数字0
# result2 = tk.StringVar()           #显示面板显示结果2，用于显示计算过程
# result2.set('')
# #显示版
# label = tk.Label(form1,font = ('微软雅黑',20),bg = '#EEE9E9',bd ='9',fg = '#828282',anchor = 'se',textvariable = result2)
# # label.place(width = 280,height = 170)
# label.grid(row=0,column=0,sticky=tk.EW)
# label2 = tk.Label(form1,font = ('微软雅黑',30),bg = '#EEE9E9',bd ='9',fg = 'black',anchor = 'se',textvariable = result)
# # label2.place(y = 170,width = 280,height = 60)
# label2.grid(row=1,column=0,sticky=tk.EW)
#第二部分
#创建frame框架


f1=tk.Frame(form1)
f1.grid(row=2,column=0)

#开始创建按钮
#按钮文本的流标

#fh=[7,8,9,"X",4,5,6,"——",1,2,3,"+",0,".","AC","←"]
fh=["AC","%","←","/",7,8,9,"*",4,5,6,"-",1,2,3,"+",0,"00","."]
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