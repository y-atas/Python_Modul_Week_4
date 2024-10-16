import membersTransactions
import menuDisplay as display
import bookTransactions


while True:
    try:

        display.displayMainMenu()
        choose = input("Enter your preference (1 to 3):")
        if choose.isdigit() and 1 <= int(choose) <= 3:
            print("\n")

            match int(choose):
                case 1:
                    print("\n\033[95mIt is MEMBERS transaction appear.\n")
                    while True:
                        display.displaymembersMenu()
                        option1 = input("Enter your preference (0 to 7):")
                        if option1.isdigit() and 0 <= int(option1) <= 7:
                            print("\n")

                            match int(option1):
                                case 0:  # cikis
                                    break
                                case 1:  # butun uyleri cagir.

                                    membersTransactions.membersAllList()
                                case 2:  # uye ekleme
                                    membersTransactions.membersAdd()
                                case 3:  # Uye arama
                                    membersTransactions.searchMember()
                                case 4:  # Uye sil
                                    membersTransactions.memberDelete()
                                case 5:  # Kitap odunc alma
                                    membersTransactions.bookLending()
                                case 6:  # Kitap iade.
                                    membersTransactions.bookReturn()
                                case 7:
                                    membersTransactions.booktracking()
                        else:
                            print(
                                "\nLutfen belirtilen aralikta bir deger giriniz.\n")

                case 2:
                    print("\n\033[95mIt is BOOK transaction appear.\n")
                    while True:

                        display.displayBookMenu()
                        option2 = (
                            input("Enter your preference (0 to 4):"))
                        if option2.isdigit() and 0 <= int(option2) <= 4:
                            print("\n")

                            match int(option2):
                                case 0:
                                    break
                                case 1:
                                    bookTransactions.listAllBooks()

                                case 2:
                                    bookTransactions.addBook()
                                case 3:
                                    bookTransactions.searchBook()
                                case 4:
                                    bookTransactions.deleteBook()
                        else:
                            print(
                                "\nLutfen belirtilen aralikta bir deger giriniz.\n")

                case 3:
                    print("\n\033[93mYou are exit(3)")
                    break
        else:
            print("\nLutfen belirtilen aralikta bir deger giriniz.\n")
    except Exception as e:
        print("Hata olustur", e)
