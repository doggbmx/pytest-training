import pytest
import time
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
    with pytest.raises(ValueError):
        ## Es decir, el test pasa porque sabemos que tira un error de ZeroDivisionError
        my_functions.divide(1, 0)


## TIME ISSUES -- will only run if you run `pytest -m slow`
@pytest.mark.slow  
def test_very_slow_function():
    time.sleep(1)
    result = my_functions.divide(10, 5)
    assert result == 2      
        
@pytest.mark.skip(reason="This feature is currently broken")
def test_add():
    ## This would be the output: `s....`
    assert my_functions.add(1, 2) == 3
    
@pytest.mark.xfail(reason="We know we can not divide by zero")
def test_divide_by_zero_broken():
    ## This would be the output: `s....x`
    assert my_functions.divide(1, 0)