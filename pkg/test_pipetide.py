import os
import pytest
import numpy as np
from pkg import pipetidebert_preprocess

@pytest.fixture
def test_file():
    # Create a temporary file with some test data
    file_path = "test_data.npz"
    test_data = np.array([ 2, 20, 12,  2, 20, 18, 15, 11, 20, 10,  2, 17, 20, 10,  1,  8, 19, 3, 11, 19,  2,  1, 10, 12, 12, 12])
    np.savez(file_path, arr_0=test_data)
    yield file_path
    # Clean up the temporary file
    os.unlink(file_path)

class TestPipetide:
    def test_pipetidebert_preprocess(self, test_file):
        pipetidebert_preprocess(test_file)
        processed_data = np.load(test_file)
        assert np.array_equal(processed_data["arr_0"], np.array([13,  8, 12, 13,  8, 24, 16,  5,  8, 11, 13, 15,  8, 11,  6,  7, 20, 17,  5, 20, 13,  6, 11, 12, 12, 12]))
