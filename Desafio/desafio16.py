from abc import ABC, abstractmethod
                                 #Achei esse desafio super difícil
class ContaBancaria(ABC):
    def __init__(self, saldo_inicial=0.0):
        self.saldo = saldo_inicial

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

class ContaCorrente(ContaBancaria):
    TAXA_MANUTENCAO = 5.00

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        valor_total = valor + self.TAXA_MANUTENCAO
        
        if self.saldo >= valor_total:
            self.saldo -= valor_total
            print(f"Saque CC de R$ {valor:.2f} (Taxa: R$ {self.TAXA_MANUTENCAO:.2f}).")
        else:
            print(f"ERRO: Saldo insuficiente na Conta Corrente.")

class ContaPoupanca(ContaBancaria):
    TAXA_JUROS = 0.005  

    def depositar(self, valor):
        self.saldo += valor
        self.aplicar_juros()  

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque CP de R$ {valor:.2f}.")
        else:
            print(f"ERRO: Saldo insuficiente na Conta Poupança.")

    def aplicar_juros(self):
        rendimento = self.saldo * self.TAXA_JUROS
        self.saldo += rendimento
        print(f"Juros CP aplicados: R$ {rendimento:.2f}.")

print("--- TESTE DO SISTEMA ---")

cc = ContaCorrente(saldo_inicial=100.00)
cp = ContaPoupanca(saldo_inicial=500.00)

print(f"\nSaldo Inicial CC: R$ {cc.saldo:.2f}")
print(f"Saldo Inicial CP: R$ {cp.saldo:.2f}")

print("\nOperações Conta Corrente:")
cc.depositar(200.00)  
cc.sacar(50.00)       
print(f"Saldo Atual CC: R$ {cc.saldo:.2f}")

print("\nOperações Conta Poupança:")
cp.depositar(100.00)  
cp.sacar(53.00)        
print(f"Saldo Atual CP: R$ {cp.saldo:.2f}")

print("\n--- SALDO FINAL ---")
print(f"Conta Corrente: R$ {cc.saldo:.2f}")
print(f"Conta Poupança: R$ {cp.saldo:.2f}")