from app.main import is_even

def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(7) == False