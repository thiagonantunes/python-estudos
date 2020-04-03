import csv

html_output = ''
names = []

with open('/Users/Thiago/Documents/PyhtonProgresso/patrons.csv', 'r') as data_file:
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