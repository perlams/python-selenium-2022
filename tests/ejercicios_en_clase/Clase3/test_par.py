def es_par(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return True
    else:
        return False

def test_positive():
    result = es_par(2,4)
    assert result

def test_negative():
    result = es_par(3,9)
    assert result, "Los numeros no son pares"

def test_negative_mixed_params():
    result = es_par(2,3)
    assert not result

def test_negative_min_max_param():
    result = es_par(0,22222222222)
    assert result

