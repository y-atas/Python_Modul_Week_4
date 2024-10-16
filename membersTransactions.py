import File  # File islemlerini ac ma kaydetme bu modulde
import getTime  # zaman islemleri bu modulden cagriliyor.


def membersAdd():
    members = File.loadData(
        File.membersFileName)  # Üyeleri yükle

    emty_slot = File.loadData(File.emtySlot)
    id = len(members) + 1 if not emty_slot else emty_slot.pop(0)

    new_member = {
        "id": id,
        "Uye adi": input("Enter your name: "),
        "Telefon": input("Enter your telefoon number: "),
        "Adres": input("Enter your address: ")
    }

    members.append(new_member)  # Yeni üyeyi ekle
    members.sort(key=lambda member: member["id"])
    File.saveData(File.membersFileName,
                  members)  # Verileri kaydet
    File.saveData(File.emtySlot, emty_slot)


def membersAllList():
    try:

        # Üyeleri yükle
        members = File.loadData(File.membersFileName)

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
    members = File.loadData(File.membersFileName)

    while True:

        delete_ID = int(input("Silmek istenilen id'yi giriniz: "))
        found = False  # Üye bulunup bulunmadığını kontrol etmek için bir değişken

        for mem in members:
            if mem["id"] == delete_ID:
                # Dosyadan bir kayit siliniyorsa, bunlari kayit altina aliyoruz.
                emty_slot = File.loadData(File.emtySlot)
                emty_slot.append(mem["id"])
                # Burada ilk once listeyi siraya koyduk ve sonra dosyamiza ekledik.
                emty_slot.sort()
                # silinen id yi silinen dosyasina ekle
                File.saveData(File.emtySlot, emty_slot)

                members.remove(mem)  # Üyeyi sil
                print(f"Üye {delete_ID} başariyla silindi.")

                found = True  # Üye bulundu
                # veri silindikten sonra uyeleri guncelle.
                File.saveData(File.membersFileName, members)
                break  # Üye bulunduktan sonra döngüyü kır

        if not found:  # Eğer döngü tamamlandı ve üye bulunamadıysa
            print(f"Üye {delete_ID} bulunamadi.")

        # While loop tan çıkmak istiyormusunuz ..
        continue_decision = input("Devam etmek istiyor musunuz? (E/H): ")
        if continue_decision.lower() != 'e':
            break


def searchMember():
    membersAllList()

    members = File.loadData(File.membersFileName)
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

    taksi = File.loadData(File.taksi)
    books = File.loadData(File.books)
    members = File.loadData(File.membersFileName)
    tracking = File.loadData(File.tracking)
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
                        File.saveData(File.tracking, tracking)
                        File.saveData(File.books, books)
                        File.saveData(
                            File.membersFileName, members)
                        File.saveData(File.taksi, taksi)

                        print(f"\nBarkodu: {book_barcode} olan kitap, {returnTime} tarihine kadar {
                            member['Uye adi']} kişisine verilmiştir.")
                    else:
                        print(f"{book_barcode} is not found in the books list.")
    except Exception as e:
        print(f"Bir hata olustu.", e)


def bookReturn():

    taksi = File.loadData(File.taksi)
    books = File.loadData(File.books)
    members = File.loadData(File.membersFileName)
    tracking = File.loadData(File.tracking)

    if len(taksi) == 0:
        print(f"Iade edilecek hic bir kitap bulunamadi.")

    else:
        try:

            book_barcode = int(
                input("Enter the barcode you wish to return : "))
            book_found = False
            for track in tracking:
                if track["Barkod"] == book_barcode:
                    book_found = True
                    print(f"\n{book_barcode} kitap iade edildi.. ")
                    tracking.remove(track)
                    for taks in taksi:
                        if taks["Barkod"] == book_barcode:
                            books.append(taks)
                            taksi.remove(taks)
                            File.saveData(File.books, books)
                            File.saveData(
                                File.tracking, tracking)
                            File.saveData(File.taksi, taksi)
                            break
                if not book_found:
                    print(f"{book_barcode} bulunamadi..")
                    break

        except Exception as e:
            print(f"Bir hata olustu.", e)


def booktracking():
    from datetime import datetime  # tarih işlemleri için gerekli.

    tracking = File.loadData(File.tracking)
    if len(tracking) == 0:
        print("Takip listesinde hiçbir kitap bulunmamaktadir.")
    else:
        for track in tracking:
            # Burada kitap iade tarihi hala geçerli mi diye bakıyoruz
            # Str olan tarihleri datetime'a çeviriyoruz
            # Listedeki iade tarihini aldik.
            return_time = track["Kitap iade Tarihi"]
            # Alinan tarihi str den datetime formatina cevirdik.
            return_time = datetime.strptime(return_time, '%d-%m-%Y %H:%M')
            current_time = datetime.now()

            # Şu anki zamanı iade tarihi ile karşılaştırıyoruz
            if return_time >= current_time:
                print(f'Barkod: {track["Barkod"]}, Kitap adi: {
                      track["Kitap_Adi"]}')
                print(f'{track["Kitap iade Tarihi"]
                         } tarihine kadar iade edilmelidir.\n')
            else:

                print(f'Barkod: {track["Barkod"]}, Kitap adı: {
                      track["Kitap_Adi"]}')
                print(f"{(current_time - return_time)}  Iade günü geçmiştir.\n")


if __name__ == "__main__":
    books = File.loadData(File.books)
    print(f"{len(books)}")
