import File  # File islemlerini  bu modulde
import json


def listAllBooks():
    books = File.loadData(File.books)
    for book in books:
        # ensure_ascii=False Turkce karakter vs duzgun goruntulemek icin. Json formatinda ekrana cikti aliyoruz.
        print(json.dumps(book, indent=4, ensure_ascii=False))

        print('-' * 62)  # Satırları ayırmak için)


def addBook():
    books = File.loadData(File.books)
    while True:

        bookName = input("Listeye eklemek istediğiniz kitabin adıni giriniz: ")
        auteur = input(
            "Listeye eklemek istediğiniz kitabin yazarını giriniz: ")
        publisher = input("Listeye eklemek kitabinyayınevini giriniz: ")
        barcode = input(
            "Listeye eklemek istediğiniz kitabin barkodunu giriniz: ")
        language = input(
            "Listeye eklemek istediğiniz kitabin dilini giriniz: ")
        price = input("Listeye eklemek istediğiniz kitabin fiyatini giriniz: ")

        if barcode in [barcode["Barkod"] for barcode in books]:
            print(f"{barcode}  Bu barkod zaten kitap listesinde mevcut.")
            if File.areYouSure():
                print("\nYeni kitap ekleme islemi baslatildi\n")
            else:
                break

        else:

            books.append({
                "Barkod": barcode,
                "Dil": language,
                "Fiyat": price,
                "Kitap_Adi": bookName,
                "Yayinevi": publisher,
                "Yazar": auteur
            })
            File.saveData(File.books, books)
            break


def deleteBook():

    books = File.loadData(File.books)
    barcode = input(
        "Listeden silmek istediğiniz kitabin barkodunu giriniz: ")
    for book in books:
        if book["Barkod"] == barcode:
            print(
                f"{barcode}  Kitap listede bulundu silmek icin devam edebilirsiniz.")
            if File.areYouSure():
                books.remove(book)
                File.saveData(File.books, books)
                print(f"\n{book["Kitap_Adi"]} basari ile silinmistir.")
                # burada kirilacak bir dongu yok ama menu dongusunu bu kod kiriyor.
                break


def searchBook():
    books = File.loadData(File.books)
    search = input(
        "Aramak istediğiniz kitabın barkodunu ya da kitap ile ilgili bir metin giriniz: ")

    found = False  # Kitap bulunduğunu kontrol etmek için bir bayrak

    for book in books:
        # Barkod'u string'e çeviriyoruz ki .lower() kullanılabilsin.
        if (
            # Barkod int olabilir, bu yüzden str'ye çevriliyor
            search.lower() in str(book["Barkod"]).lower()
            or search.lower() in book["Dil"].lower()
            or search.lower() in book["Kitap_Adi"].lower()
            or search.lower() in book["Yayinevi"].lower()
            or search.lower() in book["Yazar"].lower()
        ):
            found = True
            # Kitap bilgilerini yazdırma
            for key, value in book.items():
                print(f"{key} : {value}")
            print('-' * 50)  # Kitapları ayırmak için çizgi ekliyoruz.
            # Kitap bulunduğunda döngüyü kırmak yerine sadece found bayrağını kullanıyoruz

        elif not found:
            print("Aradiginiz kitap listede mevcut degildir.")
        if File.areYouSure():
            print()
        else:
            break
