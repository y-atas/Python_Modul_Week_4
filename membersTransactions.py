import load_or_save  # File islemlerini ac ma kaydetme bu modulde
import getTime  # zaman islemleri bu modulden cagriliyor.


def membersAdd():
    members = load_or_save.loadData(
        load_or_save.membersFileName)  # Üyeleri yükle

    emty_slot = load_or_save.loadData(load_or_save.emtySlot)
    id = len(members) + 1 if not emty_slot else emty_slot.pop(0)

    new_member = {
        "id": id,
        "Uye adi": input("Enter your name: "),
        "Telefon": input("Enter your telefoon number: "),
        "Adres": input("Enter your address: ")
    }

    members.append(new_member)  # Yeni üyeyi ekle
    members.sort(key=lambda member: member["id"])
    load_or_save.saveData(load_or_save.membersFileName,
                          members)  # Verileri kaydet
    load_or_save.saveData(load_or_save.emtySlot, emty_slot)


def membersAllList():
    try:

        # Üyeleri yükle
        members = load_or_save.loadData(load_or_save.membersFileName)

        if not members:  # Eğer üye yoksa
            print("Hicbir uye bulunamadi.")
        else:
            print("\nUye listesi :\n")
            for mem in members:
                print(mem)
    except Exception as e:
        print("Dosya icerigini goruntuleme hatasi.", e)


def memberDelete():

    membersAllList()  # Butun members uyelerini oncelikle goruntule
    # Üyeleri yükle
    members = load_or_save.loadData(load_or_save.membersFileName)

    while True:

        delete_ID = int(input("Silmek istenilen id'yi giriniz: "))
        found = False  # Üye bulunup bulunmadığını kontrol etmek için bir değişken

        for mem in members:
            if mem["id"] == delete_ID:
                # Dosyadan bir kayit siliniyorsa, bunlari kayit altina aliyoruz.
                emty_slot = load_or_save.loadData(load_or_save.emtySlot)
                emty_slot.append(mem["id"])
                # Burada ilk once listeyi siraya koyduk ve sonra dosyamiza ekledik.
                emty_slot.sort()
                # silinen id yi silinen dosyasina ekle
                load_or_save.saveData(load_or_save.emtySlot, emty_slot)

                members.remove(mem)  # Üyeyi sil
                print(f"Üye {delete_ID} başariyla silindi.")

                found = True  # Üye bulundu
                # veri silindikten sonra uyeleri guncelle.
                load_or_save.saveData(load_or_save.membersFileName, members)
                break  # Üye bulunduktan sonra döngüyü kır

        if not found:  # Eğer döngü tamamlandı ve üye bulunamadıysa
            print(f"Üye {delete_ID} bulunamadi.")

        # While loop tan çıkmak istiyormusunuz ..
        continue_decision = input("Devam etmek istiyor musunuz? (E/H): ")
        if continue_decision.lower() != 'e':
            break


def searchMember():
    membersAllList()

    members = load_or_save.loadData(load_or_save.membersFileName)
    search = input("Type here what you want to search for: ").strip()

    counter = 0  # Kac adet eslesme varsa onu sayacaktir.
    for member in members:
        if (
            str(search) == str(member["id"])
            or search.lower() in member["Uye adi"].lower()
            or search in member["Telefon"]
            or search.lower() in member["Adres"].lower()
        ):
            counter += 1
            print(f"\n{counter}.Eslesme")
            for key in member:
                print(f"{key} : {member[key]}")
            print("\033[91m-"*62)
    print(f"\nToplam eslesme sayisi ({counter})`dir. ")

    if counter == 0:
        print("\033[91m-"*62)
        print(f"Malesef  esleme yok ({counter}) ")


def bookLending():

    taksi = load_or_save.loadData(load_or_save.taksi)
    books = load_or_save.loadData(load_or_save.books)
    members = load_or_save.loadData(load_or_save.membersFileName)
    tracking = load_or_save.loadData(load_or_save.tracking)
    try:

        personID = int(input("Enter your user ID no: "))
        book_found = False

        for member in members:
            if member["id"] == personID:
                print(f"Hallo {member['Uye adi']}")

                book_barcode = int(
                    input("Enter the barcode you want to borrow: "))
                # kitap zaten odunc verilmis mi?
                if book_barcode in [track["Barkod"] for track in tracking]:
                    print(f"\n{book_barcode} nolu kitap zaten odunc verilmis. ")
                    break

                else:
                    for book in books:
                        if book["Barkod"] == book_barcode:
                            print(f"\n{book['Barkod']} kitap adı: {
                                book['Kitap_Adi']} ödünç olarak veriliyor")
                            taksi.append(book)  # Kitabı 'taksi'ye ekle
                            books.remove(book)  # Kitabı 'books'tan çıkar

                            book_found = True
                            break

                    if book_found:
                        registTime, returnTime = getTime.datas()  # Tarih bilgilerini al

                        # Yeni bir takip kaydı oluştur ki tek bir index te butun degerleri birlestir.
                        new_tracking_entry = {
                            "id": 2,
                            "Uye adi": member["Uye adi"],
                            "Telefon": member["Telefon"],
                            "Adres": member["Adres"],
                            "Barkod": book["Barkod"],
                            "Dil": book["Dil"],
                            "Fiyat": book["Fiyat"],
                            "Kitap_Adi": book["Kitap_Adi"],
                            "Yayinevi": book["Yayinevi"],
                            "Yazar": book["Yazar"],
                            "Kayit Tarihi": registTime,
                            "Kitap iade Tarihi": returnTime
                        }

                        # Tracking listesine ekle
                        tracking.append(new_tracking_entry)

                        # Verileri dosyalara kaydet
                        load_or_save.saveData(load_or_save.tracking, tracking)
                        load_or_save.saveData(load_or_save.books, books)
                        load_or_save.saveData(
                            load_or_save.membersFileName, members)
                        load_or_save.saveData(load_or_save.taksi, taksi)

                        print(f"\nBarkodu: {book_barcode} olan kitap, {returnTime} tarihine kadar {
                            member['Uye adi']} kişisine verilmiştir.")
                    else:
                        print(f"{book_barcode} is not found in the books list.")
    except Exception as e:
        print(f"Bir hata olustu.", e)


if __name__ == "__main__":
    books = load_or_save.loadData(load_or_save.books)
    print(f"{len(books)}")
