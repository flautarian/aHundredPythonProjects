#Dictionary
crypt = {
    "a": "Alpha",
    "b": "Bravo",
    "c": "Charlie",
    "d": "Delta",
    "e": "Eco",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliet",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Québec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    "v": "Victor",
    "w": "Whisky",
    "x": "X-Ray",
    "y": "Yanki",
    "z": "Zulú",
}

#Encrypt Function
def encrypt():
    encrypted = ''
    words = input('Enter text to encrypt:\n').lower()
    for char in words:
        if char in crypt:
            encrypted += crypt[char]
        else:
            encrypted += char
    print(encrypted)

#Decrypt Function
def decrypt():
    decrypted = ''
    code = input('Enter the code:\n')
    inv_crypt = {v: k for k, v in crypt.items()}

    for n1, n2, n3 in zip(code[::3], code[1::3], code[2::3]):
        splitted = (n1+n2+n3)
        if splitted in inv_crypt:
            decrypted += inv_crypt[splitted]
        else:
            decrypted += splitted
    print(decrypted)


#Ask user for encrypt or decrypt
while True:
    print('Select an option\n', '1 to Encrypt\n', '2 to Decrypt\n', '3 to Exit\n')
    option = input()

    if option == '1':
        encrypt()
        break
    elif option == '2':
        decrypt()
        break
    elif option == '3':
        break
    else:
        print('No correct option selected\n')