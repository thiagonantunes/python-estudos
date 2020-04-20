def min_nums(cents):
    coins = [25, 10, 5, 1]
    tot = 0
    for coin in coins:
        while cents >= coin:
            cents -= coin
            tot += 1
            print(f'{coin}')
    return tot

money = int(input('Digite um valor: R$'))

print(f'Numbers of coins: {min_nums(money)}')