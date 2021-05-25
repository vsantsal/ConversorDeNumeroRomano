import abc
from types import MappingProxyType
from typing import List


class ConversorDeNumeroRomano(metaclass=abc.ABCMeta):
    tabela: MappingProxyType = MappingProxyType({
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    })

    @classmethod
    def converte(cls, numero_em_romano: str) -> int:
        """
        Recebe texto numero_em_romano e retorna sua representação decimal (int).

        :param numero_em_romano: str com numero_em_romano
        :return:
        """
        # fail fast se não é string
        try:
            numero_romano_caixa_alta = numero_em_romano.upper()
        except AttributeError:
            raise TypeError("%s deve ter <'class'> = 'str'" % numero_em_romano)

        # confirmamos se não há repetição de V, L ou D
        cls._valida_nao_repeticao_de_simbolos_especiais(numero_romano_caixa_alta)

        # obtém os valores de cada posição
        # não utilizamos método get para lançar KeyError
        # invertemos a lista
        try:
            valores: List = [cls.tabela[letra]
                             for letra in
                             numero_romano_caixa_alta][::-1]
        except KeyError:
            raise ValueError('%s possui símbolos não reconhecidos!' % numero_em_romano)

        # confirma se a sequência é válida
        cls._valida_se_nao_possui_quatro_simbolos_iguais_em_sequencia(valores)
        cls._valida_se_nao_possui_tres_digitos_menores_ou_mais_a_esquerda_do_maior(valores)

        # aplica regra para somar os valores decimais representados pela sequência simbólica
        numero_em_decimal = cls._soma_sequencia_invertida_simbolos_romanos(valores)

        return numero_em_decimal

    @staticmethod
    def _soma_sequencia_invertida_simbolos_romanos(sequencia_numeros: List) -> int:
        # acumulador condicional:
        # algarismos de menor ou igual valor à direita são somados ao algarismo de maior valor
        # algarismos de menor valor à esquerda são subtraídos do algarismo de maior valor
        valores_com_sinais = [
            valor
            if ((not posicao) or valor >= sequencia_numeros[posicao - 1])
            else -valor
            for posicao, valor
            in enumerate(sequencia_numeros)
        ]

        return sum(valores_com_sinais)

    @staticmethod
    def _valida_se_nao_possui_quatro_simbolos_iguais_em_sequencia(sequencia_numeros: List) -> None:
        flag_numerico: int = 1
        for posicao, valor in enumerate(sequencia_numeros):
            if (not posicao) or (valor != sequencia_numeros[posicao - 1]):
                flag_numerico = 1
            else:
                flag_numerico += 1
                if flag_numerico > 3:
                    raise ValueError('Não é permitida sequência com 4 símbolos ou mais repetidos')

    @staticmethod
    def _valida_se_nao_possui_tres_digitos_menores_ou_mais_a_esquerda_do_maior(valores: List) -> None:
        num_valores_menores: int = 0
        ultimo_valor: int = valores[0]
        for valor in valores:
            if valor < ultimo_valor:
                num_valores_menores += 1
                if num_valores_menores > 2:
                    raise ValueError
            else:
                ultimo_valor = valor

    @staticmethod
    def _valida_nao_repeticao_de_simbolos_especiais(numero_romano: str) -> None:
        if (numero_romano.count('V') > 1 or
                numero_romano.count('L') > 1 or
                numero_romano.count('D') > 1):
            raise ValueError
