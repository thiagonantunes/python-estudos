# import csv

# with open('names.csv', 'r') as csv_file:
#     # csv_reader = csv.reader(csv_file)  # delimiter='\t'

#     # Exibi o arquivo em forma de diconário
#     csv_reader = csv.DictReader(csv_file)


#     # UTILIZANDO CSV.DICTREADER
#     with open('new_names.csv', 'w', newline='') as new_file:
#         fieldnames = ['first_name', 'last_name', 'email']
#         # fieldnames = ['first_name', 'last_name'] # deletado no laço for tirar daqui para não exibir no cabeçalho

#         # fieldname -> exibir cabeçalho
#         csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')  # delimiter -> tipo de separação \t = tab

#         csv_writer.writeheader() # Exibir o cabeçalho 

#         for line in csv_reader:
#             # del line['email']  # para deletar coluna
#             csv_writer.writerow(line)  # imprimir cada linha do arquivo


#     # UTILIZANDO CSV.READER

#     #newline não irá deixar uma linha me branco
#     # with open('new_names.csv', 'w', newline='') as new_file:
#     #     csv_writer = csv.writer(new_file, delimiter='\t')  # delimiter -> tipo de separação \t = tab

#     # # # next(csv_reader)  # mostra a primeira linha do arquivo, com isso o for abaixo começa de segunda linha

#     #     for line in csv_reader:
#     #         csv_writer.writerow(line)  # imprimir cada linha do arquivo

import csv

html_output = ''
names = []

with open('patrons.csv', 'r') as data_file:
# with open('/Users/Thiago/Documents/PyhtonProgresso/patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'No Reward':
            break
        names.append(f'{line[0]} {line[1]}')

html_output += (f'<p>There are currently {len(names)} public contributions. Thank You!<>/p')
html_output += f'\n<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

print(html_output)
