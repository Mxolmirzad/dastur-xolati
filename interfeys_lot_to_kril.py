#MxolmirzaD

import math
from tkinter import*
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Krill to lotin or lotin to krill ")
window.configure(bg="LightSteelBlue")
window.geometry("1200x680")
photo = tk.PhotoImage(file="icon.ico")
window.iconphoto(False, photo)
window.minsize(600,325)
window.maxsize(1200,680)
window.resizable(True,True)

# c=Canvas(top,bg="white",height=1000, width=10)
file_name=PhotoImage(file="1200x680_4.ico")
background_label=Label(window,image=file_name)
background_label.place(x=0,y=0, relheight=1, relwidth=1)
# c.pack

# ekran_image = PhotoImage(file="ekran_1.png")

# sarlavha = Label(window, text="Крилл_ёзуви >>> Lotin_yozuvi yoki Lotin_yozuvi >>> Крилл_ёзуви ", font=("Times new Roman",20), bg="LightSteelBlue" )
# sarlavha.place(x=150, y=2)

soz = Text(window,font=("Times new Roman",14), bg="AliceBlue", width=128, height=11 )
soz.place(x=20,y=30)

matnlar = Text(window, font=("Times new Roman",14),height=11,width=128, bg="AliceBlue")
matnlar.place(x=20, y=320)

def kril_to_lotin():
    matn = soz.get(1.0, END)
    #matn = matn.lower()
    matn = matn.replace("ў", "o‘")
    matn = matn.replace("ғ", "g‘")
    matn = matn.replace("ев", "yev")
    matn = matn.replace("ем", "yem")
    matn = matn.replace("еб", "yeb")
    matn = matn.replace("ер", "yer")
    matn = matn.replace("еп", "yep")
    matn = matn.replace("еф", "yef")
    matn = matn.replace("ел", "yel")
    matn = matn.replace("енг", "yeng")
    matn = matn.replace("я", "ya")
    matn = matn.replace("ё", "yo‘")
    matn = matn.replace("ў", "o'")
    matn = matn.replace("ғ", "g'")
    matn = matn.replace("ъ", "'")
    matn = matn.replace("ю", "yu")
    matn = matn.replace("ш", "sh")
    matn = matn.replace("ч", "ch")
    matn = matn.replace("а", "a")
    matn = matn.replace("б", "b")
    matn = matn.replace("д", "d")
    matn = matn.replace("е", "e")
    matn = matn.replace("ф", "f")
    matn = matn.replace("г", "g")
    matn = matn.replace("х", "h")
    matn = matn.replace("и", "i")
    matn = matn.replace("ж", "j")
    matn = matn.replace("к", "k")
    matn = matn.replace("л", "l")
    matn = matn.replace("м", "m")
    matn = matn.replace("н", "n")
    matn = matn.replace("о", "o")
    matn = matn.replace("п", "p")
    matn = matn.replace("қ", "q")
    matn = matn.replace("р", "r")
    matn = matn.replace("с", "s")
    matn = matn.replace("т", "t")
    matn = matn.replace("у", "u")
    matn = matn.replace("в", "v")
    matn = matn.replace("ҳ", "x")
    matn = matn.replace("й", "y")
    matn = matn.replace("з", "z")
    matn = matn.replace("ц", "s")
    matn = matn.replace("э", "e")

    matn = matn.replace("Ў", "O‘")
    matn = matn.replace("Ғ", "G‘")
    matn = matn.replace("Ев", "Yev")
    matn = matn.replace("Ем", "Yem")
    matn = matn.replace("Еб", "Yeb")
    matn = matn.replace("Ер", "Yer")
    matn = matn.replace("Еп", "Yep")
    matn = matn.replace("Еф", "Yef")
    matn = matn.replace("Ел", "Yel")
    matn = matn.replace("Енг", "Yeng")
    matn = matn.replace("Я", "Ya")
    matn = matn.replace("Ё", "Yo‘")
    matn = matn.replace("Ў", "O'")
    matn = matn.replace("Ғ", "G'")
    matn = matn.replace("Ъ", "'")
    matn = matn.replace("Ю", "Yu")
    matn = matn.replace("Ш", "Sh")
    matn = matn.replace("Ч", "Ch")
    matn = matn.replace("А", "A")
    matn = matn.replace("Б", "B")
    matn = matn.replace("Д", "D")
    matn = matn.replace("Е", "E")
    matn = matn.replace("Ф", "F")
    matn = matn.replace("Г", "G")
    matn = matn.replace("Х", "H")
    matn = matn.replace("И", "I")
    matn = matn.replace("Ж", "J")
    matn = matn.replace("К", "K")
    matn = matn.replace("Л", "L")
    matn = matn.replace("М", "M")
    matn = matn.replace("Н", "N")
    matn = matn.replace("О", "O")
    matn = matn.replace("П", "P")
    matn = matn.replace("Қ", "Q")
    matn = matn.replace("Р", "R")
    matn = matn.replace("С", "S")
    matn = matn.replace("Т", "T")
    matn = matn.replace("У", "U")
    matn = matn.replace("В", "V")
    matn = matn.replace("Ҳ", "X")
    matn = matn.replace("Й", "Y")
    matn = matn.replace("З", "Z")
    matn = matn.replace("Ц", "S")
    matn = matn.replace("Э", "E")

    # matn = matn.split(". ")
    # n = 0
    # matnlar_soz =""
    # for m in matn:
    #    m = m.capitalize()
    #   matn[n] = m
    #    matnlar_soz += f"{matn[n]}. "
    #    n += 1

    matnlar.insert(1.0,matn)
    
def lotin_to_kril():
    matn = soz.get(1.0, END)
    #matn = matn.lower()

    matn = matn.replace("Yu", "Ю")
    matn = matn.replace("Sh", "Ш")
    matn = matn.replace("Ch", "Ч")
    matn = matn.replace("Ye", "Е")
    matn = matn.replace("Ya", "Я")
    matn = matn.replace("Yo‘", "Ё")
    matn = matn.replace("Yo'", "Ё")

    matn = matn.replace("o‘", "ў")
    matn = matn.replace("g‘", "ғ")
    matn = matn.replace("ye", "е")
    matn = matn.replace("ya", "я")
    matn = matn.replace("yo‘", "ё")
    matn = matn.replace("yo'", "ё")
    matn = matn.replace("o'", "ў")
    matn = matn.replace("g'", "ғ")
    matn = matn.replace("'", "ъ")
    matn = matn.replace("yu", "ю")
    matn = matn.replace("sh", "ш")
    matn = matn.replace("ch", "ч")
    matn = matn.replace("a", "а")
    matn = matn.replace("b", "б")
    matn = matn.replace("d", "д")
    matn = matn.replace("e", "е")
    matn = matn.replace("f", "ф")
    matn = matn.replace("g", "г")
    matn = matn.replace("h", "ҳ")
    matn = matn.replace("i", "и")
    matn = matn.replace("j", "ж")
    matn = matn.replace("k", "к")
    matn = matn.replace("l", "л")
    matn = matn.replace("m", "м")
    matn = matn.replace("n", "н")
    matn = matn.replace("o", "о")
    matn = matn.replace("p", "п")
    matn = matn.replace("q", "қ")
    matn = matn.replace("r", "р")
    matn = matn.replace("s", "с")
    matn = matn.replace("t", "т")
    matn = matn.replace("u", "у")
    matn = matn.replace("v", "в")
    matn = matn.replace("x", "ҳ")
    matn = matn.replace("y", "й")
    matn = matn.replace("z", "з")

    matn = matn.replace("O‘", "Ў")
    matn = matn.replace("G‘", "Ғ")
    matn = matn.replace("O'", "Ў")
    matn = matn.replace("G'", "Ғ")
    matn = matn.replace("'", "ъ")

    matn = matn.replace("A", "А")
    matn = matn.replace("B", "Б")
    matn = matn.replace("D", "Д")
    matn = matn.replace("E", "Е")
    matn = matn.replace("F", "Ф")
    matn = matn.replace("G", "Г")
    matn = matn.replace("H", "Х")
    matn = matn.replace("I", "И")
    matn = matn.replace("J", "Ж")
    matn = matn.replace("K", "К")
    matn = matn.replace("L", "Л")
    matn = matn.replace("M", "М")
    matn = matn.replace("N", "Н")
    matn = matn.replace("O", "О")
    matn = matn.replace("P", "П")
    matn = matn.replace("Q", "Қ")
    matn = matn.replace("R", "Р")
    matn = matn.replace("S", "С")
    matn = matn.replace("T", "Т")
    matn = matn.replace("U", "У")
    matn = matn.replace("V", "В")
    matn = matn.replace("X", "Ҳ")
    matn = matn.replace("Y", "Й")
    matn = matn.replace("Z", "З")

    #matn = matn.split(". ")
    #n = 0
    #matnlar_soz =""
    #for m in matn:
    #    m = m.capitalize()
    #   matn[n] = m
    #    matnlar_soz += f"{matn[n]}. "
    #    n += 1
    matnlar.insert(1.0,matn)
    
def clear_soz():
    soz.delete(1.0, END)
    
def clear_matn():
    matnlar.delete(1.0, END)

def select_all():
    matnlar.tag_add('sel','1.0','end')
    matnlar.tag_config('sel',background='deepskyblue', foreground='white')
    

lotin_kril_bt = Button(window, text="Lotindan krillga", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=lotin_to_kril)
lotin_kril_bt.place(x=250,y=270)

kril_lotin_bt = Button(window, text="Криллдан лотинга", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=kril_to_lotin)
kril_lotin_bt.place(x=840,y=270)

btn_clear_soz = Button(window, text="Clear", font=("Times new Roman",10), bg="red", bd=3,fg="white", command=clear_soz)
btn_clear_soz.place(x=1135,y=238)

paste_bt = Button(window, text="Nusxalangan matnni joylash", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=lambda:soz.event_generate("<<Paste>>"))
paste_bt.place(x=500,y=270)

select_all_bt = Button(window, text="Barchasini belgilash", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=select_all)
select_all_bt.place(x=230,y=560)

cut_btn = Button(window, text="Qirqib olish", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=lambda:matnlar.event_generate("<<Cut>>"))
cut_btn.place(x=550,y=560)

copy_bt = Button(window, text="Nusxa olish", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=lambda:matnlar.event_generate("<<Copy>>"))
copy_bt.place(x=860,y=560)

btn_clear_matn = Button(window,text="Clear", font=("Times new Roman",10), bg="red", bd=3,fg="white", command=clear_matn,)
btn_clear_matn.place(x=1135,y=528)

def help_info():
    
    window = tk.Tk()
    window.title("Krill to lotin or lotin to krill ")
    window.configure(bg="LightSteelBlue")
    window.geometry("1000x600")
    window.minsize(450,340)
    window.resizable(True,True)
    
    malumot = f"Bu dastur lotin yozuvidagi mantni krill yozuviga yoki aksincha o'tkazuvchi dastur"

    soz_malumot = f"Birinchi maydonchaga tarjima qilinishi kerak bo'lgan matn kiritiladi."
    matn_malumot = f"Ikkinchi maydonchada tarjima qilingan matn paydo bo'ladi."

    clear_malumot = f"> Belgilangan maydonni tozalaydi."
    lotin_krill_malumot = f"> Birinchi maydondagi matnni krill yozuviga o'tkazadi."
    krill_lotin_malumot = f"> Birinchi maydondagi matnni lotin yozuviga o'tkazadi."
    nushalangan_malumot = f"> Kompyuter xotirasiga nusxalab olgan malumotingizni maydonchaga tashlab beradi."
    qirqish_malumot = f"> Belgilangan matnni kompyuter xotirasiga vaqtinchalik ko'chirib oladi."
    kochirish_malumot = f"> Belgilangan matnni kompyuter xotirasiga vaqtinchalik nusxalab oladi."
    barchasi_malumot = f"> Ikkinchi maydonchadagi ma'lumotni barchasini belgilab beradi."

    yordam_malumot = f"Dastur tuzishda imlo.uz sayti ma'lumotlaridan foydalanildi."
    dasturchi_malumot = f"Dastur Mirzayev Xolmirza tomonidan yaratilgan. \nDastur haqida fikr va mulohazalaringizni kutib qolaman."
    boglanish_malumot = f"Bog'lanish uchun manzillar: \n \nTelegram: @mxolmirzad \nInstagram: @mxolmirzad \nFacebok: @mxolmirzad \n \nElektron pochta: mxolmirzad474@gmail.com"

    sarlavha = Label(window, text=malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
    sarlavha.place(x=200, y=2)

    
    # ekran_image = PhotoImage(file="ekran_1.png")
    
    def maydon_info():
        
        ekran = Label(window, bg="LightSteelBlue", width=1000, height=600)
        ekran.place(x=0,y=100)
        
        # maydon_image_bt = Label(window, image=ekran_image, width=100, height=100,bd=0, bg="LightSteelBlue")
        # maydon_image_bt.place(x=200, y=200)
        
        birinchi_maydon_matn = Label(window, text=soz_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
        birinchi_maydon_matn.place(x=50, y=110)
        
        ikkinchi_maydon_matn = Label(window, text=matn_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
        ikkinchi_maydon_matn.place(x=50, y=160)
        

    def tugma_info():
        
        ekran = Label(window, bg="LightSteelBlue", width=1000, height=600)
        ekran.place(x=0,y=100)
        
        lotin_kril_bt = Button(window, text="Lotindan krillga", font=("Times new Roman",14), bg="Cornsilk", bd=5)
        lotin_kril_bt.place(x=50,y=110)
        
        lotin_krill_malumot_label = Label(window, text=lotin_krill_malumot, font=("Times new Roman",16), bg="LightSteelBlue")
        lotin_krill_malumot_label.place(x=300, y=110)

        kril_lotin_bt = Button(window, text="Криллдан лотинга", font=("Times new Roman",14), bg="Cornsilk", bd=5)
        kril_lotin_bt.place(x=50,y=160)
        
        krill_lotin_malumot_label = Label(window, text=krill_lotin_malumot, font=("Times new Roman",16), bg="LightSteelBlue")
        krill_lotin_malumot_label.place(x=300, y=160)
        
        btn_clear_soz = Button(window, text="Clear", font=("Times new Roman",14), bg="red", bd=3,fg="white")
        btn_clear_soz.place(x=50,y=210)
        
        clear_malumot_label = Label(window, text=clear_malumot, font=("Times new Roman",16), bg="LightSteelBlue")
        clear_malumot_label.place(x=300, y=210)

        paste_bt = Button(window, text="Nusxalangan matnni joylash", font=("Times new Roman",14), bg="Cornsilk", bd=5)
        paste_bt.place(x=50,y=260)
        
        nushalangan_malumot_label = Label(window, text=nushalangan_malumot, font=("Times new Roman",16), bg="LightSteelBlue")
        nushalangan_malumot_label.place(x=300, y=260)

        select_all_bt = Button(window, text="Barchasini belgilash", font=("Times new Roman",14), bg="Cornsilk", bd=5)
        select_all_bt.place(x=50,y=310)
        
        barchasi_malumot_label = Label(window, text=barchasi_malumot, font=("Times new Roman",16), bg="LightSteelBlue")
        barchasi_malumot_label.place(x=300, y=310)

        cut_btn = Button(window, text="Qirqib olish", font=("Times new Roman",14), bg="Cornsilk", bd=5)
        cut_btn.place(x=50,y=360)
        
        qirqish_malumot_label = Label(window, text=qirqish_malumot, font=("Times new Roman",16), bg="LightSteelBlue")
        qirqish_malumot_label.place(x=300, y=360)
        
        copy_bt = Button(window, text="Nusxa olish", font=("Times new Roman",14), bg="Cornsilk", bd=5, )
        copy_bt.place(x=50,y=410)
        
        nushalangan_malumot_label = Label(window, text=nushalangan_malumot, font=("Times new Roman",16), bg="LightSteelBlue")
        nushalangan_malumot_label.place(x=300, y=410)
        
    def dasturchi_info():
        
        ekran = Label(window, bg="LightSteelBlue", width=1000, height=600)
        ekran.place(x=0,y=100)
        
        yordam_matn = Label(window, text=yordam_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
        yordam_matn.place(x=270, y=120)
        
        dasturchi_matn = Label(window, text=dasturchi_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
        dasturchi_matn.place(x=280, y=150)
        
        boglanish_matn = Label(window, text=boglanish_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
        boglanish_matn.place(x=320, y=210)
            
    maydon_bt = Button(window, text="Maydonlar haqida ma'lumot", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=maydon_info)
    maydon_bt.place(x=50,y=50)

    tugma_bt = Button(window, text="Tugmalar haqida ma'lumot", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=tugma_info)
    tugma_bt.place(x=400,y=50)

    dasturchi_bt = Button(window, text="Dasturchi haqida ma'lumot", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=dasturchi_info)
    dasturchi_bt.place(x=720,y=50)

    window.mainloop()

help_image = PhotoImage(file="help_1.ico")
help_image_bt = Button(window, image=help_image, width=100, height=100, command=help_info)
help_image_bt.place(x=0, y=578)

logo_image = PhotoImage(file="logo_1.ico")
help_image_bt = Label(window, image=logo_image, width=100, height=100)
help_image_bt.place(x=1100, y=578)

window.mainloop()