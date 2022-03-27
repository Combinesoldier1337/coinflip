from tkinter import *
from tkinter import messagebox
import random
import re
from threading import Timer
from time import sleep
window=Tk()
def btn_click():
    t=(title.cget("text"))
    s=0;
    c=0;
    r=0;
    w=0;
    b=0;
    is_int = True
    a=int(re.search(r'\d+', t).group())
    amax = a;
    login=loginInput.get()
    value =(loginInput.get())
    result = re.match("[-+]?\d+$", value)
   
    if result is None or int(loginInput.get()) == 0:
        messagebox.showerror(title='Ошибка', message='Введите сумму!')
    else:
            b=int(loginInput.get())
            if int(b) > a:
                messagebox.showerror(title='Ошибка', message='Недостаточно денег на балансе!!!')
            else:
                    a = a-int(b);
                    r = random.randint(1,25);
            def foo():
                    print ("timer went off!")
            t = Timer(1, foo)
            t.start()
            for i in range(r-c):
                c=c+1
                res = "Множитель: {}".format(c*0.1)
                title2.configure(text=res) 
                sleep(.1)

            if a>0:
                a=a+(b*c*0.1)
                res = "Баланс: ${}".format(a)
                title.configure(text=res)  
            else: 
                sagebox.showerror(title='GAME OVER', message='Вы потратили все деньги!')
        #if amax > 100:
         #   bestcore=f'Рекорд: ${str(amax)}'
         #   messagebox.showinfo(title='Scoreboard', message=bestcore);
        #window.destroy()
window['bg'] = '#252525'
window.title('1xUp')
#window.wm_attributes('-alpha', 0.7)
window.geometry('300x250')
window.resizable(width=False, height=False)
frame = Frame(window, bg='#252525')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
title=Label(frame, bg='#252525', fg='#6fa960', text='Баланс: $100',  font=("Arial Bold", 20))
title.pack()
title1=Label(frame, bg='#252525', fg='#707070', text='Сумма ставки:',  font=("Arial Bold", 10))
title1.pack()
loginInput = Entry(frame, bg='#404040', fg='#6fa960')
loginInput.pack()
title2=Label(frame, bg='#252525', fg='#707070', text='Множитель: 1.0',  font=("Arial Bold", 10))
title2.pack()
btn=Button(frame, bg='#404040', fg='#909090', text='Начать!',  command=btn_click)
btn.pack()
window.mainloop()