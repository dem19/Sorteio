
import abc
import random

class Jogo(abc.ABC):

    @abc.abstractmethod
    def sorteio(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class Megasena(Jogo):

    def __init__(self, quantidade = 6):
        self.numeros = []
        if quantidade >= 6:
            self.quantidade = quantidade
        else:
            self.quantidade = 6

    def sorteio(self):
        return random.randint(1, 60)

    def adicionar_numero(self):
        while len(self.numeros) < self.quantidade:
            numero_soteado = self.sorteio()
            if numero_soteado not in self.numeros:
                self.numeros.append(numero_soteado)

    def __len__(self):
        return len(self.numeros)

    def __getitem__(self, item):
        return self.numeros[item]

    def __str__(self):
        return str(self.numeros)

class Lotofacil(Jogo):

    def __init__(self, quantidade = 15):
        self.numeros = []
        if quantidade >= 15:
            self.quantidade = quantidade
        else:
            self.quantidade = 15

    def sorteio(self):
        return random.randint(1, 25)

    def adicionar_numero(self):
        while len(self.numeros) < self.quantidade:
            numero_soteado = self.sorteio()
            if numero_soteado not in self.numeros:
                self.numeros.append(numero_soteado)

    def __len__(self):
        return len(self.numeros)

    def __getitem__(self, item):
        return self.numeros[item]

    def __str__(self):
        return str(self.numeros)

class Quina(Jogo):

    def __init__(self, quantidade = 5):
        self.numeros = []
        if quantidade >= 5:
            self.quantidade = quantidade
        else:
            self.quantidade = 5

    def sorteio(self):
        return random.randint(1, 80)

    def adicionar_numero(self):
        while len(self.numeros) < self.quantidade:
            numero_soteado = self.sorteio()
            if numero_soteado not in self.numeros:
                self.numeros.append(numero_soteado)

    def __len__(self):
        return len(self.numeros)

    def __getitem__(self, item):
        return self.numeros[item]

    def __str__(self):
        return str(self.numeros)

class Lotomania(Jogo):

    def __init__(self, quantidade = 50):
        self.numeros = []
        if quantidade >= 50:
            self.quantidade = quantidade
        else:
            self.quantidade = 50

    def sorteio(self):
        return random.randint(1, 100)

    def adicionar_numero(self):
        while len(self.numeros) < self.quantidade:
            numero_soteado = self.sorteio()
            if numero_soteado not in self.numeros:
                self.numeros.append(numero_soteado)

    def __len__(self):
        return len(self.numeros)

    def __getitem__(self, item):
        return self.numeros[item]

    def __str__(self):
        return str(self.numeros)

