import os
import csv
import pandas as pd
from os import get_terminal_size
from masking import get_pass
from gotoxy import gotoxy
from encryption import encrypt
from colorama import Fore

def cls(): os.system('cls')

def authenticate():
    'Returns True if the credentials are valid otherwise this will return false'
    cls()
    print()
    if user == username and passd == password:
        main()
        return
    print(Fore.RED + 'Incorrect credentials. You can try again'.center(terminal_width) + Fore.RESET + '\n\n')
    os.system('pause')
    login()

def pid_exist(pid):
    try:
        ids = pd.read_csv('./database/inventory.csv')['PID']
        if int(pid) not in ids: return False
        return True
    except:
        return False

def login():
    'This is the entry point - main function'
    cls()
    global terminal_width
    terminal_width  = get_terminal_size().columns
    print('Log-in:\n')
    print('Username:')
    print('Password:')
    global username
    global user
    user = '1019910410110997110101'
    gotoxy(11,3)
    username = encrypt(input())
    global password
    global passd
    passd = '69485150575048484869'
    gotoxy(0,4)
    password = encrypt(get_pass('Password: '))
    authenticate()

def print_inventory():
    file = open('./database/inventory.csv','r')
    lines = file.readlines()
    print(Fore.CYAN)
    fieldnames = lines[0].split(',')
    print(fieldnames[0].rjust(5), end='')
    print(fieldnames[1].rjust(25), end='')
    print(fieldnames[2].rjust(25), end='')
    print(fieldnames[3].rjust(20), end='')
    print(fieldnames[4].rjust(15), end='')
    print(fieldnames[5].strip().rjust(15), end='')
    print('\n'+ Fore.RESET)

    for x in range(1,len(lines)):
        data = lines[x].split(',')
        print(data[0].rjust(5), end='')
        print(data[1].rjust(25), end='')
        print(data[2].rjust(25), end='')
        print(data[3].rjust(20), end='')
        print(data[4].rjust(15), end='')
        print(data[5].strip().rjust(15), end='')
        print()

    file.close()

def exit_app():
    cls()
    print()
    print(Fore.BLUE + 'Thank You'.center(terminal_width) + Fore.RESET)
    print()

def sort_inventory(column_name: str):
    df = pd.read_csv('./database/inventory.csv')
    df = df.sort_values(by=[column_name], ascending=True)
    df.to_csv('./database/inventory.csv', index=False)

# ====================COMPONENTS=======================
def view_product():
    cls()
    print('\n'+'Product Inventory'.center(terminal_width)+'\n')
    print_inventory()
    print()
    os.system('pause')
    main()

def view_product2():
    cls()
    print('\n'+'Product Inventory'.center(terminal_width)+'\n')
    print_inventory()
    print()
    os.system('pause')

def add_product():
    cls()
    print(Fore.CYAN+'\nAdd Product\n'+Fore.RESET+"Enter 'cancel' to cancel.\n")

    file = pd.read_csv('./database/inventory.csv')

    pid = len(file['PID'])

    print('Product ID:'.rjust(29),pid)
    name = input('Product Name: '.rjust(30))
    if name == 'cancel': return main()
    desc = input('Description: '.rjust(30))
    if desc == 'cancel': return main()
    manuf = input('Manufacturer: '.rjust(30))
    if manuf == 'cancel': return main()
    price = input('Price(Php)/Piece: '.rjust(30))
    if price == 'cancel': return main()
    stock = input('Stock (ex: 12-dozens/packs): '.rjust(30))
    if stock == 'cancel': return main()

    try:
        with open('./database/inventory.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow([pid,name,desc,manuf,price,stock])

            sort_inventory('PID')

            print()
            print(Fore.GREEN+'Product added successfully' + Fore.RESET)
            print('\n1. View Products')
            print('2. Go back to home')
            print('3. Exit application\n')
    except Exception:
        print(Exception,'\n')
        print('\n'+Fore.RED + 'Something went wrong, try again' + Fore.RESET + '\n')
        os.system('pause')
        return add_product()

    command = input('Command: ')
    if command == '1': view_product()
    elif command == '2': main()
    elif command == '3': exit_app()
    else: main()

def update_product():
    cls()
    command = input('Check the inventory first? y-yes or n-no: ')
    if command.lower() == 'y':
        view_product2()
    cls()
    print('\n')
    update_id = input('Update Product\n\nEnter Product ID\nor \'cancel\' to cancel: ')

    if update_id.lower() == 'cancel': return main()

    if not pid_exist(update_id):
        print('\nProduct '+Fore.YELLOW + update_id + Fore.RESET + ' is not in the inventory.\n')
        os.system('pause')
        return update_product()
    else:
        print('\nEnter the field you want to update\n')
        print('1. Product Name')
        print('2. Decription')
        print('3. Manufacturer')
        print('4. Price(Php)/Piece')
        print('5. Stock/Unit\n')
        id = update_id
        command = input('command: ')
        'PID,Product Name,Description,Manufacturer,Price(Php),Stocks/Unit'
        if command == '1': update_id = 'Product Name'
        elif command == '2': update_id = 'Description'
        elif command == '3': update_id = 'Manufacturer'
        elif command == '4': update_id = 'Price(Php)'
        elif command == '5': update_id = 'Stocks/Unit'
        else:
            print(Fore.RED+'\nInvalid command'+Fore.RESET,'\n')
            os.system('pause')
            return update_product()
        
        print(Fore.YELLOW + '\nUpdate Product ' + id + '.' + Fore.RESET)
        
        df = pd.read_csv('./database/inventory.csv')

        for x in range(len(df)):
            if df['PID'][x] == int(id):
                print('\nIs these the product you want to update? "'+Fore.CYAN+ df['Product Name'][x]+Fore.RESET+'"')
                command = input('y-yes or n-no: ')
                if command.lower() == 'y':
                    update = input('\nChange its '+ Fore.YELLOW +str(update_id) + Fore.RESET + ' to: ')
                    df[update_id][x] = update
                    cls()
                    df.to_csv('./database/inventory.csv', index=False)
                    print(Fore.GREEN+'\nUpdate Successful\n'+Fore.RESET)
                else:
                    cls()
                    print('\nPlease check the Inventory first\n')
                os.system('pause')
                return main()      

def delete_product():
    cls()
    print(Fore.YELLOW + 'Delete Product' + Fore.RESET,'\n')

    command = input('Check the inventory first: y-yes | n-no : ')

    if command.lower() == 'y':
        view_product2()
        cls()

    id_tobe_deleted = input('\nEnter the ID of the product you want to delete\nor enter \'cancel\' to cancel\n\nProduct ID: ')

    if id_tobe_deleted.lower() == 'cancel': 
        return main()

    if not pid_exist(id_tobe_deleted):
        print(Fore.RED+'Product '+id_tobe_deleted+Fore.RESET+' is not in the inventory\n')
        os.system('pause')
        return delete_product()
    else:
        df = pd.read_csv('./database/inventory.csv')
        
        f = list(df[df.PID==int(id_tobe_deleted)].values[0])
        with open('./database/deleted.csv','a',newline='') as file:
            w = csv.writer(file)
            w.writerow(f)
        
        df = df[df.PID != int(id_tobe_deleted)]

        for x in range(int(id_tobe_deleted)+1,len(df)+1):
            df['PID'].replace({x: x-1},inplace=True)

        df.to_csv('./database/inventory.csv',index=False)

        print('\n'+Fore.YELLOW + 'Product ' +id_tobe_deleted+ ' Successfully Deleted' + Fore.RESET + '\n')
        sort_inventory('PID')
        os.system('pause')
        return main()

def main():
    cls()
    print()
    print('Welcome to EE Store'.center(terminal_width))
    print('Product Inventory Management System'.center(terminal_width))
    print('\n')

    print('Enter corresponding number of command:\n')
    print('1. View Products')
    print('2. Add Product')
    print('3. Update Product')
    print('4. Delete Product')
    print('5. Exit application\n')

    command = input('Command: ')

    if command == '1': view_product()
    elif command == '2': add_product()
    elif command == '3': update_product()
    elif command == '4': delete_product()
    elif command == '5': exit_app()
    else:
        print(Fore.YELLOW + '\n' + 'Invalid command' + Fore.RESET)
        os.system('pause')
        main()

login()