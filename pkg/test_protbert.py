"""Tests for the preprocess_protein_sequence function in the package."""
import pytest
import re
from pkg import preprocess_protein_sequence


@pytest.fixture
def test_sequence():
    """Create a sequence with some test data."""
    return "A E T C Z A O"


class TestProtbert:
    """A Test class for the function preprocess_protein_sequence."""

    def test_preprocess_protein_sequence(self, test_sequence):
        """Test preprocess_protein_sequence."""
        processed_sequence = preprocess_protein_sequence(test_sequence)
        expected_result = "A   E   T   C   X   A   X"
        assert processed_sequence == expected_result
