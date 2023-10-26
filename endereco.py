class Endereco:
    def __init__(self, cidade, estado):
      self.cidade = cidade
      self.estado = estado

    def __del__(self): # método destrutor 
      print(f'{self.cidade}/{self.estado} FOI APAGADO') # quando o objeto é apagado, o endereço é apagado também