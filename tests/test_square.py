import pytest
import source.shapes as shapes

## Asi marcamos parametrizacion
@pytest.mark.parametrize("side_length, expected_area", [
    (1, 1),
    (2, 4),
    (3, 9),
    (4, 16),
    (5, 25),
    (6, 36),
    (7, 49),
    (8, 64),
    (9, 81),
    (10, 100)
])
def test_multiple_square_areas(side_length, expected_area):
    # Output => '..........', por la cantidad de parametros que tenemos
    assert shapes.Square(side_length).area() == expected_area
    

@pytest.mark.parametrize("side_length, expected_perimeter", [(1, 4), (2, 8), (3, 12), (4, 16), (5, 20)])
def test_multiple_perimeters(side_length, expected_perimeter):
    assert shapes.Square(side_length).perimeter() == expected_perimeter