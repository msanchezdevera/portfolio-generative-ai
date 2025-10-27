Plan (pseudocódigo detallado):

Import pytest y la clase SumDigits usando import absoluto: from labs.class09.code_before import SumDigits
Crear una serie de pruebas parametrizadas que cubran:
cadena vacía -> resultado 0
cadena sin dígitos -> resultado 0
cadenas con un solo dígito (0 y 5) -> resultado igual al dígito
cadena con dígitos dispersos "a1b2c3" -> sumar dígitos 1+2+3 = 6
cadena con dígitos consecutivos "12" -> sumar dígitos 1+2 = 3 (no interpretar como 12)
cadena con símbolos y números "The cost is 45$" -> 4+5 = 9
cadena con ceros a la izquierda "007" -> 0+0+7 = 7
Para cada caso:
instanciar SumDigits
llamar sum_digits(text)
afirmar que el resultado coincide con el esperado
Opcional: comprobar que pasar None produce una excepción de atributo (AttributeError) para documentar comportamiento con tipo no str

# python
import pytest
from labs.class09.code_before import SumDigits

@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),                      # empty string -> 0
        ("no digits here", 0),        # no digits -> 0
        ("0", 0),                     # single digit zero -> 0
        ("5", 5),                     # single digit five -> 5
        ("a1b2c3", 6),                # scattered digits -> 1+2+3 = 6
        ("12", 3),                    # consecutive digits treated individually -> 1+2 = 3
        ("The cost is 45$", 9),       # mixed text and symbols -> 4+5 = 9
        ("007", 7),                   # leading zeros -> 0+0+7 = 7
    ],
)
def test_sum_digits_various_inputs(text, expected):
    sd = SumDigits()
    assert sd.sum_digits(text) == expected

def test_sum_digits_with_non_string_raises_attribute_error():
    sd = SumDigits()
    with pytest.raises(AttributeError):
        # None has no isdigit method; documents behavior for non-str input
        sd.sum_digits(None)# python
import pytest
from labs.class09.code_before import SumDigits

@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),                      # empty string -> 0
        ("no digits here", 0),        # no digits -> 0
        ("0", 0),                     # single digit zero -> 0
        ("5", 5),                     # single digit five -> 5
        ("a1b2c3", 6),                # scattered digits -> 1+2+3 = 6
        ("12", 3),                    # consecutive digits treated individually -> 1+2 = 3
        ("The cost is 45$", 9),       # mixed text and symbols -> 4+5 = 9
        ("007", 7),                   # leading zeros -> 0+0+7 = 7
    ],
)
def test_sum_digits_various_inputs(text, expected):
    sd = SumDigits()
    assert sd.sum_digits(text) == expected

def test_sum_digits_with_non_string_raises_attribute_error():
    sd = SumDigits()
    with pytest.raises(AttributeError):
        # None has no isdigit method; documents behavior for non-str input
        sd.sum_digits(None)