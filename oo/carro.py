""" Criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:
1) Motor
2) Direção

O Motor terá responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que devera incrementar a velocidade de uma unidade
3) Método freiar, que devera decrementar a velocidade de duas uidades

A Direção terá responsabilidade de controlar a direção.Ela oferece os seguinte atributos:
1) Valor de direção com valores possíveis:Norte, Sul, Leste, Oeste
2) Método girar a direita
2) Método girar a esquerda
    N
 O     L
    S

"""
NORTE='Norte'
SUL= 'Sul'
LESTE='Leste'
OESTE= 'Oeste'

class Direcao:
    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }
    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]
    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dct[self.valor]
class Motor:

    def __init__(self):
        self.velocidade = 0


    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


if __name__ == '__main__':
    motor = Motor()
