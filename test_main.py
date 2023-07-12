from numpy import multiply


def test_multiply_with_positive_nums():
    a = 10
    b = 29
    expected = 290
    res = multiply(a, b)
    assert res == expected


def test_result_less_than():
    a = 19
    b = 29
    expected = 300
    res = multiply(a, b)
    assert res < expected
