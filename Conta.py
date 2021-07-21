class Conta:

    def __init__(self, número, titular, saldo, limite=1000.0):
        print(f"Construindo objeto... {self}")
        self.__número = número
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__banco = "001"

    def extrato(self):
        print(f"O saldo do titular {self.titular} é de {self.saldo}")

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponível = self.__saldo + self.limite
        return valor <= valor_disponível

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod
    def banco():
        return "001"
