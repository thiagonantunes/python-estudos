import csv

with open('/Users/Thiago/Documents/PyhtonProgresso/names.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)  # delimiter='\t'

    # Exibi o arquivo em forma de diconário
    csv_reader = csv.DictReader(csv_file)


    # UTILIZANDO CSV.DICTREADER
    with open('/Users/Thiago/Documents/PyhtonProgresso/estudos/aulas/module_csv/new_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name', 'email']
        # fieldnames = ['first_name', 'last_name'] # deletado no laço for tirar daqui para não exibir no cabeçalho

        # fieldname -> exibir cabeçalho
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')  # delimiter -> tipo de separação \t = tab

        csv_writer.writeheader() # Exibir o cabeçalho 

        for line in csv_reader:
            # del line['email']  # para deletar coluna
            csv_writer.writerow(line)  # imprimir cada linha do arquivo


    # UTILIZANDO CSV.READER

    # newline não irá deixar uma linha me branco
    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')  # delimiter -> tipo de separação \t = tab

        # next(csv_reader)  # mostra a primeira linha do arquivo, com isso o for abaixo começa de segunda linha

        for line in csv_reader:
            csv_writer.writerow(line)  # imprimir cada linha do arquivo