from ast import If
import random
from turtle import circle






#OOP
#class => person(name,surname,age,birthday,calculateAge())
#instance (object)

# class calisan:
#     def __init__(self,name,surname,age): #self => oluşturulan değişkene otomatik gönderilir
#         print("__init__ fonksiyonu çalışıyor") #calisan1 = self
#         #attributes
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def show_info(self):
#         print(f"Ad:{self.name} Soyad: {self.surname}  Yaş: {self.age}")

# calisan1 = calisan("Ali","Veli",10)
# print(calisan1.name,calisan1.surname,calisan1.age)      

# calisan2 = calisan("Ayşe","Yıldız",35)
# print(calisan2.name,calisan2.surname,calisan2.age)

# calisan1.show_info()

# calisan.show_info(calisan1)




################################################################

#ÖRNEK1
#SAYI TAHMİN OYUNU
#BİR TANE OYUNCU SINIFI OLUŞTURUN
#OYUNCU SINIFININ PUAN,SAYI GİBİ DEĞİŞKENLERİ OLSUN
#OYNA METODU OLSUN
#BİLGİSAYARIN RASTGELE OLUŞTURDUĞU 1-10 ARASI SAYIYI HER SEFERİNDE
#TAHMİN ETMEYE ÇALIŞSIN
#BİLEMEZSE -5 PUAN BİLİRSE +50 PUAN KAZANSIN
#OYUN 100 PUAN OLUNCA VEYA 0 PUAN OLUNCA BİTSİN
#BAŞLANGIÇ PUANI FARKETMEZ

# class Oyun:
#     def __init__(self,isim,puan,pcpuan):
#         self.isim =isim
#         self.puan =puan
#         self.pcpuan = pcpuan

#     def zarPC(self):
#         self.zarPC = random.randint(1-10)
#         print(self.zarPC)
#     def zarPlayer(self):
#         self.zarPlayer = random.randint(1-10)
#         print(self.zarPlayer)

#     def puanlama(self):
#         if self.zarPC > self.zarPlayer:
#             self.zarPC +=10
#             self.zarPlayer -=10
#         if self.zarPlayer > self.zarPC:
#             self.zarPlayer += 10
#             self.zarPC -= 10

# oyun = Oyun("hamza",50,50)
# while True:
#     Oyun.zarPC()
#     Oyun.zarPlayer()
#     Oyun.puanlama()

#     if oyun.bilgisayarPuan == 100 or oyun.oyuncuPuan == 0:
#         print("PC kazandı")
#     if oyun.bilgisayarPuan == 0 or oyun.oyuncuPuan == 100:
#         print(oyun.isimgirdisi,"Kazandı")
#         break


# class oyun:
#     def __init__(self,isim,oyuncuPuan,bilgisayarPuan):
#         self.isimgirdisi = isim
#         self.oyuncuPuan = oyuncuPuan
#         self.bilgisayarPuan = bilgisayarPuan
#     isimgirdisi = input("Lütfen isminizi giriniz")


#     def zarPC(self):
#         self.zarPC = random.randint(1,10)
#         print(self.zarPC)

#     def zarOyuncu(self):
#         self.zarOyuncu = random.randint(1,10)
#         print(self.zarOyuncu)
    

#     def puanlama(self):
#         if self.zarPC > self.zarOyuncu:
#             self.bilgisayarPuan += 10
#             self.oyuncuPuan -= 5
#             print(self.bilgisayarPuan,self.oyuncuPuan)
#         if self.zarOyuncu > self.zarPC:
#             self.oyuncuPuan += 10
#             self.bilgisayarPuan -=5
#             print(self.bilgisayarPuan,self.oyuncuPuan)
    
# oyun = oyun("hamza",50,50)
# while True:
#     oyun.zarOyuncu()
#     oyun.zarPC()
#     oyun.puanlama()
#     if oyun.bilgisayarPuan == 100 or oyun.oyuncuPuan == 0:
#         print("PC kazandı")
#         break
#     if oyun.bilgisayarPuan == 0 or oyun.oyuncuPuan == 100:
#         print(oyun.isimgirdisi,"Kazandı")
#         break

########################################################################
        
# class oyun:
#     def __init__(self,isim,puan,bpuan):
#         ##attributes
#         self.isimgirdiisim = isim
#         self.puan = puan
#         self.bpuan = bpuan
        

#     isimgirdi = input("isim giriniz : ")

#     def zar1(self):
#          self.zar = random.randint(1,6)
#          print(self.zar)

#     def zar2(self):
#          self.zarGamer = random.randint(1,6)
#          print(self.zarGamer)


#     def puanla(self):
#             if self.zar < self.zarGamer:
#                 self.bpuan +=10
#                 self.puan -=5
#                 print(self.puan,self.bpuan)

#             if self.zar > self.zarGamer:
#                 self.puan += 10
#                 self.bpuan -=10
#                 print(self.puan,self.bpuan)

# oyun = oyun("Oyuncu",50,50)
# while True:
#    oyun.zar1()
#    oyun.zar2()
#    oyun.puanla()
#    if oyun.bpuan == 100 or oyun.puan == 0:
#        print("PC Kazandı")
#        break
#    if oyun.puan == 100 or oyun.bpuan == 0:
#        print(oyun.isimgirdiisim, "kazandı")
#        break

#################################################################

#ÖRNEK-2

# class Circle:
#     #Class object attribute
#     pi = 3.14

#     def __init__(self,yaricap=1):
#         self.yaricap = yaricap;
#         #methods
#     def cevre_hesapla(self):
#         return 2*self.pi+self.yaricap
#     def alan_hesapla(self):
#         return self.pi *(self.yaricap**2)
    
# c1 = Circle() # yaricap = 1
# c2 = Circle(5) 

# print(f"c1 : alan =  { c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
# print(f"c2 : alan =  { c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")

#####################################################################

# lst = [1,2,3]
# lst2 = [1,2,3,4,5]

# result = type(lst)
# result = type(lst2)


# print(result)


#class


# class Person:
    

#     #class attributes
#     address = "no information given"

#     #construcor(yapıcı metod)
#     def __init__(this,name,year):  #self = classtan türetilen herhangi bir objeyi temsil eder
        
#         #object attributes
#         this.name =name
#         this.year = year
        


#     #instance methods
#     def intro(self):
#         print("hello there")



#     #object,instance
# p1 = Person(name = "ali",year ="1990")
# p2 = Person(name ="yagmur",year ="1993")

# p1.intro()

#     #updating
# p1.name = "Ahmet"
# p2.year = 1983
#     #accesing object attributes

# print(f"name:{p1.name} year{p1.year} address:{p1.adress}")
# print(f"name:{p2.name} year{p2.year} address:{p2.adress}")

############################################################################

# 1-Klavyeden girilen 2 adet not bilgisi ortalama 50 üzeri iste geçti ,değilse kaldı yazan program

# vizeNot = input("Vize notunuzu giriniz")
# finalNot = input("Final notunuzu giriniz")
# vizeNotOrtalama = int(vizeNot) / 60
# finalNotOrtalama = int(finalNot) / 40


# ortalamaNot = vizeNotOrtalama + finalNotOrtalama

# if ortalamaNot>50:
#     print("Geçtiniz")
# else :
#     print("kaldınız")
#########################################################################

#Contrustur metotun icindeki parametrelere
#Miktar tur ve cevrilcektur
#Biri yazdir  Diger metotta cevir diye metot
#Sinifin adi cevirici
#Bu klavyeden girişleri ise metot disinda sorucan main yani
#3 tane olcak
#Miktar giriniz para turu giriniz ve cevrilcek turu giriniz diye

class Cevirici:
      def __init__(self,miktar,tür,cevirilecektür):
         self.miktar = miktar
         self.tür = tür
         self.cevirilecektür = cevirilecektür

      def yazdir(self):
        print(self.sonuc)

      def cevir(self):
        if self.tür == "dolar" and self.cevirilecektür == "tl":
            self.tldegeri = self.miktar * 16
            self.sonuc = self.tldegeri
        if self.tür == "tl" and self.cevirilecektür == "dolar":
            self.dolardegeri = self.miktar / 16
            self.sonuc = self.dolardegeri

while True:

  miktar = int(input("miktar giriniz"))
  tür = input(str("tür giriniz"))
  cevirilecektür = input(str("cevirilecektür giriniz"))

  Cevirici = Cevirici(miktar,tür,cevirilecektür)

  Cevirici.cevir()
  Cevirici.yazdir()
  break


            


            


# class Cevirici:
#     def __init__(self,miktar,tür,cevirilecektür):
#         self.miktar = miktar
#         self.tür = tür
#         self.cevirilecektür = cevirilecektür
        

#     def cevir(self):
#             if self.tür == "dolar" and self.cevirilecektür == "tl":
#                tldegeri = self.miktar * 17             
#                self.sonuc = tldegeri
#             if self.tür == "tl" and self.cevirilecektür == "dolar":
#                dolardegeri = self.miktar / 17
#                print("girdiğiniz dolar miktarının dolar değeri ", dolardegeri)
#                self.sonuc = dolardegeri

#     def yazdir(self):
#         print(self.sonuc)

#         miktar = int(input("miktar giriniz"))
#         tür = input("tür giriniz")
#         cevirilecektür = input("cevirilecektür giriniz")

              
#         cevir1=Cevirici(miktar,tür,cevirilecektür)
#         cevir1.cevir()
#         cevir1.yazdir()
    

        
        



            
        
        

    
            

                

                


   





    

        





# 2-Belirlenen kullanıcı adı ve şifre doğru girildiğinde "giriş başarılı" , yanlış girildiğinde "giriş başarısız" yazan program

# kullaniciAdi = input("lütfen kullanıcı adınızı girin")
# sifre = input("lütfen şifrenizi girin")

# while True:
#     girisEkranKullaniciAdi = input("lütfen belirlediğiniz kullanıcı adını girin")
#     if kullaniciAdi == girisEkranKullaniciAdi:
#         print("kullanıcı adını doğru girdiniz")
#     else :
#         print("kullanıcı adı uyuşmuyor")
#         break
#     girisEkranSifre = input("lütfen belirlediğiniz şifreyi girin")
#     if girisEkranSifre == sifre:
#         print("şifrenizi doğru girdiniz")
#     else:
#         print("şifre uyuşmuyor")
#         break
#     print("Giriş başarılı")
#     break

# 3-Klavyeden girilen sayının tek mi çift mi olduğunu gösteren program

# 4-bir mağazada alınan ürünün fiyatı 100 tl ve üzeri iste 5tl olan kargo ücreti alınmamaktadır
## ürünün fiyatı girilidğinde toplam ödenmesi gereken tutarı gösteren program

# 5-Kullanıcıdan girdiği iki sayı ve yapılacak işlem türü(toplama,çıkarma,çarpma,bölme) seçildiğinde, sonucu
## hesaplayarak ekranda gösteren program

# 6-klavyeden iki ürünün fiyatı girildiğinde toplam fiyat 200tl den fazla ise 2. üründen yüzde 25 indirim
## yaparak ödenece tutarı gösteren program

# 7-kullanıcıdan 2 tane sayı istenerek 1. sayı 2. sayıya tam bölünüyorsa ekrana yazan aksi durumda
## bölünmüyor diyerek kalanı ekrana yazan program


# 8-klavyeden girilen bir sayının seçime bağlı olarak karesini,küpünü ve karekökünü alan program



        


