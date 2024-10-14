import membersTransactions
import menuDisplay as display


while True:
    display.displayMainMenu()
    choose = int(input("Enter your preference (1 to 3):"))

    match choose:
        case 1:
            print("\n\033[95mIt is MEMBERS transaction appear.\n")
            while True:
                display.displaymembersMenu()
                choose_memb_transaction = int(
                    input("Enter your preference (0 to 7):"))

                match choose_memb_transaction:
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

        case 2:
            print("\n\033[91mIt is BOOK transaction appear.\n")
            while True:
                display.displayBookMenu()
                choose_book_transaction = int(
                    input("Enter your preference (0 to 4):"))

                match choose_book_transaction:
                    case 0:
                        break
        case 3:
            print("\n\033[93mYou are exit(3)")
            break
