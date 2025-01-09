# PubMed Entity Annotator

This program takes the abstract of a PubMed article ID (PMID) as a command line argument and saves the annotations of recognized entities (e.g. proteins, drugs, diseases) as a JSON file.

It does this by performing the following steps:
1. Ask the user to type in the PMID of interest
2. Uses the PubMed web service to retreive the PubMed article for that PMID
3. Extracts the abstract from the PubMed article
4. Uses Gilda, an entity recognition web service, to annotate the abstract with recognized entities

It contains the following files:
* `fetch_pubmed.py` – code used to obtain the PubMed article based on the PMID and extract the abstract
* `use_gilda.py` – code used to extract the annotations from the abstract

To run the code, simply down onto computer and then in a python environment, run the following code:

```python
python main.py