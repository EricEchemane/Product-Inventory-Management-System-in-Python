import msvcrt
def get_pass(prompt: str = '',mask: str='*') -> str:
    'This function will mask what ever you type'
    print(prompt, end='')
    length = 0
    password = ''
    while True:
        x = msvcrt.getch().decode('utf-8')
        if x == '\r': break
        if x == '\b':
            if length > 0:
                password = password[:-1]
                print('\b \b', end='')
                length -= 1
            continue
        print(mask, end='')
        password += x
        length += 1
    return password