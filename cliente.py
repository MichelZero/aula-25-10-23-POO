from endereco import Endereco as E

class Cliente:
    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade
      self.enderecos = [] # lista de endereços do cliente (composição)
      

    def insereEndereco(self, cidade, estado):
      self.enderecos.append(E(cidade, estado)) # adiciona um endereço na lista de endereços do cliente (composição)
      

    def listaEnderecos(self):
      for i in self.enderecos:
        print(i.cidade, i.estado) # imprime os endereços do cliente (composição) 
        

    def __del__(self):
      print(f'{self.nome} FOI APAGADO') # quando o objeto é apagado, o cliente é apagado também