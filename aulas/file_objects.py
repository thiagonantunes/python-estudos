# File objects

import os

os.chdir('/Users/Thiago/Music/nova pasta')


for f in os.listdir():
    new_name = (f.title())
    os.rename(f, new_name)

"""
character   Meaning
'r'         open for reading (default)
'w'         open for writing, truncating the file first
'x'         open for exclusive creation
'a'         opne fro writing, appending to the end of the file if it exists
'b'         binary mode
't'         text mode (default)
'+'         open for updating (reading and writing)
"""
# with open('abc.txt', 'r') as f:
#     f_contents = f.read()  # f.read(100) 100 refere-se a quantidade de caracteres impressos
#     # f_contents = f.readline()
#     print(f_contents)


# with open('abc.txt', 'w+') as file:
#     file.write('Linha1\n')
#     file.write('Linha2\n')
#     file.write('Linha4\n')

#     file.seek(0, 0)  # começa ler da primeira linha, primeiro caractere
#     print('Lendo linhas:')
    
#     file.close()

