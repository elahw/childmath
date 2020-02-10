#! /usr/bin/python 
# -*- coding: UTF-8 -*-

import tkinter.messagebox as tm
import tkinter as tk
import random as rd
import time
import threading
import sys

def WelcomeWindow(Last_time):
    master = tk.Tk()
    #tm.showinfo("Hello World !")
    master.title('Maths Welcome You !')
    
    #sw = master.winfo_screenwidth()
    #sh = master.winfo_screenheight()
    #ww = 500
    #hh = 500
    #x = (sw - ww)/2
    #y = (sh - hh)/2
    #
    #master.geometry("%dx%d+%d+%d"%(ww,hh, x,y))

    #wc = tk.Label(master, text="欢迎来\n儿童数学训练营",font=("华文行楷", 40), fg="red", justify = "center")
    gif_file = tk.PhotoImage(file="/home/alex/Desktop/child_camp_picture/welcome_picture.gif")
    wc = tk.Label(master, image=gif_file)
    wc.pack()
    
    # set time lenght of Weclome GUI.
    def shutMaster():
        time.sleep(Last_time) 
        master.quit()

    func_quit = threading.Thread(target=shutMaster)
    func_quit.start()
    master.mainloop()



#*****************************************************
# Function: MathTypeChose
#
# Used    : 
#*****************************************************
def MathTypeChose():
    master = tk.Tk()
    master.title('Maths Type')
    sw = master.winfo_screenwidth()
    sh = master.winfo_screenheight()
    ww = 500
    hh = 500
    x = (sw - ww)/2
    y = (sh - hh)/2
    master.geometry("%dx%d+%d+%d"%(ww,hh, x,y))
    #master.geometry("%d+%d"%(x,y))
    
      
    tk.Label(master, text="请选择题型",font=("华文行楷",20), fg="red",justify="center").grid(row=0,column=1,columnspan=4,rowspan=3) 

    #tk.Label(master, text="计算大小",font=("华文行楷"), fg="black").grid(row=3,column=0,sticky="w") 
    #tk.LabelFrame(master, text="计算大小", padx=5, pady=5).grid(row=0,column=0)

    ############################ group 1 ##########################################
    group1 = tk.LabelFrame(master, text="计算大小", fg="blue", labelanchor='n')
    group1.grid(row=3,column=0, padx=10,pady=10)

    num_range = tk.IntVar()

    tk.Radiobutton(group1,text="30",  variable=num_range, value=30 ).grid(row=4, column=0, sticky="w")
    tk.Radiobutton(group1,text="50",  variable=num_range, value=50 ).grid(row=5, column=0, sticky="w")
    tk.Radiobutton(group1,text="100", variable=num_range, value=100).grid(row=6, column=0, sticky="w")
    tk.Radiobutton(group1,text="200", variable=num_range, value=200).grid(row=7, column=0, sticky="w")

    ent0 = tk.Label(group1, text="自定义：",font=("华文行楷",8), fg="black")
    ent0.grid(row=8,column=0, sticky="E")

    en0 = tk.Entry(group1,width=4)
    en0.grid(row=8, column=1,sticky="w")

    ## 得到数学题的运算范围
    #Ret_math_range = num_range.get() if en0.get()=="" else int(en0.get())

    ############################ group 2 ##########################################
    group2 = tk.LabelFrame(master, text="计算类型",fg="blue",  labelanchor='n')
    group2.grid(row=3,column=1, padx=10,pady=10)

    strs = tk.IntVar()
    tk.Radiobutton(group2,text="加",   variable=strs, value=1).grid(row=4, column=3, sticky="w")
    tk.Radiobutton(group2,text="减",   variable=strs, value=2).grid(row=5, column=3, sticky="w")
    tk.Radiobutton(group2,text="乘",   variable=strs, value=3).grid(row=6, column=3, sticky="w")
    tk.Radiobutton(group2,text="除",   variable=strs, value=4).grid(row=7, column=3, sticky="w")
    tk.Radiobutton(group2,text="混合", variable=strs, value=5).grid(row=8, column=3, sticky="w")

    ## 得到数学提的运算类型
    #Ret_math_type = strs.get()

     
    ############################ group 3 ##########################################
    group3 = tk.LabelFrame(master, text="多项运算",fg="blue", labelanchor='n')
    group3.grid(row=3,column=2, padx=10,pady=10)

    yun_num = tk.IntVar() 
    tk.Radiobutton(group3, text="两项", variable=yun_num, value=2).grid(row=4, column=4, sticky="w")
    tk.Radiobutton(group3, text="三项", variable=yun_num, value=3).grid(row=5, column=4, sticky="w")
    tk.Radiobutton(group3, text="四项", variable=yun_num, value=4).grid(row=6, column=4, sticky="w")
    tk.Label(group3, text=" ").grid(row=7, column=4, sticky="w")
    tk.Label(group3, text=" ").grid(row=8, column=4, sticky="w")
    ## 一道题有几个数参与运算
    #Ret_opera_num = yun_num.get()

     
    ############################ group 4 ##########################################
    group4 = tk.LabelFrame(master, text="题目数量",fg="blue", labelanchor='n')
    group4.grid(row=3,column=3, padx=10,pady=10)

    math_num = tk.IntVar()
    tk.Radiobutton(group4, text="200", variable=math_num, value=2).grid(row=4, column=0, sticky="w")
    tk.Radiobutton(group4, text="100", variable=math_num, value=3).grid(row=5, column=0, sticky="w")
    tk.Radiobutton(group4, text="50",  variable=math_num, value=4).grid(row=6, column=0, sticky="w")
    tk.Radiobutton(group4, text="30",  variable=math_num, value=5).grid(row=7, column=0, sticky="w")

    ent1 = tk.Label(group4, text="自定义：",font=("华文行楷",8), fg="black")
    ent1.grid(row=8,column=0, sticky="E")

    en1 = tk.Entry(group4,width=4)
    en1.grid(row=8, column=1, padx=0,sticky="w")
    
    # 得到需要计算的题目的数量
    #Ret_math_num =  math_num.get() if en1.get()=='' else en1.get()
    

    def SubmitType():
        global Ret_math_range
        global Ret_math_type
        global Ret_opera_num
        global Ret_math_num
        ## 得到数学题的运算范围
        if en0.get() != "":
            try:
                Ret_math_range = int(en0.get())
            except:
                txt = "计算大小: 自定义\"" + en0.get() + "\"不是有效的数字！"
                #tk.Message(master, text=txt).pack()
                tm.showwarning("注意",txt)
                return 0
        else:
            if num_range.get() == 0:
                txt = "请设置计算大小"
                tm.showwarning("注意",txt)
                return 0
            Ret_math_range = num_range.get()
        #print(Ret_math_range)
        
        ## 得到数学提的运算类型
        Ret_math_type = strs.get()
        if Ret_math_type == 0:
            txt = "请设置运算类型"
            tm.showwarning("注意:", txt)
            return 0
        #print(Ret_math_type)

        ## 一道题有几个数参与运算
        Ret_opera_num = yun_num.get()
        if Ret_opera_num == 0:
            txt = "请设置多项运算"
            tm.showwarning("注意:", txt)
            return 0
        #print(Ret_opera_num)


        ## 得到需要计算的题目的数量
        if en1.get() != "":
            try:
                Ret_math_range = int(en1.get())
            except:
                txt = "题目数量: 自定义\"" + en1.get() + "\"不是有效的数字！"
                #tk.Message(master, text=txt).pack()
                tm.showwarning("注意",txt)
                return 0
        else:
            Ret_math_num =  math_num.get()
            if math_num.get() == 0:
                txt = "请设置题目数量"
                tm.showwarning("注意",txt)
                return 0
        #print(Ret_math_num)
        master.quit()


    def ExitGui():
        master.quit()
        sys.exit(0) 

    tk.Button(master, text="题型已经选好", command=SubmitType, font=("华文行楷"), fg="blue",bg="yellow").grid(row=9, column=1, sticky="w")
    tk.Button(master, text="退出数学训练", command=ExitGui   , font=("华文行楷"), fg="blue",bg="yellow").grid(row=9, column=3, sticky="w")

    master.protocol("WM_DELETE_WINDOW",ExitGui) ## 点击GUI右上角的x，会退出程序，不再往下执行
    master.mainloop()
    

#************************************
# Function: GetUnionNumber( num )
#
# Used    : 得到所有小于Num的合数
#*************************************
def GetUnionNumber(Num):
    union_l = []
    for i in range(2, Num):
        for j in range(2, i):
            if i%j == 0:
                union_l.append(i)
                break
    #print (union_l, len(union_l) )
    return union_l, len(union_l)


#************************************
# Function: DecompositionPrime(Num)
#
# Used    : 得到Num的所有约数
#*************************************
def DecompositionPrime(Num):
    prime_l = []
    for i in range(2, Num+1):
        if Num%i == 0:
            prime_l.append(i)
    return prime_l, len(prime_l)



#************************************
# Function: GetPrimeNumber( num )
#
# Used    : 得到Num的所有的质数因子
#*************************************
def GetPrimeNumber(Num):
    prime_l, prime_num = DecompositionPrime(Num)
    print(prime_l)
    print(prime_num)
    for num in prime_l:
        for i in range(2,num//2):
            if num%i == 0:
                prime_l.remove(num)
                prime_num -= 1
                break
    print(prime_l)
    print(prime_num)
    return prime_l, prime_num


#***************************************************************
# Function: GetRandUnionPrime(Num)
#
# Used    : 随机返回Num以内的合数，并随机返回这个合数的一个因子
#***************************************************************
def GetRandUnionPrime(Num):
    union_l, union_num = GetUnionNumber(Num)
    rand_union = union_l[rd.randint(union_num)]
    print(rand_union)
    print(rand_union)
    
    prime_l, prime_num = DecompositionPrime(rand_union)
    rand_prime = prime_l[rd.randint(prime_num)]
    print(rand_prime)
    print(prime_l)

    return union_l, rand_prime





#************************************
# Function: GenerateMathProblem()
#
# Used    : 产生数学题
#*************************************
def GenerateMathProblem():
    # 产生一道题：
    name = () # ("题目"，结果)
    type_list = [1, 2, 3, 4] ## == ["加", "减"，"乘"，"除"]
    if Ret_math_type == 5:   ## 混合运算
        
        ## 有两个操作数
        if Ret_opera_num == 2:
            gen_type = type_list[rd.randint(1,4)]

            opera1 = rd.randint(1, Ret_math_range)
            if gen_type == 1: # 加
                opera2 = rd.randint(1, Ret_math_range)
                prob = str(opera1) + " + " + str(opera2) + " = "
                prob_tuple = (prob, opera1 + opera2)              
            elif gen_type == 2: # 减
                opera2 = rd.randint(1, opera1)    
                pro = str(opera1) + " - " + str(opera2) + " = "
                prob_tuple = (prob, opera1 - opera2)              
            elif gen_type == 3: # 乘
                opera2 = rd.randint(1, Ret_math_range)
                prob = str(opera1) + " × " + str(opera2) + " = "
                prob_tuple = (prob, opera1 * opera2)              
            elif gen_type == 4: # 除
                union_list, union_list_num = GetUnionNumber(Ret_math_range)
                opera1 = union_list[rd.randint(1,union_list_num)]
                prime_list, prime_list_num = DecompositionPrime(opera1)
                opera2 = prime_list[rd.randint(1,prime_list_num)]
                prob = str(opera1) + " ÷ " + str(opera2) + " = "
                prob_tuple = (prob, opera1 / opera2)              

        
        ## 有三个操作数
        elif Ret_opera_num == 3:
            type_list.append(type_list[rd.randint(1,4)])
            type_list.append(type_list[rd.randint(1,4)])
            
            if   type_list==[1,1]: # a + b + c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 + opera2 + opera3
            elif type_list==[1,2]: # a + b - c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, Ret_math_range)
                opera3 = rd.randint(1, opera1 + opera2)   
                #if (opera1 + opera2) > Ret_math_range:  # FIXME
                #    opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 + opera2 - opera3
            elif type_list==[1,3]: # a + b x c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 + (opera2 * opera3)
            elif type_list==[1,4]: # a + b / c
                opera1 = rd.randint(1, Ret_math_range)                
                union_list, union_list_num = GetUnionNumber(Ret_math_range)
                opera2 = union_list[rd.randint(1,union_list_num)]
                prime_list, prime_list_num = DecompositionPrime(opera2)
                opera3 = prime_list[rd.randint(1,prime_list_num)]
                prob_result =  opera1 + (opera2 / opera3)
                
            elif type_list==[2,1]: # a - b + c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, opera1)
                opera3 = rd.randint(1, Ret_math_range)   
                prob_result =  opera1 - opera2 + opera3
                
            elif type_list==[2,2]: # a - b - c
                tmp = rd.randint(2, Ret_math_range)
                opera2 = rd.randint(1, tmp)
                opera3 = tmp - opera2
                opera1 = rd.randint(tmp, Ret_math_range)
                prob_result =  opera1 - opera2 - opera3

            elif type_list==[2,3]: # a - b x c
                tmp, opera2 = GetUnionNumber(Ret_math_range)
                opera3 = tmp/opera2
                opera1 = rd.randint(tmp, Ret_math_range) 
                prob_result = opera1 - opera2 * opera3 

            elif type_list==[2,4]: # a - b / c
                opera2, opera3 = GetUnionNumber(Ret_math_range)
                tmp = opera2/opera3
                opera1 = rd.randint(tmp, Ret_math_range) 
                prob_result = opera1 - opera2 / opera3 
            elif type_list==[3,1]: # a * b + c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 * opera2 + opera3
            elif type_list==[3,2]: # a * b - c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                if opera1 * opera2 < opera3:
                    opera3 = rd.randint(1, opera1 * opera2)
                prob_result =  opera1 * opera2 - opera3
                
            elif type_list==[3,3]: # a * b * c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 * opera2 - opera3

            elif type_list==[3,4]: # a * b / c
                opera1 = rd.randint(1, Ret_math_range)
                opera2 = rd.randint(1, Ret_math_range)
                prime_list, prime_list_num = DecompositionPrime(opera1 * opera2)
                opera3 = prime_list[rd.randint(prime_list_num)]
                prob_result =  opera1 * opera2 / opera3

            elif type_list==[4,1]: # a / b + c
                opera1, opera2 = GetRandUnionPrime(Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 / opera2 + opera3
                
            elif type_list==[4,2]: # a / b - c
                opera1, opera2 = GetRandUnionPrime(Ret_math_range)
                opera3 = rd.randint(1, opera1/opera2)
                prob_result =  opera1 / opera2 - opera3

            elif type_list==[4,3]: # a / b * c
                opera1, opera2 = GetRandUnionPrime(Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 / opera2 * opera3 
            elif type_list==[4,4]: # a / b / c
                union_list, union_list_num  = GetUnionNumber(Ret_math_range)
                while 1: 
                    tmp =  union_list[rd.randint(union_list_num)]
                    prime_list, prime_list_num = GetPrimeNumber(tmp)
                    if prime_list_num > 2:
                        break
                opera1 = tmp
                opera2 = prime_list[rd.randint(prime_list_num)]
                opera3 = prime_list[rd.randint(prime_list_num)]
                prob_result =  opera1 / opera2 / opera3 
                

            
    

####################### Main ###########################
if __name__ == "__main__":

    WELCOM_TIME = 2
    
    #WelcomeWindow(WELCOM_TIME)
    #time.sleep(WELCOM_TIME)
    #MathTypeChose()
    #print(Ret_math_range, Ret_math_type, Ret_opera_num, Ret_math_num)

    #GetRandUnionPrime(100)
    GetPrimeNumber(100)
