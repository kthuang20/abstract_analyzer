# Abstract Analyzer

This program takes the abstract of a PubMed article ID (PMID) as a command line argument and saves the annotations of recognized entities (e.g. proteins, drugs, diseases) as a JSON file.

It contains the following files:
* fetch_pubmed.py – code used to obtain the PubMed article based on the PMID and extract the abstract
* use_gilda.py – code used to extract the annotations from the abstract

To run the code, simply down onto computer and then in a python environment, run the following code:
`python main.py`