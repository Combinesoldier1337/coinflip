import random
a=100;
s=0;
c=0;
r=0;
w=0;
b=0;
amax=0;
def out_red(text):
    print("\033[31m {}" .format(text))
def out_white(text):
    print("\033[39m {}" .format(text))
def out_green(text,number):
    print("\033[32m {}" .format(text), "\033[32m {}" .format(number))
def out_lose(text,number):
    print("\033[33m {}" .format(text), "\033[33m {}" .format(number))
    
#out_white("Введите сумму:");
#a=int(input());
while w < 2 :
    
    out_green("\n Баланс: $",a);
    out_white("Ваша ставка:");
    b=int(input());
    if b > a:
        out_red("Не достаточно денег на балансе!!!");
        
    else:
        out_white("Выберите сторону:");
        out_white("1. Орёл");
        out_white("2. Решка");
        c=int(input());
        if (c != 1 and c != 2):
            out_red("!!!Ошибка!!!");
        else:
            a = a-b;
            r = random.randint(1,2);
            if (c == 1):
                print("\n", "Ваш выбор - Орёл");
                if r ==1:
                    print("Cторона монеты - Орёл");
                else:
                    print("Cторона монеты - Решка");
            else:
                    print("Ваш выбор - Решка");
                    if r ==1:
                        print("Cторона монеты - Орёл");
                    else:
                        print("Cторона монеты - Решка");
            
            if c == r:
                b=b*2
                a=a+b;
                out_green("Вы выиграли $",b);
                if amax < a:
                    amax = a*1;
            else:
                out_lose("Вы потеряли $",b);
                b = 0;
            if a == 0:
                out_red("GAME OVER")
                out_green("Лучший счёт: $", amax);
                w = 3;