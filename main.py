import tkinter as tk
import random

stu_list = ['龚泉全','李知衡','李坤泽','蒲俊翔','刘芮含','秦子恒',
	'戴吉满','彭康峻','郭隆浩','杨曜恺','代淳玺',
	'亢泓博','龚子涵','李忻芸','张芮博',
               '张家洲','丁翌航','唐粲然','张齐家','蔡述合',
            '肖知止','彭诗涵','杨睿杰','刘知几','殷梦可',
            '曾煜航','李君昊','吴思诺','乔瞰','陈禹竹',
	'杜翰霖','杜芋霏','刘衍辰','杨沛翰','张森越','覃索菲',
            '杨沁妤','刘泫妙','赵思齐','李秉战',
	'黄婉榕','卢彦朵','郑绍益','邓钦元','邓涵',
	'魏梓涵','朱美霖','楚言熙','张瀚予','高梓洵','孔维栖','吴思诺','吴思诺','吴思诺','吴思诺','吴思诺','吴思诺','吴思诺','吴思诺','吴思诺']
print(len(stu_list))
re_list = []
random.shuffle(stu_list)


root = tk.Tk()
root.geometry("1000x900")
root.title('点名器V1.0')
root.resizable(False,False)

stu = '开始点名'
last = []
text = tk.StringVar()
text.set(stu)

bj = '项目已开放:https://github.com/sffffre/15dian'

lb2 = tk.Label(root,text=bj,font=('黑体',20),width=50,height=0)
lb2.place(x=0,y=30)

label = tk.Label(root, text=stu,font=('黑体',70),width=20,height=5,textvariable=text)
label.place(x=75,y=75)

def callback():
    while True:
        random.shuffle(stu_list)
        stu=random.choice(stu_list)
        if stu in re_list:
            pass
        else:
            re_list.append(stu)
            if len(re_list) > 7:
                del re_list[0]
            break
    
    text.set(stu)

b = tk.Button(root, text="点名", command=callback, width=10,height=5,font='black 20 bold')
b.place(x=450,y=550)

root.mainloop()
