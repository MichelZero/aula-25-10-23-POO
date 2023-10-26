from cliente import Cliente as C


c1 = C('Davi', 32) # cria um objeto da classe Cliente (composição)
c1.insereEndereco('Cajazeiras', 'PB') # adiciona um endereço na lista de endereços do cliente (composição)
print(c1.nome) # imprime o nome do cliente (composição)
c1.listaEnderecos() # imprime os endereços do cliente (composição)
del c1 # apaga o objeto da classe Cliente (composição)
print()  # pula uma linha





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