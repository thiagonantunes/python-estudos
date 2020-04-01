from contapoupanca import ContaPoupanca
from contacorrente import ContaCorrente

cp1 = ContaCorrente(1111, 2222, saldo=100, limite=500)

print(cp1.saldo)
cp1.sacar(100)