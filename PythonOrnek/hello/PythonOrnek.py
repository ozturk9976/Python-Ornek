
# 1-Klavyeden girilen 2 adet not bilgisi ortalama 50 �zeri iste ge�ti ,de�ilse kald� yazan program

vizeNot = input("Vize notunuzu giriniz")
finalNot = input("Final notunuzu giriniz")
vizeNotOrtalama = int(vizeNot) / 60
finalNotOrtalama = int(finalNot) / 40


ortalamaNot = vizeNotOrtalama + finalNotOrtalama

if ortalamaNot>50:
    print("Geçtiniz")
else :
    print("kaldınız")





