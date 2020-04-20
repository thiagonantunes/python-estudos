# File objects
import os
import shutil

# os.chdir('/Users/Thiago/Music')

# for f in os.listdir():
#     new_name = (f.title())
#     os.rename(f, new_name)

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


# path = '/Users/Thiago/Documents/TJSP2019/Leis'
# file_search = 'const'

# for root, directories, files in os.walk(path):
#     for f in files:
#         if file_search in f.lower():
#             complete_path = os.path.join(root, f)
#             archive_name, extension = os.path.splitext(complete_path)
#             size_file = os.path.getsize(complete_path)
#             print(f)


# path = r'C:\Users\Thiago\Pictures\Projetos de Vídeo\testpython'
path = '/Users/Thiago/Pictures/Projetos de Vídeo'
new_path = '/Users/Thiago/Pictures/Projetos de Vídeo/testpython'

try:
    os.mkdir(new_path)
except FileExistsError as e:
    print(f'Pasta {new_path} já existe')

for root, dirs, files in os.walk(path):
    for file in files:
        old_file_path = os.path.join(root,file)
        new_file_path = os.path.join(new_path, file)
        
        shutil.copy(old_file_path, new_file_path)
        print(old_file_path)