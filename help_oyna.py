#MxolmirzaD

from tkinter import*
import tkinter as tk

window = tk.Tk()
window.title("Krill to lotin or lotin to krill ")
window.configure(bg="LightSteelBlue")
window.geometry("1000x600")
photo = tk.PhotoImage(file="help.png")
window.iconphoto(False, photo)
window.minsize(450,340)
window.resizable(True,True)

malumot = f"Bu dastur lotin yozuvidagi mantni krill yozuviga yoki aksincha o'tkazuvchi dastur"

soz_malumot = f"Birinchi maydonchaga tarjima qilinishi kerak bo'lgan matn kiritiladi."
matn_malumot = f"Ikkinchi maydonda tarjima qilingan matn paydo bo'ladi."

clear_malumot = f"> Belgilangan maydonni tozalaydi."
lotin_krill_malumot = f"> Birinchi maydondagi matnni krill yozuviga o'tkazadi."
krill_lotin_malumot = f"> Birinchi maydondagi matnni lotin yozuviga o'tkazadi."
nushalangan_malumot = f"> Kompyuter xotirasiga nusxalab olgan malumotingizni maydonchaga tashlab beradi."
qirqish_malumot = f"> Belgilangan matnni kompyuter xotirasiga vaqtinchalik ko'chirib oladi."
kochirish_malumot = f"> Belgilangan matnni kompyuter xotirasiga vaqtinchalik nusxalab oladi."
barchasi_malumot = f"> Ikkinchi maydonchadagi ma'lumotni barchasini belgilab beradi."

yordam_malumot = f"Dastur tuzishda imlo.uz sayti ma'lumotlaridan foydalanildi."
dasturchi_malumot = f"Dastur Mirzayev Xolmirza tomonidan yaratilgan. \nDastur haqida fikr va mulohazalaringizni kutib qolaman."
boglanish_malumot = f"Bog'lanish uchun manzillar \nTelegram: @mxolmirzad \nInstagram: @mxolmirzad \nFacebok: @mxolmirzad \nElektron pochta: mxolmirzad474@gmail.com"

sarlavha = Label(window, text=malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
sarlavha.place(x=200, y=2)

maydon_image = PhotoImage(file="ekran_1.PNG")

def maydon_info():
    
    ekran = Label(window, bg="LightSteelBlue", width=1000, height=600)
    ekran.place(x=0,y=100)
    
    maydon_image_bt = Button(window, image=maydon_image, width=500, height=250,bd=0, bg="LightSteelBlue")
    maydon_image_bt.place(x=250, y=120)
    
    birinchi_maydon_matn = Label(window, text=soz_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
    birinchi_maydon_matn.place(x=50, y=400)
    
    ikkinchi_maydon_matn = Label(window, text=matn_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
    ikkinchi_maydon_matn.place(x=50, y=450)
    

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
    
    maydon_image = PhotoImage(file="ekran_1.PNG")
    note_image_bt = Button(window, image=maydon_image, width=500, height=250,bd=0, bg="LightSteelBlue")
    note_image_bt.place(x=250, y=120)
    
    yordam_matn = Label(window, text=yordam_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
    yordam_matn.place(x=270, y=120)
    
    dasturchi_matn = Label(window, text=dasturchi_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
    dasturchi_matn.place(x=280, y=150)
    
    boglanish_matn = Label(window, text=boglanish_malumot, font=("Times new Roman",16), bg="LightSteelBlue" )
    boglanish_matn.place(x=320, y=205)
        
maydon_bt = Button(window, text="Maydonlar haqida ma'lumot", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=maydon_info)
maydon_bt.place(x=50,y=50)

tugma_bt = Button(window, text="Tugmalar haqida ma'lumot", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=tugma_info)
tugma_bt.place(x=400,y=50)

dasturchi_bt = Button(window, text="Dasturchi haqida ma'lumot", font=("Times new Roman",14), bg="Cornsilk", bd=5, command=dasturchi_info)
dasturchi_bt.place(x=720,y=50)

window.mainloop()