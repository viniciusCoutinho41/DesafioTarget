### Programa 5
texto = input('Digite uma string a ser invertida: ')
string = []
invert = ''

for cont in range(len(texto)):
    string.append(texto[cont])

for item in range(len(string) -1, -1, -1):
    invert += string[item]

print(invert)