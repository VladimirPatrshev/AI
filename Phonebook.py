def add_contact():
    pass

def print_contacts():
    pass

def find_contact():
    pass

def interface():
    with open('phonebook.txt', 'a'):
        pass
    print("Варианты действий:\n"
           "1 - Ввод контакта\n"
           "2 - Вывод контакта\n"
           "3 - Поиск контакта\n"
           "4 - Выход\n"
        )
    command =input("Введите варант действия:")

    while command not in ("1","2","3","4"):
        print("Введены не корректны данные. Введите число от 1 до 4")
        command =input("Введите варант действия:")
        
    match command:
        
        case "1":
            add_contact()
        case "2":
            print_contacts()
        case "3":
            find_contact()
        case "4":
            print("Всего доброго!")         
    
interface()