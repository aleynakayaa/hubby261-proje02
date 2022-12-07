from tkinter import *
from tkinter import ttk
import tkinter as tk
import time
from dataURL import DataURL
from getURL import GetURL

pencere = Tk()
pencere.title("Ana Pencere")
pencere.geometry("300x200")

def urllistele():
    pencere1 = Tk()
    pencere1.title("URL Listesi")
    pencere.geometry("300x200")
    with open("dataUrl.txt") as f:
        liste = f.read()
    etiket= Label(pencere1, text=liste)
    etiket.pack()
    buton1 = Button(pencere1, text= "Geri Dön", command= pencere1.destroy)
    buton1.pack()

def urlekle():
    pencere2 = Tk()
    pencere2.title("URL Ekle")
    pencere.geometry("300x200")
    etiket= Label(pencere2 )
    etiket.pack()

def orumcekgonder():
    pencere3 = Tk()
    pencere3.title("Örümcek Gönder")
    pencere.geometry("300x200")
    with open("getURL.py") as f:
        liste = f.read()
    etiket= Label(pencere3, text=liste)
    etiket.pack()
    buton3 = Button(pencere3, text= "Geri Dön", command= pencere3.destroy)
    buton3.pack()

def sonuclarılistele():
    pencere4 = Tk()
    pencere4.title("Sonuçları Listele")
    pencere.geometry("300x200")
    with open("getURL.txt") as f:
        liste = f.read()
    etiket= Label(pencere4, text=liste)
    etiket.pack()
    buton4 = Button(pencere4, text= "Geri Dön", command= pencere4.destroy)
    buton4.pack()

def quit():
    pencere5 = Tk()
    pencere5.title("Çıkış")
    pencere.geometry("300x200")
    buton5 = Button(pencere5, text="Geri Dön", command=quit)
    buton5.pack()


menuOgeleri = ["URL Listele", "URL Ekle", "Örümcek Gönder", "Sonuçları Listele", "Çıkış"]
menuFonksiyonlari = [urllistele, urlekle, orumcekgonder, sonuclarılistele,quit]

for idx, oge in enumerate(menuOgeleri):
    ttk.Button(pencere, text= " " +oge, command=menuFonksiyonlari[idx]).pack()




pencere.mainloop()

useDataURL = DataURL()
useGetURL = GetURL()

#print("-: Mini Örümceğe hoş geldiniz! :-")
#print("|------------------------------|")
#print("")
#time.sleep(2)

while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    menuSecim = (input("Tercihiniz: "))
    if menuSecim.isdigit():
        menuSecim = int(menuSecim)
        if menuSecim == 0:
            print("Mini Örümcek kapatılıyor...")
            time.sleep(1)
            break
        elif menuSecim == 1:
            useDataURL.dataRead()
        elif menuSecim == 2:
            useDataURL.dataWrite()
        elif menuSecim == 3:
            useGetURL.getWeb()
        elif menuSecim == 4:
            useGetURL.getList()
        elif menuSecim>=4:
            print("0 ile 4 arasında bir seçim yapınız.")
    else:
        print("Lütfen geçerli bir menü numarası giriniz.")