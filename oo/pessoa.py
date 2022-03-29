class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
       return f'Olá, Meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos} '

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    luiza = Mutante(nome='Luiza')
    rafael = Homem(luiza, nome='Rafael')
    print(Pessoa.cumprimentar(rafael))
    print(id(rafael))
    print(rafael.cumprimentar())
    print(rafael.nome)
    print(rafael.idade)
    for filho in rafael.filhos:
        print(filho.nome)
    rafael.sobrenome = 'Andreotti'
    del rafael.filhos
    rafael.olhos = 1
    del rafael.olhos
    print(rafael.__dict__)
    print(luiza.__dict__)
    print(Pessoa.olhos)
    print(rafael.olhos)
    print(luiza.olhos)
    print(Pessoa.metodo_estatico(), rafael.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), rafael.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(luiza, Pessoa))
    print(isinstance(luiza, Homem))
    print(luiza.olhos)
    print(rafael.cumprimentar())
    print(luiza.cumprimentar())