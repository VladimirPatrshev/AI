def input_name():
    return input("Введите имя: \n").title()

def input_surname():
    return input("ВВедите фамилию: \n").title()

def input_patronumic():
    return input("Введите отчество: \n").title()

def input_phone_number():
    return input("Введите номер: \n")

def input_address():
    return input("Введите адрес: \n").title()

def copy_contact():
    return input("Введите номер строки для копирования:\n")

def create_contact():
    surname = input_surname()
    name = input_name()
    patronumic = input_patronumic()
    phone_number = input_phone_number()
    address = input_address()
    return f'{surname} {name} {patronumic} {phone_number}\n{address}\n\n'

def add_contact():
    contact = create_contact()
    with open('phonebook.txt', 'a', encoding="UTF-8") as file_a:
        file_a.write(contact)
        
def print_contacts():
    with open('phonebook.txt', 'r', encoding="UTF-8") as file_r:
        lst_contacts=file_r.read().rstrip().split("\n\n")
    for i, contact in enumerate(lst_contacts,1):
           print(i,contact)   
        
def search_contact():
    print("Варианты поиска:\n\n"
            "1 - По фамилии контакта\n"
            "2 - По имени контакта\n"
            "3 - По отчеству контакта\n"
            "4 - По адресу контакта\n"
            "5 - Выход\n"
            )
    var = input("Выберите вариант поиска: ")
    while var not in ('1','2','3','4','5'):
            print()
            print("Введены не корректны данные. Введите число от 1 до 5")
            var = input("Введите вариант поиска: ") 
    index_var = int(var) - 1    
    search = input("Введите данные для поиска: ").title()
    
    with open('phonebook.txt', 'r', encoding="UTF-8") as file_r:
        lst_contacts=file_r.read().rstrip().split("\n\n")
         
    for contact_str in lst_contacts:
        contact_lst = contact_str.split()
        if search in contact_lst[index_var]:
            print("****************")
            print(contact_str) 
            print("****************")
    
def copy():
    pass

def interface():
    with open('phonebook.txt', 'a', encoding="UTF-8"):
        pass    
    command = ' '
    while command != '5':
        print("Варианты действий:\n\n"
            "1 - Ввод контакта\n"
            "2 - Вывод контакта\n"
            "3 - Поиск контакта\n"
            "4 - Копировать контакт\n"
            "5 - Выход\n"
            )
        command = input("Введите вариант действия:")

        while command not in ('1','2','3','4','5'):
            print("Введены не корректны данные. Введите число от 1 до 5")
            command = input("Введите вариант действия:")
            
        match command:
            
            case '1':
                add_contact()
            case '2':
                print_contacts()
            case '3':
                search_contact()
            case '4':
                copy_contact()
            case '5':
                print("Всего доброго!")         
    
interface()