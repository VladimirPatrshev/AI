def input_name():
    return ("Введите имя: \n").title()

def input_surname():
    return ("ВВедите фамилию: \n").title()

def input_patronumic():
    return ("Введите отчество: \n").title()

def input_phone_number():
    return("Введите номер: \n").title()

def input_address():
    return ("Введите адресс: \n").title()

def copy_contact():
    return("Введите номер строки для копирования:\n")

def create_contact():
    surname = input_surname()
    name = input_name()
    patronumic = input_patronumic()
    phone_number = input_phone_number()
    address = input_address()
    return f'{surname}{name}{patronumic}{phone_number}\n{address}\n\n'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt' 'a', encoding="UTF-8") as file_a:
        file_a.write(contact)
        

def print_contacts():
    pass

def find_contact():
    pass

def copy():
    pass

def interface():
    with open('phonebook.txt', 'a', encoding="UTF-8"):
            pass
    command =" "
    while command !="5":
        print("Варианты действий:\n\n"
            "1 - Ввод контакта\n"
            "2 - Вывод контакта\n"
            "3 - Поиск контакта\n"
            "4 - Копировать контакт\n"
            "5 - Выход\n"
            )
        command =input("Введите варант действия:")

        while command not in ("1","2","3","4","5"):
            print("Введены не корректны данные. Введите число от 1 до 5")
            command =input("Введите варант действия:")
            
        match command:
            
            case "1":
                add_contact()
            case "2":
                print_contacts()
            case "3":
                find_contact()
            case "4":
                copy_contact()
            case "5":
                print("Всего доброго!")         
    
interface()