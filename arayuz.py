from faulthandler import disable
from operator import lt
import insta
import jsonSil
import hikayebegenme
import takipEtmeyeniCikar
import Twitter
from tkinter import *
from tkinter import messagebox 
from threading import Thread
import notifypy
yeni=notifypy.Notify()

def bildirim():
    yeni.title="Instagram"
    yeni.message="İslemler Bitmiştir"
    yeni.application_name="Instagram"
    yeni.send()


def otoB():
    o1=Thread(target=OtoBaslaFun)
    o1.start()

def otoE():
    e1=Thread(target=ElIleGirisFun)
    e1.start()

def otoBegenme():
    hb=Thread(target=HikayeBegenme)
    hb.start()

def otoTakipCikar():
    tc=Thread(target=TakipciCikarFun)
    tc.start()
    messagebox.showinfo("Consola Bakınız","Lütfen konsoldaki soruyu cevaplayın")

def otoTwitter():
    ta=Thread(target=TwitterBasla)
    ta.start()

def otoLTemizle():
    Lt=Thread(target=ListeTemizle)
    Lt.start()

def otoK():
    k1=Thread(target=Kapat)
    k1.start()

#Thread sornası

def OtoBaslaFun():
    global Ilk_Defa_Giris
    Ilk_Defa_Giris=False
    insta.BaslaIslem(Toplam_Islme1_Input.get(),Bir_Sayfada_KacKisi_Takip1_Input.get(),Begen_Yorum_Sayisi1_Input.get(),Ilk_Defa_Giris,kullaniciAdiInput.get(),sifreInput.get())
    
def ElIleGirisFun():
    if(kullaniciAdiInput.get()!="" and sifreInput.get()!=""):
        Ilk_Defa_Giris=True
        insta.BaslaIslem(Toplam_Islme1_Input.get(),Bir_Sayfada_KacKisi_Takip1_Input.get(),Begen_Yorum_Sayisi1_Input.get(),Ilk_Defa_Giris,kullaniciAdiInput.get(),sifreInput.get())
    else:
        messagebox.showerror("Sorun","kullanci adi ve sifre yeri bos")

def HikayeBegenme():
    try:
        hikayebegenme.basla()
    except:
        print("baslamadı")
    bildirim()
def TakipciCikarFun():
    try:
        takipEtmeyeniCikar.basla()
        
        yeni.send()
    except:
        print("takip etmeyen den çıkıldı")
        messagebox.showerror("hata","takip etmeyeyeni çıkar başarsız")
    bildirim()

def TwitterBasla():
    Twitter.basla()
    yeni.title="Twitter1"
    yeni.message="İslemler Bitmiştir"
    yeni.application_name="Twitter2"
    yeni.send()

def ListeTemizle():
    jsonSil.basla()
    bildirim()

def bilgiCek():
    try:
        Takip_Edilen.config(text="Takip_Edilen: "+str(insta.kacKisiTakipEdildi))
    except:
        print("Takip Edilen cekilemedi")
        messagebox.showerror("Hata","Takip edilen okumada sorun var \n BASLATIGINIZDAN EMİN OLUN")
    try:
        Yorum_Begeni.config(text="Yorum_Begeni: "+str(insta.begen_yorum))
    except:
        print("yorum da sorun cikti")

def Kapat():
    
    try:
        insta.driver.close()
    except:
        print("takip et kapatlilmadı")

    try:
        hikayebegenme.driver.close()
    except:
        print("Hikaye begen kapatlilmadı")

    try:
        takipEtmeyeniCikar.driver.close()
    except:
        print("Takip etmeyeeni çikar kapatlilmadı")

    try:
        Twitter.driver.close()
    except:
        print("Twitter Takip et kapatlilmadı")


#############################       Arya yüz
root=Tk()
root.title("Instagram Botu")
root.geometry("1000x500")

#root.config(bg="#FF7F01")

global oto
oto =Label(root,text="Oto")
oto.place(relx=0.2,rely=0.15,relwidth=0.2,relheight=0.1)

global otoBasla
otoBasla=Button(root,text="Basla",command=otoB,width=4,height=3)
otoBasla.place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.1)


#'''''blok1{
blok1x=0.01
blok1y=0.4
global Toplam_Islme1
Toplam_Islme1 =Label(root,text="Toplam Islem :")
Toplam_Islme1.place(relx=blok1x,rely=blok1y,relwidth=0.2,relheight=0.1)

global Toplam_Islme1_Input
Toplam_Islme1_Input=Entry(root,width=40,bg="#FF7F00")
Toplam_Islme1_Input.place(relx=blok1x+0.19,rely=blok1y+0.02,relwidth=0.03,relheight=0.05)

global Toplam_Islme2
Toplam_Islme2 =Label(root,text="//10")
Toplam_Islme2.place(relx=blok1x+0.23,rely=blok1y,relwidth=0.022,relheight=0.1)


global Bir_Sayfada_KacKisi_Takip1
Bir_Sayfada_KacKisi_Takip1 =Label(root,text="Bir Sayfada KacKisi Takip Edilecek :")
Bir_Sayfada_KacKisi_Takip1.place(relx=blok1x,rely=blok1y+0.1,relwidth=0.2,relheight=0.1)

global Bir_Sayfada_KacKisi_Takip1_Input
Bir_Sayfada_KacKisi_Takip1_Input=Entry(root,width=40,bg="#FF7F00")
Bir_Sayfada_KacKisi_Takip1_Input.place(relx=blok1x+0.19,rely=blok1y+0.12,relwidth=0.03,relheight=0.05)

global Bir_Sayfada_KacKisi_Takip2
Bir_Sayfada_KacKisi_Takip2 =Label(root,text="//9")
Bir_Sayfada_KacKisi_Takip2.place(relx=blok1x+0.23,rely=blok1y+0.1,relwidth=0.022,relheight=0.1)


global Begen_Yorum_Sayisi1
Begen_Yorum_Sayisi1 =Label(root,text="Begen Yorum Sayisi Input :")
Begen_Yorum_Sayisi1.place(relx=blok1x,rely=blok1y+0.2,relwidth=0.2,relheight=0.1)

global Begen_Yorum_Sayisi1_Input
Begen_Yorum_Sayisi1_Input=Entry(root,width=40,bg="#FF7F00")
Begen_Yorum_Sayisi1_Input.place(relx=blok1x+0.19,rely=blok1y+0.22,relwidth=0.03,relheight=0.05)

global Begen_Yorum_Sayisi2
Begen_Yorum_Sayisi2 =Label(root,text="//2")
Begen_Yorum_Sayisi2.place(relx=blok1x+0.23,rely=blok1y+0.2,relwidth=0.02,relheight=0.1)


global Takip_Edilen
Takip_Edilen =Label(root,text="Takip_Edilen: 0",fg="#FF7F00")
Takip_Edilen.place(relx=blok1x+0.26,rely=blok1y,relwidth=0.13,relheight=0.1)

global Yorum_Begeni
Yorum_Begeni =Label(root,text="Yorum_Begeni: 0",fg="#FF7F00")
Yorum_Begeni.place(relx=blok1x+0.26,rely=blok1y+0.1,relwidth=0.13,relheight=0.1)

global BilgiCekkapat
BilgiCek=Button(root,text="Bilgi Cek",command=bilgiCek,width=4,height=3)
BilgiCek.place(relx=blok1x+0.26,rely=blok1y+0.2,relwidth=0.13,relheight=0.1)

def isCheckedTakipEtmeyeiniCikar():
    global TBaslaFalse 
    global hBegenFalse
    global TCikarFalse
    global hIzleFalse
    global LTemizleFalse
    TBaslaFalse=False
    LTemizleFalse=False
    hBegenFalse =False
    TCikarFalse=False
    hIzleFalse=False

    if TCikar.get() == 1:
        checkbtn['state'] = NORMAL
        checkbtn.configure(text='Başla!')
        TCikarFalse=True
    elif TCikar.get() == 0 :
        checkbtn['state'] = DISABLED
        checkbtn.configure(text='Seçim Yok!!')
        TCikarFalse=False

def isCheckedTwiter():
    global TBaslaFalse 
    global hBegenFalse
    global TCikarFalse
    global hIzleFalse
    global LTemizleFalse
    TBaslaFalse=False
    LTemizleFalse=False
    hBegenFalse =False
    TCikarFalse=False
    hIzleFalse=False

    if TBasla.get() == 1:
        checkbtn['state'] = NORMAL
        checkbtn.configure(text='Başla!')
        TBaslaFalse=True
    elif TBasla.get() == 0 :
        checkbtn['state'] = DISABLED
        checkbtn.configure(text='Seçim Yok!!')
        TBaslaFalse=False

def isCheckedListeTemizle():
    global TBaslaFalse 
    global hBegenFalse
    global TCikarFalse
    global hIzleFalse
    global LTemizleFalse
    TBaslaFalse=False
    LTemizleFalse=False
    hBegenFalse =False
    TCikarFalse=False
    hIzleFalse=False

    if LTemizle.get()==1:
        checkbtn["state"]=NORMAL
        checkbtn.configure(text="Başla")
        LTemizleFalse=True
    elif LTemizle.get()==0:
        checkbtn["state"]=DISABLED
        checkbtn.configure(text="Secim Yok!!")
        LTemizleFalse=False

def isChecked():
    global TBaslaFalse 
    global hBegenFalse
    global TCikarFalse
    global hIzleFalse
    global LTemizleFalse
    TBaslaFalse=False
    LTemizleFalse=False
    hBegenFalse =False
    TCikarFalse=False
    hIzleFalse=False
    if hBegen.get() == 1:
        checkbtn['state'] = NORMAL
        checkbtn.configure(text='Başla!')
        hBegenFalse=True
    elif hBegen.get() == 0 :
        checkbtn['state'] = DISABLED
        checkbtn.configure(text='Seçim Yok!!')
        hBegenFalse=False

    if hIzle.get() == 1:
        checkbtn['state'] = NORMAL
        checkbtn.configure(text='Başla!')
        hIzleFalse=True
        
    if hIzle.get() == 0 :
        checkbtn['state'] = DISABLED
        checkbtn.configure(text='Seçim Yok!!')
        hIzleFalse=False
    if hIzle.get() == 1 and hBegen.get()==1 and TCikar.get() == 1 :
        checkbtn['state'] = DISABLED
        checkbtn.configure(text='3 Seçim Olmaz !!')
    print("buraya  giildi")

def CheckedBasla():
    
    if(hIzleFalse==True):
        pass
    if(hBegenFalse==True):
        otoBegenme()
    if(TCikarFalse==True):
        otoTakipCikar()
    if TBaslaFalse==True:
        otoTwitter()
    if LTemizleFalse==True:
        print("liste temizleniyor")
        otoLTemizle()
    
    
hIzle = IntVar()
hBegen = IntVar()
TCikar = IntVar()
TBasla=IntVar()
LTemizle=IntVar()

Checkbutton(root,text="Hikaye İzle", variable=hIzle, onvalue=1, offvalue=0, command=isChecked)\
    .place(relx=blok1x+0.1,rely=blok1y+0.3,relwidth=0.08,relheight=0.03)
Checkbutton(root,text="Hikaye Beğen", variable=hBegen, onvalue=1, offvalue=0, command=isChecked)\
    .place(relx=blok1x+0.1,rely=blok1y+0.335,relwidth=0.095,relheight=0.03)
Checkbutton(root,text="Takip Etmeyeneleri Çikar", variable=TCikar, onvalue=1, offvalue=0, command=isCheckedTakipEtmeyeiniCikar)\
    .place(relx=blok1x+0.1,rely=blok1y+0.370,relwidth=0.152,relheight=0.03)
Checkbutton(root,text="Twitter", variable=TBasla, onvalue=1, offvalue=0, command=isCheckedTwiter)\
    .place(relx=blok1x+0.1,rely=blok1y+0.405,relwidth=0.06,relheight=0.03)
Checkbutton(root,text="Takip eden listesini sil (el ile eklenler haric)", variable=LTemizle, onvalue=1, offvalue=0, command=isCheckedListeTemizle)\
    .place(relx=blok1x+0.1,rely=blok1y+0.435,relwidth=0.245,relheight=0.03)

checkbtn = Button(root,text='Seçim Yok!', state=DISABLED, padx=20, pady=15,command=CheckedBasla)
checkbtn.place(relx=blok1x+0.26,rely=blok1y+0.3,relwidth=0.2,relheight=0.1)


#^^^^blok1}

global urlLabel1
urlLabel1 =Label(root,text="El İle")
urlLabel1.place(relx=0.4,rely=0.15,relwidth=0.6,relheight=0.1)

global kullaniciAdi
kullaniciAdi =Label(root,text="Kullanici Adi: ")
kullaniciAdi.place(relx=0.5,rely=0.3,relwidth=0.2,relheight=0.05)

global kullaniciAdiInput
kullaniciAdiInput=Entry(root,width=40,bg="#FF7F00")
kullaniciAdiInput.place(relx=0.7,rely=0.3,relwidth=0.2,relheight=0.05)


global sifre
sifre =Label(root,text="Şifre: ")
sifre.place(relx=0.5,rely=0.4,relwidth=0.2,relheight=0.05)

global sifreInput
sifreInput=Entry(root,width=40,bg="#FF7F00")
sifreInput.place(relx=0.7,rely=0.4,relwidth=0.2,relheight=0.05)

global elIleBasla
elIleBasla=Button(root,text="Basla",command=otoE,width=4,height=3)
elIleBasla.place(relx=0.7,rely=0.5,relwidth=0.2,relheight=0.1)

#kapt
global kapat1
kapat1=Button(root,text="Kapat",command=otoK,width=4,height=3,bg="#ff0000")
kapat1.place(relx=0.8,rely=0.9,relwidth=0.2,relheight=0.1)


#############################       Arya yüz

root.mainloop()
