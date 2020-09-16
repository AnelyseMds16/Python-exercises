class baldes:
    capacidade = 5
    volume = 0
    def __init__(self):
        print("A capacidade do balde é de 5 Litros")
        
    def encher(self, quantidade):
        if(quantidade > self.capacidade):
            print("O valor tem que ser menor")
        else:
            self.volume = quantidade
            print("O balde está com {} litros".format(self.volume))
        
    def esvaziar(self, menos):
        if(menos<0):
            print("O valor deve ser maior que zero ")
        else:
            self.volume -= menos
        print("O balde está agora com {} litros".format(self.volume))
            
objeto = baldes()
objeto.encher(3)
objeto.esvaziar(2)