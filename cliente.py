from endereco import Endereco as E

class Cliente:
    def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade
      self.enderecos = []
      

    def insereEndereco(self, cidade, estado):
      self.enderecos.append(E(cidade, estado))
      

    def listaEnderecos(self):
      for i in self.enderecos:
        print(i.cidade, i.estado)
        

    def __del__(self):
      print(f'{self.nome} FOI APAGADO')