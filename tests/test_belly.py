#First line in test_belly.py
import re
from features.steps.steps import convertir_palabra_a_numero
import pytest

def test_convertir_palabra_a_numero():
    assert convertir_palabra_a_numero("quarto") == 0.25
    assert convertir_palabra_a_numero("media") == 0.5
    assert convertir_palabra_a_numero("medio") == 0.5
    assert convertir_palabra_a_numero("uno") == 1
    assert convertir_palabra_a_numero("cinco") == 5
    assert convertir_palabra_a_numero("diez") == 10
    assert convertir_palabra_a_numero("veinte") == 20
    assert convertir_palabra_a_numero("cincuenta") == 50
    assert convertir_palabra_a_numero("cien") == 100
    assert convertir_palabra_a_numero("ciento") == 100
    assert convertir_palabra_a_numero("doscientos") == 200
    assert convertir_palabra_a_numero("trescientos") == 300
    assert convertir_palabra_a_numero("cuatrocientos") == 400
    assert convertir_palabra_a_numero("quinientos") == 500
    assert convertir_palabra_a_numero("seiscientos") == 600
    assert convertir_palabra_a_numero("setecientos") == 700
    assert convertir_palabra_a_numero("ochocientos") == 800
    assert convertir_palabra_a_numero("novecientos") == 900
    assert convertir_palabra_a_numero("mil") == 1000
    assert convertir_palabra_a_numero("") == 0
    assert convertir_palabra_a_numero(" ") == 0
#    assert convertir_palabra_a_numero(None) == TypeError
    assert convertir_palabra_a_numero("dos mil") == 0

