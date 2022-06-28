import os 
from cryptography.fernet import Fernet


resp = input("Selecione o que deseja fazer: \n-> 1 para encriptar \n-> 2 para descriptografar \n-> ")

if resp not in ['1', '2', '0']:
    print("Selecione apenas numeros validos.")
    resp = input("Selecione o que deseja fazer: \n-> 1 para encriptar \n-> 2 para descriptografar \n-> ")

list = []

key = Fernet.generate_key()

if resp == '1':
    with open ('.secret.key', 'wb') as keysave:
        keysave.write(key)

    for file in os.listdir():
        if file == 'roader.py':
            continue
        
        if file == '.secret.key':
            continue

        if os.path.isfile(file):
            list.append(file)


        for file in list:
            with open (file, 'rb') as arq:
                content = arq.read()

        content_encrypt = Fernet(key).encrypt(content)
        with open(file, "wb") as arq:
            arq.write(content_encrypt)

if resp ==  '2':

    with open ('.secret.key', 'rb') as keysave:
        secret = keysave.read()

    for file in os.listdir():
        if file == 'roader.py': 
            continue
        
        if file == '.secret.key':
            continue

        if os.path.isfile(file):
            list.append(file)

        for file in list:
            with open (file, 'rb') as arq:
                content = arq.read()
        content_crypt = Fernet(secret).decrypt(content)
        with open(file, "wb") as arq:
            arq.write(content_crypt)

if resp == '0':
    print('Saindo do sistema...')
    exit()