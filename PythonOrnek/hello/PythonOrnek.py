import random

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


# 2-Belirlenen kullanıcı adı ve şifre doğru girildiğinde "giriş başarılı" , yanlış girildiğinde "giriş başarısız" yazan program
