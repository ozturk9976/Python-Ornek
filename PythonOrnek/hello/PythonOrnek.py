#OOP
#class => person(name,surname,age,birthday,calculateAge())
#instance (object)

class calisan:
    def __init__(self,name,surname,age): #self => oluşturulan değişkene otomatik gönderilir
        print("__init__ fonksiyonu çalışıyor") #calisan1 = self
        #attributes
        self.name = name
        self.surname = surname
        self.age = age
    def show_info(self):
        print(f"Ad:{self.name} Soyad: {self.surname}  Yaş: {self.age}")

calisan1 = calisan("Ali","Veli",10)
print(calisan1.name,calisan1.surname,calisan1.age)      

calisan2 = calisan("Ayşe","Yıldız",35)
print(calisan2.name,calisan2.surname,calisan2.age)

calisan1.show_info()





























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




















