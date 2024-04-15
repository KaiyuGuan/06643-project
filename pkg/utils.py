"""Define helper functions for the preictive model."""

import numpy as np
import re


def pipetidebert_preprocess(file):
    """Preprocess protein sequence for pipetidebert model.

    file: string of path to file
    """
    f = np.load(file)
    m1 = [
        "[PAD]",
        "A",
        "R",
        "N",
        "D",
        "C",
        "Q",
        "E",
        "G",
        "H",
        "I",
        "L",
        "K",
        "M",
        "F",
        "P",
        "S",
        "T",
        "W",
        "Y",
        "V",
    ]
    m2 = dict(
        zip(
            [
                "[PAD]",
                "[UNK]",
                "[CLS]",
                "[SEP]",
                "[MASK]",
                "L",
                "A",
                "G",
                "V",
                "E",
                "S",
                "I",
                "K",
                "R",
                "D",
                "T",
                "P",
                "N",
                "Q",
                "F",
                "Y",
                "M",
                "H",
                "C",
                "W",
                "X",
                "U",
                "B",
                "Z",
                "O",
            ],
            range(30),
        )
    )
    arr = np.array(
        list(map(lambda x: m2[m1[int(x)]], f["arr_0"].flat))
    ).reshape(f["arr_0"].shape)

    np.savez(file, arr_0=arr)


def preprocess_protein_sequence(seq):
    """Preprocess protein sequence for pipetidebert model.

    seq: string representation of amino acid sequence
    """
    return " ".join(re.sub(r"[UZOB]", "X", seq))
