# Criar duas classes, A e B:
# Sendo que a classe B tem um relacionamento de agregação com a classe A.
# onde A recebe valor 1 e valor 2, B recebe valor 3 e valor 4 e tem um método somaTodosNun, 

# agregação é quando uma classe tem um relacionamento com outra classe, mas uma classe não depende da outra para existir	
# composição é quando uma classe tem um relacionamento com outra classe, mas uma classe depende da outra para existir
# exemplo de agregação: uma pessoa tem um carro, mas a pessoa pode existir sem o carro
# exemplo de composição: uma pessoa tem um coração, mas a pessoa não pode existir sem o coração

# class Pessoa:

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

class Empresa:
  def __init__(self, nome, pessoas):
    self.nome = nome
    self.pessoas = pessoas
    
# A classe Empresa faz uso de agregação, pois possui uma lista de objetos da classe Pessoa.