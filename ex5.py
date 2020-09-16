class ContaBancaria:
    nome = str(input("Informe o nome: "))
    saldo = float(input("Informe o saldo: "))
    numero = int(input("Informe o número da conta: "))
    def depositar(self):
        deposito = int(input("Informe o valor do depósito: "))
        self.saldo+=deposito
        print("Depósito concluído! Saldo: {}".format(self.saldo))
    def sacar(self):
        saque = int(input("Informe o valor do saque: "))
        self.saldo-=saque
        print("Saque concluído! Saldo: {}".format(self.saldo))
    

class ContaCorrente(ContaBancaria):
    def pagarBoleto(self):
        boleto = int(input("Informe o valor do boleto: "))
        self.saldo = self.saldo-boleto
        print("Boleto pago! Saldo: {}".format(self.saldo))
        

class ContaPoupanca(ContaBancaria):
    taxa=0
    def resgatar(self):
        self.taxa = float(input("Qual a taxa que você deve pagar?"))
        print("O resgate da classe Poupança foi feito")
        
class ContaInvestimento(ContaBancaria):
    consultor = ""
    def resgatar(self):
        self.consultor = str(input("Qual o nome do consultor?"))
        print("O resgate da classe Investimento foi feito")
        print("Seu consultor {} conseguiu resgatar seu investimento".format(self.consultor))
        

obj = ContaBancaria()
objCorrente = ContaCorrente()
objPoupanca = ContaPoupanca()
objInvestimento = ContaInvestimento()

obj.depositar()
obj.sacar()
objCorrente.pagarBoleto()
objPoupanca.resgatar()
objInvestimento.resgatar()



