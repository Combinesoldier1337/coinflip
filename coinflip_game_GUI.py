from tkinter import *
from tkinter import messagebox
import random
import re
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
                c=int(lang.get())
                a = a-int(b);
                r = random.randint(1,2);
                if r==1:
                		messagebox.showinfo(title='Внимание!', message='Выпал орёл!');
                else:
                	messagebox.showinfo(title='Внимание!', message='Выпала решка!');       
                if c == r:
                    b=b*2
                    a=a+b;
                    res = "Баланс: ${}".format(a)
                    title.configure(text=res)  
                    message = f'Вы выиграли ${int(b/2)}'
                    messagebox.showinfo(title='Внимание!', message=message);
                    if amax < a:
                        amax = a*1;
                else:
                    res = "Баланс: ${}".format(a)
                    title.configure(text=res) 
                    message = f'Вы потеряли ${int(b)}'
                    messagebox.showinfo(title='Внимание!', message=message);
                    b = 0;
    if a == 0:
            messagebox.showerror(title='GAME OVER', message='Вы потратили все деньги!')
            if amax > 100:                
                bestcore=f'Рекорд: ${str(amax)}'
                messagebox.showinfo(title='Scoreboard', message=bestcore);
            window.destroy()
window['bg'] = '#252525'
window.title('Монетка')
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
lang = IntVar()
Radiobutton1 = Radiobutton(frame, bg='#252525', fg='#707070', activebackground='#252525', activeforeground='#404040', selectcolor='#404040', text="Орёл", value=1, variable=lang)
Radiobutton1.select()
Radiobutton1.pack()
Radiobutton2 = Radiobutton(frame, bg='#252525', fg='#707070', activebackground='#252525', activeforeground='#404040', selectcolor='#404040', text="Решка", value=2, variable=lang)
Radiobutton2.deselect()
Radiobutton2.pack()
btn=Button(frame, bg='#404040', fg='#909090', text='Подбросить!',  command=btn_click)
btn.pack()
window.mainloop()