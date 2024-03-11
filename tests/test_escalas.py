from pytest import mark, raises

from python_training.escalas import ESCALAS, NOTAS, escala


def test_escala_deve_funcionar_com_notas_minusculas():
    tonica = "c"
    tonalidade = "maior"

    result = escala(tonica, tonalidade)

    assert result


def test_escala_deve_retornar_uma_mensagem_dizendo_que_a_nota_nao_existe():
    tonica = "X"
    tonalidade = "maior"

    mensagem_de_erro = f"Essa nota não existe, tente uma dessas {NOTAS}"

    with raises(ValueError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


def test_deve_retornar_um_erro_dizendo_que_a_escala_nao_existe():
    tonica = "c"
    tonalidade = "tonalidade_inexistente"

    mensagem_de_erro = f"Essa escala não existe ou não foi implementada, tente uma dessas {list(ESCALAS.keys())}"

    with raises(KeyError) as error:
        escala(tonica, tonalidade)

    assert mensagem_de_erro == error.value.args[0]


@mark.parametrize(
    "tonica, resultado_esperado",
    [
        ("C", ["C", "D", "E", "F", "G", "A", "B"]),
        ("C#", ["C#", "D#", "F", "F#", "G#", "A#", "C"]),
        ("F", ["F", "G", "A", "A#", "C", "D", "E"]),
    ],
)
def test_deve_retornar_as_notas_corretas(tonica, resultado_esperado):
    resultado = escala(tonica, "maior")

    assert resultado["notas"] == resultado_esperado


def test_deve_retornar_os_sete_graus():
    tonica = "c"
    tonalidade = "maior"
    esperado = ["I", "II", "III", "IV", "V", "VI", "VII"]

    resultado = escala(tonica, tonalidade)

    assert resultado["graus"] == esperado
