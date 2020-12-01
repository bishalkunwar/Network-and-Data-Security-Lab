#ceaser cipher encryption coding example.

from string import printable as letters

def encrypt(message, key):
    cipher = []
    for a in message:
        position = letters.find(a)
        newPosition = position + key %len(letters)
        encrypt = letters[newPosition]
        cipher.append(encrypt)

    return ''.join(cipher)

def decrypt (cipher, key):
    plainText = []
    for a in cipher:
        position = letters.find(a)
        newPosition = position - key %len(letters)
        decrypt = letters[newPosition]
        plainText.append(plainText)

    return ''.join(plainText)

message = 'BishalKunwar'

cipher = encrypt(message,3)
print(cipher)
plainText = decrypt(cipher,3)
print(plainText)


