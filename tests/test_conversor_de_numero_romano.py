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
            ('DCCC', 800)
        }
        self.simbolos_combinacoes_nao_permitidas = {
            'VV', 'IIII', 'LL', 'DD', 'IIIX',
            'XXXC', 'MMMM'
        }
        self.numero = ConversorDeNumeroRomano.converte
        self.inputs_nao_permitidos = [None, 1, ('i', ), ['i', ]]

    def test_deve_entender_simbolo_basico_numero_romano_maisuculo(self):
        for simbolo, digito in self.simbolos_uma_posicao_permitidos:
            self.assertEqual(digito, self.numero(simbolo.upper()))

    def test_deve_entender_o_simbolo_basico_numero_romano_minusculo(self):
        for simbolo, digito in self.simbolos_uma_posicao_permitidos:
            self.assertEqual(digito, self.numero(simbolo.lower()))

    def test_deve_entender_simbolos_seguidos_permitidos(self):
        for simbolo, digito in self.simbolos_seguidos_permitidos:
            self.assertEqual(digito, self.numero(simbolo))

    def test_deve_lancar_value_error_se_simbolo_desconhecido(self):
        with self.assertRaises(ValueError):
            self.numero('a')

    def test_deve_lancar_type_error_se_nao_eh_str(self):
        with self.assertRaises(TypeError):
            for entrada in self.inputs_nao_permitidos:
                self.numero(entrada)

    def test_deve_entender_numeros_com_simbolo_menor_a_esquerda(self):
        for simbolo, digito in self.simbolo_menor_antes_simbolo_maior:
            self.assertEqual(digito, self.numero(simbolo))

    def test_deve_entender_simbolos_combinacoes_complexas(self):
        for simbolo, digito in self.simbolos_combinacoes_complexas:
            self.assertEqual(digito, self.numero(simbolo))

    def test_nao_deve_entender_simbolos_combinacoes_nao_permitidas_e_lancar_value_error(self):
        for simbolo in self.simbolos_combinacoes_nao_permitidas:
            with self.assertRaises(ValueError):
                self.numero(simbolo)
