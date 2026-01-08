import pytest
from reto_01_invertir_cadena import invertir_cadena_segura


def test_invierte_texto_normal():
    assert invertir_cadena_segura("hola") == "aloh"


def test_cadena_vacia():
    assert invertir_cadena_segura("") == ""


def test_none_devuelve_vacio():
    assert invertir_cadena_segura(None) == ""


def test_tipo_incorrecto_lanza_typeerror():
    with pytest.raises(TypeError):
        invertir_cadena_segura(123)

