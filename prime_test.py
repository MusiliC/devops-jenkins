import pytest
from prime import is_prime

def test_prime_number():
    # Test if a prime number (e.g., 7) is identified as prime
    result = is_prime(7)
    assert result is True
