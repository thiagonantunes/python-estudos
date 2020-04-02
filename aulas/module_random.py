import random

# números aleatórios entre 0 e 9
value = random.randint(0, 9)

# escolhe um opção na list
greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']
value = random.choice(greetings)

#lista aleatória, weights indica chance de ser escolhido, k indica quantos valores
colors = ['Red', 'Black', 'Green']
result = random.choices(colors, weights=(18, 18, 2), k=10)

#shuffle embaralha os valores
deck = list(range(1, 53))
random.shuffle(deck)

#Seleciona valores sem repeti-los, k indica quantos valores
hand = random.sample(deck, k=5)

