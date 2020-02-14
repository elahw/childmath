#! /usr/bin/python 
# -*- coding: UTF-8 -*-
import tkinter.messagebox as tm
import tkinter as tk
import random as rd
import time
import threading
import sys
import os

#********************************************
# Function: WelcomeAndPraise()
#
# Used    : 如果得了100分或0分，显示表扬界面
#********************************************
def WelcomeAndPraise(welcome_flag, score):
    praw = tk.Tk()
    praw.title("评语板")

    
    if welcome_flag==0:
        praw.title("评语板")
        if score == 100:
            gif_file = tk.PhotoImage(file=SCORE_100)
            (ww, hh) = (305 , 330)
        elif score == 0:
            gif_file = tk.PhotoImage(file=SCORE_000)
            (ww, hh) = (495 , 250)
        elif score >= 60: ## FIXME 及格，继续努力
            gif_file = tk.PhotoImage(file=SCORE_060)
            (ww, hh) = (870 , 530)
        else:             ## FIXME 不及格，要更加努力才行啊！
            gif_file = tk.PhotoImage(file=SCORE_059)
            (ww, hh) = (720 , 450)
    else:
        praw.title('Maths Welcome You !')
        gif_file = tk.PhotoImage(file=WELCOME_GIF)
        (ww, hh) = (1200 , 700)

    tk.Label(praw, image=gif_file).pack()



    sw = praw.winfo_screenwidth()
    sh = praw.winfo_screenheight()
    #ww = praw.winfo_reqwidth()
    #hh = praw.winfo_reqheight()
    x = (sw - ww)/2
    y = (sh - hh)/2
    praw.geometry("+%d+%d"%(x,y))


    praw.after(WAIT_TIME, praw.destroy)
    praw.mainloop()


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
    ww = 475
    hh = 300
    x = (sw - ww)/2
    y = (sh - hh)/2
    master.geometry("%dx%d+%d+%d"%(ww,hh, x,y))
    
      
    tk.Label(master, text="请选择题型",font=("华文行楷",16), fg="Purple",justify="center").grid(row=0,column=0,columnspan=6,rowspan=3) 
    
    group_ft = ("宋体", 13, "bold")
    group_fg = "blue"
    item_ft  = ("宋体", 13)
    item_fg  = "black"
    ############################ group 1 ##########################################
    group1 = tk.LabelFrame(master, text="计算大小",font=group_ft, fg=group_fg, labelanchor='n')
    group1.grid(row=3,column=0, padx=5,pady=5)

    num_range = tk.IntVar()

    tk.Radiobutton(group1,text="30" , font=item_ft, fg=item_fg, variable=num_range, value=30 ).grid(row=4, column=0, sticky="w")
    tk.Radiobutton(group1,text="50" , font=item_ft, fg=item_fg, variable=num_range, value=50 ).grid(row=5, column=0, sticky="w")
    tk.Radiobutton(group1,text="100", font=item_ft, fg=item_fg, variable=num_range, value=100).grid(row=6, column=0, sticky="w")
    tk.Radiobutton(group1,text="200", font=item_ft, fg=item_fg, variable=num_range, value=200).grid(row=7, column=0, sticky="w")

    ent0 = tk.Label(group1, text="自定义：", font=("华文行楷",12), fg=item_fg)
    ent0.grid(row=8,column=0, sticky="E")

    en0 = tk.Entry(group1, width=4, font=("华文行楷",12))
    en0.grid(row=8, column=1,sticky="w",padx=5)

    ## 得到数学题的运算范围
    #Ret_math_range = num_range.get() if en0.get()=="" else int(en0.get())

    ############################ group 2 ##########################################
    group2 = tk.LabelFrame(master, text="计算类型",font=group_ft, fg=group_fg,  labelanchor='n')
    group2.grid(row=3,column=1, padx=5,pady=5)

    strs = tk.IntVar()
    tk.Radiobutton(group2,text="加"  ,font=item_ft, fg=item_fg, variable=strs, value=1).grid(row=4, column=3, columnspan=2, sticky="w")
    tk.Radiobutton(group2,text="减"  ,font=item_ft, fg=item_fg, variable=strs, value=2).grid(row=5, column=3, sticky="w")
    tk.Radiobutton(group2,text="乘"  ,font=item_ft, fg=item_fg, variable=strs, value=3).grid(row=6, column=3, sticky="w")
    tk.Radiobutton(group2,text="除"  ,font=item_ft, fg=item_fg, variable=strs, value=4).grid(row=7, column=3, sticky="w")
    tk.Radiobutton(group2,text="混合",font=item_ft, fg=item_fg, variable=strs, value=5).grid(row=8, column=3, sticky="w")

     
    ############################ group 3 ##########################################
    group3 = tk.LabelFrame(master, text="多项运算",font=group_ft, fg=group_fg, labelanchor='n')
    group3.grid(row=3,column=2, padx=5,pady=5)

    yun_num = tk.IntVar()
    tk.Radiobutton(group3, text="两项", font=item_ft, fg=item_fg, variable=yun_num, value=2).grid(row=4, column=4, sticky="w")
    tk.Radiobutton(group3, text="三项", font=item_ft, fg=item_fg, variable=yun_num, value=3).grid(row=5, column=4, sticky="w")
    tk.Label(group3, text=" ", font=item_ft, fg=item_fg).grid(row=6, column=4, sticky="w")
    tk.Label(group3, text=" ", font=item_ft, fg=item_fg).grid(row=7, column=4, sticky="w")
    tk.Label(group3, text=" ", font=item_ft, fg=item_fg).grid(row=8, column=4, sticky="w")
     

    ############################ group 4 ##########################################
    group4 = tk.LabelFrame(master, text="题目数量", font=group_ft, fg=group_fg, labelanchor='n')
    group4.grid(row=3,column=3, padx=5,pady=5)

    math_num = tk.IntVar()
    tk.Radiobutton(group4, text="200", font=item_ft, fg=item_fg, variable=math_num, value=200).grid(row=4, column=0, sticky="w")
    tk.Radiobutton(group4, text="100", font=item_ft, fg=item_fg, variable=math_num, value=100).grid(row=5, column=0, sticky="w")
    tk.Radiobutton(group4, text="50" , font=item_ft, fg=item_fg, variable=math_num, value=50).grid(row=6, column=0, sticky="w")
    tk.Radiobutton(group4, text="30" , font=item_ft, fg=item_fg, variable=math_num, value=30).grid(row=7, column=0, sticky="w")

    ent1 = tk.Label(group4, text="自定义：",font=("华文行楷",12), fg=item_fg)
    ent1.grid(row=8,column=0, sticky="E")

    en1 = tk.Entry(group4, font=("华文行楷",12), width=4)
    en1.grid(row=8, column=1, padx=5, sticky="w")
    

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
                Ret_math_num = int(en1.get())
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
        master.destroy()


    def ExitGui():
        master.destroy()
        sys.exit(0) 

    tk.Button(master, text="选好", command=SubmitType, font=("华文行楷", 12), fg="blue",bg="yellow", width=6).grid(row=9, column=1, sticky="w")
    tk.Button(master, text="退出", command=ExitGui   , font=("华文行楷", 12), fg="blue",bg="yellow", width=6).grid(row=9, column=2, sticky="E")

    master.protocol("WM_DELETE_WINDOW",ExitGui) ## 点击GUI右上角的x，会退出程序，不再往下执行
    master.mainloop()
    

#**********************************************
# Function: GetUnionNumber( num )
#
# Used    : 得到所有小于Num的合数,和其数量
#**********************************************
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
# Function: GetPrimeNumber( n )
#
# Used    : 得到Num的所有的质数因子
#*************************************
def GetPrimeNumber(Num):
    prime_l, prime_num = DecompositionPrime(Num)
    #print(prime_l)
    #print(prime_num)
    prime_l2 = prime_l.copy()
    for n in prime_l:
        for i in range(2,n):
            if n%i == 0:
                prime_l2.remove(n)
                break
    return prime_l2, len(prime_l2)


#*******************************************************************
# Function: GetRandUnionPrime(Num)
#
# Used    : 随机返回小于Num的一个合数，并随机返回这个合数的一个约数
#*******************************************************************
def GetRandUnionPrime(Num):
    union_l, union_num = GetUnionNumber(Num)
    rand_union = union_l[rd.randint(0,union_num-1)]
    #print(rand_union)
    #print(rand_union)
    
    prime_l, prime_num = DecompositionPrime(rand_union)
    rand_prime = prime_l[rd.randint(0,prime_num-1)]
    #print(rand_prime)
    #print(prime_l)

    return rand_union, rand_prime





#************************************
# Function: GenerateMathProblem()
#
# Used    : 产生数学题
#*************************************
def GenerateMathProblem():
    # 产生一道题：
    name = () # ("题目"，结果)
    type_list = [1, 2, 3, 4] ## == ["加", "减"，"乘"，"除"]
    type_dic  = {1:" + ", 2:" - ", 3:" × ", 4:" ÷ "}
            
    opera1 = rd.randint(1, Ret_math_range)
    opera2 = rd.randint(1, Ret_math_range)
    opera3 = rd.randint(1, Ret_math_range)

    if Ret_math_type == 5:
        # 三个操作数时用到
        gen_types = []
        gen_types.append(type_list[rd.randint(0,3)])
        gen_types.append(type_list[rd.randint(0,3)])
        # 两个操作数时用到
        gen_type = type_list[rd.randint(0,3)]
    else:
        gen_types = [Ret_math_type, Ret_math_type]
        gen_type  = Ret_math_type
    

    if Ret_math_type == 5:   ## 混合运算
        
        ## 有两个操作数
        if Ret_opera_num == 2:

            #opera1 = rd.randint(1, Ret_math_range)
            #opera2 = rd.randint(1, Ret_math_range)
            if gen_type == 1: # 加
                prob_result = opera1 + opera2
            elif gen_type == 2: # 减
                opera2 = rd.randint(1, opera1)    
                prob_result = opera1 - opera2
            elif gen_type == 3: # 乘
                prob_result = opera1 * opera2
            elif gen_type == 4: # 除
                union_list, union_list_num = GetUnionNumber(Ret_math_range)
                opera1 = union_list[rd.randint(0,union_list_num-1)]
                prime_list, prime_list_num = DecompositionPrime(opera1)
                opera2 = prime_list[rd.randint(0,prime_list_num-1)]

                prob_result = int(opera1 / opera2)

            #prob = str(opera1) + type_dic[gen_type] + str(opera2) + " = "
            #prob_tuple = (prob, prob_result)   
            #print (prob, prob_result)

        
        ## 有三个操作数
        elif Ret_opera_num == 3:
            #gen_types = []
            #gen_types.append(type_list[rd.randint(0,3)])
            #gen_types.append(type_list[rd.randint(0,3)])

            if gen_types==[1,1]: # a + b + c
                prob_result =  opera1 + opera2 + opera3
            elif gen_types==[1,2]: # a + b - c
                opera3 = rd.randint(1, opera1 + opera2)   
                #if (opera1 + opera2) > Ret_math_range:  # FIXME
                #    opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 + opera2 - opera3
            elif gen_types==[1,3]: # a + b x c
                prob_result =  opera1 + (opera2 * opera3)
            elif gen_types==[1,4]: # a + b / c
                union_list, union_list_num = GetUnionNumber(Ret_math_range)
                opera2 = union_list[rd.randint(1,union_list_num-1)]
                prime_list, prime_list_num = DecompositionPrime(opera2)
                opera3 = prime_list[rd.randint(1,prime_list_num-1)]
                prob_result =  opera1 + (opera2 // opera3)
                
            elif gen_types==[2,1]: # a - b + c
                opera2 = rd.randint(1, opera1)
                opera3 = rd.randint(1, Ret_math_range)   
                prob_result =  opera1 - opera2 + opera3
                
            elif gen_types==[2,2]: # a - b - c
                tmp = rd.randint(2, Ret_math_range)
                opera2 = rd.randint(1, tmp)
                opera3 = tmp - opera2
                opera1 = rd.randint(tmp, Ret_math_range)
                prob_result =  opera1 - opera2 - opera3

            elif gen_types==[2,3]: # a - b x c
                tmp, opera2 = GetRandUnionPrime(Ret_math_range)
                opera3 = int(tmp/opera2)
                opera1 = rd.randint(tmp, Ret_math_range) 
                prob_result = opera1 - opera2 * opera3 

            elif gen_types==[2,4]: # a - b / c
                opera2, opera3 = GetRandUnionPrime(Ret_math_range)
                tmp = opera2/opera3
                opera1 = rd.randint(tmp, Ret_math_range) 
                prob_result = opera1 - int(opera2 / opera3) 
            elif gen_types==[3,1]: # a * b + c
                prob_result =  opera1 * opera2 + opera3
            elif gen_types==[3,2]: # a * b - c
                if opera1 * opera2 < opera3:
                    opera3 = rd.randint(1, opera1 * opera2)
                prob_result =  opera1 * opera2 - opera3
                
            elif gen_types==[3,3]: # a * b * c
                prob_result =  opera1 * opera2 - opera3

            elif gen_types==[3,4]: # a * b / c
                prime_list, prime_list_num = DecompositionPrime(opera1 * opera2)
                opera3 = prime_list[rd.randint(0,prime_list_num-1)]
                prob_result =  int(opera1 * opera2 / opera3)

            elif gen_types==[4,1]: # a / b + c
                opera1, opera2 = GetRandUnionPrime(Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 // opera2 + opera3
                
            elif gen_types==[4,2]: # a / b - c
                opera1, opera2 = GetRandUnionPrime(Ret_math_range)
                opera3 = rd.randint(1, opera1//opera2)
                prob_result =  opera1 // opera2 - opera3

            elif gen_types==[4,3]: # a / b * c
                opera1, opera2 = GetRandUnionPrime(Ret_math_range)
                opera3 = rd.randint(1, Ret_math_range)
                prob_result =  opera1 // opera2 * opera3 
            elif gen_types==[4,4]: # a / b / c
                while 1:
                    opera2 = rd.randint(2, Ret_math_range//2)
                    opera3 = rd.randint(2, Ret_math_range//2)
                    opera1 = opera2 * opera3 * rd.randint(2, Ret_math_range//2)
                    if opera1 <= Ret_math_range:
                        break
                prob_result =  int(opera1 / opera2 / opera3)
                
            #prob_tuple = str(opera1) + type_dic[gen_types[0]] + str(opera2) + type_dic[gen_types[1]] + str(opera3) + " = " 
            #print (prob_tuple, prob_result)
    
    elif Ret_math_type == 1:
        if Ret_opera_num == 2:
            prob_result = opera1 + opera2
        else:
            prob_result = opera1 + opera2 + opera3
    
    elif Ret_math_type == 2:
        if Ret_opera_num == 2:
            opera2 = rd.randint(1, opera1)    
            prob_result = opera1 - opera2
        else:
            tmp = rd.randint(2, Ret_math_range)
            opera2 = rd.randint(1, tmp)
            opera3 = tmp - opera2
            opera1 = rd.randint(tmp, Ret_math_range)
            prob_result =  opera1 - opera2 - opera3
            
    elif Ret_math_type == 3:
        if Ret_opera_num == 2:
            prob_result = opera1 * opera2
        else:
            prob_result = opera1 * opera2 * opera3
    elif Ret_math_type == 4:
        if Ret_opera_num == 2:
            union_list, union_list_num = GetUnionNumber(Ret_math_range)
            opera1 = union_list[rd.randint(0,union_list_num-1)]
            prime_list, prime_list_num = DecompositionPrime(opera1)
            opera2 = prime_list[rd.randint(0,prime_list_num-1)]

            prob_result = int(opera1 / opera2)
        else:
            while 1:
                opera2 = rd.randint(2, Ret_math_range//2)
                opera3 = rd.randint(2, Ret_math_range//2)
                opera1 = opera2 * opera3 * rd.randint(2, Ret_math_range//2)
                if opera1 <= Ret_math_range:
                    break
            prob_result =  int(opera1 / opera2 / opera3)
    
    if Ret_opera_num == 2:
        prob_tuple = str(opera1) + type_dic[gen_type] + str(opera2) + " = "
    else:
        prob_tuple = str(opera1) + type_dic[gen_types[0]] + str(opera2) + type_dic[gen_types[1]] + str(opera3) + " = " 

    #print(prob_tuple, prob_result) 
    return (prob_tuple, prob_result)


#************************************
# Function: GenerateAllProblem()
#
# Used    : 产生所有数学题
#*************************************
def GenerateAllProblem(problem_number):
    problem_tuple = ()
    problem_list = []
    for i in range(problem_number):
        problem_tuple = GenerateMathProblem()
        #print (problem_tuple)
        problem_list.append(problem_tuple)
    #print(problem_list)
    return problem_list



#************************************
# Function: ProblemWin()
#
# Used    : 产生题目的大窗口
#*************************************
def ProblemWin(problem_list):
    prowin = tk.Tk()

    win_title = "第%1d组 共%1d组" %(Array_no, Arry_Num) 
    prowin.title(win_title)

    sw       = prowin.winfo_screenwidth()
    sh       = prowin.winfo_screenheight()
    (ww, hh) = (350, 670)
    (x, y)   = ((sw - ww)/2,(sh - hh)/2) 
    prowin.geometry("%dx%d+%d+%d"%(ww,hh,x,y))
    
    if Array_no < Arry_Num:
        arry_problem_list = problem_list[(Array_no-1)*10:Array_no*10 ]
    else:
        arry_problem_list = problem_list[(Array_no-1)*10:]
        

    i = 0
    entry_list = []
    for sing_prob in arry_problem_list:
        
        prob_txt = sing_prob[0] 

        label_entry_ft = ("time", 20)
        label_entry_fg = "blue"
        tk.Label(prowin, text =prob_txt, font=label_entry_ft, fg=label_entry_fg, width=10).grid(row=i, column=0, sticky="E",padx=10, pady=10)
        enty = tk.Entry(prowin,font=label_entry_ft, fg=label_entry_fg, width=6)
        enty.grid(row=i, column=1, sticky="W",padx=10, pady=10)

        entry_list.append(enty)
        i += 1

    def NextArray():
        global Array_no
        global Answer_Tuple_List
        
        for en_no in range(len(entry_list)):
            try:
                if entry_list[en_no].get()=="":
                    input_rst = None
                    judge = "Empty"
                else:
                    input_rst = int(entry_list[en_no].get())
                    if input_rst == arry_problem_list[en_no][1]:
                        judge = "Right"
                    else:
                        judge = "Wrong"
                answer_tuple = arry_problem_list[en_no] + (input_rst, judge)
            except:
                txt = "第%1d道题填入的不是数字" % (en_no+1)
                tm.showwarning("注意：", txt)
                return 0
                
            #print (answer_tuple)
            Answer_Tuple_List.append(answer_tuple)
            
        prowin.destroy()
        Array_no += 1
        if Array_no <= Arry_Num:
            ProblemWin(problem_list)


    def WinWarning():
        mssg = "还未做完，要推出吗？"
        flag = tm.askokcancel("注意", mssg)
        if flag:  ## return True or False
            prowin.destroy()
            sys.exit(0)

    
    if Array_no == Arry_Num:
        tk.Button(prowin, text="我要交卷",font=("time", 20, "bold"), fg="black", bg="yellow", command=NextArray).grid(row=i, column=0, columnspan=32, padx=10, pady=10) 
    else:
        tk.Button(prowin, text="下一组",  font=("time", 20, "bold"), fg="black", bg="yellow", command=NextArray).grid(row=i, column=0, columnspan=32, padx=10, pady=10) 

    #if Array_no > 1: # FIXME
    #    tk.Button(prowin, text="上一组").grid(row=i, column=1, padx=10, pady=10)  
    
    prowin.protocol("WM_DELETE_WINDOW",WinWarning)   
    prowin.mainloop()


#********************************************
# Function: ReExecuteProgram()
#
# Used    : 点击“再做一次训练”，程序重新执行
#********************************************
def ReExecuteProgram():
    global Ret_math_range
    global Ret_math_type
    global Ret_opera_num 
    global Ret_math_num

    global Problem_List
    global Problem_Num
    global Every_Arry_Num
    global Arry_Num
    global Array_no
    global Answer_Tuple_List
    global Answer_Dic

    Ret_math_range  = 0
    Ret_math_type   = 0
    Ret_opera_num   = 0
    Ret_math_num    = 0

    MathTypeChose()
    Problem_List = []
    Problem_List = GenerateAllProblem(Ret_math_num)


    Problem_Num = len(Problem_List)
    Every_Arry_Num = 10
    
    Arry_Num    = Problem_Num//Every_Arry_Num if Problem_Num%Every_Arry_Num==0 else\
                  Problem_Num//Every_Arry_Num + 1
    Array_no = 1
    Answer_Tuple_List = []
    Answer_Dic = {0:"Right", 1:"Wrong", 3:"Empty" }

    ProblemWin(Problem_List)
    
    #print (Answer_Tuple_List)
    time.sleep(1)
    MathScoreBoard(Answer_Tuple_List)
    



#********************************************
# Function: MathScoreBoard()
#
# Used    : 总结做题的正确率，并在窗口展示
#********************************************
def MathScoreBoard(answer_list):
    right_cnt = 0
    wrong_cnt = 0
    empty_cnt = 0
    for rst in answer_list:
        if rst[3] == "Right":
            right_cnt += 1
        elif rst[3] == "Wrong":
            wrong_cnt += 1
        else:
            empty_cnt += 1
    
    score_cnt = int(right_cnt / len(answer_list) * 100)
    
    tx = "{0:<5}{1:{2}<3}"
    wrong_text = tx.format("错误数量:",wrong_cnt," ")
    rihgt_text = tx.format("正确数量:",right_cnt," ")
    empty_text = tx.format("没做数量:",empty_cnt," ")
    score_text = tx.format("本次得分:",score_cnt," ")
    #wrong_text = "错误数量：%-3d" %wrong_cnt
    #rihgt_text = "正确数量：%-3d" %right_cnt
    #empty_text = "没做数量：%-3d" %empty_cnt
    #score_text = "本次得分：%-3d" %score_cnt
    

    ## 如果得了满分或者0分，显示表扬界面
    #score_cnt = 100
    if 0 <= score_cnt <= 100:
        WelcomeAndPraise(0,score_cnt)

    ## 弹出窗口显示得分
    score_win = tk.Tk()
    score_win.title("测试结果板")
    sw       = score_win.winfo_screenwidth()
    sh       = score_win.winfo_screenheight()
    (ww, hh) = (350, 540)
    (x, y)   = ((sw - ww)/2,(sh - hh)/2)  
    score_win.geometry("%dx%d+%d+%d"%(ww,hh,x,y))
    
    score_lfm = tk.LabelFrame(score_win)
    score_lfm.pack()
    tk.Label(score_lfm, text=score_text,font=("PakTypeNaqsh",30,"bold"), fg="red").pack()
    tk.Label(score_lfm, text=wrong_text,font=("华文行楷",20), fg="blue").pack()
    tk.Label(score_lfm, text=rihgt_text,font=("华文行楷",20), fg="blue").pack()
    tk.Label(score_lfm, text=empty_text,font=("华文行楷",20), fg="blue").pack()
    
    def ListWrongProb(list_wrong):
        lbl = tk.Tk()
        sw       = lbl.winfo_screenwidth()
        sh       = lbl.winfo_screenheight()
        (ww, hh) = (841, 721)
        (x, y)   = ((sw - ww)/2,(sh - hh)/2) 
        lbl.geometry("%dx%d+%d+%d"%(ww,hh,x,y))
       
        lbl.title("ANSWER")
        lfm = tk.LabelFrame(lbl)
        lfm.grid(row=0, column=0,columnspan=2, padx=10, pady=10)

        txt = tk.Text(lfm, font=("Helvetica", 14), height=25)
        txt.pack()
            
        result_list = []
        for prob in answer_list:
            tuple0_prob_stem   = prob[0].replace("=", '')
            tuple1_equal_sig   = "="
            tuple4_right_value = "答案: " + str(prob[1])
            if prob[3] == "Wrong":
                tuple2_child_value = str(prob[2])
                tuple3_wrong_right = "✘"
            elif prob[3] == "Empty":
                tuple2_child_value = "?"
                tuple3_wrong_right = "没做"
            elif prob[3] == "Right":
                tuple2_child_value = str(prob[2]) 
                tuple3_wrong_right = "✔"
                tuple4_right_value = " "

            answer_tuple = (tuple0_prob_stem, tuple1_equal_sig, tuple2_child_value, tuple3_wrong_right, tuple4_right_value)
            result_list.append(answer_tuple)

            
            
            if list_wrong==1:
                if prob[3] in ["Wrong", "Empty"]:
                    l0 = tk.Label(txt, text=tuple0_prob_stem  , font=("Helvetica", 14, "bold"), fg="black", bg="white", justify="left"  , width=16)
                    l1 = tk.Label(txt, text=tuple1_equal_sig  , font=("Helvetica", 14, "bold"), fg="black", bg="white", justify="left"  , width=3 )
                    l2 = tk.Label(txt, text=tuple2_child_value, font=("Helvetica", 14, "bold"), fg="black", bg="white", justify="left"  , width=8)
                    l3 = tk.Label(txt, text=tuple3_wrong_right, font=("Helvetica", 14, "bold"), fg="red"  , bg="white", justify="left"  , width=8)
                    l4 = tk.Label(txt, text=tuple4_right_value, font=("Helvetica", 14, "bold"), fg="green", bg="white", justify="left"  , width=8)
                    txt.window_create("insert", window=l0)
                    txt.window_create("insert", window=l1)
                    txt.window_create("insert", window=l2)
                    txt.window_create("insert", window=l3)
                    txt.window_create("insert", window=l4)
                    txt.insert("insert", "\n")
                    lf_name = "错误题目及参考答案"
            else:
                l0 = tk.Label(txt, text=tuple0_prob_stem  , font=("Helvetica", 14, "bold"), fg="black", bg="white", justify="left"  , width=16)
                l1 = tk.Label(txt, text=tuple1_equal_sig  , font=("Helvetica", 14, "bold"), fg="black", bg="white", justify="left"  , width=3 )
                l2 = tk.Label(txt, text=tuple2_child_value, font=("Helvetica", 14, "bold"), fg="black", bg="white", justify="left"  , width=8)
                l3 = tk.Label(txt, text=tuple3_wrong_right, font=("Helvetica", 14, "bold"), fg="red"  , bg="white", justify="left"  , width=8)
                l4 = tk.Label(txt, text=tuple4_right_value, font=("Helvetica", 14, "bold"), fg="green", bg="white", justify="left"  , width=8)
                txt.window_create("insert", window=l0)
                txt.window_create("insert", window=l1)
                txt.window_create("insert", window=l2)
                txt.window_create("insert", window=l3)
                txt.window_create("insert", window=l4)
                txt.insert("insert", "\n")
                lf_name = "全部题目及参考答案"
      

        # 设置参考答案的弹框窗口副名称：
        lfm.config(text=lf_name, labelanchor="n",font=("宋体", 15), fg="blue",padx=5,pady=5)

        # 设置滚动条
        scl = tk.Scrollbar(lbl)
        scl['command'] = txt.yview
        scl.grid(row=0, column=3, sticky="s" + "n")
        txt.config(yscrollcommand = scl.set)

        # 设置保存结果的按钮
        def SaveAnswerReslut():
            now_time = time.strftime("%m%d-%H%M", time.localtime())
            gen_file = "训练结果"  + now_time + ".txt"
            f = open(gen_file, "w")
            for aw in result_list:
                write_str = "%-16s %-1s %-3s %-2s %-1s" % aw
                f.write(write_str)
            f.close()
            tm.showinfo("文件信息", "文件： \"" + gen_file + "\"已成功生成!\n放在: " + os.getcwd() + " 中")
                
        tk.Button(lbl, text="保存此结果", font=("time", 14), bg="black", fg="yellow", command=SaveAnswerReslut, width=10).grid(row=1, column=0, pady=10)
        tk.Button(lbl, text="退出此界面", font=("time", 14), bg="black", fg="yellow", command=lbl.destroy     , width=10).grid(row=1, column=1, pady=10)

        lbl.mainloop()


    def ExitProgram(): 
        score_win.destroy()
        sys.exit(0)
    
    def ReExec():
        score_win.destroy()
        ReExecuteProgram()

    tk.Button(score_win, text="查看错误题目", font=("华文行楷",20), fg="black",bg="yellow", command=lambda:ListWrongProb(1) ).pack(padx=10,pady=10)
    tk.Button(score_win, text="查看所有题目", font=("华文行楷",20), fg="black",bg="pink"  , command=lambda:ListWrongProb(0) ).pack(padx=10,pady=10)
    tk.Button(score_win, text="再做一次训练", font=("华文行楷",20), fg="black",bg="green" , command=ReExec                  ).pack(padx=10,pady=10)
    tk.Button(score_win, text="退出数学训练", font=("华文行楷",20), fg="black",bg="blue"  , command=ExitProgram             ).pack(padx=10,pady=10)
    
    score_win.mainloop()




############################################ Main #################################################
if __name__ == "__main__":
    
    #********************************** Const Parameter ******************************************#
    WELCOME_GIF     = "welcome.gif"     # 欢迎界面
    SCORE_000       = "fen_000.gif"     # 评判界面：得了0分
    SCORE_100       = "fen_100.gif"     # 评判界面：得了100分
    SCORE_060       = "fen_060.gif"     # 评判界面：得了60分
    SCORE_059       = "fen_059.gif"     # 评判界面：得了59分

    WAIT_TIME       = 1000              # 界面的持续时间： 2000 毫秒
    Every_Arry_Num  = 10                # GUI的题目十个分成一组
    #*********************************************************************************************#
   
    #************************************* Global Variable ***************************************#
    Array_no        = 1     # 题目分组之后，这个变量代表当前的组的组号，初始值是1
    Ret_math_range  = 0     # 数学题的范围：比如是30以内的数（的加减法）
    Ret_math_type   = 0     # 数学的类型：加减乘除，以及混合
    Ret_opera_num   = 0     # 一道题的操作数有几个
    Ret_math_num    = 0     # 数学题的数量

    Problem_List    = []    # 产生数学集合而成的列表，列表的元素是元组，
                            # 其形式类似这样(有连个元素)：（“ op1 + op2 ”, 正确结果值）
    Answer_Tuple_List = []  # 孩子的回答也以元组的形式存在列表Answer_Tuple_List，
                            # 其形式类似这样(有四个元素)：
                            # (“ op1 + op2 ”， 正确结果值，孩子回答值，回答正确性Right/Wrong/Empty）

    #*********************************************************************************************#
    rd.seed(int(sys.argv[1]))
   

    WelcomeAndPraise(welcome_flag=1, score=0)
    MathTypeChose()  ## give the value : 

    #Ret_math_range  = 100
    #Ret_math_type   = 5
    #Ret_opera_num   = 2
    #Ret_math_num    = 8

    Problem_List = GenerateAllProblem(Ret_math_num) # 通过GUI界面获取的数据，在这个函数中生成题目
                                                    # 生成的题目放入的Problem_List中
    
    Problem_Num = len(Problem_List)
    Arry_Num    = Problem_Num//Every_Arry_Num if Problem_Num%Every_Arry_Num==0 else\
                  Problem_Num//Every_Arry_Num + 1
    #Array_no = 1

    ProblemWin(Problem_List)
    
    time.sleep(1)
    MathScoreBoard(Answer_Tuple_List)
