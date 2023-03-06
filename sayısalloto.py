import random

sLotoNumaraları = range(1,50) #1 den 49 a kadar olan sayıları aldık.

lotoSonuc = random.sample(sLotoNumaraları, 6) #6 tane numune aldık


while True:
    islem = int(input(""" 
    -------------Sayısal Loto---------------------
       ---Lütfen 1-49 arasında sayı giriniz---
    1- Oyna
    2- Sonuç Getir
    3- Çık
    """))
    if islem == 1:
        kolon = input("""
        Kolon-1 oynamak için a'ya bas
        Kolon-2 oynamak için b'ye bas
        """)
        if kolon == "a":

            kSayi11 = int(input("Birinci sayıyı gir:(1-49) "))  #ksayi = kullaniciSayi
            while kSayi11 < 1:
                kSayi11 = int(input("Sayı birden küçük OLAMAZ. Birinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi11 > 49:
                kSayi11 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Birinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi21 = int(input("İkinci  sayıyı gir: "))
            while kSayi21 < 1:
                kSayi21 = int(input("Sayı birden küçük OLAMAZ. İkinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi21 > 49:
                kSayi21 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. İkinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi31 = int(input("Üçüncü  sayıyı gir: "))
            while kSayi31 < 1:
                kSayi31 = int(input("Sayı birden küçük OLAMAZ. Üçüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi31 > 49:
                kSayi31 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Üçüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi41 = int(input("Dördüncü  sayıyı gir: "))
            while kSayi41 < 1:
                kSayi41 = int(input("Sayı birden küçük OLAMAZ. Dördüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi41 > 49:
                kSayi41 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Dördüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi51 = int(input("Beşinci  sayıyı gir: "))
            while kSayi51 < 1:
                kSayi51 = int(input("Sayı birden küçük OLAMAZ. Beşinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi51 > 49:
                kSayi51 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Beşinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi61 = int(input("Altıncı  sayıyı gir: "))
            while kSayi61 < 1:
                kSayi61 = int(input("Sayı birden küçük OLAMAZ. Altıncı sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi61 > 49:
                kSayi61 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Altıncı sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass



            kListe = [kSayi11,kSayi21,kSayi31,kSayi41,kSayi51,kSayi61] #kListe = kullaniciListe
        if kolon == "b":
            kSayi12 = int(input("Birinci sayıyı gir:(1-49) "))  #ksayi = kullaniciSayi
            while kSayi12 < 1:
                kSayi12 = int(input("Sayı birden küçük OLAMAZ. Birinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi12 > 49:
                kSayi12 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Birinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi22 = int(input("İkinci  sayıyı gir: "))
            while kSayi22 < 1:
                kSayi22 = int(input("Sayı birden küçük OLAMAZ. İkinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi22 > 49:
                kSayi22 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. İkinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi32 = int(input("Üçüncü  sayıyı gir: "))
            while kSayi32 < 1:
                kSayi32 = int(input("Sayı birden küçük OLAMAZ. Üçüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi32 > 49:
                kSayi32 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Üçüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi42 = int(input("Dördüncü  sayıyı gir: "))
            while kSayi42 < 1:
                kSayi42 = int(input("Sayı birden küçük OLAMAZ. Dördüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi42 > 49:
                kSayi42 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Dördüncü sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi52 = int(input("Beşinci  sayıyı gir: "))
            while kSayi52 < 1:
                kSayi52 = int(input("Sayı birden küçük OLAMAZ. Beşinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi52 > 49:
                kSayi52 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Beşinci sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            kSayi61 = int(input("Altıncı  sayıyı gir: "))
            while kSayi62 < 1:
                kSayi62 = int(input("Sayı birden küçük OLAMAZ. Altıncı sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass
            while kSayi62 > 49:
                kSayi62 = int(input("Sayı kırk dokuzdan büyük OLAMAZ. Altıncı sayıyı gir:(1-49) "))  # ksayi = kullaniciSayi
            else:
                pass

            kListe2 = [kSayi12, kSayi22, kSayi32, kSayi42, kSayi52, kSayi62] #kListe = kullaniciListe

    elif islem == 2:
        kSonuc = set(kListe)  # liste kümeye dönüştürüldü, kesişim bulmak için
        sonuc = set(lotoSonuc)
        bilinenSayilar1 = kSonuc.intersection(sonuc) #kesişimi alındı

        kSonuc2 = set(kListe2)  # liste kümeye dönüştürüldü, kesişim bulmak için
        sonuc2 = set(lotoSonuc)
        bilinenSayilar2 = kSonuc2.intersection(sonuc2)  #kesişimi alındı

        print("a kolonundaki sayılarınız", kListe)
        print("b kolonundaki sayılarınız", kListe2)
        print("Loto Sonuçları", lotoSonuc)
        if bilinenSayilar1 == set():
            print("Hiç sayı bilemediniz")
        else:
            print(f" a kolonunda Bildiğiniz Sayılar: {bilinenSayilar1}")
        if bilinenSayilar2 == set():
            print("Hiç sayı bilemediniz")
        else:
            print(f" b kolonunda Bildiğiniz Sayılar: {bilinenSayilar2}")
    elif islem == 3:
        break
else:
    print("Oyundan çıkıyorsunuz")