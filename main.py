from cliente import Cliente as C

c1 = C('Davi', 32)
c1.insereEndereco('Cajazeiras', 'PB')
print(c1.nome)
c1.listaEnderecos()
del c1
print()





c2 = C('Maria', 55)
c2.insereEndereco('Natal', 'RN')
c2.insereEndereco('Campina grande', 'PB')
print(c2.nome)
c2.listaEnderecos()
del c2
print()





c3 = C('João', 19)
c3.insereEndereco('Patos', 'PB')
print(c3.nome)
c3.listaEnderecos()
del c3
print()

print('#########################################################')