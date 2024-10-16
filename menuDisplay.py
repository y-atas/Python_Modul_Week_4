
def displayMainMenu():
    # Sarı RENK KODU ICIN   \033[93m  ANSI escape kodları kullanılır.
    print("\033[93m-" * 62)
    print("-" + " "*9 + "HALK KUTUPHANESINE HOS GELDINIZ" + " "*9 + " - ")
    print("-" + " "*50+"-")
    print("-" + " "*9 + " 1 - UYELIK ISLEMLERI " +
          " " * 10 + "1" + " " * 8 + "-")
    print("-" + " "*9 + " 2 - KITAP ISLEMLERI " + " " * 11 + "2" + " " * 8 + "-")
    print("-" + " "*9 + " 3 - CIKIS " + " " * 21 + "3" + " " * 8 + "-")
    print("-" + " "*50+"-")
    print("-" * 62)


def displaymembersMenu():
    print("\033[93m-" * 62)
    print(f"{'-':<3} {'UYELER':<15} {"= 1":<5} {"=":<5} {
          "KITAP ODUNC VERME":<20} {"= 5":<5} {"-":>3}")
    print(f"{'-':<3} {'UYE EKLEME':<15} {"= 2":<5} {"=":<5} {"KITAP IADE":<20} {"= 6":<5} {"-":>3}")
    print(f"{'-':<3} {'UYE ARA':<15} {"= 3":<5} {"=":<5} {"KITAP TAKIBI":<20} {"= 7":<5} {"-":>3}")
    print(f"{'-':<3} {'UYE SIL':<15} {"= 4":<5} {"=":<5} {"CIKIS":<20} {"= 0":<5} {"-":>3}")
    print("\n"+"-" * 62)


def displayBookMenu():
    print("\033[93m-" * 62)
    print(f"{"-":<3} {"KITAPLAR":<15} {"= 1":<40} {"-"}")
    print(f"{"-":<3} {"KITAP EKLE":<15} {"= 2":<40} {"-"}")
    print(f"{"-":<3} {"KITAP ARA":<15} {"= 3":<40} {"-"}")
    print(f"{"-":<3} {"KITAP SIL":<15} {"= 4":<10} {"CIKIS":<10} {"= 0":<5} {"-":>14}")
    print("\n"+"-" * 62)


# displayMainMenu()
# displaymembersMenu()
# displayBookMenu()
