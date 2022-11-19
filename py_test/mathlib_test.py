import python_pytest

#Added line to test workfloww
def test_addition():

    output = python_pytest.addition(2, 4)
    assert output == 6

def test_substraction():

    output = python_pytest.substraction(8, 4)
    assert output == 4

def test_multiply():

    output = python_pytest.multiply(2, 4)
    assert output == 8