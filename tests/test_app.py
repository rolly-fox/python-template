from python_template.app import greet
import pytest

def test_greet_basic():
    assert greet("Rolly") == "Hello, Rolly! ??"

def test_greet_empty_defaults():
    assert greet("   ") == "Hello, friend! ??"

def test_greet_type_error():
    with pytest.raises(TypeError):
        greet(None)  # type: ignore
