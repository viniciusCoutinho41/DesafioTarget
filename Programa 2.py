### Programa 2
print('Sequência Fibonacci')
num = int(input('Digite um valor para verificar se está na sequência: '))
n1 = 0
n2 = 1

while n1 < num:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    
if num == n1:
    print(f'{num} está na sequência')
else:
    print(f'{num} não está na sequência')