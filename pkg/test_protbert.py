import pytest
import re
from pkg import preprocess_protein_sequence

@pytest.fixture
def test_sequence():
    return "A E T C Z A O"

class TestProtbert:
    def test_preprocess_protein_sequence(self, test_sequence):
        processed_sequence = preprocess_protein_sequence(test_sequence)
        expected_result = "A   E   T   C   X   A   X"
        assert processed_sequence == expected_result
