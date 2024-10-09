
import json
import os

# json dosya adlari
membersFilename = "members.json"
deletedIdFilename = "deleted_ids.json"




def loadData(filename):
    try:
        if os.path.exists(filename) :
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        else:
            return []
    except Exception as e:
        print(f"Dosya okuma hatasi ({filename}): {e}")
        return []


def saveData(filename,data):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            json.dump(data,file, ensure_ascii = False, indent=4)
    except Exception as e:
        print(f"Dosya yazma hatasi ({filename}): {e}")



def generateID(members, deletedID):

    existingID = [m["id"] for m in members]  #Mevcut id leri al.
    if deletedID:
        return deletedID.pop(0)
    else:
        return max(existingID, default=0) +1  # yeni id olustur.


def add_member():
   
    try:
        with open(membersFilename, "r") as file:
            members = json.load(file)

        
        new_member = {
            "id": generateID(),  # Yeni ID oluştur
            "uye_adi": input("Uye adini giriniz :"),
            "tel":input("Uye telefoon numarasini giriniz :") ,
            "adres": input("Uye adresini giriniz :")
        }
        members.append(new_member)  # Yeni üyeyi ekle
        print(f"Üye eklendi: {new_member}")

    except Exception as e:
        print(f"Üye ekleme hatasi: {e}")
    


def memberDel(member):
    pass


# Uye okuyucuya kitap odunc verme (tarih islemlerini burada yapiyorum).
def borrowedBook():
    pass

#Takip.json dosyasini buradan olusturuyorum.
def trackBookSave(data):
    pass

#Takip.json dosyasini buradan okuyacagiz.
def trackBookRead(data):
    pass

def returnBook():
    pass
def main():
    members= loadData(membersFilename)
    deletedID = loadData(deletedIdFilename)


if __name__ == "__main__":
    main()