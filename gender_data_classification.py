import os
import shutil

# Veri seti dizini
veri_seti_dizini = r"C:\Users\Semih\Desktop\Ayak-Dataset\Photos"

# Hedef dizinler
erkekler_dizini = r"C:\Users\Semih\Desktop\Ayak-Dataset\Erkek"
kadinlar_dizini = r"C:\Users\Semih\Desktop\Ayak-Dataset\Kadin"

# Hedef dizinlerin var olup olmadığını kontrol et ve yoksa oluştur
for hedef_dizin in [erkekler_dizini, kadinlar_dizini]:
    if not os.path.exists(hedef_dizin):
        os.makedirs(hedef_dizin)

# Veri setindeki her bir fotoğraf üzerinde dön
for dosya_ismi in os.listdir(veri_seti_dizini):
    # Dosya uzantısını kontrol et (sadece .JPG uzantılı dosyaları al)
    if dosya_ismi.lower().endswith(".jpg"):
        # Dosya adından cinsiyet ID'sini çıkar
        cinsiyet_id = int(dosya_ismi.split("_")[1])

        # Hedef dizinine göre fotoğrafı taşı
        if cinsiyet_id == 1:
            kaynak_path = os.path.join(veri_seti_dizini, dosya_ismi)
            hedef_path = os.path.join(erkekler_dizini, dosya_ismi)
            shutil.move(kaynak_path, hedef_path)
        elif cinsiyet_id == 2:
            kaynak_path = os.path.join(veri_seti_dizini, dosya_ismi)
            hedef_path = os.path.join(kadinlar_dizini, dosya_ismi)
            shutil.move(kaynak_path, hedef_path)
        else:
            print(f"Bilinmeyen Cinsiyet ID değeri: {cinsiyet_id}")

print("Fotoğraflar başarıyla ayrıldı.")
