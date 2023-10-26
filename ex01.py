# Criar duas classes, A e B:
# Sendo que a classe B tem um relacionamento de Composição 
# com a classe A, para isso inicialize o objeto A no método somaTodosNum


#Composição
#class A
class A:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c

class B:
  def __init__(self, d, e,):
    self.d = d
    self.e = e
    self.A = A("soma = ", 2, 8) # composição da classe A dentro da classe B (A é um atributo de B)

  def somaTodosNum(self):
    x = self.d + self.e + self.A.b + self.A.c # soma de todos os atributos das classes A e B 
    return x
  
  
  
  
  
##############################################################
# usando as classes A e B
b1 = B(8, 10)
# imprimir a composição de B e A
print(f"{b1.A.a} {b1.somaTodosNum()}")