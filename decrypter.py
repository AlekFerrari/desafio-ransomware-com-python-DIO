import os
import pyaes

##Abrir o arquivo cryptografado

file_name = 'clientes_cobranca.txt.ransomwaretroll'
file = open(file_name, 'rb')
file_data = file.read()
file.close()

##Chave de descriptografia

Key = b'testeansomwares'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

##Remove arquivo criptografado

os.remove(file_name)

##Criar um novo arquivo descripografado

new_file = 'clientes_cobranca.txt'
new_file = open(f'{new_file}','wb')
new_file.write(decrypt_data)
new_file.close()

