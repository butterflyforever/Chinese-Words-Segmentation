# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import*
from tkinter.messagebox import*
from tkinter.simpledialog import*
root = Tk()
root.title("中文用户界面")
root.geometry('1000x500')
root.iconbitmap('SJTU.ico')#添加图标
#背景
background=Canvas(root,height=1000,width=500)

image1=PhotoImage(file='100008742769036.gif')

background.create_image(300,-100,image =image1,anchor=NW)

background.pack(expand = YES, fill = BOTH)

#left
frm_L = LabelFrame(background,bg='SkyBlue',text="请在方框中输入文字", font=("楷体", 12), width=20, height=3)

scrollbar_LV=Scrollbar(frm_L, orient=VERTICAL)
scrollbar_LV.pack(side=RIGHT,fill=Y)
text1=Text(frm_L,width=40, height=30,font=("楷体"),yscrollcommand = scrollbar_LV.set,bg='SkyBlue')
scrollbar_LV.config(command=text1.yview)
text1.pack()
frm_L.pack(side=LEFT)
#right

frm_R = LabelFrame(background,bg='SkyBlue',text="分词结果", font=("楷体", 12), width=20, height=3)

scrollbar_RV=Scrollbar(frm_R, orient=VERTICAL)
scrollbar_RV.pack(side=RIGHT,fill=Y)
text2=Text(frm_R,width=40, height=30,font=('楷体'),bg='SkyBlue',yscrollcommand = scrollbar_RV.set)
scrollbar_RV.config(command=text2.yview)
text2.pack()

frm_R.pack(side=RIGHT)
#新建文件
def new1():
    text1.delete(0.0,END)
def new2():
    text2.delete(0.0,END)

#打开文件
def open_file():
    filename=askopenfilename(filetypes=[('text files', '.txt'),('all files', '.*')])
    file_input=open(filename,'r').read()

    text1.insert(END,file_input)

Button(background,text = '清空文本' , font=("楷体", 9), command =new1,bg='skyblue').place(x=249,y=0,anchor=NW)
Button(background,text = '清空文本' ,font=("楷体", 9), command = new2,bg='skyblue').place(x=905,y=0,anchor=NW)
#保存文件
def save1():
  t = text1.get(0.0,END)
  b=asksaveasfilename(defaultextension ='*.txt',filetypes=[('text files', '.txt'),('all files', '.*')])
  f = open(b,'w')
  f.write(t)
def save2():
  t = text2.get(0.0,END)
  b=asksaveasfilename(defaultextension ='*.txt',filetypes=[('text files', '.txt'),('all files', '.*')])
  f = open(b,'w')
  f.write(t)
Button(background,text = '保存' , font=("楷体", 9), command =save1,bg='skyblue').place(x=204,y=0,anchor=NW)
Button(background,text = '保存' , font=("楷体", 9), command =save2,bg='skyblue').place(x=860,y=0,anchor=NW)

#菜单
def delete_word():
    a=askstring(title = '删除词语',prompt = '请输入想删除的词语')
    txtreplace=""
    if len(a)==2:
        if a in dic2:
            dic2.pop(a)
            filetxt1=open("result2.txt",encoding="utf-8")
            filetxt=filetxt1.readlines()
            filetxt1.close()
            for line in filetxt:
                if line[0:2]!=a:
                    txtreplace+=line
            file2=open("result2.txt","w",encoding="utf-8")
            file2.write(txtreplace)
            file2.close()

        else:
            showinfo('提示','词典中没有该词')
    if len(a)==3:
        if a in dic3:
            dic3.pop(a)
            filetxt1=open("result3.txt",encoding="utf-8")
            filetxt=filetxt1.readlines()
            filetxt1.close()
            for line in filetxt:
                if line[0:3]!=a:
                    txtreplace+=line
            file2=open("result3.txt","w",encoding="utf-8")
            file2.write(txtreplace)
            file2.close()
        else:
            showinfo('提示','词典中没有该词')
    if len(a)==4:
        if a in dic4:
            dic4.pop(a)
            filetxt1=open("result4.txt",encoding="utf-8")
            filetxt=filetxt1.readlines()
            filetxt1.close()
            for line in filetxt:
                if line[0:4]!=a:
                    txtreplace+=line
            file2=open("result4.txt","w",encoding="utf-8")
            file2.write(txtreplace)
            file2.close()
        else:
            showinfo('提示','词典中没有该词')
    if len(a)==5:
        if a in dic5:
            dic5.pop(a)
            filetxt1=open("result5.txt",encoding="utf-8")
            filetxt=filetxt1.readlines()
            filetxt1.close()
            for line in filetxt:
                if line[0:5]!=a:
                    txtreplace+=line
            file2=open("result5.txt","w",encoding="utf-8")
            file2.write(txtreplace)
            file2.close()
        else:
            showinfo('提示','词典中没有该词')
    if len(a)>=6:
        if a in dic6:
            dic6.pop(a)
            filetxt1=open("result6.txt",encoding="utf-8")
            filetxt=filetxt1.readlines()
            filetxt1.close()
            for line in filetxt:
                if line[0:len(a)]!=a:
                    txtreplace+=line
            file2=open("result6.txt","w",encoding="utf-8")
            file2.write(txtreplace)
            file2.close()
        else:
            showinfo('提示','词典中没有该词')


def about():
   filewin = Toplevel(root)
   Message(filewin,text='开发者:\n李大松\n李洋\n姚宇航').pack()
def help():
    filewin = Toplevel(root)
    Message(filewin,text='通过手动输入或打开文件中的txt文本进行分词、分句和搜索新词，搜索新词可自动生成建议新词的词频，搜索词义会显示字典中的释义，没有会自动打开百度百科，可添加或删除字典中的词语').pack()
def Exit():
    ans = askokcancel('Verify exit', "Really quit?")
    if ans: exit()

def Cut():
    text = text1.get(SEL_FIRST, SEL_LAST)
    text1.delete(SEL_FIRST, SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(text)
def Copy():
    text = text1.get(SEL_FIRST, SEL_LAST)
    root.clipboard_clear()
    root.clipboard_append(text)
def Paste():
    try:
      text =root.selection_get(selection='CLIPBOARD')
      text1.insert(INSERT, text)
    except TclError:
      pass
def Delete():
    text1.delete(SEL_FIRST, SEL_LAST)
def find_means():
    text = text1.get(SEL_FIRST, SEL_LAST)
def undo():
    text1.edit_undo()
def redo():
    text1.edit_redo()
#全选
def Select_All():
        text1.tag_add(SEL, "1.0",END)
        return 'break'
#搜索词义
def findmean(a,dictionary):
    if a in dictionary:
        mean=dictionary[a]
        return mean
    else:
        import webbrowser
        url="http://www.baidu.com/s?wd="+a+"百度百科"
        webbrowser.open(url)
        print(webbrowser.get())
        return '词典中没有此词，转到百度百科搜索'

def makedic1():
    if dictionary=={}:
        import string
        file=open("dictionary.txt","r",encoding="utf-8")
        file1=file.read()
        file.close()
        a="\n\n\u3000\u3000"
        file1=file1.split(a)
        file1[0]=file1[0].replace("\n\n\u3000\u3000","")
        dic_xiandai={}
        for i in range(len(file1)):
           if file1[i][0]=="*":
               dic_xiandai[file1[i][1]]=file1[i][2:]
           else:
                front=file1[i].find("【")
                behind=file1[i].find("】")
                dic_xiandai[file1[i][front+1:behind]]=file1[i][behind+1:]
        return dic_xiandai

def findwordsmean():
    file = text1.get(SEL_FIRST, SEL_LAST)
    global dictionary
    dictionary={}
    dictionary=makedic1()
    mean=findmean(file,dictionary)
    text2.delete(0.0,END)
    text2.insert(END,mean)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="新建", command=new1)
filemenu.add_command(label="打开", command=open_file)
filemenu.add_command(label="保存", command=save2)

filemenu.add_separator()

filemenu.add_command(label="退出", command=Exit)
menubar.add_cascade(label="文件（F）", menu=filemenu)
editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label="撤销", command=undo)

editmenu.add_separator()

editmenu.add_command(label="剪切", command=Cut)
editmenu.add_command(label="复制", command=Copy)
editmenu.add_command(label="粘贴", command=Paste)
editmenu.add_command(label="删除", command=Delete)
editmenu.add_command(label="全选", command=Select_All)
editmenu.add_command(label="删除词语", command=delete_word)

menubar.add_cascade(label="编辑（E）", menu=editmenu)
helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label="查看帮助", command=help)
helpmenu.add_command(label="关于", command=about)
menubar.add_cascade(label="帮助（H）", menu=helpmenu)
root.config(menu=menubar)
#右键菜单

# 创建一个弹出菜单

menu = Menu(text1,tearoff=False)
menu.add_command(label="撤销", command=undo)
menu.add_command(label="重做", command=redo)
menu.add_command(label="剪切", command=Cut)
menu.add_command(label="复制", command=Copy)
menu.add_command(label="粘贴", command=Paste)
menu.add_command(label="删除", command=Delete)
menu.add_command(label="全选", command=Select_All)
menu.add_command(label="搜索", command=findwordsmean)
def popup(event):
    menu.post(event.x_root, event.y_root)

# 绑定鼠标右键
text1.bind("<Button-3>", popup)
#分词
#导入词库
def make_dic():
    global dic2
    global dic3
    global dic4
    global dic5
    global dic6
    dic2={}
    dic3={}
    dic4={}
    dic5={}
    dic6={}
    long=0
    file2=open("result2.txt","r",encoding="utf-8")
    file3=open("result3.txt","r",encoding="utf-8")
    file4=open("result4.txt","r",encoding="utf-8")
    file5=open("result5.txt","r",encoding="utf-8")
    file6=open("result6.txt","r",encoding="utf-8")
    file2copy=file2.readlines()
    file3copy=file3.readlines()
    file4copy=file4.readlines()
    file5copy=file5.readlines()
    file6copy=file6.readlines()
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()
    for line in file2copy:
        line=line.strip("\n,\ufeff")
        linelist=line.split()
        dic2[linelist[0]]=int(linelist[1])
    for line in file3copy:
        line=line.strip("\n,\ufeff")
        linelist=line.split()
        dic3[linelist[0]]=int(linelist[1])
    for line in file4copy:
        line=line.strip("\n,\ufeff")
        linelist=line.split()
        dic4[linelist[0]]=int(linelist[1])
    for line in file5copy:
        line=line.strip("\n,\ufeff")
        linelist=line.split()
        dic5[linelist[0]]=int(linelist[1])
    for line in file6copy:
        line=line.strip("\n,\ufeff")
        linelist=line.split()
        dic6[linelist[0]]=int(linelist[1])
        if len(linelist[0])>long:
            long=len(linelist[0])
    return long
# 选择合适字典
def dfine(wer):
    if len(wer)>=6:
        if wer in dic6:
            return 1
    if len(wer)==5:
        if wer in dic5:
            return 1
    if len(wer)==4:
        if wer in dic4:
            return 1
    if len(wer)==3:
        if wer in dic3:
            return 1
    if len(wer)==2:
        if wer in dic2:
            return 1
    return -1




def dfine2(wer):
    if len(wer)>=6:
            return dic6[wer]
    if len(wer)==5:
            return dic5[wer]
    if len(wer)==4:
            return dic4[wer]
    if len(wer)==3:
            return dic3[wer]
    if len(wer)==2:
            return dic2[wer]

#按照切割位点（index—list）切割
def modify(file,index_list,result):
    for i in range(len(file)):
        if i!=0:
            if i in index_list:
                result=result+"|"+file[i]
            else:
                result=result+file[i]
        else:
            result=result+file[i]
    return result
def modify2(m,op2):
    mi=[]
    for i in range(len(m)):
        if m[i] not in op2:
            mi=mi+[m[i]]
    return mi

#确定正向切割位点
def recurision(file,max,front_index_list,index,length,file_length):
    while (index<file_length) and (file!=""):
        if max<=len(file):
            for i in range(max):
                if dfine(file[:max-i])==1:
                    file=file[max-i:]
                    index=index+max-i
                    front_index_list=front_index_list+[index]
                    break
                else:
                    if max-i<=2:
                        file=file[1:]
                        index=index+1
                        front_index_list=front_index_list+[index]
                        break
        else:
            length=len(file)
            for i in range(length):
                if dfine(file[:length-i])==1:
                    file=file[length-i:]
                    index=index+length-i
                    front_index_list=front_index_list+[index]
                    break
                else:
                    if length-i<=2:
                        file=file[1:]
                        index=index+1
                        front_index_list=front_index_list+[index]
                        break

    return front_index_list

def werty(a):
    d=[48,49,50,51,52,53,54,55,56,57]
    b=[65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90]
    c=[97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
    i=0
    op=[]
    wety=""
    rty=""

    while i<len(a):
        u=i
        while ord(a[i]) in d:
            wety=wety+a[i]
            i=i+1
            if i>=len(a):
                break
        if len(wety)==1:
            i=u+1
            wety=""
            continue
        if len(wety)>=2:
            for j in range(1,len(wety)):
                op=op+[u+j]
            i=u+len(wety)
            wety=""
            continue
        wety=""
        while ord(a[i]) in b+c:
            rty=rty+a[i]
            i=i+1
            if i>=len(a):
                break
        if len(rty)==1:
            i=u+1
            rty=""
            continue
        if len(rty)>=2:
            for j in range(1,len(rty)):
                op=op+[u+j]
            i=u+len(rty)
            rty=""
            continue
        rty=""
        i=i+1
    return(op)


#确定逆向切割位点
def recurision1(file,max,reverse_index_list,index,length,file_length):
    while (index>0) and (file!=""):
        if max<=len(file):
            for i in range(max):
                if dfine(file[len(file)+i-max:])==1:
                    index=index-max+i
                    file=file[:len(file)-max+i]
                    reverse_index_list=reverse_index_list+[index]
                    break
                else:
                    if max-i<=2:
                        file=file[:len(file)-1]
                        index=index-1
                        reverse_index_list=reverse_index_list+[index]
                        break
        else:
            length=len(file)
            for i in range(length):
                if dfine(file[len(file)+i-length:])==1:
                    file=file[:len(file)-length+i]
                    index=index-length+i
                    reverse_index_list=reverse_index_list+[index]
                    break
                else:
                    if length-i<=2:
                        file=file[:len(file)-1]
                        index=index-1
                        reverse_index_list=reverse_index_list+[index]
                        break
    reverse_index_list=reverse_index_list+[file_length]
    reverse_index_list.sort()
    reverse_index_list=reverse_index_list[1:]
    return reverse_index_list

#词频比较（此处均通过切割位点比较，最终确定最终位点）
def finder(a,b):
    for i in range(len(b)):
        if a==b[i]:
            return i

def sleter(filecopy,front_indexlist,front_result,reverse_indexlist,reverse_result,dictp):
    front_result_list=front_result.split("|")
    reverse_result_list=reverse_result.split("|")
    front_indexlist=[0]+front_indexlist
    reverse_indexlist=[0]+reverse_indexlist
    same_point=[0]


    front_cut_times=0
    reverse_cut_times=0
    p=0
    k=0
    word_rates1=0
    word_rates2=0
    for i in range(1,len(front_indexlist)):
        if front_indexlist[i] in reverse_indexlist:
            same_point=same_point+[front_indexlist[i]]
    final_point_list = same_point
    front_record=[]
    reverse_record=[]
    front_all_record=[]
    reverse_all_record=[]
    for i in range(len(same_point)-1):
        for j in range(finder(same_point[i],front_indexlist),finder(same_point[i+1],front_indexlist)):
            if front_indexlist[j] not in same_point:
                front_cut_times=front_cut_times+1
                front_record=front_record+[front_indexlist[j]]
            front_all_record=[same_point[i]]+front_record+[same_point[i+1]]
        for j in range(finder(same_point[i],reverse_indexlist),finder(same_point[i+1],reverse_indexlist)):
            if reverse_indexlist[j] not in same_point:
                reverse_cut_times=reverse_cut_times+1
                reverse_record=reverse_record+[reverse_indexlist[j]]
            reverse_all_record=[same_point[i]]+reverse_record+[same_point[i+1]]

        if front_cut_times>=1 and reverse_cut_times>=1:
            if filecopy[same_point[i]:same_point[i+1]] in dictp:
                for word11 in dictp[filecopy[same_point[i]:same_point[i+1]]]:
                    final_point_list=final_point_list+[same_point[i]+word11]
            else:
                if front_cut_times>reverse_cut_times:
                    final_point_list=final_point_list+reverse_record
                elif front_cut_times<reverse_cut_times:
                    final_point_list=final_point_list+front_record
                else:
                    for j in range(len(front_all_record)-1):
                        if front_all_record[j+1]-front_all_record[j]>=2:
                            p=p+1
                            word_rates1=word_rates1+dfine2(front_result_list[finder(front_all_record[j],front_indexlist)])

                    for j in range(len(reverse_all_record)-1):
                        if reverse_all_record[j+1]-reverse_all_record[j]>=2:
                            k=k+1
                            word_rates2=word_rates2+dfine2(reverse_result_list[finder(reverse_all_record[j],reverse_indexlist)])
                    if word_rates1*k>= word_rates2*p:
                        final_point_list=final_point_list+front_record
                    else:
                        final_point_list=final_point_list+reverse_record

        word_rates1=0
        word_rates2=0
        front_all_record=[]
        reverse_all_record=[]

        k=0
        p=0

        front_cut_times=0
        reverse_cut_times=0
        front_record=[]
        reverse_record=[]
    return final_point_list

#运行分词程序

max=make_dic()
def main(file_input):
    filecopy=file_input
    op2=werty(filecopy)
    front_index_list = recurision(file_input,max,[],0,0,len(file_input))
    front_index_list=modify2(front_index_list,op2)
    front_result=modify(filecopy,front_index_list,"")
    reverse_index_list=recurision1(file_input,max,[],len(file_input),0,len(file_input))
    reverse_index_list=modify2(reverse_index_list,op2)
    reverse_result=modify(filecopy,reverse_index_list,"")
    finisfer=sleter(filecopy,front_index_list,front_result,reverse_index_list,reverse_result,{"中共创":[1],"公信处女干事":[3],"请把手":[1,2],"王军虎去":[3],"网球拍卖":[3],"乒乓球拍卖":[4],"实在理":[1]})
    final_result=modify(filecopy,finisfer,"")
    return final_result

def fenci():
    file_input=text1.get(0.0,END)
    file_input=file_input.strip()
    if file_input=='':

       showwarning('警告','请输入文字')
    else:
        mf=main(file_input)
        text2.delete(0.0,END)
        text2.insert(END,mf)
#分词图片
image2=PhotoImage(file='100006952536802.gif')
Button(background,fg='white',text='分词',image=image2,font=("楷体", 20),compound=CENTER,command = fenci,bd=0).pack(side=TOP)
#分句
def fenju():
    text2.delete(0.0,END)
    a=text1.get(0.0,END)
    a=a.strip()
    record1=[]
    b=[]
    for i in range(len(a)):
        if (a[i]=="，") or (a[i]=="。")or (a[i]=="；")or (a[i]=="!")or (a[i]=="？")or (a[i]=="’")or(a[i]=="“")or(a[i]=="”")or(a[i]=="‘")or(a[i]=="："):
           record1=record1+[i]

    i=0
    while i<len(record1):
        u=i
        if a[record1[i]]=="“":
            u=u+1
            while a[record1[u]]!="”":
                u=u+1
            i=u+1
        elif a[record1[i]]=="‘":
            u=u+1
            while a[record1[u]]!="’":
                u=u+1
            i=u+1
        else:
           b=b+[record1[i]]
           i=i+1
    for i in range(len(b)):
        b[i]=b[i]+1
    c=""
    d=[]
    text2.insert(END,"1."+a[:b[0]]+"\n")
    for i in range(len(b)-1):
        me=str(i+2)
        text2.insert(END,me+"."+a[b[i]:b[i+1]]+"\n")
image3=PhotoImage(file='10000333751497.gif')
Button(background,fg='white',text='分句',image=image3,command = fenju,font=("楷体", 20),compound=CENTER,bd=0).pack(side=TOP)

#搜索新词
def judge(a):
    if len(a)>5:
        return a in dic6
    if len(a)==5:
        return a in dic5
    if len(a)==4:
        return a in dic4
    if len(a)==3:
        return a in dic3
    if len(a)==2:
        return a in dic2

def findnumber(a):
    if len(a)>5:
        return dic6[a]
    if len(a)==5:
        return dic5[a]
    if len(a)==4:
        return dic4[a]
    if len(a)==3:
        return dic3[a]
    if len(a)==2:
        return dic2[a]



def remove_words(file,max):
    import string
    cal_dic={}
    new_file=""
    while len(file)>=max:
        for i in range(max-1):
            if judge(file[:max-i]):
                if file[:max-i] in cal_dic:
                    cal_dic[file[:max-i]]=cal_dic[file[:max-i]]+1
                else:
                    cal_dic[file[:max-i]]=1
                file=file[max-i:]
                break
            else:
                if max-i==2:
                    new_file+=file[0]
                    file=file[1:]
                    break
    threshold1=0
    number=0
    number_list=[]
    dicnumber=[]
    cal_number=[]
    for i in cal_dic:
        threshold1+=cal_dic[i]
        number_list+=[cal_dic[i]]
        number+=1
    number_list.sort()
    new_number_list=number_list[len(number_list)-8:]+number_list[0:8]
    word_list=[]
    for i in range(len(new_number_list)):
      for j in cal_dic:
         if cal_dic[j]==new_number_list[i] and j not in word_list:
            word_list+=[j]
            cal_number+=[cal_dic[j]]
            break
    for i in range(len(word_list)):
        dicnumber+=[findnumber(word_list[i])]
    global times
    time=0
    for i in range(len(cal_number)):
        time=int(dicnumber[i]/cal_number[i])
    if len(cal_number)!=0:
       times=time/len(cal_number)
       threshold=threshold1/number*2
       return new_file,threshold
    else:
        return None,0


def remove_punctuation(file):
    import string
    for i in range(len(file)):
      if file[i] in string.punctuation or file[i] in "\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）\n “ ” 《 》：；0123456789":
          file=file[:i]+" "+file[i+1:]
    return file

def find_new(file,threshold):
    new_dic={}
    for i in range(len(file)):
        word_len=8
        j=8
        while j>=2:
            if " " not in file[i:i+j] and len(file[i:i+j])>=2:
                if file[i:i+j] not in new_dic:
                    new_dic[file[i:i+j]]=0
                else:
                    new_dic[file[i:i+j]]=new_dic[file[i:i+j]]+1
            j=j-1
    new_word=""
    for i in new_dic:
        if new_dic[i]>=threshold:
            new_word+=str(i)+"   "+str(int(new_dic[i]*times))+"\n"
    return new_word

def search():
    file=text1.get(0.0,END)
    new_file,threshold=remove_words(file,max)
    if new_file!=None:
       file=remove_punctuation(new_file)
       new_word=find_new(file,threshold)
       if len(new_word)==0:
         new_word="文本太小或新词出现频率太少，不足以认定有新词"
    else:
        new_word="文本太小或新词出现频率太少，不足以认定有新词"
    text2.delete(0.0,END)
    text2.insert(END,new_word)
image4=PhotoImage(file='100007591354623.gif')
Button(background,fg='white', text="搜索新词", image=image4,command = search,font=("楷体", 20),compound=CENTER,bd=0).pack(side=TOP)
image5=PhotoImage(file='100001857828937.gif')


def findwordsmean2():
    file = askstring(title = '搜索词义',prompt = '请输入所要查找的词语')
    global dictionary
    dictionary={}
    dictionary=makedic1()
    mean=findmean(file,dictionary)
    text2.delete(0.0,END)
    text2.insert(END,mean)
Button(background, fg='white',text="搜索词义", image=image5,command = findwordsmean2,font=("楷体", 20),compound=CENTER,bd=0).pack(side=TOP)


#用户自定义词

frequency = IntVar()

Radiobutton(background, text = "低频", font=("楷体", 10),variable = frequency, value = 10).place(x = 420,y = 450,anchor = NW)
Radiobutton(background, text = "中频", font=("楷体", 10),variable = frequency, value = 160).place(x = 472,y = 450,anchor = NW)
Radiobutton(background, text = "高频", font=("楷体", 10),variable = frequency, value = 1000).place(x = 523,y = 450,anchor = NW)
Entry(background, textvariable = frequency,width=4).place(x = 390,y = 450,anchor = NW)


var1 = StringVar()
Entry(background, textvariable = var1).place(x = 430,y = 430,anchor = NW)
image6=PhotoImage(file='100009821779670.gif')
var11=Label(background,fg='white',text='请在下方输入新词',font=("楷体", 12),image=image6,compound=CENTER,bd=0).place(x = 430,y = 405,anchor = NW)
def definition():
    word=var1.get()
    if len(word) <= 1:
       showinfo('提示','请输入词语')
    elif frequency.get() == 0:
         showinfo('提示','请选择词频')
    elif askokcancel('提示','确认添加新词？'):
       if len(word)==2:
           if word not in dic2:
             dic2[var1.get()]=frequency.get()
             file=open("result2.txt",'a+',encoding="utf-8")
             file.write(var1.get()+' '+str(frequency.get())+'\n')
           else:
            showinfo('提示','词典中已有该词')
       elif len(word)==3:
          if word not in dic3:
             dic3[var1.get()]=frequency.get()
             file=open("result3.txt",'a+',encoding="utf-8")
             file.write(var1.get()+' '+str(frequency.get())+'\n')
          else:
            showinfo('提示','词典中已有该词')
       elif len(word)==4:
          if word not in dic4:
             dic4[var1.get()]=frequency.get()
             file=open("result4.txt",'a+',encoding="utf-8")
             file.write(var1.get()+' '+str(frequency.get())+'\n')
          else:
            showinfo('提示','词典中已有该词')
       elif len(word)==5:
          if word not in dic5:
             dic5[var1.get()]=frequency.get()
             file=open("result5.txt",'a+',encoding="utf-8")
             file.write(var1.get()+' '+str(frequency.get())+'\n')
          else:
            showinfo('提示','词典中已有该词')
       elif len(word)>=6:
          if word not in dic6:
             dic6[var1.get()]=frequency.get()
             file=open("result6.txt",'a+',encoding="utf-8")
             file.write(var1.get()+' '+str(frequency.get())+'\n')
          else:
            showinfo('提示','词典中已有该词')
    file.close()
image7=PhotoImage(file='10000254965367.gif')
Button(background, text="添加新词",fg='white',command = definition,font=('楷体',12),image=image7,compound=CENTER,bd=0).place(x = 575,y = 430,anchor = NW)

root.mainloop()