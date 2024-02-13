import pytest
import source.my_functions as my_functions

def test_add():
    result = my_functions.add(1, 2)
    assert result == 3
    
def test_add_strings():
    result = my_functions.add("Hello ", "World")
    assert result == "Hello World"
    
def test_divide():
    result = my_functions.divide(4, 2)
    assert result == 2
    
## BONUS TRACK
def test_divide_by_zero():
    ## Con esto aseguramos que de la funcion tire un error de ZeroDivisionError
    with pytest.raises(ZeroDivisionError):
        ## Es decir, el test pasa porque sabemos que tira un error de ZeroDivisionError
        my_functions.divide(1, 0)
    