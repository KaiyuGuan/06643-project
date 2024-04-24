06643-Project
==============

# Overview
The aim of this project focus on creating a package that contains the helper functions that is used when training a predictive model that predict the binding affinity between a protein and a peptide. This predictive model takes the advantages of pre-trained transformers, **PeptideBert** and **MoLFormer**, where the previous transfomer takes input of string representation of amino acid sequence of a protein, and the later takes in SMILES string representation of the structure of the peptide.

# Usage
In this package, the helper functions focus primarily on the data pre-processing steps as the raw data has to be transformed into correct format that can be inputted into these transformers. There are 2 functions in this packages:
- the function `peptidebert_preprocess` is designed for the transformer peptidebert. The function takes arrays of integers as input and returns arrays of integers. The details of this function will be discussed in later sections.
- the function `preprocess_protein_sequence` is designed for the transformer ProtBert, which is not part of the model. However, we use it as a comparison to PeptideBert transformer. Both these transformers tokenizes the amino acid sequences of a protein in order to obtain something that machines has better understanding of. 

# Future Steps
The project that I am working on is still in progress and these are just the helper functions that I encountered during my research and training. As the project keeps developing and furnishing, more helper functions will be added to this package. 

It is important to note that not all helper functions used in the project is included in this package. Some helper functions are not included due to the computational constraints (these functions are the ones that run for hours even on GPUs).

# Reference
More details about the transformers discussed can be found in the following link:

[ProtBert](https://huggingface.co/Rostlab/prot_bert)  
[MoLFormer](https://huggingface.co/ibm/MoLFormer-XL-both-10pct)  
[PeptideBert](https://arxiv.org/pdf/2309.03099.pdf)
