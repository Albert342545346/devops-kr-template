# tests/test_validator.py
from validator import validate_email, validate_phone


def test_validate_email():
    assert validate_email("test@example.com")
    assert not validate_email("invalid")


def test_validate_phone():
    assert validate_phone("+79991234567")
    assert not validate_phone("89991234567")
    assert not validate_phone("+7999123")
