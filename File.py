import os
import json

# Global değişkenler
emtySlot = "emtySlot.json"
membersFileName = "members.json"
tracking = "tracking.json"
taksi = "taksi.json"
books = "kitap.json"


def loadData(file_name, data=[]):  # Dosyadan veri aliyoruz.

    try:
        if os.path.exists(file_name):
            with open(file_name, "r+", encoding="utf-8") as file:
                return json.load(file)
        else:
            with open(file_name, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
                return data
    except Exception as e:
        print(f"\nVeriler {file} Dosya`dan aktarilirken bir hata olustu.", e)


def saveData(file, data):  # Dosyaya veri yukluyor

    try:
        with open(file, "w+", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
            print(f"\nVeriler başariyla {file} dosyasina islemistir..")
    except Exception as e:
        print(
            f"\nVeriler {file} dosyasina eklenirken kayit sirasinda bir hata olustu.", e)


def areYouSure() -> bool:  # Bu sonsuz döngüleri kırmak için True ya da False döndüren fonksiyon
    while True:  # Sonsuz döngü, kullanıcı doğru yanıt verene kadar devam eder
        answer = input("Devam etmek ister misiniz? (E)vet / (H)ayir: ")
        print()
        if answer.upper() == "E":
            return True
        elif answer.upper() == "H":
            return False
        else:
            print("Geçersiz giriş. Lütfen 'E' veya 'H' girin.")


if __name__ == "__main__":
    areYouSure()
