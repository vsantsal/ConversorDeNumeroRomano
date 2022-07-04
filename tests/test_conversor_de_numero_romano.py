import unittest

from src.conversor_de_numero_romano import (
    ConversorDeNumeroRomano,
)


class TestConversorDeNumeroRomano(unittest.TestCase):

    def setUp(self) -> None:
        self.simbolos_uma_posicao_permitidos = {
            ('I', 1), ('V', 5), ('X', 10),
            ('L', 50), ('C', 100), ('D', 500),
            ('M', 1000)}
        self.simbolos_seguidos_permitidos = {
            ('II', 2), ('XX', 20), ('CC', 200),
            ('MM', 2000), ('III', 3), ('XXX', 30),
            ('CCC', 300), ('MMM', 3000)
        }
        self.simbolo_menor_antes_simbolo_maior = {
            ('IX', 9), ('IV', 4), ('XL', 40),
            ('XC', 90)
        }
        self.simbolos_combinacoes_complexas = {
            ('XXII', 22), ('XXIV', 24), ('XLIV', 44),
            ('CDLXXXIV', 484), ('CMXCVII', 997),
            ('DCCC', 800), ('CDXLIV', 444),
        }
        self.simbolos_combinacoes_nao_permitidas = {
            'VV', 'IIII', 'LL', 'DD', 'IIIX',
            'XXXC', 'MMMM'
        }
        self.nome_arquivo_numeros_1_a_3999: str = 'tests/numeros_1_a_3999.txt'
        self.numero = ConversorDeNumeroRomano.converte_romano_para_int
        self.romano = ConversorDeNumeroRomano.converte_int_para_romano
        self.inputs_nao_permitidos = [None, 1.0, ('i', ), ['i', ]]
        self._inteiros_fora_do_escopo_romano = [0, -1, -100,
                                                4000, 40000, 1000000]

    def test_converte_para_int_deve_entender_simbolo_basico_numero_romano_maisuculo(self):
        for simbolo, digito in self.simbolos_uma_posicao_permitidos:
            self.assertEqual(digito, self.numero(simbolo.upper()))

    def test_converte_para_int_deve_entender_o_simbolo_basico_numero_romano_minusculo(self):
        for simbolo, digito in self.simbolos_uma_posicao_permitidos:
            self.assertEqual(digito, self.numero(simbolo.lower()))

    def test_converte_para_int_deve_entender_simbolos_seguidos_permitidos(self):
        for simbolo, digito in self.simbolos_seguidos_permitidos:
            self.assertEqual(digito, self.numero(simbolo))

    def test_converte_para_int_deve_lancar_value_error_se_simbolo_desconhecido(self):
        with self.assertRaises(ValueError) as erro:
            self.numero('a')
        self.assertEqual('a possui símbolos não reconhecidos!',
                         *erro.exception.args)

    def test_converte_para_int_deve_lancar_type_error_se_nao_eh_str(self):
        with self.assertRaises(TypeError) as erro:
            for entrada in self.inputs_nao_permitidos:
                self.numero(entrada)
                self.assertEqual("{} deve ter <'class'> = 'str'".format(entrada),
                                 *erro.exception.args)

    def test_converte_para_int_deve_entender_numeros_com_simbolo_menor_a_esquerda(self):
        for simbolo, digito in self.simbolo_menor_antes_simbolo_maior:
            self.assertEqual(digito, self.numero(simbolo))

    def test_converte_para_int_deve_entender_simbolos_combinacoes_complexas(self):
        for simbolo, digito in self.simbolos_combinacoes_complexas:
            self.assertEqual(digito, self.numero(simbolo))

    def test_converte_para_int_nao_deve_entender_simbolos_combinacoes_nao_permitidas_e_lancar_value_error(self):
        for simbolo in self.simbolos_combinacoes_nao_permitidas:
            with self.assertRaises(ValueError):
                self.numero(simbolo)

    def test_converte_para_int_funciona_para_numeros_de_1_a_3999(self):
        with open(self.nome_arquivo_numeros_1_a_3999, 'r') as cenarios_testes:
            conteudo = cenarios_testes.readlines()
        for linha in conteudo:
            numero, simbolo = linha.strip().split(sep='\t')
            resultado = self.numero(simbolo)
            self.assertEqual(int(numero), resultado)
