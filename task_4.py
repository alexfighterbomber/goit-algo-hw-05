def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
        except KeyError:
            return "Key not found. Please enter a valid name."

    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args # Считываем первые два элемент из списка args
    if name in contacts:  # если имя есть в контактах
        contacts[name] = phone
        return "Contact updated." 
    else: return 'Нема такого!'

@input_error
def show_phone(args, contacts):
    name = args[0]  # Считываем первый элемент из списка args
    return contacts.get(name, "Такий тут не живе!")  # Возвращаем значение по ключу или ошибку если ключ не найден
    
@input_error
def show_all(contacts):
    ret_str = ""
    for name in contacts:
        ret_str += name + ': ' + contacts[name] + '\n'  # формируем строку для вывода контактов
    return ret_str.rstrip() # обрезаем последний перевод строки

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:# команда "close", "exit"
            print("Good bye!")
            break
        elif command == "hello":        # команда "hello"
            print("How can I help you?")
        elif command == "add":          # команда "add"
            print(add_contact(args, contacts))
        elif command == 'change':       # команда 'change'
            print(change_contact(args, contacts))
        elif command == 'phone':        # команда 'phone'
            print(show_phone(args, contacts))
        elif command == 'all':          # команда 'all'
            print(show_all(contacts))
        else:                           # неизвестная  команда
            print("Invalid command.")


if __name__ == "__main__":
    main()
