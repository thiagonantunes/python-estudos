import csv

with open('/Users/Thiago/Documents/PyhtonProgresso/clientes.csv','r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('/Users/Thiago/Documents/PyhtonProgresso/estudos/aulas/module_csv/new_clients.csv', 'w', newline='') as new_file:
        fieldnames = ['Nome', 'Sobrenome', 'E-mail', 'Telefone']
        csv_write = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',', quotechar='|', quoting=csv.QUOTE_ALL)
        # quotechar -> símbolo aparece em cada item
        # quoting -> quando aparece o símbolo

        csv_write.writeheader()

        for line in csv_reader:
            csv_write.writerow(line)