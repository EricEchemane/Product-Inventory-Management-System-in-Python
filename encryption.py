def encrypt(message: str) -> str:
    'Returns encrypted message base on a secret encryption process'
    encrypted = []
    for each in message:
        encrypted.append(str(ord(each)))
    return ''.join(encrypted)