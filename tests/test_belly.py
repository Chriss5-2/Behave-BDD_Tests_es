#First line in test_belly.py
import re
from feature.steps.steps import convertir_palabra_a_numero
import pytest

def test_convertir_palabra_a_numero():
    assert convert_palabra_a_numero("quarto") == 0.25
    assert convert_palabra_a_numero("media") == 0.5
    assert convert_palabra_a_numero("medio") == 0.5
    assert convert_palabra_a_numero("uno") == 1
    assert convert_palabra_a_numero("cinco") == 5
    assert convert_palabra_a_numero("diez") == 10
    assert convert_palabra_a_numero("veinte") == 20
    assert convert_palabra_a_numero("cincuenta") == 50
    assert convert_palabra_a_numero("cien") == 100
    assert convert_palabra_a_numero("ciento") == 100
    assert convert_palabra_a_numero("doscientos") == 200
    assert convert_palabra_a_numero("trescientos") == 300
    assert convert_palabra_a_numero("cuatrocientos") == 400
    assert convert_palabra_a_numero("quinientos") == 500
    assert convert_palabra_a_numero("seiscientos") == 600
    assert convert_palabra_a_numero("sietecientos") == 700
    assert convert_palabra_a_numero("ochocientos") == 800
    assert convert_palabra_a_numero("novecientos") == 900
    assert convert_palabra_a_numero("mil") == 1000


