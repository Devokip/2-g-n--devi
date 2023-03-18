ogrenciler = []

def ogrenci_ekle(adi, soyadi):
    ogrenciler.append([adi, soyadi])
    print(f"{adi} {soyadi} isimli öğrenci kaydedildi.")

def ogrenci_listele():
    print("Kayıtlı Öğrenciler:")
    for i, ogrenci in enumerate(ogrenciler):
        print(f"{i+1}- {ogrenci[0]} {ogrenci[1]}")

def ogrenci_sil(adi, soyadi):
    i = 0
    while i < len(ogrenciler):
        if ogrenciler[i][0] == adi and ogrenciler[i][1] == soyadi:
            ogrenciler.pop(i)
        else:
            i += 1
    print(f"{adi} {soyadi} isimli öğrenci(ler) listeden silindi.")

# Kullanıcıdan işlem seçimini isteyelim
while True:
    print("1- Öğrenci Ekle")
    print("2- Öğrenci Sil")
    print("3- Öğrenci Listele")
    print("0- Çıkış")

    secim = input("İşlem Seçiniz: ")

    if secim == "1":
        adi = input("Öğrenci Adı: ")
        soyadi = input("Öğrenci Soyadı: ")
        ogrenci_ekle(adi, soyadi)
    elif secim == "2":
        adi = input("Öğrenci Adı: ")
        soyadi = input("Öğrenci Soyadı: ")
        ogrenci_sil(adi, soyadi)
    elif secim == "3":
        ogrenci_listele()
    elif secim == "0":
        break
    else:
        print("Geçersiz işlem seçimi.")
