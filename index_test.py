import pytest
from ind import ArthimeticClass

class TestArithmeticClass:
    def test_add(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 3.0
        # act
        actual_output = ArthimeticClass.add(x, y)
        assert expected_output == actual_output
        
    def test_sub(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = -1.0
        # act
        actual_output = ArthimeticClass.subtract(x, y)
        assert expected_output == actual_output
        
    def test_mul(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 2.0
        # act
        actual_output = ArthimeticClass.multiply(x, y)
        # assert
        assert expected_output == actual_output
        
    def test_mul(self ):
        # arrange
        x, y = 1.0, 2.0
        expected_output = 0.5
        # act
        actual_output = ArthimeticClass.divide(x, y)
        assert expected_output == actual_output
